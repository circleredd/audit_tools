from dataclasses import dataclass
from PySide6.QtWidgets import (
    QPlainTextEdit, QTextBrowser, QPushButton, QLineEdit, QComboBox, QCheckBox
)

@dataclass
class WidgetContainer():
    # ID
    id_input_field: QPlainTextEdit
    id_result_browser: QTextBrowser
    id_insert_button: QPushButton
    id_generate_button: QPushButton
    id_copy_button: QPushButton
    id_clear_button: QPushButton

    # SQL
    sql_variables_num_field: QLineEdit
    sql_command_input: QPlainTextEdit
    sql_variable_1: QPlainTextEdit
    sql_variable_2: QPlainTextEdit
    sql_variable_3: QPlainTextEdit
    sql_count_button_1: QPushButton
    sql_count_button_2: QPushButton
    sql_count_button_3: QPushButton
    sql_count_result_1: QTextBrowser
    sql_count_result_2: QTextBrowser
    sql_count_result_3: QTextBrowser
    sql_clear_button: QPushButton
    sql_generate_button: QPushButton
    sql_result_browser: QTextBrowser
    sql_copy_button: QPushButton
    sql_clear_variables_button: QPushButton


    # merge
    merge_upload_button_1: QPushButton
    merge_upload_button_2: QPushButton
    merge_upload_path_1: QLineEdit
    merge_upload_path_2: QLineEdit
    merge_id_field_1: QLineEdit
    merge_id_field_2: QLineEdit
    merge_name_field_1: QLineEdit
    merge_name_field_2: QLineEdit
    merge_value_field_1: QLineEdit
    merge_value_field_2: QLineEdit
    merge_result_field: QTextBrowser
    merge_mode_list: QComboBox
    merge_generate_button: QPushButton
    merge_save_button: QPushButton
    merge_replicate_checkbox: QCheckBox



    # 此方法會讓編輯器無法得知型別
    # def __init__(self, **kwargs):
    #     """
    #     初始化控件容器，通過關鍵字參數傳遞控件。
    #     kwargs: 可以傳入任意數量的控件，會自動轉化為類的屬性。
    #     """
    #     self.__dict__.update(kwargs)
        
    # def get_widget(self, name: str):
    #     """
    #     根據控件名稱返回控件，如果不存在則返回 None。
    #     """
    #     return getattr(self, name, None)