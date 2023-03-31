import math


class TrackableObject:
	def __init__(self, objectID, xmin, ymin, xmax, ymax, det_area_xmin, det_area_ymin, det_area_xmax, det_area_ymax):
		self.det_area_xmin = det_area_xmin
		self.det_area_ymin = det_area_ymin
		self.det_area_xmax = det_area_xmax
		self.det_area_ymax = det_area_ymax

		self.classified = False
		self.start_classifying = False
		self.start_classifying_margin = 40
		self.track_side_index = -1

		self.count_classification = 0

		self.class_occurances = [0, 0, 0, 0, 0, 0]

		self.find_min_side(xmin, ymin, xmax, ymax)

		width = xmax - xmin
		height = ymax - ymin
		cx = xmin + (width / 2)
		cy = ymin + (height / 2)
		self.objectID = objectID
		self.class_name = -1
		self.area = width * height
		self.prev_centroid = [cx, cy]
		self.walk_distance = 0
	
	def calculate_distance(self, xmin, ymin, xmax, ymax):
		width = xmax - xmin
		height = ymax - ymin
		cx = xmin + (width / 2)
		cy = ymin + (height / 2)
		self.area = width * height
		self.walk_distance += math.dist(self.prev_centroid, [cx, cy])
		self.prev_centroid = [cx, cy]
	
	def find_min_side(self, xmin, ymin, xmax, ymax):
		xmin_distance = xmin-self.det_area_xmin
		ymin_distance = ymin-self.det_area_ymin
		xmax_distance = self.det_area_xmax-xmax
		ymax_distance = self.det_area_ymax-ymax
		distances = [xmin_distance, ymin_distance, xmax_distance, ymax_distance]
		self.track_side_index = distances.index(min(distances)) 

	
	def can_start_classifying(self, xmin, ymin, xmax, ymax):
		xmin_distance = xmin-self.det_area_xmin
		ymin_distance = ymin-self.det_area_ymin
		xmax_distance = self.det_area_xmax-xmax
		ymax_distance = self.det_area_ymax-ymax
		self.distances = [xmin_distance, ymin_distance, xmax_distance, ymax_distance]
		# print('-->', self.objectID, min(self.distances))
		self.start_classifying = True if self.distances[self.track_side_index] > self.start_classifying_margin else False
