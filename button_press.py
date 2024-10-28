import os
import time

import is_fullwidth


def button_press(b, display):
    w_count = 0
    for i, s in enumerate(b[2]):
        display[b[1]][b[0]+i] = "_"
        if is_fullwidth.is_fullwidth(s):
            w_count += 1
    for i in range(w_count):
        display[b[1]].insert(b[0], "_")
    os.system("clear")
    for d in display:
        print("\n"+"".join(d), end="")
    # for i, s in enumerate(b[2]):
    #     if unicodedata.east_asian_width(s) == "W":
    #         del display[b[1]][b[0]+i]
    #     display[b[1]][b[0]+i] = s
    time.sleep(0.2)
    # os.system("clear")
    # for d in display:
    #     print("\n"+"".join(d), end="")
