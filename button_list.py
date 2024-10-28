import os


def button_list(folder_path, terminal_size, x):
    files = os.listdir(folder_path)

    button_list = []
    for i, f in enumerate(files):
        if i == terminal_size.lines:
            break
        if os.path.isdir(os.path.join(folder_path, f)):
            r_f = "📁 " + f
        else:
            r_f = "📄 " + f
        button_list.append([10+50*x, i, r_f, folder_path+f])
    return button_list
