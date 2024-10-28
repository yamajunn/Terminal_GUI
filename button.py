import unicodedata


def button(b, display, x):
    for i, s in enumerate(b[2]):
        if unicodedata.east_asian_width(s) == "W":
            del display[b[1]][b[0]+i]
        display[b[1]][b[0]+i+x] = s
    return display
