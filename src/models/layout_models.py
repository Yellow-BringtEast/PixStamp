import os
from configparser import ConfigParser

from src.models.config_models import FontModel, LogosModel, CONFIG_PATH


class LayoutModel(FontModel, LogosModel):
    def __init__(self, exif, style):
        FontModel.__init__(self)
        LogosModel.__init__(self)

        self.exif = exif
        self.settings_text = f"{self.exif['FocalLength']}  {self.exif['FNumber']}  {self.exif['ExposureTime']}  {self.exif['ISOSpeedRatings']}"
        self.exif['settings_text'] = self.settings_text

        self.logo = self.load_logo(self.exif['Make'])
        self.font = self.get_font(bold=False)
        self.bold_font = self.get_font(bold=True)
        self.font_padding_level = self.get_font_padding_level()

        self.layout_parser = ConfigParser()
        self.layout_parser.read(os.path.join(CONFIG_PATH, 'layout_config.cfg'))

        self.logo_position = self.layout_parser.get(style, 'logo_position')
        self.logo_enable = self.layout_parser.getint(style, 'logo_enable')
        self.is_logo_left = self.layout_parser.getint(style, 'is_logo_left')
        self.bg_color = self.layout_parser.get(style, 'bg_color')
        self.line_color = self.layout_parser.get(style, 'line_color')

        self.left_top_text = exif[self.layout_parser.get(f'{style}.left_top', 'text')]
        self.font_color_lt = self.layout_parser.get(f'{style}.left_top', 'font_color')
        self.bold_font_lt = self.layout_parser.getint(f'{style}.left_top', 'bold_font')

        self.left_bottom_text = exif[self.layout_parser.get(f'{style}.left_bottom', 'text')]
        self.font_color_lb = self.layout_parser.get(f'{style}.left_bottom', 'font_color')
        self.bold_font_lb = self.layout_parser.getint(f'{style}.left_bottom', 'bold_font')

        self.right_top_text = exif[self.layout_parser.get(f'{style}.right_top', 'text')]
        self.font_color_rt = self.layout_parser.get(f'{style}.right_top', 'font_color')
        self.bold_font_rt = self.layout_parser.getint(f'{style}.right_top', 'bold_font')

        self.right_bottom_text = exif[self.layout_parser.get(f'{style}.right_bottom', 'text')]
        self.font_color_rb = self.layout_parser.get(f'{style}.right_bottom', 'font_color')
        self.bold_font_rb = self.layout_parser.getint(f'{style}.right_bottom', 'bold_font')
