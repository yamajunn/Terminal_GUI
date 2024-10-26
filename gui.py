from pynput import mouse
import subprocess
import shutil
import os
import time

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

button_list = [terminal_size.columns//2-5, terminal_size.columns //
               2+5, terminal_size.lines//2-1, terminal_size.lines//2+1]


def button(button_list):
    display = [[" " for _ in range(terminal_size.columns)]
               for _ in range(terminal_size.lines)]
    for button_y in range(button_list[2], button_list[3]):
        display[button_y][button_list[0]:button_list[1]] = [
            "#" for _ in range(button_list[1]-button_list[0])]
    for d in display:
        print("".join(d))


def button_press(button_list):
    os.system("clear")
    display = [[" " for _ in range(terminal_size.columns)]
               for _ in range(terminal_size.lines)]
    for button_y in range(button_list[2], button_list[3]):
        display[button_y][button_list[0]:button_list[1]] = [
            "_" for _ in range(button_list[1]-button_list[0])]
    for d in display:
        print("".join(d))
    for button_y in range(button_list[2], button_list[3]):
        display[button_y][button_list[0]:button_list[1]] = [
            "#" for _ in range(button_list[1]-button_list[0])]
    time.sleep(0.5)
    for d in display:
        print("".join(d))


def on_move(mouse_x, mouse_y):
    global x, y, width, height, terminal_size, count, terminal_cursor_x, terminal_cursor_y
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
        terminal_cursor_y = int((mouse_y - y) / height * terminal_size.lines)
    else:
        terminal_cursor_x = 0
        terminal_cursor_y = 0

# マウスのクリックを監視


def on_click(x, y, button, pressed):
    if pressed:
        if button_list[0] <= terminal_cursor_x <= button_list[1] and button_list[2] <= terminal_cursor_y <= button_list[3]:
            button_press(button_list)


button(button_list)

with mouse.Listener(on_move=on_move, on_click=on_click) as listener:
    listener.join()
