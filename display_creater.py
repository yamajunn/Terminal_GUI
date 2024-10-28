from button_list import button_list
from button import button


def display_creater(terminal_size, folder_path):
    global display
    display = [[" " for _ in range(terminal_size.columns)]
               for _ in range(terminal_size.lines)]
    folder_path_list = [p for p in folder_path.split("/")]
    for i in range(len(folder_path_list)):
        if folder_path_list[i] == "":
            folder_path_list.pop(i)
    for x, path in enumerate(folder_path_list):
        print(path)
        for b in button_list(path, terminal_size):
            display = button(b, display, x*50)
    for d in display:
        print("\n"+"".join(d), end="")
