from pynput import mouse
import subprocess
import shutil
import os
import sys

import button_list
import button_press
import display_creater
import folder_path_split

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from image import image_viewer

# ターミナルのカーソルを非表示にする
# os.system("tput civis")

# AppleScriptを用いてターミナルウィンドウの位置とサイズを取得
script = '''
tell application "Terminal"
    set win to window 1
    set position_list to position of win
    set size_list to size of win
    return (item 1 of position_list) & " " & (item 2 of position_list) & " " & (item 1 of size_list) & " " & (item 2 of size_list)
end tell
'''
# AppleScriptを実行して出力を取得
result = subprocess.run(
    ['osascript', '-e', script], stdout=subprocess.PIPE)
output = result.stdout.decode().strip()
x, y, width, height = map(int, output.replace(",", "").split())

terminal_size = shutil.get_terminal_size()

count = 0

terminal_cursor_x = 0
terminal_cursor_y = 0

cursor_under_str = ""

folder_path = "./"

# display = [[" " for _ in range(terminal_size.columns)]
#            for _ in range(terminal_size.lines)]


def on_move(mouse_x, mouse_y):
    global x, y, width, height, terminal_size, count, terminal_cursor_x, terminal_cursor_y, display, cursor_under_str
    if count > 50:
        terminal_size = shutil.get_terminal_size()

        # AppleScriptを実行して出力を取得
        result = subprocess.run(
            ['osascript', '-e', script], stdout=subprocess.PIPE)
        output = result.stdout.decode().strip()
        x, y, width, height = map(int, output.replace(",", "").split())
        count = 0
    count += 1

    if x < mouse_x < x + width and y < mouse_y < y + height:
        terminal_cursor_x = int((mouse_x - x) / width * terminal_size.columns)
        terminal_cursor_y = int(
            (mouse_y - y) / height * (terminal_size.lines+0.8))
    else:
        terminal_cursor_x = 0
        terminal_cursor_y = 0

    print(f"\033[{terminal_cursor_y+1};{terminal_cursor_x+1}H", end="")

# マウスのクリックを監視


def on_click(x, y, button, pressed):
    global folder_path, display
    if pressed:
        folder_path_list = folder_path_split.folder_path_split(folder_path)
        for i, f in enumerate(folder_path_list):
            for b in button_list.button_list(f, terminal_size, i):
                if b[0] <= terminal_cursor_x < b[0]+len(b[2]) and b[1] == terminal_cursor_y:
                    button_press.button_press(b, display)
                    if b[3].endswith('.png'):
                        image_viewer.image_viewer(
                            b[3], terminal_size.columns, terminal_size.lines)
                        return
                    else:
                        folder_path = b[3]
        display = display_creater.display_creater(
            terminal_size, folder_path)


display = display_creater.display_creater(terminal_size, folder_path)

with mouse.Listener(on_move=on_move, on_click=on_click) as listener:
    listener.join()
