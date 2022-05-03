import heapq
from collections import defaultdict


def ReadFile():
    with open(
        "/Users/bzabert/Documents/Python/Adevent of code/Day 15/AoC - day 15 - Input.txt"
    ) as data:
        df_list = data.read().strip()
        map = [[int(i) for i in line] for line in df_list.split("\n")]
        x_lim = len(map[0])
        y_lim = len(map)
        return map, x_lim, y_lim


def get(x, y):
    nro = map[y % y_lim][x % x_lim] + (x // x_lim) + (y // y_lim)
    return (nro - 1) % 9 + 1


def Seacrh_path(fisrt_nod):
    while len(fisrt_nod) > 0:
        cost, x, y = heapq.heappop(fisrt_nod)

        if (x, y) in nod_visited:
            continue
        nod_visited.add((x, y))

        cost_dic[(x, y)] = cost

        if x == X - 1 and y == Y - 1:
            break

        for (row_mov, col_mov) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_x = x + row_mov
            new_y = y + col_mov
            if not (0 <= new_x < X and 0 <= new_y < Y):
                continue
            heapq.heappush(
                fisrt_nod, (cost + get(new_x, new_y), new_x, new_y),
            )
    return cost_dic


if __name__ == "__main__":
    map, x_lim, y_lim = ReadFile()
    Y = y_lim * 5
    X = x_lim * 5
    nod_list = [(0, 0, 0)]
    heapq.heapify(nod_list)
    cost_dic = defaultdict(int)
    nod_visited = set()
    cost_dic = Seacrh_path(nod_list)
    print(cost_dic[(X - 1, Y - 1)])

