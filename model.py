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
# SORT tracker
from utils.sort_tracker import SORT
trackers = []
sort_tracker = SORT(max_lost=25, iou_threshold=0.3)
trackableObjects = {}

########################################
MAX_DETECTION_NUM = 500



class_id_map = {
    'none'  : '0',
    'truck' : '1',
    'car'   : '2',
    'bus'   : '3',
    'bicycle': '4',
    'motorcycle': '5'
}
class_id_map.update({item[1]: item[0] for item in class_id_map.items()})

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
        self.save_crops_path = './images'
        if not Path(self.save_crops_path).exists():
            os.makedirs(self.save_crops_path)
        self.CARDINAL_DIRECTIONS = ['North', 'East', 'West', 'South']
        self.allowed_classes = ['truck', 'car', 'bus', 'bicycle', 'motorcycle']
        self.vehicle_counter = {'1':0, '2':0, '3':0, '4':0, '5':0}  # 1 truck, 2 car, 3 bus, 4 bicycle, 5 motorcycle
        self.initialize_counting()
        self.images_root = None

        self.db_conn = conn 
        self.db_cur = cur 

        #initialize color map
        cmap = plt.get_cmap('tab20b')
        self.colors = [(255, 89, 94), (255, 202, 58), (138, 201, 38), (25, 130, 196), (106, 76, 147)]  # colors which are being used https://coolors.co/palette/ff595e-ffca3a-8ac926-1982c4-6a4c93

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
                frame = self.drawBoundingBox(frame_original, class_name, uid, x_min, y_min, x_max, y_max, detected)

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
                    'row_id':False
                }
            
            object_polygon = Polygon([[x_min, y_min], [x_max, y_min], [x_max, y_max], [x_min, y_max]])

            if uid not in self.counted_ids:
                # compute distance traveled
                prev_centroid = tracker_dict[uid]['prev_centroid'] 
                tracker_dict[uid]['prev_centroid'] = centroid
                tracker_dict[uid]['prev_frame_num'] = frame_num
                if math.dist(prev_centroid, centroid) > 1 and tracker_dict[uid]['in_cardinal_side']:
                    tracker_dict[uid]['dist'] = tracker_dict[uid]['dist'] + math.dist(prev_centroid, centroid)

                for cardinal_side_id, cardinal_side in enumerate(self.cardinal_direction_points):
                    cardinal_side_copy = cardinal_side.copy() + [[point[0]+5, point[1]+5] for point in cardinal_side.copy()]
                    cardinal_side_polygon = Polygon(cardinal_side_copy)
                    is_intersects = self.myTouches(cardinal_side_polygon, object_polygon)
                    if is_intersects:
                        if tracker_dict[uid]['in_cardinal_side'] and tracker_dict[uid]['dist'] > 300:
                            tracker_dict[uid]['out_cardinal_side'] = self.CARDINAL_DIRECTIONS[cardinal_side_id]
                            row_id = f"{self.CARDINAL_DIRECTIONS.index(tracker_dict[uid]['in_cardinal_side'])}{self.CARDINAL_DIRECTIONS.index(tracker_dict[uid]['out_cardinal_side'])}"
                            if self.cardinal_vehicle_counter.get(row_id):
                                self.cardinal_vehicle_counter[row_id] += 1
                            else:
                                self.cardinal_vehicle_counter[row_id] = 1
                            img = self.getVehicleImage(detection, frame)
                            exps = os.listdir(self.save_crops_path)
                            if not self.images_root:
                                self.images_root = os.path.join(self.save_crops_path, str(len(exps)))
                            if not Path(self.images_root).exists():
                                os.makedirs(self.images_root)
                            image_path = os.path.join(self.images_root, str(class_id))
                            if not Path(image_path).exists():
                                os.makedirs(image_path)
                            image_save_path = os.path.join(image_path, f'{len(os.listdir(image_path))}.png')
                            cv2.imwrite(os.path.join(image_save_path), img)
                            self.counted_ids.append(uid)
                            self.vehicle_counter[str(class_id)] += 1
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
                            del tracker_dict[uid]
                            self.vehicle_count_signal.emit(class_id, int(uid), self.cardinal_vehicle_counter[row_id], img, row_id, self.vehicle_counter[str(class_id)])
                        else:
                            tracker_dict[uid]['in_cardinal_side'] = self.CARDINAL_DIRECTIONS[cardinal_side_id]
                        break
        except Exception as err:
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
        # self.input_video_path = './videos/test.mp4'
        # self.vid = cv2.VideoCapture(self.input_video_path)
        # _, frame = self.vid.read()
        # self.draw_line_widget = DrawLineWidget(frame)
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # self.frame_update_signal.emit(frame, 0)
        # self.cardinal_direction_points = self.draw_line_widget.list_coordinates
        # arguments for yolov5 model inference
        weights = ['./weights/vehicle.pt']  # model path or triton URL
        source = [os.path.join('./videos', os.listdir('videos')[0])]  # file/dir/URL/glob/screen/0(webcam)
        # source = 'https://www.youtube.com/watch?v=GgriNm5S2WE'
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

        # Load model
        device = select_device()
        model = DetectMultiBackend(weights, device=device, dnn=dnn, data=data)
        stride, class_names, classes, pt = model.stride, list(model.names.values()), model.names, model.pt
        imgsz = check_img_size(imgsz, s=stride)  # check image size

        # Load dataset
        if self.use_video:
            dataset = LoadImages(source, imgsz, stride, pt)
            print('FPS:  ', dataset.fps)
            self.time_now = datetime.datetime.now()
            self.add_time = datetime.timedelta(seconds=1/dataset.fps)
        else:
            dataset = LoadHikvisionCamera(ip=self.cam_ip if self.cam_ip.startswith('http') else f'http://{self.cam_ip}', username=self.cam_username, password=self.cam_password, display_name=self.cam_name, cam_id=self.cam_id, imgsz=imgsz, stride=stride, auto=pt)
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
        
        for path, im, im0s in dataset:
            try:
                start_time = time()
                if self.stop_counting:
                    self.counted_ids = []
                    break
                if self.use_video:
                    self.time_now += self.add_time
                original_frame = im0s.copy()
                frame_num += 1
                frame_data = np.zeros((MAX_DETECTION_NUM, 6), dtype=int)
                im = torch.from_numpy(im).to(model.device)
                im = im.half() if model.fp16 else im.float()  # uint8 to fp16/32
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
                    seen += 1
                    p, im0, frame = path, im0s.copy(), getattr(dataset, 'frame', 0)

                    if len(det):
                        # print('Detes', det)
                        # Rescale boxes from img_size to im0 size
                        det[:, :4] = scale_boxes(im.shape[2:], det[:, :4], im0.shape).round()
                        # Write results
                        for *xyxy, conf, cls in reversed(det):
                            class_indx = int(cls.cpu())
                            class_name = class_names[class_indx]
                            if class_name not in self.allowed_classes:
                                continue
                            classes.append(cls.cpu())
                            scores.append(conf.cpu())
                            # print(xyxy)
                            xmin, ymin, xmax, ymax = xyxy
                            bboxes.append(np.array([xmin.cpu(), ymin.cpu(), xmax.cpu(), ymax.cpu()]))
                            # # print('*()*&)(*&)(*&)(*&)(*&)(*&)(&*)(*&)(*&)(*&)(*&)(*&)')
                            # xmin, ymin, w, h = xmin.cpu(), ymin.cpu(), xmax.cpu()-xmin.cpu(), ymax.cpu()-ymin.cpu()
                            # bboxes.append(np.array([xmin.cpu(), ymin.cpu(), w.cpu(), h.cpu()]))

                objects = sort_tracker.update(np.array(bboxes), np.array(classes), np.array(scores))
                obj_num = 0
                for obj in objects:
                    # print(obj)
                    objectID = obj[1]
                    x_min, y_min, x_max, y_max = int(obj[2]), int(obj[3]), int(obj[4]), int(obj[5])
                    class_name = class_names[int(obj[6])]
                    class_id = self.getClassId(class_name)
                    frame_data[obj_num] = [class_id, objectID, x_min, y_min, x_max, y_max]

                    # Count vehicles
                    # print('I am in')
                    # print('Before custom vehicles count')
                    self.countVehiclesCustom(original_frame, frame_num, frame_data[obj_num])
                    # print('After custom vehicle count')
                    # detected = self.countVehicles(original_frame, frame_num, frame_data[obj_num])

                    # draw bbox on screen
                    original_frame = self.drawBoundingBox(original_frame, class_name, objectID, x_min, y_min, x_max, y_max)
                    
                    obj_num = obj_num +  1


                # draw cardinal directions
                # print(len(self.cardinal_direction_points))
                for cardinal_direction_positions, side_txt in zip(self.cardinal_direction_points[:4], ['A', 'B', 'C', 'D']):
                    cv2.putText(original_frame, 
                                side_txt, 
                                (cardinal_direction_positions[0][0], cardinal_direction_positions[0][1]), 
                                cv2.FONT_HERSHEY_SIMPLEX, 3, 
                                self.draw_color,  
                                2, 
                                cv2.LINE_4)
                    original_frame = cv2.line(original_frame, cardinal_direction_positions[0], cardinal_direction_positions[1], self.draw_color, 3)

                # update frame on UI
                self.frame_update_signal.emit(cv2.cvtColor(original_frame, cv2.COLOR_BGR2RGB), frame_num)
                fps = 1/(time()-start_time)
                print(fps)


                # print('Frame #: ', frame_num)
            except Exception as err:
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
