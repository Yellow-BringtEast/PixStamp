import warnings
from fractions import Fraction

from PIL import Image, ExifTags

from src.exceptions import ExifNotFound

warnings.filterwarnings('ignore')


def extract_exif(file_path):
    img = Image.open(file_path)
    exif = img._getexif()

    if exif is None:
        raise ExifNotFound(f'{file_path} 不包含exif信息...')

    readable_exif = {}
    for tag_id, value in exif.items():
        tag = ExifTags.TAGS.get(tag_id, tag_id)
        if tag in ['Make', 'Model', 'DateTime', 'FNumber', 'FocalLength', 'ExposureTime', 'ISOSpeedRatings',
                   'LensModel']:
            readable_exif[tag] = value

    if readable_exif:
        fraction = Fraction(readable_exif['ExposureTime']).limit_denominator().as_integer_ratio()
        if fraction[0] == 1:
            readable_exif['ExposureTime'] = f'{fraction[0]}/{fraction[1]}s'
        else:
            readable_exif['ExposureTime'] = f'{fraction[0]}s'

        readable_exif['FocalLength'] = f'{int(readable_exif['FocalLength'])}mm'
        readable_exif['FNumber'] = f'f/{readable_exif['FNumber']}'
        readable_exif['ISOSpeedRatings'] = f'ISO{readable_exif['ISOSpeedRatings']}'

    return readable_exif


if __name__ == '__main__':
    print(extract_exif(r'E:\semi-utils\output\满月.jpg'))




