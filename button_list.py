import os


def button_list(folder_path, terminal_size):
    files = os.listdir(folder_path)

    button_list = []
    for i, f in enumerate(files):
        if i == terminal_size.lines:
            break
        if os.path.isdir(os.path.join(folder_path, f)):
            f = "📁 " + f
        button_list.append([10, i, f])
    return button_list
