import sys
from PySide6 import QtWidgets
from ui.ui_main_window import Ui_MainWindow
from logic.main_logic import IdLogic, SqlLogic, Mergelogic
from widgets.widgets_container import WidgetContainer



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

   
        # 將所有物件封裝在 WidgetContainer 中
        widgets = WidgetContainer(
            # ID
            id_input_field = self.plainTextEdit,
            id_result_browser=self.textBrowser, 
            id_insert_button=self.pushButton,   
            id_generate_button=self.pushButton_2,  
            id_copy_button=self.pushButton_3,
            id_clear_button=self.pushButton_4,
            
            # SQL
            sql_variables_num_field = self.lineEdit,
            sql_command_input = self.plainTextEdit_2,
            sql_variable_1 = self.plainTextEdit_3,
            sql_variable_2 = self.plainTextEdit_4,
            sql_variable_3 = self.plainTextEdit_5,
            sql_count_button_1 = self.pushButton_9,
            sql_count_button_2 = self.pushButton_10,
            sql_count_button_3 = self.pushButton_11,
            sql_count_result_1 = self.textBrowser_4,
            sql_count_result_2 = self.textBrowser_5,
            sql_count_result_3 = self.textBrowser_6,
            sql_clear_button = self.pushButton_12,
            sql_generate_button = self.pushButton_6,
            sql_result_browser = self.textBrowser_2,
            sql_copy_button = self.pushButton_5,
            sql_clear_variables_button = self.pushButton_13,

            # Merge
            merge_upload_button_1 = self.pushButton_14,
            merge_upload_button_2 = self.pushButton_15,
            merge_upload_path_1 = self.lineEdit_2,
            merge_upload_path_2 = self.lineEdit_3,
            merge_id_field_1 = self.lineEdit_4,
            merge_id_field_2 = self.lineEdit_7,
            merge_name_field_1 = self.lineEdit_5,
            merge_name_field_2 = self.lineEdit_9,
            merge_value_field_1 = self.lineEdit_6,
            merge_value_field_2 = self.lineEdit_8,
            merge_result_field=self.textBrowser_7,
            merge_mode_list = self.comboBox,
            merge_generate_button= self.pushButton_17,
            merge_save_button = self.pushButton_16,
            merge_replicate_checkbox = self.checkBox

        )
        
        self.id_logic = IdLogic(widgets) 
        self.sql_logic = SqlLogic(widgets)
        self.merge_logic = Mergelogic(widgets)
        self.setup_id_events() # 身分證字號分頁
        self.setup_sql_events() # SQL分頁
        self.setup_merge_events() # 清冊合併分頁
    
    
    def setup_id_events(self):      
        self.pushButton.clicked.connect(self.id_logic.insert_button_click) # "加入" 按鈕
        self.pushButton_2.clicked.connect(self.id_logic.generate_button_click) # "產生" 按鈕
        self.pushButton_3.clicked.connect(self.id_logic.copy_button_click) # "複製文字" 按鈕
        self.pushButton_4.clicked.connect(self.id_logic.clear_button_click) # "清空" 按鈕
        return
        

    def setup_sql_events(self):
        self.pushButton_9.clicked.connect(lambda: self.sql_logic.count_input_button_click(1)) # count1
        self.pushButton_10.clicked.connect(lambda: self.sql_logic.count_input_button_click(2)) # count2
        self.pushButton_11.clicked.connect(lambda: self.sql_logic.count_input_button_click(3)) # count3
        self.pushButton_13.clicked.connect(self.sql_logic.clear_variables_button_click) # 清除變數
        self.pushButton_12.clicked.connect(self.sql_logic.clear_result_button_click) # 清除結果
        self.pushButton_5.clicked.connect(self.sql_logic.copy_button_click) # 複製結果
        self.pushButton_6.clicked.connect(self.sql_logic.generate_button_click) # 產生結果
        self.lineEdit.textChanged.connect(self.sql_logic.on_variables_num_change) # 偵測輸入變數數量改變
        pass 

    def setup_merge_events(self):
        self.pushButton_14.clicked.connect(lambda: self.merge_logic.file_upload_click(1)) # 上傳清冊A
        self.pushButton_15.clicked.connect(lambda: self.merge_logic.file_upload_click(2)) # 上傳清冊B
        self.pushButton_17.clicked.connect(self.merge_logic.generate_file_click) # 產生合併清冊
        self.pushButton_16.clicked.connect(self.merge_logic.save_file_click) # 儲存合併清冊
        self.checkBox.stateChanged.connect(self.merge_logic.replicate_checkbox_change)
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    ui = Ui_MainWindow()
    # ui.setupUi(window) # MainWindow中已設定
    window.show()
    sys.exit(app.exec())