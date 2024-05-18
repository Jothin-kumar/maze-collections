from os import mkdir, path, remove
from json import loads
from parse_maze import parse as parse_maze

if not path.exists('maze'):
    mkdir('maze')
    mkdir('maze/easy')
    mkdir('maze/medium')
    mkdir('maze/hard')
if path.exists('stats.txt'):
    remove('stats.txt')

for lvl in ['easy', 'medium', 'hard']:
    datas = []
    print("============================================================\n")
    print(f"Starting level - {lvl}")
    with open(f"maze-data/{lvl}.txt") as f:
        lines = [s.removesuffix("\n") for s in f.readlines()]
        assert len(lines) == len(set(lines)), f"Duplicate mazes in {lvl}.txt"
        for i, line in enumerate(lines):
            file_name = f"maze/{lvl}/{i+1}.json"
            if path.exists(file_name):
                with open(file_name, "r") as f2:
                    data = f2.read()
            else:
                with open(file_name, "w") as f2:
                    data = parse_maze(line, lvl, i+1)
                    f2.write(data)
            datas.append(loads(data))
            print(f"{lvl} level -> {str(i+1).zfill(5)} / {len(lines)} completed")
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
    print(f"Wrote stats for level - {lvl}")
    
    with open(f"maze/{lvl}/ratings.txt", "w") as f:
        f.write("\n".join(map(str, ratings)))
    print(f"Wrote ratings for level - {lvl}")

    print(f"Level - {lvl} completed", end="============================================================\n")
print("All mazes completed")