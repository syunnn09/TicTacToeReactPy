def calculate_winner(squares):
    lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for i in range(len(lines)):
        a, b, c = lines[i]
        if squares[a] and squares[a] == squares[b] == squares[c]:
            return squares[a]
    return None
