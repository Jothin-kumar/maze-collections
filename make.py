from os import mkdir, path

if not path.exists('maze'):
    mkdir('maze')

with open("mazes.txt") as f:
    for i, line in enumerate(f.readlines()):
        with open(f"maze/{i+1}.txt", "w") as f2:
            f2.write(line)

with open("maze/max.txt", "w") as f:
    f.write(str(i+1))