from button_list import button_list
from button import button


def display_creater(terminal_size, folder_path_list):
    global display
    display = [[" " for _ in range(terminal_size.columns)]
               for _ in range(terminal_size.lines)]
    for x, path in enumerate(folder_path_list[-4:]):
        print(path)
        for b in button_list(path, terminal_size, x):
            display = button(b, display)
    for d in display:
        print("\n"+"".join(d), end="")
    return display
