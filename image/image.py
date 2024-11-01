from PIL import Image
from rich.console import Console
from rich.text import Text
import os

# コンソールの初期化
console = Console()

# 画像のファイルパスを指定
image_path = "/Users/chinq500/Desktop/GUI/image5.png"
image = Image.open(image_path)

# 最大の幅と高さを設定
max_width = 120
max_height = 40

original_width, original_height = image.size

# 幅と高さの比率を計算し、比率を維持した最大のサイズを決定
width_ratio = max_width / original_width
height_ratio = max_height / original_height
scaling_factor = min(width_ratio, height_ratio)

# 比率を維持したサイズにリサイズ
new_width = int(original_width * scaling_factor * 2)
new_height = int(original_height * scaling_factor)
resized_image = image.resize((new_width, new_height))

pixels = resized_image.load()

# アスキー文字のリストとピクセル密度
chars_list = [('M', 0.037*27), ('@', 0.037*26), ('%', 0.037*25), ('N', 0.037*24), ('B', 0.037*23), ('w', 0.037*22), ('m', 0.037*21), ('6', 0.037*20), ('E', 0.037*19), ('b', 0.037*18), ('4', 0.037*17), ('3', 0.037*16), ('2', 0.037*15),
              ('k', 0.037*14), ('7', 0.037*13), ('f', 0.037*12), ('1', 0.037*11), ('l', 0.037*10), ('r', 0.037*9), ('i', 0.037*8), ('!', 0.037*7), ('/', 0.037*6), ("'", 0.037*5), ('-', 0.037*4), (',', 0.037*3), ('_', 0.037*2)]

# ピクセルごとのアスキー文字に変換
pixel_list = []
for y in range(new_height):
    line_text = Text()
    for x in range(new_width):
        pixel = pixels[x, y]
        r, g, b = pixel[:3]  # RGB値
        brightness = sum(pixel[:3]) / (255 * 3)
        closest_char = min(
            chars_list, key=lambda char: abs(char[1] - brightness))[0]

        # Richでのカラー指定付きの文字を追加
        line_text.append(closest_char, style=f"rgb({r},{g},{b})")
    pixel_list.append(line_text)

os.system('clear')
# 結果を表示
for line in pixel_list:
    console.print(line)
