from os import mkdir, path, remove
from json import loads
from pytz import timezone
from datetime import datetime
from parse_maze import parse as parse_maze

if not path.exists('maze'):
    mkdir('maze')
    mkdir('maze/easy')
    mkdir('maze/medium')
    mkdir('maze/hard')
if path.exists('stats.txt'):
    remove('stats.txt')

total_maze_count = 0

for lvl in ['easy', 'medium', 'hard']:
    datas = []
    print("********************\n")
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
    total_maze_count += len(lines)
    with open(f"stats.txt", "a+") as f:
        f.write(f"""
Level: {lvl}
 -> Mazes count: {len(lines)}
 -> Average rating: {str(round(sum(ratings)/len(ratings), 2)).rjust(10)}
 -> Minimum rating: {str(min_rating).rjust(10)}          Maze(s) with this rating: {', '.join([str(i+1) for i, r in enumerate(ratings) if r == min_rating])}
 -> Maximum rating: {str(max_rating).rjust(10)}          Maze(s) with this rating: {', '.join([str(i+1) for i, r in enumerate(ratings) if r == max_rating])}
""")
    print(f"Wrote stats for {lvl} level")

    with open(f"maze/{lvl}/ratings.txt", "w") as f:
        f.write("\n".join(map(str, ratings)))
    print(f"Wrote ratings for {lvl} level")

    print(f"{lvl} level completed", end="\n"*2)

print("All mazes completed")


with open("stats.txt", "a") as f:
    f.write(f"""

Total maze count: {total_maze_count}
Last updated: {datetime.now(timezone("Asia/Kolkata")).strftime("%d %B %Y (%A) | %I:%M:%S %p [IST]")}
""")

print("\n********************\n\nStats:")
with open("stats.txt", "r") as f:
    print(f.read())
print("********************\n")