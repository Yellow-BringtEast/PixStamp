# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QAction, QFont)
from PySide6.QtWidgets import (QComboBox, QHBoxLayout, QLabel,
                               QMenu, QMenuBar, QPushButton,
                               QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
                               QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1036, 503)
        self.actionsave = QAction(MainWindow)
        self.actionsave.setObjectName(u"actionsave")
        self.actionsave_as = QAction(MainWindow)
        self.actionsave_as.setObjectName(u"actionsave_as")
        self.actionexit = QAction(MainWindow)
        self.actionexit.setObjectName(u"actionexit")
        self.actionfile = QAction(MainWindow)
        self.actionfile.setObjectName(u"actionfile")
        self.actionfiles = QAction(MainWindow)
        self.actionfiles.setObjectName(u"actionfiles")
        self.actionfolder = QAction(MainWindow)
        self.actionfolder.setObjectName(u"actionfolder")
        self.actionhelp = QAction(MainWindow)
        self.actionhelp.setObjectName(u"actionhelp")
        self.actionabout = QAction(MainWindow)
        self.actionabout.setObjectName(u"actionabout")
        self.actionlisence = QAction(MainWindow)
        self.actionlisence.setObjectName(u"actionlisence")
        self.actionexif = QAction(MainWindow)
        self.actionexif.setObjectName(u"actionexif")
        self.actionfont = QAction(MainWindow)
        self.actionfont.setObjectName(u"actionfont")
        self.actionsave_all = QAction(MainWindow)
        self.actionsave_all.setObjectName(u"actionsave_all")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_11 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_img = QLabel(self.centralwidget)
        self.label_img.setObjectName(u"label_img")
        self.label_img.setMinimumSize(QSize(600, 400))
        self.label_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_img)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_first = QPushButton(self.centralwidget)
        self.pushButton_first.setObjectName(u"pushButton_first")

        self.horizontalLayout.addWidget(self.pushButton_first)

        self.pushButton_prev = QPushButton(self.centralwidget)
        self.pushButton_prev.setObjectName(u"pushButton_prev")

        self.horizontalLayout.addWidget(self.pushButton_prev)

        self.pushButton_next = QPushButton(self.centralwidget)
        self.pushButton_next.setObjectName(u"pushButton_next")

        self.horizontalLayout.addWidget(self.pushButton_next)

        self.pushButton_last = QPushButton(self.centralwidget)
        self.pushButton_last.setObjectName(u"pushButton_last")

        self.horizontalLayout.addWidget(self.pushButton_last)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_11.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 0))
        self.label.setMaximumSize(QSize(200, 30))

        self.verticalLayout_2.addWidget(self.label)

        self.comboBox_styleSeletor = QComboBox(self.centralwidget)
        self.comboBox_styleSeletor.addItem("")
        self.comboBox_styleSeletor.addItem("")
        self.comboBox_styleSeletor.addItem("")
        self.comboBox_styleSeletor.addItem("")
        self.comboBox_styleSeletor.addItem("")
        self.comboBox_styleSeletor.setObjectName(u"comboBox_styleSeletor")
        self.comboBox_styleSeletor.setMinimumSize(QSize(200, 30))
        self.comboBox_styleSeletor.setMaximumSize(QSize(400, 20))

        self.verticalLayout_2.addWidget(self.comboBox_styleSeletor)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(200, 20))
        self.label_17.setMaximumSize(QSize(200, 20))

        self.verticalLayout_3.addWidget(self.label_17)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 20))
        self.label_2.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_8.addWidget(self.label_2)

        self.label_Make = QLabel(self.centralwidget)
        self.label_Make.setObjectName(u"label_Make")
        self.label_Make.setMinimumSize(QSize(340, 20))
        self.label_Make.setMaximumSize(QSize(340, 20))

        self.horizontalLayout_8.addWidget(self.label_Make)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(60, 20))
        self.label_5.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_Model = QLabel(self.centralwidget)
        self.label_Model.setObjectName(u"label_Model")
        self.label_Model.setMinimumSize(QSize(340, 20))
        self.label_Model.setMaximumSize(QSize(340, 20))

        self.horizontalLayout_7.addWidget(self.label_Model)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(60, 20))
        self.label_7.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_6.addWidget(self.label_7)

        self.label_LensModel = QLabel(self.centralwidget)
        self.label_LensModel.setObjectName(u"label_LensModel")
        self.label_LensModel.setMinimumSize(QSize(340, 20))
        self.label_LensModel.setMaximumSize(QSize(340, 20))

        self.horizontalLayout_6.addWidget(self.label_LensModel)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(60, 20))
        self.label_9.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_5.addWidget(self.label_9)

        self.label_FocalLength = QLabel(self.centralwidget)
        self.label_FocalLength.setObjectName(u"label_FocalLength")
        self.label_FocalLength.setMinimumSize(QSize(340, 20))
        self.label_FocalLength.setMaximumSize(QSize(340, 20))

        self.horizontalLayout_5.addWidget(self.label_FocalLength)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(60, 20))
        self.label_11.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_4.addWidget(self.label_11)

        self.label_FNumber = QLabel(self.centralwidget)
        self.label_FNumber.setObjectName(u"label_FNumber")
        self.label_FNumber.setMinimumSize(QSize(340, 20))
        self.label_FNumber.setMaximumSize(QSize(340, 20))

        self.horizontalLayout_4.addWidget(self.label_FNumber)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_ = QLabel(self.centralwidget)
        self.label_.setObjectName(u"label_")
        self.label_.setMinimumSize(QSize(60, 20))
        self.label_.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_9.addWidget(self.label_)

        self.label_ISOSpeedRatings = QLabel(self.centralwidget)
        self.label_ISOSpeedRatings.setObjectName(u"label_ISOSpeedRatings")
        self.label_ISOSpeedRatings.setMinimumSize(QSize(340, 20))
        self.label_ISOSpeedRatings.setMaximumSize(QSize(340, 20))

        self.horizontalLayout_9.addWidget(self.label_ISOSpeedRatings)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(60, 20))
        self.label_12.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_3.addWidget(self.label_12)

        self.label_ExposureTime = QLabel(self.centralwidget)
        self.label_ExposureTime.setObjectName(u"label_ExposureTime")
        self.label_ExposureTime.setMinimumSize(QSize(340, 20))
        self.label_ExposureTime.setMaximumSize(QSize(340, 20))

        self.horizontalLayout_3.addWidget(self.label_ExposureTime)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(60, 20))
        self.label_15.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_2.addWidget(self.label_15)

        self.label_DateTime = QLabel(self.centralwidget)
        self.label_DateTime.setObjectName(u"label_DateTime")
        self.label_DateTime.setMinimumSize(QSize(340, 20))
        self.label_DateTime.setMaximumSize(QSize(340, 20))

        self.horizontalLayout_2.addWidget(self.label_DateTime)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_3.addWidget(self.label_16)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_processCurrent = QPushButton(self.centralwidget)
        self.pushButton_processCurrent.setObjectName(u"pushButton_processCurrent")
        self.pushButton_processCurrent.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_10.addWidget(self.pushButton_processCurrent)

        self.pushButton_processAll = QPushButton(self.centralwidget)
        self.pushButton_processAll.setObjectName(u"pushButton_processAll")
        self.pushButton_processAll.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_10.addWidget(self.pushButton_processAll)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_11.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1036, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menu)
        self.menu_2.setObjectName(u"menu_2")
        font = QFont()
        font.setUnderline(False)
        self.menu_2.setFont(font)
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_6 = QMenu(self.menu_4)
        self.menu_6.setObjectName(u"menu_6")
        self.menu_5 = QMenu(self.menubar)
        self.menu_5.setObjectName(u"menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actionsave)
        self.menu.addAction(self.actionsave_as)
        self.menu.addAction(self.actionsave_all)
        self.menu.addSeparator()
        self.menu.addAction(self.actionexit)
        self.menu_2.addAction(self.actionfile)
        self.menu_2.addAction(self.actionfiles)
        self.menu_2.addAction(self.actionfolder)
        self.menu_3.addAction(self.actionexif)
        self.menu_4.addAction(self.menu_6.menuAction())
        self.menu_6.addAction(self.actionfont)
        self.menu_5.addAction(self.actionhelp)
        self.menu_5.addAction(self.actionabout)
        self.menu_5.addSeparator()
        self.menu_5.addAction(self.actionlisence)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PixStamp", None))
        self.actionsave.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.actionsave_as.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a...", None))
        self.actionexit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.actionfile.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.actionfiles.setText(QCoreApplication.translate("MainWindow", u"\u591a\u4e2a\u6587\u4ef6", None))
        self.actionfolder.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5939", None))
        self.actionhelp.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.actionabout.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e PixStamp", None))
        self.actionabout.setIconText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e PixStamp", None))
        self.actionlisence.setText(QCoreApplication.translate("MainWindow", u"\u8bb8\u53ef\u8bc1", None))
        self.actionexif.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91 exif \u4fe1\u606f ", None))
        self.actionfont.setText(QCoreApplication.translate("MainWindow", u"font", None))
        self.actionsave_all.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u5168\u90e8\u56fe\u7247", None))
        self.actionsave_all.setIconText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u5168\u90e8\u56fe\u7247", None))
        self.label_img.setText("")
        self.pushButton_first.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e00\u5f20", None))
        self.pushButton_prev.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u5f20", None))
        self.pushButton_next.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u5f20", None))
        self.pushButton_last.setText(QCoreApplication.translate("MainWindow", u"\u6700\u540e\u4e00\u5f20", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6837\u5f0f\u9009\u62e9", None))
        self.comboBox_styleSeletor.setItemText(0, QCoreApplication.translate("MainWindow", u"\u65e0\u6837\u5f0f", None))
        self.comboBox_styleSeletor.setItemText(1, QCoreApplication.translate("MainWindow", u"Style 1", None))
        self.comboBox_styleSeletor.setItemText(2, QCoreApplication.translate("MainWindow", u"Style 2", None))
        self.comboBox_styleSeletor.setItemText(3, QCoreApplication.translate("MainWindow", u"Style 3", None))
        self.comboBox_styleSeletor.setItemText(4, QCoreApplication.translate("MainWindow", u"Style 4", None))

        self.label_17.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u54c1\u724c\uff1a", None))
        self.label_Make.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u578b\u53f7\uff1a", None))
        self.label_Model.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u955c\u5934\uff1a", None))
        self.label_LensModel.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u7126\u8ddd\uff1a", None))
        self.label_FocalLength.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5149\u5708\uff1a", None))
        self.label_FNumber.setText("")
        self.label_.setText(QCoreApplication.translate("MainWindow", u"ISO\uff1a", None))
        self.label_ISOSpeedRatings.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u95e8\u901f\u5ea6\uff1a", None))
        self.label_ExposureTime.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u65f6\u95f4\uff1a", None))
        self.label_DateTime.setText("")
        self.label_16.setText("")
        self.pushButton_processCurrent.setText(QCoreApplication.translate("MainWindow", u"\u5904\u7406\u5f53\u524d\u56fe\u7247", None))
        self.pushButton_processAll.setText(QCoreApplication.translate("MainWindow", u"\u5904\u7406\u5168\u90e8\u56fe\u7247", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.menu_6.setTitle(QCoreApplication.translate("MainWindow", u"\u9996\u9009\u9879", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u66f4\u591a", None))
    # retranslateUi

