from pynput import mouse
import subprocess
import shutil
import os
import time
import unicodedata

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


def button(b):
    global display
    for i, s in enumerate(b[2]):
        if unicodedata.east_asian_width(s) == "W":
            del display[b[1]][b[0]+i]
        display[b[1]][b[0]+i] = s


def button_press(b):
    global display
    os.system("clear")
    for i, s in enumerate(b[2]):
        w_count = 0
        if unicodedata.east_asian_width(s) == "W":
            del display[b[1]][b[0]+i]
            display[b[1]][b[0]+i] = "_"
            display[b[1]][b[0]+i+1] = "_"
            w_count += 1[0, 11, 2, 3, 4, 5]
        else:
            display[b[1]][b[0]+i] = "_"
    for d in display:
        print("\n"+"".join(d), end="")
    for i, s in enumerate(b[2]):
        display[b[1]][b[0]+i] = s
    time.sleep(0.5)
    for d in display:
        print("\n"+"".join(d), end="")


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
        # os.system("clear")
    count += 1

    if x < mouse_x < x + width and y < mouse_y < y + height:
        terminal_cursor_x = int((mouse_x - x) / width * terminal_size.columns)
        terminal_cursor_y = int(
            (mouse_y - y) / height * (terminal_size.lines+0.8))
    else:
        terminal_cursor_x = 0
        terminal_cursor_y = 0

    print(f"\033[{terminal_cursor_y};{terminal_cursor_x}H", end="")
    # cursor_under_str = display[terminal_cursor_y][terminal_cursor_x]
    # display[terminal_cursor_y][terminal_cursor_x] = "X"
    # print(f"\033[0;0H", end="")
    # for d in display:
    #     print("\n"+"".join(d), end="")
    # display[terminal_cursor_y][terminal_cursor_x] = cursor_under_str

# マウスのクリックを監視


def on_click(x, y, button, pressed):
    if pressed:
        for b in button_list:
            if b[0] <= terminal_cursor_x < b[0]+len(b[2]) and b[1] == terminal_cursor_y:
                button_press(b)


look_path = "./"
files = os.listdir(look_path)

button_list = []
for i, f in enumerate(files):
    if i == terminal_size.lines:
        break
    button_list.append([10, i, f])
print(len(button_list))
print(terminal_size.lines)

display = [["#" for _ in range(terminal_size.columns)]
           for _ in range(terminal_size.lines)]

for b in button_list:
    button(b)
for d in display:
    print("\n"+"".join(d), end="")

with mouse.Listener(on_move=on_move, on_click=on_click) as listener:
    listener.join()
