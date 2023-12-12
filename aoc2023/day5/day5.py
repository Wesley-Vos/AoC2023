from aoc2023.day5.farm import Farm

filename = "day5.in"
# filename = "part1.test"


class Day5:
    farm: Farm

    def __init__(self):
        self.farm = Farm(filename)

    def solve_part1(self):
        return self.farm.find_closest_location_simple()

    def solve_part2(self):
        return self.farm.find_closest_location_ranges()

    def run(self):
        print("Part 1: ", self.solve_part1())
        print("Part 2: ", self.solve_part2())


if __name__ == "__main__":
    day = Day5()
    day.run()
