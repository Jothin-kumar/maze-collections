from json import dumps

encodeChrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!._$,()"
decodeToNum = lambda a: encodeChrs.index(a) + 1
decodeToCoords = lambda alpha: (decodeToNum(alpha[0]), decodeToNum(alpha[1]))

lvl_size = {
    "easy": 25,
    "medium": 49,
    "hard": 69,
}

def parse(data: str, level: str, maze_num) -> bool:

    data_original = data
    error_msg_prefix = f"Error in maze data {maze_num} of level {level}: "

    if len(data) < 6:
        raise ValueError(error_msg_prefix, "Too short")
    if [c for c in data if c not in encodeChrs[:lvl_size[level]]] != ["-", "-"]:
        raise ValueError(error_msg_prefix, "Invalid character(s) found")

    path = [
        decodeToCoords(data[2:4]),  # End
        decodeToCoords(data[0:2]),  # Start
    ]

    data = data[4:].split("-")
    if not all([len(d) % 2 == 0 for d in data]):
        raise ValueError(error_msg_prefix, "Invalid coordinates")

    d = data[0]
    for i in range(0, len(d), 2):
        path.insert(1, decodeToCoords(d[i:i+2]))
    for i in range(len(path)-1):
        if abs(path[i][0] - path[i+1][0]) + abs(path[i][1] - path[i+1][1]) != 1:
            raise ValueError(error_msg_prefix, "Lack of continuity in correct path")

    if len(set(path)) != len(path):  # Check for duplicates
        raise ValueError(error_msg_prefix, "Repetition found in correct path")

    # Now, the maze data is valid
    hidden_lines_coords = []
    for i in range(0, len(data[1]), 2):
        hidden_lines_coords.append((
            2*decodeToNum(data[1][i])+1,
            2*decodeToNum(data[1][i+1])
        ))
    for i in range(0, len(data[2]), 2):
        hidden_lines_coords.append((
            2*decodeToNum(data[2][i]),
            2*decodeToNum(data[2][i+1])+1
        ))
    get_movable_neighbors = lambda x, y: [(x+x_, y+y_) for x_, y_ in [(1, 0), (-1, 0), (0, 1), (0, -1)] if (2*x+x_, 2*y+y_) in hidden_lines_coords]
    rating = 0
    for x, y in path:
        rating += len(get_movable_neighbors(x, y)) - 2
    
    accepted_squares = path.copy()
    prev_connectables = accepted_squares.copy()
    def connect_connectable_squares():
        connectables = []
        for sq in prev_connectables:
            for neighbour_sq in get_movable_neighbors(*sq):
                if neighbour_sq not in connectables and neighbour_sq not in accepted_squares:
                    connectables.append(neighbour_sq)
        accepted_squares.extend(connectables)
        prev_connectables.clear()
        prev_connectables.extend(connectables)
        return len(connectables) > 0
    r = connect_connectable_squares()
    while r:
        r = connect_connectable_squares()
    rating *= len(accepted_squares)

    if level == "easy":
        rating /= 625
    elif level == "medium":
        rating /= 2401
    elif level == "hard":
        rating /= 4761
    rating *= 1000
    rating = int(rating)

    return dumps({
        "maze-data": data_original,
        "rating": rating
    }, indent=4)
