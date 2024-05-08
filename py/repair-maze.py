for lvl in ['easy', 'medium', 'hard']:
    with open(f"maze-data/{lvl}.txt", "r") as f:
        c = f.read()

    while "\n\n" in c:
        c = c.replace("\n\n", "\n")
    c = c.replace("\"", "")
    c = c.removesuffix("\n")

    with open(f"maze-data/{lvl}.txt", "w") as f:
        f.write(c)