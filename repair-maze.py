with open("mazes.txt", "r") as f:
    c = f.read()

while "\n\n" in c:
    c = c.replace("\n\n", "\n")
c = c.replace("\"", "")
c = c.removesuffix("\n")

with open("mazes.txt", "w") as f:
    f.write(c)