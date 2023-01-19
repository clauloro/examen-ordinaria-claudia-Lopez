def movimientos_caballo(inicial, final):
    tablero = [[0 for _ in range(8)] for _ in range(8)]
    movimientos = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    cola = [(start[0], start[1], 0)]
    while cola:
        x, y, count = cola.pop(0)
        if (x, y) == (final[0], final[1]):
            return count
        tablero[x][y] = 1
        for dx, dy in movimientos:
            if 0 <= x+dx < 8 and 0 <= y+dy < 8 and tablero[x+dx][y+dy] != 1:
                cola.append((x+dx, y+dy, count+1))
    return -1

start = (0, 0)
end = (1, 2)
print(movimientos_caballo(start, end))
