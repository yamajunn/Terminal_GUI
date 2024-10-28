import os


def folder_select(folder_path, terminal_size, x):
    files = os.listdir(folder_path)

    button_list = []
    for i, f in enumerate(files):
        if i == terminal_size.lines:
            break
        button_list.append([10+50*x, i, f, folder_path+f])
    return button_list
