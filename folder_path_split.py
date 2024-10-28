def folder_path_split(folder_path):
    pp = [""]
    for p in folder_path.split("/"):
        if p == "":
            break
        pp.append(pp[-1]+p+"/")
    pp.pop(0)
    return pp
