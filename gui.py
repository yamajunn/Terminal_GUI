from pynput import mouse
import subprocess
import shutil
import os

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

terminal_str_x = 0
terminal_str_y = 0


def on_move(mouse_x, mouse_y):
    global x, y, width, height, terminal_size, count, terminal_str_x, terminal_str_y
    if count > 50:
        terminal_size = shutil.get_terminal_size()

        # AppleScriptを実行して出力を取得
        result = subprocess.run(
            ['osascript', '-e', script], stdout=subprocess.PIPE)
        output = result.stdout.decode().strip()
        x, y, width, height = map(int, output.replace(",", "").split())
        # os.system("clear")
        count = 0
    count += 1

    if x < mouse_x < x + width and y < mouse_y < y + height:
        terminal_str_x = int((mouse_x - x) / width * terminal_size.columns)
        terminal_str_y = int((mouse_y - y) / height * terminal_size.lines)
    else:
        terminal_str_x = 0
        terminal_str_y = 0


with mouse.Listener(on_move=on_move) as listener:
    listener.join()
