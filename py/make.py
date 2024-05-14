from os import mkdir, path
from json import loads
from parse_maze import parse as parse_maze

if not path.exists('maze'):
    mkdir('maze')
    mkdir('maze/easy')
    mkdir('maze/medium')
    mkdir('maze/hard')

for lvl in ['easy', 'medium', 'hard']:
    datas = []
    with open(f"maze-data/{lvl}.txt") as f:
        lines = [s.removesuffix("\n") for s in f.readlines()]
        assert len(lines) == len(set(lines)), f"Duplicate mazes in {lvl}.txt"
        for i, line in enumerate(lines):
            with open(f"maze/{lvl}/{i+1}.json", "w") as f2:
                data = parse_maze(line, lvl, i+1)
                datas.append(loads(data))
                f2.write(data)
    ratings = [d["rating"] for d in datas]
    min_rating = min(ratings)
    max_rating = max(ratings)
    with open(f"stats.txt", "a+") as f:
        f.write(f"""
Level: {lvl}
Mazes count: {len(lines)}
Average rating: {round(sum(ratings)/len(ratings), 2)}
Minimum rating: {min_rating} <Maze(s) with this rating: {', '.join([f"/{lvl}/@{i+1}" for i, r in enumerate(ratings) if r == min_rating])}>
Maximum rating: {max_rating} <Maze(s) with this rating: {', '.join([f"/{lvl}/@{i+1}" for i, r in enumerate(ratings) if r == max_rating])}>
""")

    with open(f"maze/{lvl}/max.txt", "w") as f:
        f.write(str(i+1))