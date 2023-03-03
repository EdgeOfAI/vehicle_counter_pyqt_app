class Translator:
    def __init__(self):
        self.lang = 'eng'

        self.main_window_title = ''
        self.add_camera_btn = ''
        self.edit_camera_btn = ''
        self.remove_camera_btn = ''
        self.show_data_btn = ''
        self.use_video_checkbox = ''
        self.cars = ''
        self.buses = ''
        self.bicycles = ''
        self.motorcycles = ''
        self.trucks = ''
        self.a_in = ''
        self.b_in = ''
        self.c_in = ''
        self.d_in = ''
        self.a_out = ''
        self.b_out = ''
        self.c_out = ''
        self.d_out = ''
        self.start_inference_btn = ''
        self.stop_process_btn = ''

        # add camera window translations
        self.add_cam_window_title = ''
        self.add_cam_window_cam_ip = ''
        self.add_cam_window_cam_username = ''
        self.add_cam_window_cam_password = ''
        self.add_cam_window_cam_display_name = ''
        self.add_cam_window_add_cam_btn = ''

        # edit camera window translations
        self.edit_cam_window_title = ''
        self.edit_cam_window_IP = ''
        self.edit_cam_window_username = ''
        self.edit_cam_window_password = ''
        self.edit_cam_window_display_name = ''
        self.edit_cam_window_edit_btn = ''

        # remove camera window translations
        self.remove_camera_window_title = ''
        self.remove_camera_window_camera_names = ''
        self.remove_camera_window_remove_camera = ''

        # show calendar window  translations
        self.show_calendar_window_title = ''
        self.show_calendar_window_show_data_hourly = ''
        self.show_calendar_window_show_data_cardinalwise = ''
        self.show_calendar_window_download_excel_data = ''

        # pop up messages 
        self.information = ''
        self.warning = ''
        self.add_camera_popup_success = ''
        self.add_camera_popup_error = ''
        self.edit_camera_popup_success = ''
        self.remove_camera_popup_success = ''
        self.excel_data_written_success = ''
        self.num_cameras_exceeded = ''
        self.no_cameras_found_error = ''

        self.week_days = {
            'Sun': 'Yak',
            'Mon': "Dush",
            'Tue': 'Sesh',
            'Wed': 'Chor',
            'Thu': 'Pay',
            'Fri': 'Jum',
            'Sat': 'Shan'
        }

        self.months = {
            'Jan':'Yan',
            'Feb':'Fev',
            'Mar':'Mar',
            'Apr':'Apr',
            'May':'May',
            'Jun':'Iyun',
            'Jul':'Iyul',
            'Aug':'Avg',
            'Sep':'Sen',
            'Oct':'Okt',
            'Nov':'Noy',
            'Dec':'Dek',
        }
    
    def translateToEnglish(self):
        self.lang = 'eng'

        self.main_window_title = 'Traffic Vehicle Counter'
        self.add_camera_btn = 'Add Camera'
        self.edit_camera_btn = 'Edit Camera'
        self.remove_camera_btn = 'Remove Camera'
        self.show_data_btn = 'Show Data'
        self.use_video_checkbox = 'Use Video'
        self.cars = 'Cars'
        self.buses = 'Buses'
        self.bicycles = 'Bicycles'
        self.motorcycles = 'Motorcycles'
        self.trucks = 'Trucks'
        self.a_in = 'A in'
        self.b_in = 'B in'
        self.c_in = 'C in'
        self.d_in = 'D in'
        self.a_out = 'A out'
        self.b_out = 'B out'
        self.c_out = 'C out'
        self.d_out = 'D out'
        self.start_inference_btn = 'START'
        self.stop_process_btn = 'STOP'

        # add camera window translations
        self.add_cam_window_title = 'Add Camera'
        self.add_cam_window_cam_ip = 'Camera IP'
        self.add_cam_window_cam_username = 'Username'
        self.add_cam_window_cam_password = 'Password'
        self.add_cam_window_cam_display_name = 'Display name'
        self.add_cam_window_add_cam_btn = 'Add Camera'

        # edit camera window translations
        self.edit_cam_window_title = 'Edit Camera'
        self.edit_cam_window_IP = 'Camera IP'
        self.edit_cam_window_username = 'Username'
        self.edit_cam_window_password = 'Password'
        self.edit_cam_window_display_name = 'Display name'
        self.edit_cam_window_edit_btn = 'Edit Info'

        # remove camera window translations
        self.remove_camera_window_title = 'Remove Camera'
        self.remove_camera_window_camera_names = 'Camera names:'
        self.remove_camera_window_remove_camera = 'Remove Camera'

        # show calendar window  translations
        self.show_calendar_window_title = 'Calendar'
        self.show_calendar_window_show_data_hourly = 'Show Data Hourly'
        self.show_calendar_window_show_data_cardinalwise = 'Show Data Cardinalwise'
        self.show_calendar_window_download_excel_data = 'Download Excel Data'

        # pop up messages 
        self.information = 'Infoormation'
        self.warning = 'Warning'
        self.add_camera_popup_success = 'added to database'
        self.add_camera_popup_error = ' but camera added!'
        self.edit_camera_popup_success = 'changed on database'
        self.remove_camera_popup_success = 'removed from database'
        self.excel_data_written_success = 'data written!'
        self.num_cameras_exceeded = 'Number of cameras = 3. You cannot add more!'
        self.no_cameras_found_error = 'No camera found in database. Please add camera first!'
    
    def translateToUzbek(self):
        self.lang = 'uz'

        self.main_window_title = 'Chorraxa Analitika dasturi'
        self.add_camera_btn = 'Kamera qo\'shish'
        self.edit_camera_btn = 'Kamerani o\'zgartirish'
        self.remove_camera_btn = 'Kamerani o\'chirish'
        self.show_data_btn = 'Ma\'lumotlarni ko\'rish'
        self.use_video_checkbox = 'Video ishlatish'
        self.cars = 'Yengil mashinalar'
        self.buses = 'Avtobuslar'
        self.bicycles = 'Velosipedlar'
        self.motorcycles = 'Motosikllar'
        self.trucks = 'Yuk mashinalari'
        self.a_in = 'A kirish'
        self.b_in = 'B kirish'
        self.c_in = 'C kirish'
        self.d_in = 'D kirish'
        self.a_out = 'A chiqish'
        self.b_out = 'B chiqish'
        self.c_out = 'C chiqish'
        self.d_out = 'D chiqish'
        self.start_inference_btn = 'BOSHLASH'
        self.stop_process_btn = 'TO\'XTATISH'

        # add camera window translations
        self.add_cam_window_title = 'Kamera qo\'shish'
        self.add_cam_window_cam_ip = 'IP'
        self.add_cam_window_cam_username = 'Foydalanuvchi nomi'
        self.add_cam_window_cam_password = 'Maxfiy so\'z'
        self.add_cam_window_cam_display_name = 'Kamera nomi'
        self.add_cam_window_add_cam_btn = 'Kamera qo\'shish'

        # edit camera window translations
        self.edit_cam_window_title = 'Kamera ma\'lumotlarini o\'zgartirish'
        self.edit_cam_window_IP = 'IP'
        self.edit_cam_window_username = 'Foydalanuvchi nomi'
        self.edit_cam_window_password = 'Maxfiy so\'z'
        self.edit_cam_window_display_name = 'Kamera nomi'
        self.edit_cam_window_edit_btn = 'Ma\'lumotlarni o\'zgartirish'

        # remove camera window translations
        self.remove_camera_window_title = 'Kamerani o\'chirish'
        self.remove_camera_window_camera_names = 'Kamera nomlari:'
        self.remove_camera_window_remove_camera = 'Kamerani o\'chirish'

        # show calendar window  translations
        self.show_calendar_window_title = 'Kalendar'
        self.show_calendar_window_show_data_hourly = 'Soatlik ma\'lumotlarni ko\'rish'
        self.show_calendar_window_show_data_cardinalwise = 'Tomonlar bo\'yicha ma\'lumotlarni ko\'rish'
        self.show_calendar_window_download_excel_data = 'Excel ma\'lumotlarni yuklab olish'

        # pop up messages
        self.information = 'Ma\'lumot'
        self.warning = 'Ogohlantirish'
        self.add_camera_popup_success = 'bazaga qo\'shildi'
        self.add_camera_popup_error = ' lekin kamera qo\'shildi'
        self.edit_camera_popup_success = 'bazada o\'zgartirildi'
        self.remove_camera_popup_success = 'bazada o\'chirildi'
        self.excel_data_written_success = 'excel yaratildi!'
        self.num_cameras_exceeded = 'Kameralar soni 3 taga yetdi boshqa qo\'sha olmaysiz'
        self.no_cameras_found_error = 'Bazada kamera topilmadi'
        
