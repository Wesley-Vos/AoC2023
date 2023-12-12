from aoc2023.day8.camel_card import CamelCard

filename = "day7.in"
# filename = "part1.test"


class Day7:
    data = None

    def __init__(self):
        with open(filename) as f:
            self.data = f.read().splitlines()

    def solve_part1(self):
        return CamelCard(self.data).calc_total_winnings()

    def solve_part2(self):
        return CamelCard(self.data, joker=True).calc_total_winnings()

    def run(self):
        print("Part 1: ", self.solve_part1())
        print("Part 2: ", self.solve_part2())


if __name__ == "__main__":
    day = Day7()
    day.run()
