import button_list
import button
import folder_path_split


def display_creater(terminal_size, folder_path):
    folder_path_list = folder_path_split.folder_path_split(folder_path)[-4:]
    display = [[" " for _ in range(terminal_size.columns)]
               for _ in range(terminal_size.lines)]
    for x, path in enumerate(folder_path_list):
        for b in button_list.button_list(path, terminal_size, x):
            display = button.button(b, display)
            for d in range(len(display)):
                display[d][b[0]-5] = "|"
    for d in display:
        print("\n"+"".join(d), end="")
    return display
