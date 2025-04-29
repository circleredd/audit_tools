# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'muti_tools_2.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(807, 606)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 801, 591))
        font = QFont()
        font.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font.setPointSize(12)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.tab1.setEnabled(True)
        font1 = QFont()
        font1.setPointSize(12)
        self.tab1.setFont(font1)
        self.label = QLabel(self.tab1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 151, 21))
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color:rgb(85, 170, 255);\n"
"background-color:rgb(170, 255, 255);\n"
"background-color: rgb(112, 225, 167);")
        self.label.setScaledContents(False)
        self.plainTextEdit = QPlainTextEdit(self.tab1)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(0, 40, 211, 491))
        self.label_2 = QLabel(self.tab1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(330, 10, 41, 21))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(0, 170, 127);\n"
"background-color: rgb(255, 170, 0);\n"
"background-color: rgb(112, 225, 167);")
        self.pushButton = QPushButton(self.tab1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(230, 90, 75, 23))
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.pushButton_2 = QPushButton(self.tab1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(230, 140, 75, 23))
        self.pushButton_2.setFont(font2)
        self.pushButton_3 = QPushButton(self.tab1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(710, 510, 75, 23))
        self.pushButton_3.setFont(font2)
        self.pushButton_4 = QPushButton(self.tab1)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(230, 40, 75, 23))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4 Light"])
        font3.setBold(True)
        self.pushButton_4.setFont(font3)
        self.textBrowser = QTextBrowser(self.tab1)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(330, 40, 381, 491))
        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget_2 = QTabWidget(self.tab_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 0, 791, 561))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 51, 21))
        font4 = QFont()
        font4.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.label_4.setFont(font4)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"background-color:rgb(85, 170, 255);\n"
"background-color:rgb(170, 255, 255);\n"
"background-color: rgb(112, 225, 167);\n"
"background-color: rgb(24, 220, 220);")
        self.label_4.setScaledContents(False)
        self.comboBox_4 = QComboBox(self.tab_3)
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(60, 60, 271, 31))
        font5 = QFont()
        font5.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font5.setBold(False)
        self.comboBox_4.setFont(font5)
        self.pushButton_7 = QPushButton(self.tab_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(480, 130, 75, 21))
        self.pushButton_7.setFont(font2)
        self.comboBox_5 = QComboBox(self.tab_3)
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setGeometry(QRect(60, 110, 271, 31))
        self.comboBox_5.setFont(font5)
        self.textBrowser_3 = QTextBrowser(self.tab_3)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(0, 330, 791, 151))
        self.pushButton_8 = QPushButton(self.tab_3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(710, 490, 75, 31))
        self.pushButton_8.setFont(font2)
        self.comboBox_6 = QComboBox(self.tab_3)
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setGeometry(QRect(60, 20, 271, 31))
        self.comboBox_6.setFont(font5)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.textBrowser_2 = QTextBrowser(self.tab_4)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(0, 330, 791, 161))
        self.pushButton_5 = QPushButton(self.tab_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(700, 490, 75, 31))
        self.pushButton_5.setFont(font2)
        self.pushButton_6 = QPushButton(self.tab_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(680, 300, 91, 31))
        self.pushButton_6.setFont(font4)
        self.label_3 = QLabel(self.tab_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 151, 31))
        self.label_3.setFont(font4)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u"background-color:rgb(85, 170, 255);\n"
"background-color:rgb(170, 255, 255);\n"
"background-color: rgb(112, 225, 167);\n"
"background-color: rgb(24, 220, 220);")
        self.label_3.setScaledContents(False)
        self.plainTextEdit_2 = QPlainTextEdit(self.tab_4)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(0, 30, 781, 101))
        self.label_5 = QLabel(self.tab_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 0, 111, 31))
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"background-color:rgb(85, 170, 255);\n"
"background-color:rgb(170, 255, 255);\n"
"background-color: rgb(112, 225, 167);\n"
"background-color: rgb(24, 220, 220);\n"
"background-color: rgb(255, 170, 127);")
        self.lineEdit = QLineEdit(self.tab_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(310, 0, 31, 31))
        self.plainTextEdit_3 = QPlainTextEdit(self.tab_4)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(0, 140, 171, 121))
        self.pushButton_9 = QPushButton(self.tab_4)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(60, 260, 61, 31))
        self.pushButton_9.setFont(font2)
        self.textBrowser_4 = QTextBrowser(self.tab_4)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(60, 290, 61, 31))
        self.pushButton_10 = QPushButton(self.tab_4)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(260, 260, 61, 31))
        self.pushButton_10.setFont(font2)
        self.plainTextEdit_4 = QPlainTextEdit(self.tab_4)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setGeometry(QRect(200, 140, 171, 121))
        self.textBrowser_5 = QTextBrowser(self.tab_4)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setGeometry(QRect(260, 290, 61, 31))
        self.textBrowser_6 = QTextBrowser(self.tab_4)
        self.textBrowser_6.setObjectName(u"textBrowser_6")
        self.textBrowser_6.setGeometry(QRect(460, 290, 61, 31))
        self.pushButton_11 = QPushButton(self.tab_4)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(460, 260, 61, 31))
        self.pushButton_11.setFont(font2)
        self.plainTextEdit_5 = QPlainTextEdit(self.tab_4)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setGeometry(QRect(400, 140, 171, 121))
        self.pushButton_12 = QPushButton(self.tab_4)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(610, 490, 81, 31))
        self.pushButton_12.setFont(font)
        self.pushButton_13 = QPushButton(self.tab_4)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(680, 260, 91, 31))
        self.pushButton_13.setFont(font4)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 20, 61, 31))
        font6 = QFont()
        font6.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font6.setPointSize(16)
        font6.setBold(True)
        self.label_6.setFont(font6)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet(u"background-color:rgb(85, 170, 255);\n"
"background-color:rgb(170, 255, 255);\n"
"background-color: rgb(112, 225, 167);")
        self.label_6.setScaledContents(False)
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 150, 61, 31))
        self.label_7.setFont(font6)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet(u"background-color:rgb(85, 170, 255);\n"
"background-color:rgb(170, 255, 255);\n"
"background-color: rgb(112, 225, 167);")
        self.label_7.setScaledContents(False)
        self.horizontalLayoutWidget_2 = QWidget(self.tab)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(400, 60, 381, 80))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        font7 = QFont()
        font7.setBold(True)
        self.label_8.setFont(font7)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.lineEdit_4 = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_4.addWidget(self.lineEdit_4)

        self.label_9 = QLabel(self.horizontalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font7)

        self.horizontalLayout_4.addWidget(self.label_9)

        self.lineEdit_5 = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_4.addWidget(self.lineEdit_5)

        self.label_10 = QLabel(self.horizontalLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font7)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.lineEdit_6 = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_4.addWidget(self.lineEdit_6)

        self.horizontalLayoutWidget_3 = QWidget(self.tab)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(20, 60, 371, 80))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_5.addWidget(self.lineEdit_2)

        self.pushButton_14 = QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.horizontalLayout_5.addWidget(self.pushButton_14)

        self.horizontalLayoutWidget = QWidget(self.tab)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 190, 371, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_3 = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_3.addWidget(self.lineEdit_3)

        self.pushButton_15 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.horizontalLayout_3.addWidget(self.pushButton_15)

        self.horizontalLayoutWidget_4 = QWidget(self.tab)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(400, 190, 381, 80))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.horizontalLayoutWidget_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font7)

        self.horizontalLayout_7.addWidget(self.label_13)

        self.lineEdit_7 = QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_7.addWidget(self.lineEdit_7)

        self.label_11 = QLabel(self.horizontalLayoutWidget_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font7)

        self.horizontalLayout_7.addWidget(self.label_11)

        self.lineEdit_9 = QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.horizontalLayout_7.addWidget(self.lineEdit_9)

        self.label_12 = QLabel(self.horizontalLayoutWidget_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font7)

        self.horizontalLayout_7.addWidget(self.label_12)

        self.lineEdit_8 = QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_7.addWidget(self.lineEdit_8)

        self.verticalLayoutWidget = QWidget(self.tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(560, 480, 231, 74))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_16 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        font8 = QFont()
        font8.setPointSize(15)
        self.pushButton_16.setFont(font8)

        self.verticalLayout_2.addWidget(self.pushButton_16)

        self.verticalLayoutWidget_2 = QWidget(self.tab)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(560, 380, 231, 101))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_3.addWidget(self.checkBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_14 = QLabel(self.verticalLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font7)

        self.horizontalLayout_2.addWidget(self.label_14)

        self.comboBox = QComboBox(self.verticalLayoutWidget_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font1)

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.pushButton_17 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setFont(font8)

        self.verticalLayout_3.addWidget(self.pushButton_17)

        self.textBrowser_7 = QTextBrowser(self.tab)
        self.textBrowser_7.setObjectName(u"textBrowser_7")
        self.textBrowser_7.setGeometry(QRect(20, 290, 511, 261))
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u" \u8f38\u5165\u8eab\u5206\u8b49\u5b57\u865f\u5217\u8868 ", None))
        self.plainTextEdit.setPlainText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" \u7d50\u679c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u5165", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u7522\u751f", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u8907\u88fd\u6587\u5b57", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u5fae\u8edf\u6b63\u9ed1\u9ad4'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"\u8eab\u5206\u8b49\u5b57\u865f\u7522\u751f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u" SQL", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"ncadb_\u73fe\u5f79\u5f79\u7537\u85aa\u6c34\u4e8b\u4ef6\u8868_999", None))

        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u7522\u751f", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT", None))

        self.textBrowser_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u5fae\u8edf\u6b63\u9ed1\u9ad4'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">INSERT INTO `nca_db`.`\u73fe\u5f79\u5f79\u7537\u85aa\u6c34\u4e8b\u4ef6\u8868_999` (`\u8eab\u5206\u8b49\u5b57\u865f`, `\u85aa\u6c34\u4e8b\u4ef6\u985e\u5225`, `\u751f\u6548\u65e5\u671f`, `\u85aa\u4ff8\u4ee3\u865f`, `\u5730\u57df\u52a0\u7d66\u4ee3\u865f`, `\u4e3b\u526f\u98df\u4ee3\u865f`, `\u670d\u52e4\u55ae\u4f4d`, `\u7570\u52d5\u65e5\u671f`) VALUES ('A132196321', 'D200\u54c8\u54c8\u54c8', '2025-01-01', 'A001', 'D02', 'E001', '\u5167\u653f\u90e8\u66ff\u7ba1\u4e2d\u5fc3/', '2025-01-25');</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:"
                        "0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">INSERT INTO `nca_db`.`\u73fe\u5f79\u5f79\u7537\u85aa\u6c34\u6536\u767c\u8868_999` (`\u8eab\u5206\u8b49\u5b57\u865f`, `\u6536\u767c\u539f\u56e0`, `\u6536\u767c\u65e5\u671f`, `\u6536\u767c\u500b\u4eba\u85aa\u984d`, `\u6536\u767c\u5730\u57df\u52a0\u7d66`, `\u6536\u767c\u500b\u4eba\u4e3b\u526f\u98df\u8cbb`, `\u6536\u767c\u516c\u5eab\u4e3b\u526f\u98df\u8cbb`, `\u61c9\u6263\u91d1\u984d`, `\u6cd5\u6263\u91d1\u984d`, `\u5be6\u767c\u500b\u4eba\u5c0f\u8a08`, `\u532f\u5165\u516c\u5eab\u5c0f\u8a08`, `\u61c9\u767c\u5408\u8a08`, `\u5be6\u6536\u767c\u5408\u8a08`, `\u516c\u6587\u5b57\u865f`) VALUES ('A131105915', '0114\u6e2c\u8a66', '2025-01-14', '999', '', '999', '999', '999', '999', '999', '999', '999', '999', '1111111111');</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bo"
                        "ttom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u8907\u88fd", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT", None))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u55ae\u7b46SQL", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u5fae\u8edf\u6b63\u9ed1\u9ad4'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u8907\u88fd", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u7522\u751f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u" SQL Command", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("MainWindow", u"INSERT INTO `nca_db`.`\u73fe\u5f79\u5f79\u7537\u85aa\u6c34\u4e8b\u4ef6\u8868_999` (`\u8eab\u5206\u8b49\u5b57\u865f`, `\u85aa\u6c34\u4e8b\u4ef6\u985e\u5225`, `\u751f\u6548\u65e5\u671f`, `\u85aa\u4ff8\u4ee3\u865f`, `\u5730\u57df\u52a0\u7d66\u4ee3\u865f`, `\u4e3b\u526f\u98df\u4ee3\u865f`, `\u670d\u52e4\u55ae\u4f4d`, `\u7570\u52d5\u65e5\u671f`) VALUES ('%S', 'D111_\u5f85\u5206\u767c\u670d\u52e4', '2025-01-01', 'A001', 'D02', 'E001', '\u5167\u653f\u90e8\u66ff\u7ba1\u4e2d\u5fc3/', '2025-01-25');", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"  Variables", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.plainTextEdit_3.setPlainText("")
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"count", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u5fae\u8edf\u6b63\u9ed1\u9ad4'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"count", None))
        self.plainTextEdit_4.setPlainText("")
        self.textBrowser_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u5fae\u8edf\u6b63\u9ed1\u9ad4'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textBrowser_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u5fae\u8edf\u6b63\u9ed1\u9ad4'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"count", None))
        self.plainTextEdit_5.setPlainText("")
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u591a\u7b46\u91cd\u8907SQL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"SQL\u6279\u6b21\u7522\u751f", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u518aA", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u518aB", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ID\u6b04\u4f4d", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d\u6b04\u4f4d", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u91d1\u984d\u6b04\u4f4d", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u700f\u89bd", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u700f\u89bd", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"ID\u6b04\u4f4d", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d\u6b04\u4f4d", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u91d1\u984d\u6b04\u4f4d", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\u5132\u5b58\u65b0\u6a94\u6848", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u7559\u672a\u91cd\u758a\u540d\u55ae", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u5f0f", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u52a0\u7e3d", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6263\u9664(A-B)", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u50c5\u6311\u51fa\u4eba(\u91d1\u984d\u4ee5A\u70ba\u6e96)", None))

        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"\u7522\u751f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u6e05\u518a\u5408\u4f75", None))
    # retranslateUi

