from PIL import Image, ImageDraw, ImageFont
import string

# 使用するフォントの指定
font = ImageFont.load_default()

# 半角文字のリスト（必要に応じて変更可能）
characters = list(string.printable[:94])  # !から~までのASCII文字


def calculate_black_pixel_ratio(char):
    # 文字を描画する画像を作成
    image = Image.new("1", (10, 10), color=1)  # 10x10ピクセルの白地の画像
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), char, font=font, fill=0)  # 黒い文字として描画

    # 黒いピクセルの数を計算
    black_pixels = sum(1 for pixel in image.getdata() if pixel == 0)
    total_pixels = image.size[0] * image.size[1]
    return black_pixels / total_pixels


# 各文字の黒いピクセル割合を計算してソート
char_density = [(char, calculate_black_pixel_ratio(char))
                for char in characters]
sorted_chars = sorted(char_density, key=lambda x: x[1], reverse=True)
print(sorted_chars)
