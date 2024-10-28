from button_list import button_list
from button import button


def display_creater(terminal_size, folder_path_list):
    global display
    display = [[" " for _ in range(terminal_size.columns)]
               for _ in range(terminal_size.lines)]
    for x, path in enumerate(folder_path_list):
        print(path)
        for b in button_list(path, terminal_size):
            display = button(b, display, x*50)
    for d in display:
        print("\n"+"".join(d), end="")
    return display
