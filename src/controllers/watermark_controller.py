from PIL import Image, ImageOps, ImageQt

from src.utils.cons import TRANSPARENT, GRAY
from src.utils.pic_utils import text_to_image, concatenate_image, padding_image, append_image_by_side, \
    resize_image_with_width

NORMAL_HEIGHT = 1000
SMALL_HORIZONTAL_GAP = Image.new('RGBA', (50, 20), color=TRANSPARENT)
MIDDLE_HORIZONTAL_GAP = Image.new('RGBA', (100, 20), color=TRANSPARENT)
LARGE_HORIZONTAL_GAP = Image.new('RGBA', (200, 20), color=TRANSPARENT)
SMALL_VERTICAL_GAP = Image.new('RGBA', (20, 50), color=TRANSPARENT)
MIDDLE_VERTICAL_GAP = Image.new('RGBA', (20, 100), color=TRANSPARENT)
LARGE_VERTICAL_GAP = Image.new('RGBA', (20, 200), color=TRANSPARENT)
LINE_GRAY = Image.new('RGBA', (20, 1000), color=GRAY)
LINE_TRANSPARENT = Image.new('RGBA', (20, 1000), color=TRANSPARENT)


def add_watermark(file_path, layout):
    image = Image.open(file_path)
    width, height = image.size

    # 计算图片比例
    image_ratio = width / height

    # 下方水印的占比
    ratio = (.04 if image_ratio >= 1 else .09) + 0.02 * layout.font_padding_level

    # 水印中上下边缘空白部分的占比
    padding_ratio = (.52 if image_ratio >= 1 else .7) - 0.04 * layout.font_padding_level

    # 创建一个空白的水印图片
    watermark = Image.new('RGBA', (int(NORMAL_HEIGHT / ratio), NORMAL_HEIGHT), color='#ffffff')

    with Image.new('RGBA', (10, 100), color='#ffffff') as empty_padding:
        # 填充左边的文字内容
        left_top = text_to_image(content=layout.left_top_text,
                                 font=layout.font,
                                 bold_font=layout.bold_font,
                                 is_bold=layout.bold_font_lt,
                                 fill=layout.font_color_lt)
        left_bottom = text_to_image(content=layout.left_bottom_text,
                                    font=layout.font,
                                    bold_font=layout.bold_font,
                                    is_bold=layout.bold_font_lb,
                                    fill=layout.font_color_lb)
        left = concatenate_image([left_top, empty_padding, left_bottom])
        # 填充右边的文字内容
        right_top = text_to_image(content=layout.right_top_text,
                                  font=layout.font,
                                  bold_font=layout.bold_font,
                                  is_bold=layout.bold_font_rt,
                                  fill=layout.font_color_rt)
        right_bottom = text_to_image(content=layout.right_bottom_text,
                                     font=layout.font,
                                     bold_font=layout.bold_font,
                                     is_bold=layout.bold_font_rb,
                                     fill=layout.font_color_rb)
        right = concatenate_image([right_top, empty_padding, right_bottom])

    # 将左右两边的文字内容等比例缩放到相同的高度
    max_height = max(left.height, right.height)
    left = padding_image(left, int(max_height * padding_ratio), 'tb')
    right = padding_image(right, int(max_height * padding_ratio), 't')
    right = padding_image(right, left.height - right.height, 'b')

    logo = layout.logo
    if layout.logo_enable:
        if layout.is_logo_left:
            # 如果 logo 在左边
            line = LINE_TRANSPARENT.copy()
            logo = padding_image(logo, int(padding_ratio * logo.height))
            append_image_by_side(watermark, [line, logo, left], is_start=logo is None)
            append_image_by_side(watermark, [right], side='right')
        else:
            # 如果 logo 在右边
            if logo is not None:
                # 如果 logo 不为空，等比例缩小 logo
                logo = padding_image(logo, int(padding_ratio * logo.height))
                # 插入一根线条用于分割 logo 和文字
                line = padding_image(LINE_GRAY, int(padding_ratio * LINE_GRAY.height * .8))
            else:
                line = LINE_TRANSPARENT.copy()
            append_image_by_side(watermark, [left], is_start=True)
            append_image_by_side(watermark, [logo, line, right], side='right')
            line.close()
    else:
        append_image_by_side(watermark, [left], is_start=True)
        append_image_by_side(watermark, [right], side='right')
    left.close()
    right.close()

    # 缩放水印的大小
    watermark = resize_image_with_width(watermark, width, auto_close=False)
    # 将水印图片放置在原始图片的下方
    bg = ImageOps.expand(image.convert('RGBA'),
                         border=(0, 0, 0, watermark.height),
                         fill=layout.bg_color)

    fg = ImageOps.expand(watermark, border=(0, height, 0, 0), fill=TRANSPARENT)
    result = Image.alpha_composite(bg, fg)
    watermark.close()

    # 更新图片对象
    result = ImageOps.exif_transpose(result).convert('RGB')
    result = ImageQt.toqpixmap(result)
    return result
