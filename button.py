import is_fullwidth


def button(b, display):
    count = 0
    for d in display[b[1]]:
        if is_fullwidth.is_fullwidth(d):
            count += 1
    for i, s in enumerate(b[2]):
        if is_fullwidth.is_fullwidth(s):
            display[b[1]].pop(b[0]+i+10)
        display[b[1]][b[0]+i-count] = s
    return display
