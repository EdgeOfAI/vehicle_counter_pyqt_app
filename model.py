import os
import sys
import torch
import datetime
from time import time
from pathlib import Path
from DrawLineWidget import DrawLineWidget

from typing import Dict
from shapely.geometry import Polygon
from PySide2.QtCore import Signal, Slot, QObject, QTimer
import cv2, h5py, math
import numpy as np
import matplotlib.pyplot as plt

from yolov5.models.common import DetectMultiBackend
from yolov5.utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, LoadScreenshots, LoadStreams, LoadHikvisionCamera
from yolov5.utils.general import (LOGGER, Profile, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, print_args, scale_boxes, strip_optimizer, xyxy2xywh)
from yolov5.utils.torch_utils import select_device, smart_inference_mode
from yolov5.utils.augmentations import classify_transforms, letterbox
from yolov5.models.experimental import attempt_load
import torch.nn.functional as F
# SORT tracker
from utils.sort_tracker import SORT
sort_tracker = SORT(max_lost=25, iou_threshold=0.3)
from utils.trackableobject import TrackableObject
from utils.image_cropper import CropImage
########################################
MAX_DETECTION_NUM = 800



class_id_map = {
    'none'  : '0',
    'truck' : '6',
    'car'   : '1',
    'bus'   : '4',
    'bicycle': '2',
    'motorcycle': '3',
    'van':'5'
}
class_id_map.update({item[1]: item[0] for item in class_id_map.items()})
print(class_id_map)

class Model(QObject):
    frame_update_signal = Signal(np.ndarray, int)
    # max_frame_update_signal = Signal(int)
    process_done_signal = Signal()
    error_signal = Signal(str)
    vehicle_count_signal = Signal(int,int,int,np.ndarray,str,int)

    def __init__(self, conn, cur, draw_color):
        super().__init__()
        # Definition of the parameters
        self.sess = None
        self.infer = None
        self.encoder = None
        self.saved_model_loaded = None
        self.max_cosine_distance = 0.4
        self.start_classifying_distance = 2000
        self.iou_thresh = 0.45
        self.score_thresh = 0.7
        self.input_video_path = ''
        self.output_video_path = ''
        self.output_data_path = ''
        self.mask_path = ''
        self.cache_data = None
        self.vid = None
        self.detected_vehicles = None
        self.frame_counter = 0
        self.finishLine = (0,0,0,0)
        self.stop_inference = True
        self.stop_counting = False
        self.use_video = False
        self.count_method = 0
        self.imgMask = None
        self.cardinal_vehicle_counter = dict()
        self.cardinal_direction_points = []
        self.cam_id = 0
        self.counted_ids = []
        self.draw_color = draw_color
        self.CARDINAL_DIRECTIONS = ['North', 'East', 'West', 'South']
        
        self.allowed_classes = ['car', 'bicycle', 'motorcycle', 'bus', 'van',  'truck', '']
        self.vehicle_counter = {'0': 0,'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '':0}  # 1 truck, 2 car, 3 bus, 4 bicycle, 5 motorcycle
        self.initialize_counting()
        self.images_root = '/home/yeoju/vehicle_counter/crops'
        self.images_root = os.path.join(self.images_root, str(datetime.date.today()))
        self.db_conn = conn 
        self.db_cur = cur 
        self.trackableObjects = {}
        self.image_cropper = CropImage()
        self.det_area_x0 = 0
        self.det_area_y0 = 0
        self.det_area_x1 = 1280
        self.det_area_y1 = 720
        self.margin = 20
        #initialize color map
        cmap = plt.get_cmap('tab20b')
        self.colors = [(255, 89, 94), (255, 202, 58), (138, 201, 38), (25, 130, 196), (106, 76, 147), (1, 27, 200), (0, 0, 0)]  # colors which are being used https://coolors.co/palette/ff595e-ffca3a-8ac926-1982c4-6a4c93

#======================= Setters  ===========================
    def update_db_conn_cur(self, db_conn, db_cur):
        self.db_conn = db_conn
        self.db_cur = db_cur

    def initialize_counting(self):
        self.detected_vehicles = {class_id : {} for class_name, class_id in class_id_map.items()}

    def setInputVideoPath(self, path):
        self.input_video_path = path
        self.vid = cv2.VideoCapture(self.input_video_path)
        _, frame = self.vid.read()
        self.draw_line_widget = DrawLineWidget(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.frame_update_signal.emit(frame, 0)

        # draw cardinal coordinates
        # cv2.imshow('image', self.draw_line_widget.show_image())

    def setOutputVideoPath(self, path):
        self.output_video_path = path

    def setOutputDataPath(self, path):
        self.output_data_path = path

    def setCacheDataPath(self, path):
        self.cache_data_path = path

        # parse Model path and send signal with max frame num # Shakh
        # cache = h5py.File(self.cache_data_path, 'r')
        # cache_data = cache.get('dataset_1')
        # self.cache_data = np.array(cache_data)

        # self.max_frame_update_signal.emit(self.cache_data.shape[0])
 
    def setCameraInfo(self, id, ip, username, password, camera_name, cardinal_direction_points):
        self.cam_id = id
        self.cam_ip = ip
        self.cam_username = username
        self.cam_password = password
        self.cam_name = camera_name
        self.cardinal_direction_points = cardinal_direction_points

    def setMaskFile(self, path):
        self.mask_path = path
        mask = h5py.File(self.mask_path, 'r')
        mask = mask.get('mask')
        self.imgMask = np.array(mask)

    def saveMask(self, path, mask):
        self.imgMask = mask
        data = h5py.File(path, 'w')
        data.create_dataset('mask', data=self.imgMask)
        data.close()

    def getMask(self):
        return self.imgMask

    def setParams(self, params:dict):
        self.imgMask = params['mask']
        self.iou_thresh = params['iou_thresh']
        self.score_thresh = params['score_thresh']
        self.max_cosine_distance = params['cos_dist']
        self.filt_x_vec = params['x_vect']
        self.filt_y_vec = params['y_vect']
        self.filt_width = params['filt_width']
        self.filt_dist = params['filt_dist']
        self.filt_frame = params['filt_frames']
        self.finishFrames = params['finish_frames']
        self.finishLine = params['finish_line']
        self.count_method = params['count_method']

#==================== Counting Functions ========================
    @Slot()
    def custom_softmax(x):
        f_x = np.exp(x)/np.sum(np.exp(x))
        return f_x[0]
    @Slot()
    def get_class_name(self, img, model_cls):
        class_name = None
        transform = classify_transforms(64)
        img = transform(img)
        img = torch.Tensor(img).to(torch.device('cuda:0'))
        img = img.float()
        img = img[None]
        preds = model_cls(img)
        preds = F.softmax(preds, dim=1)
        preds = preds[0].argsort(0, descending=True)[:1].tolist()
        # print("preds: ", preds)
        class_name = preds[0]

        return class_name
    @Slot()
    def startCounting(self):
        if not self.validateInputFiles():
            return

        total_frames = int(self.vid.get(cv2.CAP_PROP_FRAME_COUNT))
        
        # tally total frame num in cahce data and video
        if total_frames != self.cache_data.shape[0]:
            self.error_signal.emit('Video and cache frame count does not match')
            return

        # reinitialize dict for counting
        self.detected_vehicles = {class_id : {} for class_name, class_id in class_id_map.items()}

        # go to first frame
        self.vid.set(cv2.CAP_PROP_POS_FRAMES, 0)
            
        for frame_num, frame_data in enumerate(self.cache_data):
            _, frame = self.vid.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.bitwise_and(frame, frame, mask=self.imgMask)

            # for detection in frame_data:
            #     self.countVehicles(frame, frame_num, detection)
                        
        self.process_done_signal.emit()
                
    @Slot()
    def analyzeFrames(self):
        if not self.counting_timer.isActive():
            self.counting_timer.setInterval(30)
            self.counting_timer.start()   
            return

        success , frame = self.vid.read()
        if success and not self.stop_counting:
            frame_original = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.bitwise_and(frame_original, frame_original, mask=self.imgMask)
            frame_data = self.cache_data[self.frame_counter]

            for detection in frame_data:
                class_name = self.getClassName(str(detection[0]))
                uid = detection[1]
                x_min = detection[2]
                y_min = detection[3]
                x_max = detection[4]
                y_max = detection[5]

                # detected = self.countVehicles(frame, self.frame_counter, detection)
                frame = self.drawBoundingBox(frame_original, class_name, uid, x_min, y_min, x_max, y_max)

            self.frame_counter += 1
            self.frame_update_signal.emit(frame, self.frame_counter)
        else:
            self.stop_counting = True
            self.counting_timer.stop()
            self.frame_counter = 0
            self.process_done_signal.emit()
            
    @Slot()
    def stopCountingAnalysis(self):
        self.stop_counting = True

    @Slot()
    def startCountingAnalysis(self):
        self.counting_timer = QTimer()
        self.counting_timer.timeout.connect(self.analyzeFrames)
        if not self.validateInputFiles():
            return

        total_frames = int(self.vid.get(cv2.CAP_PROP_FRAME_COUNT))
        
        # tally total frame num in cahce data and video
        if total_frames != self.cache_data.shape[0]:
            self.error_signal.emit('Video and cache frame count does not match')
            return

        # reinitialize dict for counting
        self.detected_vehicles = {class_id : {} for class_name, class_id in class_id_map.items()}
        self.stop_counting = False
        # go to first frame
        self.vid.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.analyzeFrames()

    @Slot(int)
    def previewFrame(self, frame_num):
        if not self.validateInputFiles():
            return

        # go to specified frame
        self.vid.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        _, frame = self.vid.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


        # draw bb box 
        for detection in self.cache_data[frame_num]:
            class_name = self.getClassName(str(detection[0]))
            uid = detection[1]
            x_min = detection[2]
            y_min = detection[3]
            x_max = detection[4]
            y_max = detection[5]

            frame = self.drawBoundingBox(frame, class_name, uid, x_min, y_min, x_max, y_max)

        # draw counting annotation

        # update frame signal
        self.frame_update_signal.emit(frame, frame_num)

    def countVehiclesCustom(self, frame, frame_num, detection):
        try:
            class_id = detection[0]
            uid = str(detection[1])

            # xmin, ymin, xmax, ymax
            x_min = detection[2]
            y_min = detection[3]
            x_max = detection[4]
            y_max = detection[5]
            width = x_max - x_min
            height = y_max - y_min
            cx = x_min + (width / 2)
            cy = y_min + (height / 2)
            centroid = [cx, cy]
            tracker_dict = self.detected_vehicles[str(class_id)]

            # detecting for the first time
            if uid not in tracker_dict.keys() and uid not in self.cardinal_vehicle_counter.keys():
                tracker_dict[uid] = {
                    'initial_centroid' : [cx, cy], 
                    'prev_centroid': [cx, cy],
                    'prev_frame_num': frame_num,
                    'dist': 0,
                    'counted': False,
                    'in_cardinal_side':None,
                    'out_cardinal_side':None,
                    'check_out_cardinal_side':False,
                    'last_in_cardinal_side_frame_num':None,
                    'row_id':False
                }

            centroid_object_width = 5
            centroid_object_height = 5 
            
            object_polygon = Polygon([[cx-centroid_object_width, cy-centroid_object_height], [cx+centroid_object_width, cy-centroid_object_height], [cx+centroid_object_width, cy+centroid_object_height], [cx-centroid_object_width, cy+centroid_object_height]])

            if uid not in self.counted_ids:
                # compute distance traveled
                # print(tracker_dict)
                prev_centroid = tracker_dict[uid]['prev_centroid'] 
                tracker_dict[uid]['prev_centroid'] = centroid
                tracker_dict[uid]['prev_frame_num'] = frame_num
                if math.dist(prev_centroid, centroid) > 1 and tracker_dict[uid]['in_cardinal_side']:
                    tracker_dict[uid]['dist'] = tracker_dict[uid]['dist'] + math.dist(prev_centroid, centroid)

                for cardinal_side_id, cardinal_side in enumerate(self.cardinal_direction_points):
                    point_2 = [[point[0]+15, point[1]+15] for point in cardinal_side.copy()]
                    line2_start = point_2[0]
                    line2_end = point_2[1]
                    vertices = np.array([line2_start, line2_end, cardinal_side[1], cardinal_side[0]])
                    cardinal_side_polygon = Polygon(vertices)
                    is_intersects = cardinal_side_polygon.intersects(object_polygon)
                    # is_intersects = self.myTouches(cardinal_side_polygon, object_polygon)
                    if is_intersects:
                        # if tracker_dict[uid]['in_cardinal_side'] and tracker_dict[uid]['dist'] > 100:

                        # if centroid intersected with cardinal side and disappeared for 5 frames it will be counted as out cardina side 
                        if tracker_dict[uid]['in_cardinal_side'] and (frame_num - tracker_dict[uid]['last_in_cardinal_side_frame_num']) > 7 and tracker_dict[uid]['dist'] > 40:
                            tracker_dict[uid]['out_cardinal_side'] = self.CARDINAL_DIRECTIONS[cardinal_side_id]
                            row_id = f"{self.CARDINAL_DIRECTIONS.index(tracker_dict[uid]['in_cardinal_side'])}{self.CARDINAL_DIRECTIONS.index(tracker_dict[uid]['out_cardinal_side'])}"

                            if self.cardinal_vehicle_counter.get(row_id):
                                self.cardinal_vehicle_counter[row_id] += 1
                            else:
                                self.cardinal_vehicle_counter[row_id] = 1

                            # start = time()
                            img = self.getVehicleImage(detection, frame)
                            # exps = os.listdir(self.save_crops_path)

                            # if not self.images_root:
                            #     self.images_root = os.path.join(self.save_crops_path, str(len(exps)))

                            # if not Path(self.images_root).exists():
                            #     os.makedirs(self.images_root)

                            # image_path = os.path.join(self.images_root, str(class_id))

                            # if not Path(image_path).exists():
                            #     os.makedirs(image_path)

                            # image_save_path = os.path.join(image_path, f'{len(os.listdir(image_path))}.png')

                            # cv2.imwrite(os.path.join(image_save_path), img)

                            self.counted_ids.append(uid)
                            self.vehicle_counter[str(class_id)] += 1
                            # print('Get image aand create folders: ', time() - start)


                            # start = time()

                            self.db_cur.execute(f"""INSERT INTO vehicles(
                                                                id,
                                                                initial_centroid_x,
                                                                initial_centroid_y,
                                                                prev_centroid_x,
                                                                prev_centroid_y,
                                                                prev_frame_num,
                                                                dist,
                                                                counted,
                                                                in_cardinal_side,
                                                                out_cardinal_side,
                                                                type,
                                                                time,
                                                                camera_id,
                                                                row_id 
                                                            ) VALUES (
                                                                {uid},
                                                                {int(cx)},
                                                                {int(cy)},
                                                                {int(cx)},
                                                                {int(cy)},
                                                                {frame_num},
                                                                {0},
                                                                FALSE,
                                                                '{tracker_dict[uid]['in_cardinal_side']}',
                                                                '{tracker_dict[uid]['out_cardinal_side']}',
                                                                {class_id},
                                                                '{self.time_now}',
                                                                {self.cam_id},
                                                                '{row_id}'
                                                            )"""
                                    )
                            self.db_conn.commit()
                            # print('Inserting into db: ', time() - start)

                            # start = time()
                            print('Removed ID:  ', uid, class_id, tracker_dict[uid])
                            del tracker_dict[uid]
                            self.vehicle_count_signal.emit(class_id, int(uid), self.cardinal_vehicle_counter[row_id], img, row_id, self.vehicle_counter[str(class_id)]) 
                            # print('Remove vehicle and send to view_controller: ', time() - start)
                        else:
                            if not tracker_dict[uid]['in_cardinal_side']:
                                track_obj = self.trackableObjects.get(int(uid), None)
                                track_obj.start_classifying = True
                                self.trackableObjects[int(uid)] = track_obj
                                tracker_dict[uid]['in_cardinal_side'] = self.CARDINAL_DIRECTIONS[cardinal_side_id]
                                
                            tracker_dict[uid]['last_in_cardinal_side_frame_num'] = frame_num
                        break
                    else:
                        # print('Not intersected:  ', uid)
                        continue
        except KeyError:
            tracker_dict[uid] = {
                    'initial_centroid' : [cx, cy], 
                    'prev_centroid': [cx, cy],
                    'prev_frame_num': frame_num,
                    'dist': 0,
                    'counted': False,
                    'in_cardinal_side':None,
                    'out_cardinal_side':None,
                    'check_out_cardinal_side':False,
                    'last_in_cardinal_side_frame_num':None,
                    'row_id':False
                }

        except Exception as err:
            import traceback
            traceback.print_exc()
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            print('Custom count error:  ', err)

            

#==================== Inference Functions ========================
    def myTouches(self, poly1, poly2):
        return poly1.intersects(poly2) and not poly1.crosses(poly2) and not poly1.contains(poly2)

    def preprocess(img, imgsz, stride):
        img = letterbox(img, imgsz, stride=stride)[0]
        img = img.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
        img = np.ascontiguousarray(img)
        img = torch.from_numpy(img).to(device)
        img = img.float()
        img /= 255.0
        if len(img.shape) == 3:
            img = img[None]
        
        return img

    @Slot()
    def startInference(self):
        # for i in range(10):
        #     time.sleep(1)
        #     self.vehicle_count_signal.emit(6, 333, i, None, '00', 1)
        #     self.vehicle_count_signal.emit(6, 333, i+1, None, '01', 1)
        #     self.vehicle_count_signal.emit(6, 333, i+2, None, '02', 1)
        #     self.vehicle_count_signal.emit(6, 333, i+3, None, '03', 1)
        #     self.vehicle_count_signal.emit(6, 333, i+4, None, '10', 1)
        #     self.vehicle_count_signal.emit(6, 333, i+5, None, '11', 1)
        #     self.vehicle_count_signal.emit(6, 333, i+6, None, '12', 1)
        #     self.vehicle_count_signal.emit(6, 333, i+7, None, '13', 1)
        #     self.vehicle_count_signal.emit(6, 333, i+8, None, '20', 1)
        #     self.vehicle_count_signal.emit(6, 333, i+9, None, '21', 1)
        #     self.vehicle_count_signal.emit(6, 333, i+10, None, '22', 1)
        #     self.vehicle_count_signal.emit(6, 333, i+11, None, '23', 1)
        #     self.vehicle_count_signal.emit(6, 333, i+12, None, '30', 1)
        #     self.vehicle_count_signal.emit(6, 333, i+13, None, '31', 1)
        #     self.vehicle_count_signal.emit(6, 333, i+14, None, '32', 1)
        #     self.vehicle_count_signal.emit(6, 333, i+15, None, '33', 1)
        # self.input_video_path = './videos/test.mp4'
        # self.vid = cv2.VideoCapture(self.input_video_path)
        # _, frame = self.vid.read()
        # self.draw_line_widget = DrawLineWidget(frame)
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # self.frame_update_signal.emit(frame, 0)
        # self.cardinal_direction_points = self.draw_line_widget.list_coordinates
        # arguments for yolov5 model inference
        weights = ['./weights/vehicle.pt']  # model path or triton URL
        weights_cls = ['./weights/classification.pt']  # model path or triton URL
        # source = [os.path.join('./videos', os.listdir('videos')[0])]  # file/dir/URL/glob/screen/0(webcam)
        # source = [os.path.join('./videos', os.listdir('videos')[0])]
        # source = [r'F:\vehicle_count\14,03,2023\24 Format 02.12']
        data='yolov5/data/coco128.yaml'  # dataset.yaml path
        imgsz=1280  # inference size (height, width)
        conf_thres=0.5  # confidence threshold
        iou_thres=0.4  # NMS IOU threshold
        max_det=1000  # maximum detections per image
        device='cuda:0'  # cuda device, i.e. 0 or 0,1,2,3 or cpu
        classes=None  # filter by class: --class 0, or --class 0 2 3
        agnostic_nms=False  # class-agnostic NMS
        augment=False  # augmented inference
        dnn=False  # use OpenCV DNN for ONNX inference
        bs = 1

        # create polygon from cardinal lines
        # for cardinal_direction_positions, side_txt in zip(self.cardinal_direction_points[:4], ['A', 'B', 'C', 'D']):
        #     point_2 = [[point[0]+15, point[1]+15] for point in cardinal_direction_positions.copy()]
        #     line1_start = point_2[0]
        #     line1_end = point_2[1]
        #     # cv2.line(original_frame, line1_start, line1_end, (255, 0, 0), 2)
        #     # cv2.line(original_frame, cardinal_direction_positions[0], cardinal_direction_positions[1], (0, 255, 0), 2)

        #     vertices = np.array([line1_start, line1_end, cardinal_direction_positions[1], cardinal_direction_positions[0]])
        #     cv2.fillConvexPoly(original_frame, vertices, (0, 255, 0))

        # Load model
        device = select_device()
        try:
            model = DetectMultiBackend(weights, device=device, dnn=dnn, data=data)
            model_cls = DetectMultiBackend(weights_cls, device=device, dnn=dnn, data=data)
        except Exception as err:
            print('Error init', err)
        
        stride, class_names, classes, pt = model.stride, list(model.names.values()), model.names, model.pt
        imgsz = check_img_size(imgsz, s=stride)  # check image size

        # Load dataset
        if self.use_video:
            dataset = LoadImages(self.source, imgsz, stride, pt)
            print('FPS:  ', dataset.fps)
            self.time_now = datetime.datetime.now()
            self.add_time = datetime.timedelta(seconds=1/dataset.fps)
            self.cam_id = 0
        else:
            # dataset = LoadHikvisionCamera(ip=self.cam_ip if self.cam_ip.startswith('http') else f'http://{self.cam_ip}', username=self.cam_username, password=self.cam_password, display_name=self.cam_name, cam_id=self.cam_id, imgsz=imgsz, stride=stride, auto=pt)
            rtsp_stream = f'rtsp://{self.cam_username}:{self.cam_password}@{self.cam_ip}:554/Streaming/Channels/101'
            # rtsp_stream = 'http://46.151.101.134:8082/?action=stream'
            dataset = LoadStreams(rtsp_stream, img_size=imgsz, stride=stride, auto=pt)
            bs = len(dataset)

        # print('Dataset initializded')

        model.warmup(imgsz=(1 if pt or model.triton else bs, 3, *imgsz))  # warmup
        seen, windows, dt = 0, [], (Profile(), Profile(), Profile())

        self.stop_inference = False
        self.detected_vehicles = {class_id : {} for class_name, class_id in class_id_map.items()}

        # go to first frame
        # self.vid.set(cv2.CAP_PROP_POS_FRAMES, 0)
        # self.max_frame_update_signal.emit(total_frames)

        frame_num = 0
        self.stop_counting = False
        # [[(292, 426), (752, 258)], [(796, 300), (902, 438)], [(896, 442), (576, 636)], [(318, 422), (506, 602)]]
        x_list = []
        y_list = []
        print('Use video', self.use_video)
        if self.cardinal_direction_points:
            for line in self.cardinal_direction_points:
                for point in line:
                    x_list.append(point[0])
                    y_list.append(point[1])
        # self.det_area_x0 = min(x_list) - self.margin 
        # self.det_area_y0 = min(y_list) - self.margin
        # self.det_area_x1 = max(x_list) + self.margin
        # self.det_area_y1 = max(y_list) + self.margin
        
        for i, (path, im, im0s) in enumerate(dataset):
            try:
                # print('Use video', self.use_video)
                start_time = time()
                if self.stop_counting:
                    self.counted_ids = []
                    self.vehicle_counter = {'0': 0,'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '':0}
                    self.cardinal_vehicle_counter = dict()
                    break
                if self.use_video:
                    self.time_now += self.add_time
                
                ################
                # self.det_area_x0 = max(0, self.det_area_x0)
                # self.det_area_y0 = max(0, self.det_area_y0)
                # self.det_area_x1 = min(self.det_area_x1, original_frame.shape[1])
                # self.det_area_y1 = min(self.det_area_y1, original_frame.shape[0])
               
                # cv2.rectangle(original_frame, (self.det_area_x0, self.det_area_y0), (self.det_area_x1, self.det_area_y1), (0,255,0), 2)
                # det_area = im[self.det_area_y0:self.det_area_y1, self.det_area_x0:self.det_area_x1]
                # det_area = im.copy()

                # im = letterbox(im, imgsz, stride=stride)[0]  # padded resize
                # im = im.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
                # im = np.ascontiguousarray(im)  # contiguous
                ###############
                frame_num += 1
                frame_data = np.zeros((MAX_DETECTION_NUM, 6), dtype=int)
                im = torch.from_numpy(im).to(model.device)
                im = im.float()  # uint8 to fp16/32
                im /= 255  # 0 - 255 to 0.0 - 1.0
                if len(im.shape) == 3:
                    im = im[None]  # expand for batch dim

                # Inference
                pred = model(im, augment=augment, visualize=False)

                # NMS
                pred = non_max_suppression(pred, conf_thres, iou_thres, None, agnostic_nms, max_det=max_det)

                bboxes, scores, classes = [], [], []
                
                # print('Predictions', pred)
                # Process predictions
                for i, det in enumerate(pred):  # per image
                    if not self.use_video:
                        original_frame = im0s[i].copy()
                        frame_for_cls = im0s[i].copy()
                    else:
                        original_frame = im0s.copy()
                        frame_for_cls = im0s.copy()
                    seen += 1
                    # p, im0, frame = path, im0s.copy(), getattr(dataset, 'frame', 0)
                    if len(det):
                        # print('Detes', det)
                        # Rescale boxes from img_size to im0 size
                        det[:, :4] = scale_boxes(im.shape[2:], det[:, :4], im0s.shape).round()
                        # Write results
                        for *xyxy, conf, cls in reversed(det):
                            class_indx = int(cls.cpu())
                            class_name = class_names[class_indx]
                            # if class_name not in self.allowed_classes:
                            #     continue
                            classes.append(cls.cpu())
                            scores.append(conf.cpu())
                            # print(xyxy)
                            xmin, ymin, xmax, ymax = xyxy
                            # xmin, ymin, xmax, ymax = xmin.cpu()+self.det_area_x0, ymin.cpu()+self.det_area_y0, xmax.cpu() + self.det_area_x0, ymax.cpu()+self.det_area_y0
                            xmin, ymin, xmax, ymax = xmin.cpu(), ymin.cpu(), xmax.cpu(), ymax.cpu()
                            bboxes.append(np.array([xmin, ymin, xmax, ymax]))
                           
                            # # print('*()*&)(*&)(*&)(*&)(*&)(*&)(&*)(*&)(*&)(*&)(*&)(*&)')
                            # xmin, ymin, w, h = xmin.cpu(), ymin.cpu(), xmax.cpu()-xmin.cpu(), ymax.cpu()-ymin.cpu()
                            # bboxes.append(np.array([xmin.cpu(), ymin.cpu(), w.cpu(), h.cpu()]))
                objects = sort_tracker.update(np.array(bboxes), np.array(classes), np.array(scores))
                obj_num = 0
                # print("len objs: ", len(objects))
                for i in self.trackableObjects:
                    track_obj = self.trackableObjects.get(i, None)
                    if track_obj is None:
                        continue
                    track_obj.live = False
                    self.trackableObjects[i] = track_obj
                for obj in objects:
                    # print(obj)
                    objectID = obj[1]
                    x_min, y_min, x_max, y_max = int(obj[2]), int(obj[3]), int(obj[4]), int(obj[5])
                    track_obj = self.trackableObjects.get(objectID, None)

                    if track_obj is None:
                        track_obj = TrackableObject(objectID, x_min, y_min, x_max, y_max, 0, 0, im0s.shape[1], im0s.shape[0])
                    
                    # if objectID == 205:
                    # print('Id', objectID, track_obj.area, track_obj.walk_distance)

                    # if not track_obj.classified:
                    #     track_obj.can_start_classifying(x_min, y_min, x_max, y_max)

                    if track_obj.class_name < 0:
                        class_name = ''
                    else:
                        class_name = self.allowed_classes[track_obj.class_name]

                    if  (not track_obj.classified) and (track_obj.start_classifying) and (track_obj.count_classification < 10):
                        track_obj.count_classification += 1
                        param = {
                                "org_img": frame_for_cls,
                                "bbox": [x_min, y_min, x_max-x_min, y_max-y_min],
                                "scale": 1,
                                "out_w": 64,
                                "out_h": 64,
                                "crop": True,
                                    }
                        crop = self.image_cropper.crop(**param)
                        # crop = im0s[y_min:y_max, x_min:x_max]
                        class_name = self.get_class_name(crop, model_cls)
                        if class_name == 6:
                            class_name = 0
                        track_obj.class_occurances[class_name] += 1
                        track_obj.class_name = track_obj.class_occurances.index(max(track_obj.class_occurances))
                        class_name = self.allowed_classes[track_obj.class_name]
                        if not os.path.exists(self.images_root):
                            os.makedirs(self.images_root)
                        image_path = os.path.join(self.images_root, str(class_name))

                        if not Path(image_path).exists():
                            os.makedirs(image_path)

                        image_save_path = os.path.join(image_path, f'{len(os.listdir(image_path))}.png')

                        cv2.imwrite(os.path.join(image_save_path), crop)
                    # if  not track_obj.classified and track_obj.start_classifying:
                    #     param = {
                    #             "org_img": frame_for_cls,
                    #             "bbox": [x_min, y_min, x_max-x_min, y_max-y_min],
                    #             "scale": 1,
                    #             "out_w": 64,
                    #             "out_h": 64,
                    #             "crop": True,
                    #                 }
                    #     crop = self.image_cropper.crop(**param)
                    #     # crop = im0s[y_min:y_max, x_min:x_max]
                    #     class_name = self.get_class_name(crop, model_cls)
                    #     if class_name == 6:
                    #         class_name = 0
                    #     track_obj.class_name=class_name
                    #     track_obj.classified = True
                    #     class_name = self.allowed_classes[track_obj.class_name]
                    #     if not os.path.exists(self.images_root):
                    #         os.makedirs(self.images_root)
                    #     image_path = os.path.join(self.images_root, str(class_name))

                    #     if not Path(image_path).exists():
                    #         os.makedirs(image_path)

                    #     image_save_path = os.path.join(image_path, f'{len(os.listdir(image_path))}.png')

                    #     cv2.imwrite(os.path.join(image_save_path), crop)

                    class_id = self.getClassId(class_name)
                    track_obj.live=True
                    track_obj.lost_count=0
                    self.trackableObjects[objectID] = track_obj

                    frame_data[obj_num] = [class_id, objectID, x_min, y_min, x_max, y_max]
                    # print()
                    self.countVehiclesCustom(original_frame, frame_num, frame_data[obj_num])
                    x_min = frame_data[obj_num][2]
                    y_min = frame_data[obj_num][3]
                    x_max = frame_data[obj_num][4]
                    y_max = frame_data[obj_num][5]
                    width = x_max - x_min
                    height = y_max - y_min
                    cx = x_min + (width / 2)
                    cy = y_min + (height / 2)
                    centroid_object_width = 5
                    centroid_object_height = 5 
                    centroid_xmin = int(cx-centroid_object_width)
                    centroid_ymin = int(cy-centroid_object_height)
                    centroid_xmax = int(cx+centroid_object_width)
                    centroid_ymax = int(cy+centroid_object_height)
                    
                    # object_polygon = Polygon([[cx-centroid_object_width, cy-centroid_object_height], [cx+centroid_object_width, cy-centroid_object_height], [cx+centroid_object_width, cy+centroid_object_height], [cx-centroid_object_width, cy+centroid_object_height]])

                    original_frame = cv2.rectangle(original_frame, (centroid_xmin, centroid_ymin), (centroid_xmax, centroid_ymax), (255, 0, 255), 2)

                    # draw bbox on screen
                    original_frame = self.drawBoundingBox(original_frame, class_name, objectID, x_min, y_min, x_max, y_max)
                    
                    obj_num = obj_num +  1
                need_to_remove = []
                for i in self.trackableObjects:
                    track_obj = self.trackableObjects.get(i, None)
                    if track_obj is None:
                        continue
                    if not track_obj.live:
                        track_obj.lost_count+=1
                        self.trackableObjects[i] = track_obj
                    if track_obj.lost_count>25:
                         need_to_remove.append(i)
                for i in need_to_remove:
                    del self.trackableObjects[i]



                # draw cardinal directions
                # print(len(self.cardinal_direction_points))
                for cardinal_direction_positions, side_txt in zip(self.cardinal_direction_points[:4], ['A', 'B', 'C', 'D']):
                    point_2 = [[point[0]+15, point[1]+15] for point in cardinal_direction_positions.copy()]
                    line1_start = point_2[0]
                    line1_end = point_2[1]
                    # cv2.line(original_frame, line1_start, line1_end, (255, 0, 0), 2)
                    # cv2.line(original_frame, cardinal_direction_positions[0], cardinal_direction_positions[1], (0, 255, 0), 2)
                    vertices = np.array([line1_start, line1_end, cardinal_direction_positions[1], cardinal_direction_positions[0]])
                    cv2.fillConvexPoly(original_frame, vertices, (0, 255, 0))

                    # cardinal_side_polygon = Polygon(cardinal_side_copy)
                    # original_frame = cv2.polylines(original_frame, cardinal_side_copy, True, self.draw_color)
                    side_xmin = min([cardinal_direction_positions[0][0], cardinal_direction_positions[1][0]])
                    side_xmax = max([cardinal_direction_positions[0][0], cardinal_direction_positions[1][0]])
                    side_ymin = min([cardinal_direction_positions[0][1], cardinal_direction_positions[1][1]])
                    side_ymax = max([cardinal_direction_positions[0][1], cardinal_direction_positions[1][1]])
                    # rect_start = (min(side_xmin, side_xmax)-10, min(side_ymin, side_ymax)-10)
                    # rect_end = (max(side_xmin, side_xmax)+10, max(side_ymin, side_ymax)+10)
                    # cv2.rectangle(original_frame, rect_start, rect_end, self.draw_color, 2)


                    side_width = abs(side_xmax - side_xmin)
                    side_height = abs(side_ymax - side_ymin)
                    text_x = int(side_xmin + (side_width / 2))
                    text_y = int(side_ymin + (side_height / 2))
                    cv2.putText(original_frame, 
                                side_txt, 
                                (text_x, text_y), 
                                cv2.FONT_HERSHEY_SIMPLEX, 3, 
                                self.draw_color,  
                                2, 
                                cv2.LINE_4)
                    # original_frame = cv2.line(original_frame, cardinal_direction_positions[0], cardinal_direction_positions[1], self.draw_color, 3)

                # update frame on UI
                self.frame_update_signal.emit(cv2.cvtColor(original_frame, cv2.COLOR_BGR2RGB), frame_num)
                fps = 1/(time()-start_time)
                print(fps)


                # print('Frame #: ', frame_num)
            except Exception as err:
                import traceback
                traceback.print_exc()
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print('Inference stopped with error:  ', err)

        print('INFERENCE STOPPED')

        self.process_done_signal.emit()

    def stopInference(self):
        self.stop_inference = True

#==================== Helper Functions ========================

    def getVehicleImage(self, detection, frame) -> np.ndarray:
        # xmin, ymin, xmax, ymax
        x_min = detection[2]
        y_min = detection[3]
        x_max = detection[4]
        y_max = detection[5]
        width = x_max - x_min
        height = y_max - y_min

        img = frame[y_min:y_max, x_min:x_max]
        return np.ascontiguousarray(img)

    def getClassId(self, class_name:str) -> int:
        id = class_id_map.get(class_name)
        if id is None:
            id = 0
        return id

    def getClassName(self, class_id:int) -> str:
        name =  class_id_map.get(class_id)
        return name

    def drawBoundingBox(self, frame:np.ndarray, class_name:str, id:int, x_min, y_min, x_max, y_max, highlight=False):
        # print(self.colors)
        # color = self.colors[id % len(self.colors)]
        color = self.colors[self.allowed_classes.index(class_name)]
        if self.text_translator.lang == 'uz':
            class_name = self.text_translator.class_names[class_name]
        # color = [i * 255 for i in color]
        cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), color, 2)
        cv2.rectangle(frame, (x_min, y_min-30), (x_min+(len(class_name)+len(str(id)) )*17, y_min), color, -1)
        cv2.putText(frame, class_name + "-" + str(id),(x_min, int(y_min-10)),0, 0.75, (255,255,255),2)

        if highlight:
            # highlight in green
            frame[y_min:y_max, x_min:x_max, 0] = 0
            frame[y_min:y_max, x_min:x_max, 2] = 0
        return frame


if __name__ == "__main__":
    model = Model()
    model.startInference()
