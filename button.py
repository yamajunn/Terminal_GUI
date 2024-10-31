import is_fullwidth


def button(b, display):
    for i, s in enumerate(b[2]):
        if is_fullwidth.is_fullwidth(s):
            display[b[1]].pop(b[0]+i)
        display[b[1]][b[0]+i] = s
    return display
