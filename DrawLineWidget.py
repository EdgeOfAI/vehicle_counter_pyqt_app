import cv2


class DrawLineWidget(object):
    def __init__(self, img):
        self.original_image = img.copy()
        self.clone = self.original_image.copy()
        self.clone2 = self.original_image.copy()
        self.font = cv2.FONT_HERSHEY_SIMPLEX

        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.extract_coordinates)

        # List to store start/end points
        self.image_coordinates = []
        self.list_coordinates = []

        # Use putText() method for inserting text on video
        cv2.putText(self.clone2, 
                    f'Draw NORTH side line', 
                    (50, 50), 
                    self.font, 1, 
                    (0, 0, 255), 
                    2, 
                    cv2.LINE_4)

    def extract_coordinates(self, event, x, y, flags, parameters):
        
        # Record starting (x,y) coordinates on left mouse button click
        if event == cv2.EVENT_LBUTTONDOWN:
            self.image_coordinates = [(x,y)]

        # Record ending (x,y) coordintes on left mouse bottom release
        elif event == cv2.EVENT_LBUTTONUP:
            self.image_coordinates.append((x,y))
            print('Starting: {}, Ending: {}'.format(self.image_coordinates[0], self.image_coordinates[1]))
            self.list_coordinates.append([self.image_coordinates[0], self.image_coordinates[1]])
            # Draw line
            cv2.line(self.clone, self.image_coordinates[0], self.image_coordinates[1], (36,255,12), 2)
            cv2.line(self.clone2, self.image_coordinates[0], self.image_coordinates[1], (36,255,12), 2)

            num_coordinates = len(self.list_coordinates)
            if num_coordinates == 0:
                coordinal_side_text = 'NORTH'
            elif num_coordinates == 1:
                coordinal_side_text = 'EAST'
            elif num_coordinates == 2:
                coordinal_side_text = 'WEST'
            elif num_coordinates == 3:
                coordinal_side_text = 'SOUTH'
            else:
                coordinal_side_text = ''
            
            self.clone2 = self.clone.copy()
            
            text = f'Draw {coordinal_side_text} side line'

            if coordinal_side_text:
                # Use putText() method for inserting text on video
                cv2.putText(self.clone2, 
                            text, 
                            (50, 50), 
                            self.font, 1, 
                            (0, 0, 255),  
                            2, 
                            cv2.LINE_4)

            cv2.imshow("image", self.clone2) 

        # Clear drawing boxes on right mouse button click
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.clone = self.original_image.copy()

    def show_image(self):
        return self.clone2