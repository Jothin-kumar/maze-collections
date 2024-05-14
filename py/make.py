from os import mkdir, path
from parse_maze import parse as parse_maze

if not path.exists('maze'):
    mkdir('maze')
    mkdir('maze/easy')
    mkdir('maze/medium')
    mkdir('maze/hard')

for lvl in ['easy', 'medium', 'hard']:
    with open(f"maze-data/{lvl}.txt") as f:
        lines = [s.removesuffix("\n") for s in f.readlines()]
        assert len(lines) == len(set(lines)), f"Duplicate mazes in {lvl}.txt"
        for i, line in enumerate(lines):
            with open(f"maze/{lvl}/{i+1}.txt", "w") as f2:
                data = parse_maze(line, lvl, i+1)
                f2.write(data)

    with open(f"maze/{lvl}/max.txt", "w") as f:
        f.write(str(i+1))