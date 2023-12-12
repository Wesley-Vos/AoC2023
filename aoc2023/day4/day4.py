from aoc2023.day4.ScratchCardGame import ScratchCardGame

filename = "day4.in"
# filename = "part1.test"


class Day4:
    game: ScratchCardGame

    def __init__(self):
        self.game = ScratchCardGame(filename)

    def solve_part1(self):
        return self.game.count_points()

    def solve_part2(self):
        return self.game.play()

    def run(self):
        print("Part 1: ", self.solve_part1())
        print("Part 2: ", self.solve_part2())


if __name__ == "__main__":
    day = Day4()
    day.run()
