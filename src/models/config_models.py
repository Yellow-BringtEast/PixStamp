import os
from configparser import ConfigParser

from PIL import Image, ImageFont

LOGOS_PATH = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..', '..', 'assets/logos'))
FONT_PATH = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..', '..', 'assets/fonts'))
CONFIG_PATH = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', 'config'))


class LogosModel:
    def __init__(self):
        self.logos_path = {
            'apple': os.path.join(LOGOS_PATH, 'apple.png'),
            'canon': os.path.join(LOGOS_PATH, 'canon.png'),
            'dji': os.path.join(LOGOS_PATH, 'DJI.png'),
            'fujifilm': os.path.join(LOGOS_PATH, 'fujifilm.png'),
            'hasselblad': os.path.join(LOGOS_PATH, 'HASSELBLAD.png'),
            'huawei': os.path.join(LOGOS_PATH, 'xmage.png'),
            'leica': os.path.join(LOGOS_PATH, 'leica.png'),
            'nikon': os.path.join(LOGOS_PATH, 'nikon.png'),
            'olympus': os.path.join(LOGOS_PATH, 'olympus.png'),
            'panasonic': os.path.join(LOGOS_PATH, 'panasonic.png'),
            'pentax': os.path.join(LOGOS_PATH, 'pentax.png'),
            'ricoh': os.path.join(LOGOS_PATH, 'ricoh.png'),
            'sony': os.path.join(LOGOS_PATH, 'sony.png'),
        }
        self.logos = {}

    def load_logo(self, make):
        make = make.lower()
        if make not in self.logos.keys():
            logo = Image.open(self.logos_path[make])
            self.logos[make] = logo
            return logo
        else:
            return self.logos[make]


class FontModel:
    def __init__(self):
        self.font_parser = ConfigParser()
        self.font_parser.read(os.path.join(CONFIG_PATH, 'font_config.cfg'))

        self.config = {
            'font_size': self.font_parser.getint('font', 'size'),
            'bold_font_size': self.font_parser.getint('bold_font', 'size'),
            'font': os.path.join(FONT_PATH, self.font_parser.get('font', 'type')),
            'bold_font': os.path.join(FONT_PATH, self.font_parser.get('bold_font', 'type')),
        }

    def get_font_size(self):
        font_size = self.config['font_size']
        if font_size == 1:
            return 240
        elif font_size == 2:
            return 250
        elif font_size == 3:
            return 300
        else:
            return 240

    def get_bold_font_size(self):
        font_size = self.config['bold_font_size']
        if font_size == 1:
            return 260
        elif font_size == 2:
            return 290
        elif font_size == 3:
            return 320
        else:
            return 260

    def get_font(self, bold):
        if bold:
            return ImageFont.truetype(self.config['bold_font'], self.get_bold_font_size())
        else:
            return ImageFont.truetype(self.config['font'], self.get_font_size())

    def get_font_padding_level(self):
        bold_font_size = self.config['bold_font_size'] if 1 <= self.config['bold_font_size'] <= 3 else 1
        font_size = self.config['font_size'] if 1 <= self.config['font_size'] <= 3 else 1
        return bold_font_size + font_size
