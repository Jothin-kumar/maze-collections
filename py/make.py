from os import mkdir, path
from validate import is_valid as maze_is_valid

if not path.exists('maze'):
    mkdir('maze')
    mkdir('maze/easy')
    mkdir('maze/medium')
    mkdir('maze/hard')

for lvl in ['easy', 'medium', 'hard']:
    with open(f"maze-data/{lvl}.txt") as f:
        for i, line in enumerate(f.readlines()):
            with open(f"maze/{lvl}/{i+1}.txt", "w") as f2:
                line = line.removesuffix("\n")
                assert maze_is_valid(line, lvl), f"Invalid maze: {i+1} in {lvl} level"
                f2.write(line)

    with open(f"maze/{lvl}/max.txt", "w") as f:
        f.write(str(i+1))