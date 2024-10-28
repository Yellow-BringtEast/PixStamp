import copy
import os
from fileinput import filename

from PIL.Image import Image
from PySide6.QtCore import Qt, QObject, QEvent
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

        # 默认样式选择
        self.style = '无样式'

        # 当前展示照片的索引
        self.current_index = 0

        # 读取的文件路径
        self.files_path = None

        # 缓存已处理的照片，确保展示切换回来后还是以处理的照片
        self.to_show_images = None

        # 初始化UI界面
        self.setupUi(self)

        # 确保鼠标移动到菜单栏时，状态栏的信息不被刷新
        self.menubar.installEventFilter(self)

        # 建立状态栏
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.default_message = "By: Yellow-BringtEast  |  version: 0.2.0"  # 默认信息
        self.status.showMessage(self.default_message)

        # 菜单栏控件逻辑
        self.menuAction()

        # 照片展示栏，默认展示灰色
        self.label_img.setPixmap(QPixmap("assets/logos/apple.png"))

        # 照片切换控件逻辑
        self.changePhoto()

        # 样式选择栏逻辑 - 当样式被选择后，设置 self.style 为对应的样式
        self.comboBox_styleSeletor.currentIndexChanged.connect(self.getCurrentStyle)

        # 处理照片
        self.pushButton_processCurrent.clicked.connect(self.processCurrentImage)
        self.pushButton_processAll.clicked.connect(self.processAllImages)

    def eventFilter(self, obj: QObject, event: QEvent) -> bool:
        """
        处理鼠标事件，确保鼠标进入菜单栏时，状态栏显示默认信息
        :param obj: QObject
        :param event: QEvent
        :return: bool
        """
        if obj == self.menubar:
            self.status.showMessage(self.default_message)
        return super().eventFilter(obj, event)

    def menuAction(self) -> None:
        """
        菜单栏控件逻辑
        :return: None
        """
        self.actionfile.triggered.connect(self.openFile)
        self.actionfile.triggered.connect(self.showExif)

        self.actionfiles.triggered.connect(self.openMultipleFiles)
        self.actionfiles.triggered.connect(self.showExif)

        self.actionfolder.triggered.connect(self.openFolder)
        self.actionfolder.triggered.connect(self.showExif)

        self.actionsave.triggered.connect(self.saveFile)
        self.actionsave_as.triggered.connect(self.saveFile)
        self.actionsave_all.triggered.connect(self.saveAllFiles)

    def changePhoto(self) -> None:
        """
        照片切换控件逻辑
        :return: None
        """
        self.pushButton_first.clicked.connect(self.showFistImage)
        self.pushButton_first.clicked.connect(self.showExif)

        self.pushButton_prev.clicked.connect(self.showPrevImage)
        self.pushButton_prev.clicked.connect(self.showExif)

        self.pushButton_next.clicked.connect(self.showNextImage)
        self.pushButton_next.clicked.connect(self.showExif)

        self.pushButton_last.clicked.connect(self.showLastImage)
        self.pushButton_last.clicked.connect(self.showExif)

    def openFile(self) -> None:
        """
        菜单栏-打开-文件 控件 slot 函数
        :return: None
        """
        # 打开文件选择对话框，获取打开的文件路径
        file_name, _ = QFileDialog.getOpenFileName(self, "打开文件", "",
                                                   "图像文件 (*.png *.jpg *.jpeg *.bmp *.gif);;所有文件 (*)")

        # 如果有文件被打开，展示照片并重置 self.files_path、self.to_show_images、self.current_index
        # 确保清空之前已经保存的信息
        if file_name:
            self.displayImage(file_name)
            self.files_path = [file_name]
            self.to_show_images = copy.deepcopy(self.files_path)
            self.current_index = 0

    def openMultipleFiles(self) -> None:
        """
        菜单栏-打开-多个文件 控件 slot 函数
        :return: None
        """
        # 打开文件选择对话框，获取打开的文件路径
        file_names, _ = QFileDialog.getOpenFileNames(self, "打开多个文件", "",
                                                     "图像文件 (*.png *.jpg *.jpeg *.bmp *.gif);;所有文件 (*)")

        # 如果有文件被打开，展示第一张照片并重置 self.files_path、self.to_show_images、self.current_index
        # 确保清空之前已经保存的信息
        if file_names:
            self.to_show_images = copy.deepcopy(file_names)
            self.displayImage(file_names[0])
            self.files_path = file_names
            self.current_index = 0

    def openFolder(self):
        """
        菜单栏-打开-文件文件夹 控件 slot 函数
        :return: None
        """
        # 打开文件选择对话框，获取打开的文件夹路径
        folder_name = QFileDialog.getExistingDirectory(self, "打开文件夹")

        # 如果有文件夹被打开，展示第一张照片并重置 self.files_path、self.to_show_images、self.current_index
        # 确保清空之前已经保存的信息
        if folder_name:
            file_names = [folder_name + '/' + file for file in os.listdir(folder_name)]
            self.to_show_images = copy.deepcopy(file_names)
            self.displayImage(file_names[0])
            self.files_path = file_names
            self.current_index = 0

    def showFistImage(self) -> None:
        """
        照片切换按钮-第一张 控件 slot 函数
        :return: None
        """
        if self.to_show_images:
            self.current_index = 0
            self.displayImage(self.to_show_images[self.current_index])

    def showPrevImage(self) -> None:
        """
        照片切换按钮-上一张 控件 slot 函数
        :return: None
        """
        if self.to_show_images:
            # 当前为第一张时，按下后展示最后一张
            if self.current_index == 0:
                self.current_index = len(self.to_show_images)

            # 当前不是第一张时，按下展示上一张
            self.current_index -= 1
            self.displayImage(self.to_show_images[self.current_index])

    def showNextImage(self) -> None:
        """
        照片切换按钮-下一张 控件 slot 函数
        :return: None
        """
        if self.to_show_images:
            # 当前为最后一张时，按下后展示第一张
            if self.current_index == len(self.to_show_images) - 1:
                self.current_index = -1

            # 当前不是最后一张时，按下展示下一张
            self.current_index += 1
            self.displayImage(self.to_show_images[self.current_index])

    def showLastImage(self) -> None:
        """
        照片切换按钮-第一张 控件 slot 函数
        :return: 
        """
        if self.to_show_images:
            self.current_index = len(self.to_show_images) - 1
            self.displayImage(self.to_show_images[self.current_index])

    def displayImage(self, file: str | Image) -> None:
        """
        在照片展示框展示照片
        :param file: 照片路径或 Image 对象
        :return: None
        """
        # 判断 file 是否为路径，处理 file
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

    def showExif(self) -> None:
        """
        展示照片 exif 信息
        :return: 
        """
        current_file_path = self.files_path[self.current_index]

        # 如果能获取当前照片的 exif 信息，则展示
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

        # 无法获取时，不展示
        except ExifNotFound:
            self.label_Make.clear()
            self.label_Model.clear()
            self.label_LensModel.clear()
            self.label_FocalLength.clear()
            self.label_FNumber.clear()
            self.label_ISOSpeedRatings.clear()
            self.label_ExposureTime.clear()
            self.label_DateTime.clear()

        # 缺失信息时，不展示
        except KeyError:
            self.label_Make.clear()
            self.label_Model.clear()
            self.label_LensModel.clear()
            self.label_FocalLength.clear()
            self.label_FNumber.clear()
            self.label_ISOSpeedRatings.clear()
            self.label_ExposureTime.clear()
            self.label_DateTime.clear()

    def getCurrentStyle(self) -> None:
        """
        获取当前选择的样式
        :return: None
        """
        self.style = self.comboBox_styleSeletor.currentText()

    def processCurrentImage(self) -> None:
        """
        处理当前展示的照片
        :return:
        """
        # 获取照片 exif 信息
        current_file_path = self.files_path[self.current_index]
        exif = exif_model.ExifModel(current_file_path)

        if self.style != '无样式':
            # 根据 exif 信息和 style 获取水印的布局
            layout = LayoutModel(exif.exif, self.style)

            # 为当前图片添加水印
            watermarked_image = add_watermark(current_file_path, layout)

            # 展示处理后的图片，并缓存在 self.to_show_images 中
            self.to_show_images[self.current_index] = watermarked_image
            self.displayImage(watermarked_image)

    def processAllImages(self) -> None:
        """
        处理全部图片并在状态栏中实时展示进度
        :return: None
        """
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

    def saveFile(self) -> None:
        """以 PNG 格式保存当前图片"""
        file_name, _ = QFileDialog.getSaveFileName(self, '保存图片', '.', '图像文件 (*.png)')
        current_file = self.to_show_images[self.current_index]

        # 如果选择保存, 保存图片
        if file_name:
            if isinstance(current_file, QPixmap):
                current_file.save(file_name)

    def saveAllFiles(self) -> None:
        """
        保存所有已处理的文件
        :return: None
        """
        folder = QFileDialog.getExistingDirectory(self, '选择保存的文件夹')
        to_save_img = [(index, file) for index, file in enumerate(self.to_show_images) if isinstance(file, QPixmap)]
        total_images = len(to_save_img)

        if folder:
            i = 1
            for index, file in to_save_img:

                save_path = f'{folder}/{self.files_path[index].split('/')[-1].split('.')[0]}.png'
                file.save(save_path)

                # 计算进度百分比
                progress = i / total_images * 100
                self.status.showMessage(f"正在保存 {save_path} - 进度: {progress:.2f}%")

                # 强制更新 UI，避免界面卡住
                QApplication.processEvents()

                i += 1

            # 处理完成后恢复默认信息
            self.status.showMessage(self.default_message)
