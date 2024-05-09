encodeChrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!._$,()"
decodeToNum = lambda a: encodeChrs.index(a) + 1
decodeToCoords = lambda alpha: (decodeToNum(alpha[0]), decodeToNum(alpha[1]))

def is_valid(data: str) -> bool:

    if len(data) < 6:
        return False
    if [c for c in data if c not in encodeChrs] != ["-", "-"]:
        return False

    path = [
        decodeToCoords(data[2:4]),  # End
        decodeToCoords(data[0:2]),  # Start
    ]

    data = data[4:].split("-")
    if not all([len(d) % 2 == 0 for d in data]):
        return False

    d = data[0]
    for i in range(0, len(d), 2):
        path.insert(1, decodeToCoords(d[i:i+2]))
    for i in range(len(path)-1):
        if abs(path[i][0] - path[i+1][0]) + abs(path[i][1] - path[i+1][1]) != 1:
            return False
    
    return True
