import re
from PySide6 import QtWidgets
from widgets.widgets_container import WidgetContainer
from PySide6.QtWidgets import ( QFileDialog )
from PySide6.QtCore import QDir
import pandas as pd
from enum import Enum

class IdLogic():
    def __init__(self,  widgets: WidgetContainer):
        self.widgets = widgets
        self.result = ''

    def clear_button_click(self) -> None:
        self.result = ''
        self.widgets.id_result_browser.clear()
        self.widgets.id_input_field.clear()
        return
    
    def insert_button_click(self) -> None:
        ids: str = self.widgets.id_input_field.toPlainText()
        if len(ids) == 0:
            return                
        ids = ids.strip(" ")
        self.id_formation_convert(ids, True)
        self.widgets.id_result_browser.setText(self.result)
        return


    def id_formation_convert(self, ids: str, is_insert_mode = False) -> None:
        id_list = re.split(r'\s+', ids.strip()) # 檢查空格和換行，遇到就分割

        id_list_remove_null = [i for i in id_list if i]

        # 加入模式
        if is_insert_mode and self.result:
            self.result += ", "
        # 產生模式
        else:
            self.result = ''
        self.result += ', '.join(f'"{id}"' for id in id_list_remove_null)            
        
        return
        
    
    def generate_button_click(self) -> None: 
        ids: str = self.widgets.id_input_field.toPlainText()
        if len(ids) == 0:
            return
                
        ids = ids.strip(" ")
        self.id_formation_convert(ids)        
        self.widgets.id_result_browser.setText(self.result)
        
        return

    def copy_button_click(self) -> None:
        result = self.widgets.id_result_browser.toPlainText()

        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(result)

        return  
        

class SqlLogic():
    def __init__(self, widgets: WidgetContainer):
        self.widgets = widgets
        
        self.buttons_map = {
            1: self.widgets.sql_variable_1, 
            2: self.widgets.sql_variable_2,
            3: self.widgets.sql_variable_3
        }
        self.count_show_map = {
            1: self.widgets.sql_count_result_1,
            2: self.widgets.sql_count_result_2,
            3: self.widgets.sql_count_result_3
        }
        self.all_variables_field = [
            self.widgets.sql_variable_1,
            self.widgets.sql_variable_2,
            self.widgets.sql_variable_3
        ]

        self.on_variables_num_change()
    
    def clear_result_button_click(self):                  
        self.widgets.sql_result_browser.clear()
        return

    def clear_variables_button_click(self):                  
        self.widgets.sql_variable_1.clear()
        self.widgets.sql_variable_2.clear()
        self.widgets.sql_variable_3.clear()
        return
    
    def count_input_button_click(self, button_id: int) -> list:
        variable_str = ''

        variable_str = self.buttons_map.get(button_id).toPlainText()

        if not variable_str:
            self.count_show_map.get(button_id).setText("")
            return
        
        variable_list = variable_str.strip().split()
        print(variable_list)

        self.count_show_map.get(button_id).setText(str(len(variable_list)))
        return variable_list

    def copy_button_click(self):
        result = self.widgets.sql_result_browser.toPlainText()
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(result)
        return
    
    def on_variables_num_change(self):
        try:
            numbers = int(self.widgets.sql_variables_num_field.text())
            if numbers < 1 or numbers > len(self.all_variables_field):
                raise ValueError("無效的變數數量")

        except ValueError:
            numbers = 0
            print("變數數量需要介於1-3之間")


        for variable in self.all_variables_field:
            variable.setEnabled(True)      
        
        for i in range(numbers, len(self.all_variables_field)):
            self.all_variables_field[i].setDisabled(True)

        return
    
    def find_all_replacement_positions(self, text: str):
        positions = []
        pattern = re.compile(r"'%S'")
        for match in pattern.finditer(text):
            positions.append(match.start())  # 或 match.end()
        return positions    

    def generate_check(self, variable_nums: int, input_sql_command: str, used_variable_texts: list[list]) -> tuple[bool, str, list]:
        variable_pos_list = self.find_all_replacement_positions(input_sql_command)

        if variable_nums != len(variable_pos_list):
            return False, "設定變數數量及%S數量不一致", []
        
        for i in range(1, variable_nums):
            tmp_variable_count = len(used_variable_texts[i-1])
            if tmp_variable_count != len(used_variable_texts[i]):
                return False, "各欄位的資料筆數不同", []           

        return True, "", variable_pos_list

    def generate_button_click(self):
        input_command = self.widgets.sql_command_input.toPlainText()
        variable_nums = int(self.widgets.sql_variables_num_field.text())
        all_variable_texts = [
            self.widgets.sql_variable_1.toPlainText().strip().split(),
            self.widgets.sql_variable_2.toPlainText().strip().split(),
            self.widgets.sql_variable_3.toPlainText().strip().split()
        ]
        # 根據 variable_nums，只取前 n 個 (1 ~ 3)
        used_variable_texts = all_variable_texts[:variable_nums]

        is_check_success, err_message, replace_pos = self.generate_check(variable_nums, input_command, used_variable_texts)
        print(replace_pos)
                
        if not is_check_success:
            self.widgets.sql_result_browser.setTextColor("#ff0000")
            self.widgets.sql_result_browser.setText(err_message)
            self.widgets.sql_result_browser.setTextColor("#000000")
            return        

        replicated_command = []
        for i in range(0, variable_nums):
            # 每個變數資料筆數
            for j in range(0, len(used_variable_texts[i])):
                if i == 0:
                    replicated_command.append(input_command)          
                replicated_command[j] = replicated_command[j].replace("%S", used_variable_texts[i][j], 1)

        replicated_command_str = "\n\n".join(replicated_command)   
        self.widgets.sql_result_browser.setText(replicated_command_str)        
        return

class MergeMode(Enum):
    ADD = 1   # 加總
    SUBTRACT = 2  # 扣除
    EXTRACT = 3  # 僅挑出


class Mergelogic():
    def __init__(self, widgets: WidgetContainer):
        self.widgets = widgets
        self.last_directory = ""  # 用來儲存上次開啟的路徑
        self.is_csv = True # 紀錄是否為csv
        self.data = [] # 儲存合併後資料
        self.is_replicated = False # 兩個清冊上沒有重複的人，是否保留在新清冊上，預設為"否"
 

    def file_upload_click(self, num: int):
        # 設定初始路徑為上次開啟的路徑，如果還沒有路徑就設為當前工作目錄
        initial_dir = self.last_directory if self.last_directory else QDir.currentPath()

        file_path, _ = QFileDialog.getOpenFileName(None, "選擇檔案", initial_dir, "CSV/Excel files (*.csv *.xls *.xlsx)")

        if file_path:
            self.update_file_path(num, file_path)
            self.last_directory = file_path  # 更新上次開啟的路徑
        else:
            self.clear_file_path(num)

        
    
    def clear_file_path(self, num: int):
        if num == 1:
            self.widgets.merge_upload_path_1.setText('尚未選擇檔案')
        else:
            self.widgets.merge_upload_path_2.setText('尚未選擇檔案')

    def update_file_path(self, num: int, file_path: str):
        if num == 1:
            self.widgets.merge_upload_path_1.setText(file_path)
        elif num == 2:
            self.widgets.merge_upload_path_2.setText(file_path)

    def replicate_checkbox_change(self):
        self.replicate_checkbox_change = self.widgets.merge_replicate_checkbox.isChecked()
        return

    
    def save_file(self, data: list[list], is_csv: bool):
        ids, names, values = data
        df = {
            '身分證字號': ids,
            '姓名': names,
            '金額': values
        }
        df = pd.DataFrame(df)
        initial_dir = self.last_directory if self.last_directory else QDir.currentPath()

        file_name, _ = QFileDialog.getSaveFileName(None, "儲存檔案", initial_dir, "CSV/Excel files (*.csv *.xls *.xlsx)")

        if is_csv:
            df.to_csv(file_name, index=False, encoding='cp950')
        else:
            if file_name.endswith(".xls"):
                file_name = file_name.replace(".xls", ".xlsx")
            df.to_excel(file_name, engine="openpyxl", index=False)
            
        print("檔案已儲存")
        pass
    

    def generate_file_click(self):
        path_1 = self.widgets.merge_upload_path_1.text()
        path_2 = self.widgets.merge_upload_path_2.text()
        mode_str = self.widgets.merge_mode_list.currentText() #1.加總  #2.扣除(A-B)  #3.僅挑出人(金額以A為準)
        if mode_str == '加總':
            mode = MergeMode.ADD
        elif mode_str == '扣除(A-B)':
            mode = MergeMode.SUBTRACT
        else:
            mode = MergeMode.EXTRACT
        
        file_1 = self.read_file(path_1)
        file_2 = self.read_file(path_2)
        file_1 = self.choose_col(file_1, 1)
        file_2 = self.choose_col(file_2, 2)
        self.data = self.merge_files(file_1, file_2, mode)
        ids, names, values = self.data
        df = {
            '身分證字號': ids,
            '姓名': names,
            '金額': values
        }
        df = pd.DataFrame(df)
        html_data = df.to_html()
        self.widgets.merge_result_field.setHtml(html_data)    
        pass

    def save_file_click(self):
        if self.data == []:
            return
        
        self.save_file(self.data, self.is_csv)
        return


    # 讀取CSV或Excel文件
    def read_file(self, file: str) -> list:
        if file.endswith('.csv'): # .csv後綴
            dataframe = pd.read_csv(file, encoding='cp950')
        else:
            dataframe = pd.read_excel(file)
            self.is_csv = False

        return dataframe.values.tolist()
    

    def get_col_field(self, num: int) -> list[int]:
        if num == 1:
            id_col, name_col, value_col = self.widgets.merge_id_field_1.text(), self.widgets.merge_name_field_1.text(), self.widgets.merge_value_field_1.text()
        elif num == 2:
            id_col, name_col, value_col = self.widgets.merge_id_field_2.text(), self.widgets.merge_name_field_2.text(), self.widgets.merge_value_field_2.text()
        
        return [self.letter_to_number(id_col), self.letter_to_number(name_col), self.letter_to_number(value_col)]
    

    def letter_to_number(self, s: str) -> int:
        result = 0
        s = s.upper()
        for char in s:
            # 每個字母對應的數字：A = 1, B = 2, ..., Z = 26
            result = result * 26 + (ord(char) - ord('A') + 1)

        return result - 1 # 每個字母對應的數字：A = 0, B = 1, ..., Z = 25, AA = 26


    # def choose_col(self, file: list, id_col: int, name_col: int, value_col: int) -> list[list]:
    def choose_col(self, file: list, num: int) -> list[list]:
        id_col, name_col, value_col = self.get_col_field(num)
        ids = [i[id_col] for i in file]
        names = [i[name_col] for i in file]
        values = [i[value_col] for i in file]
        return [ids, names, values]
    

    def merge_files(self, file1: list, file2:list, mode: MergeMode):
        file1_ids, file1_names, file1_values = file1
        file2_ids, file2_names, file2_values = file2
        
        new_ids = []
        new_names = []
        new_values = []

        for id, name, value in zip(file1_ids, file1_names,  file1_values):
            
            if id in file2_ids:
                index_of_file2 = file2_ids.index(id)
                new_ids.append(id)
                new_names.append(name)
                new_value = value + file2_values[index_of_file2] if mode == MergeMode.ADD else value - file2_values[index_of_file2]
                new_values.append(new_value)
            else:
                new_ids.append(id)
                new_names.append(name)
                new_values.append(value)

        # 勾選保留未重複名單時才做這段
        if self.replicate_checkbox_change: 
            for id, name, value in zip(file2_ids, file2_names, file2_values):
                if id not in file1_ids:
                    new_ids.append(id)
                    new_names.append(name)
                    new_values.append(value)
        
        return [new_ids, new_names, new_values]