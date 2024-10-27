import copy
import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QFileDialog, QStatusBar, QApplication

from src.controllers.watermark_controller import add_watermark
from src.exceptions import ExifNotFound
from src.models import exif_model
from src.models.layout_models import LayoutModel
from ui.main_ui import Ui_MainWindow


class MainController(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.style = '无样式'
        self.current_index = 0
        self.files_path = None
        self.to_show_images = None

        self.setupUi(self)

        self.menubar.installEventFilter(self)

        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.default_message = "By: Yellow-BringtEast  |  version: 0.1.0"
        self.status.showMessage(self.default_message)

        self.menuAction()
        self.label_img.setPixmap(QPixmap("assets/logos/apple.png"))

        self.changePhoto()
        self.comboBox_styleSeletor.currentIndexChanged.connect(self.getCurrentStyle)
        self.pushButton_processCurrent.clicked.connect(self.processCurrentImage)
        self.pushButton_processAll.clicked.connect(self.processAllImages)

    def eventFilter(self, obj, event):
        if obj == self.menubar:
            self.status.showMessage(self.default_message)
        return super().eventFilter(obj, event)

    def menuAction(self):
        self.actionfile.triggered.connect(self.openFile)
        self.actionfile.triggered.connect(self.showExif)

        self.actionfiles.triggered.connect(self.openMultipleFiles)
        self.actionfiles.triggered.connect(self.showExif)

        self.actionfolder.triggered.connect(self.openFolder)
        self.actionfolder.triggered.connect(self.showExif)

        self.actionsave.triggered.connect(self.saveFile)

    def changePhoto(self):
        self.pushButton_first.clicked.connect(self.showFistImage)
        self.pushButton_first.clicked.connect(self.showExif)

        self.pushButton_prev.clicked.connect(self.showPrevImage)
        self.pushButton_prev.clicked.connect(self.showExif)

        self.pushButton_next.clicked.connect(self.showNextImage)
        self.pushButton_next.clicked.connect(self.showExif)

        self.pushButton_last.clicked.connect(self.showLastImage)
        self.pushButton_last.clicked.connect(self.showExif)

    def openFile(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "打开文件", "",
                                                   "图像文件 (*.png *.jpg *.jpeg *.bmp *.gif);;所有文件 (*)")
        if file_name:
            self.displayImage(file_name)
            self.files_path = [file_name]
            self.to_show_images = copy.deepcopy(self.files_path)
            self.current_index = 0

    def openMultipleFiles(self):
        file_names, _ = QFileDialog.getOpenFileNames(self, "打开多个文件", "",
                                                     "图像文件 (*.png *.jpg *.jpeg *.bmp *.gif);;所有文件 (*)")
        if file_names:
            self.to_show_images = copy.deepcopy(file_names)
            self.displayImage(file_names[0])
            self.files_path = file_names
            self.current_index = 0

    def openFolder(self):
        folder_name = QFileDialog.getExistingDirectory(self, "打开文件夹")
        if folder_name:
            file_names = [folder_name + '/' + file for file in os.listdir(folder_name)]
            self.to_show_images = copy.deepcopy(file_names)
            self.displayImage(file_names[0])
            self.files_path = file_names
            self.current_index = 0

    def showFistImage(self):
        if self.to_show_images:
            self.current_index = 0
            self.displayImage(self.to_show_images[self.current_index])

    def showPrevImage(self):
        if self.to_show_images:
            if self.current_index == 0:
                self.current_index = len(self.to_show_images)

            self.current_index -= 1
            self.displayImage(self.to_show_images[self.current_index])

    def showNextImage(self):

        if self.to_show_images:
            if self.current_index == len(self.to_show_images) - 1:
                self.current_index = -1

            self.current_index += 1
            self.displayImage(self.to_show_images[self.current_index])

    def showLastImage(self):
        if self.to_show_images:
            self.current_index = len(self.to_show_images) - 1
            self.displayImage(self.to_show_images[self.current_index])

    def displayImage(self, file):
        if isinstance(file, str):
            pixmap = QPixmap(file)

        else:
            pixmap = file

        # 获取 QLabel 的大小
        label_size = self.label_img.size()

        # 根据 QLabel 的大小调整图像大小，保持原始比例
        scaled_pixmap = pixmap.scaled(label_size,
                                      Qt.KeepAspectRatio,
                                      Qt.SmoothTransformation)

        self.label_img.setPixmap(scaled_pixmap)

    def showExif(self):
        current_file_path = self.files_path[self.current_index]
        try:
            exif = exif_model.ExifModel(current_file_path)

            self.label_Make.clear()
            self.label_Make.setText(exif.Make)

            self.label_Model.clear()
            self.label_Model.setText(exif.Model)

            self.label_LensModel.clear()
            self.label_LensModel.setText(exif.LensModel)

            self.label_FocalLength.clear()
            self.label_FocalLength.setText(exif.FocalLength)

            self.label_FNumber.clear()
            self.label_FNumber.setText(exif.FNumber)

            self.label_ISOSpeedRatings.clear()
            self.label_ISOSpeedRatings.setText(exif.ISOSpeedRatings)

            self.label_ExposureTime.clear()
            self.label_ExposureTime.setText(exif.ExposureTime)

            self.label_DateTime.clear()
            self.label_DateTime.setText(exif.DateTime)

        except ExifNotFound:
            self.label_Make.clear()
            self.label_Model.clear()
            self.label_LensModel.clear()
            self.label_FocalLength.clear()
            self.label_FNumber.clear()
            self.label_ISOSpeedRatings.clear()
            self.label_ExposureTime.clear()
            self.label_DateTime.clear()

        except KeyError:
            self.label_Make.clear()
            self.label_Model.clear()
            self.label_LensModel.clear()
            self.label_FocalLength.clear()
            self.label_FNumber.clear()
            self.label_ISOSpeedRatings.clear()
            self.label_ExposureTime.clear()
            self.label_DateTime.clear()

    def getCurrentStyle(self):
        self.style = self.comboBox_styleSeletor.currentText()

    def processCurrentImage(self):
        current_file_path = self.files_path[self.current_index]
        exif = exif_model.ExifModel(current_file_path)

        if self.style != '无样式':
            layout = LayoutModel(exif.exif, self.style)
            watermarked_image = add_watermark(current_file_path, layout)
            self.to_show_images[self.current_index] = watermarked_image
            self.displayImage(watermarked_image)

    def processAllImages(self):
        total_images = len(self.files_path)
        for index, path in enumerate(self.files_path):
            exif = exif_model.ExifModel(path)

            if self.style != '无样式':
                layout = LayoutModel(exif.exif, self.style)
                watermarked_image = add_watermark(path, layout)
                self.to_show_images[index] = watermarked_image

                # 计算进度百分比
                progress = ((index + 1) / total_images) * 100
                self.status.showMessage(f"正在处理 {path} - 进度: {progress:.2f}%")

                # 强制更新 UI，避免界面卡住
                QApplication.processEvents()

            # 处理完成后恢复默认信息
            self.status.showMessage(self.default_message)
        self.displayImage(self.to_show_images[self.current_index])
