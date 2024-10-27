from src.utils.exif_utils import extract_exif

class ExifModel:
    def __init__(self, file_path):
        self.exif = extract_exif(file_path)

        # 相机品牌
        self.Make = self.exif['Make']

        # 相机型号
        self.Model = self.exif['Model']

        # 拍摄时间
        self.DateTime = self.exif['DateTime']

        # 光圈
        self.FNumber = self.exif['FNumber']

        # 焦距
        self.FocalLength = self.exif['FocalLength']

        # 快门速度
        self.ExposureTime = self.exif['ExposureTime']

        # ISO
        self.ISOSpeedRatings = self.exif['ISOSpeedRatings']

        # 镜头型号
        self.LensModel = self.exif['LensModel']

