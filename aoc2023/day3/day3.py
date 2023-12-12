import math
from collections import defaultdict

filename = 'day3.in'
# filename = "part1.test"


class Day3:
    data = None
    numbers_with_symbols_adj = list()
    gears = defaultdict(list)

    def __init__(self):
        with open(filename, 'r') as f:
            self.data = f.read().splitlines()
            self.traverse_grid()

    def find_adj(self, row_id, start, end, number):
        found_adj = False
        last = min(row_id + 1, len(self.data) - 1)

        for i in range(max(0, row_id - 1), last + 1):
            last_j = min(end + 1, len(self.data) - 1)
            for j in range(max(0, start - 1), last_j + 1):
                if not self.data[i][j].isalnum() and self.data[i][j] != '.':
                    found_adj = True
                    if self.data[i][j] == '*':
                        self.gears[(i, j)].append(int(number))

        if found_adj:
            self.numbers_with_symbols_adj.append(int(number))

    def traverse_grid(self):
        for row_id, row in enumerate(self.data):
            number = ''
            start = -1
            for column_id, cell in enumerate(self.data[row_id]):
                if cell.isdigit():
                    if start == -1:
                        start = column_id
                        number = ''
                    number += cell
                elif start != -1:
                    self.find_adj(row_id, start, column_id - 1, number)
                    start = -1
            if start != -1:
                self.find_adj(row_id, start, len(row) - 1, number)

    def solve_part1(self):
        print("Part 1: ", sum(self.numbers_with_symbols_adj))

    def solve_part2(self):
        sum_val = sum((math.prod(numbers) for numbers in self.gears.values() if len(numbers) >= 2))
        print("Part 2:", sum_val)

    def run(self):
        self.solve_part1()
        self.solve_part2()


if __name__ == "__main__":
    day = Day3()
    day.run()
