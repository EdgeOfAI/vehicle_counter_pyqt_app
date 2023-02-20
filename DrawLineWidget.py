import cv2


class DrawLineWidget(object):
    def __init__(self, img, db_conn=None, db_cur=None, added_cam_id=-1):
        self.original_image = img.copy()
        self.clone = self.original_image.copy()
        self.clone2 = self.original_image.copy()
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.db_conn = db_conn
        self.db_cur = db_cur
        self.cam_id = added_cam_id

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
            if num_coordinates == 1:
                coordinal_side_text = 'NORTH'
                update_cardial_sides_query = ''
            elif num_coordinates == 2:
                coordinal_side_text = 'EAST'
                # write north coordinates into database
                update_cardial_sides_query = f'Update cameras set nx1 = {self.image_coordinates[0][0]}, ny1 = {self.image_coordinates[0][1]}, nx2 = {self.image_coordinates[1][0]}, ny2 = {self.image_coordinates[1][1]} where id = {self.cam_id}'

            elif num_coordinates == 3:
                coordinal_side_text = 'WEST'
                # write east coordinates into database
                update_cardial_sides_query = f'Update cameras set ex1 = {self.image_coordinates[0][0]}, ey1 = {self.image_coordinates[0][1]}, ex2 = {self.image_coordinates[1][0]}, ey2 = {self.image_coordinates[1][1]} where id = {self.cam_id}'

            elif num_coordinates == 4:
                coordinal_side_text = 'SOUTH'
                # write west coordinates into database
                update_cardial_sides_query = f'Update cameras set wx1 = {self.image_coordinates[0][0]}, wy1 = {self.image_coordinates[0][1]}, wx2 = {self.image_coordinates[1][0]}, wy2 = {self.image_coordinates[1][1]} where id = {self.cam_id}'

            elif num_coordinates == 5:
                coordinal_side_text = ''
                # write south coordinates into database
                update_cardial_sides_query = f'Update cameras set sx1 = {self.image_coordinates[0][0]}, sy1 = {self.image_coordinates[0][1]}, sx2 = {self.image_coordinates[1][0]}, sy2 = {self.image_coordinates[1][1]} where id = {self.cam_id}'

            else:
                coordinal_side_text = ''
                update_cardial_sides_query = None
            
            if update_cardial_sides_query and self.cam_id > 0:
                self.db_cur.execute(update_cardial_sides_query)
                self.db_conn.commit()
            
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