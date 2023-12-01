from trebuchet import Trebuchet


class Day1:
    trebuchet: Trebuchet

    def __init__(self):
        self.trebuchet = Trebuchet()

    def run(self, include_test_data=False) -> None:
        if include_test_data:
            print("Test input part 1, solution:", self.trebuchet.calibrate("part1.test"))
            print("Test input part 2, solution:", self.trebuchet.convert_and_calibrate("part2.test"))
        print("Real input part 1, solution:", self.trebuchet.calibrate("day1.in"))
        print("Real input part 2, solution:", self.trebuchet.convert_and_calibrate("day1.in"))


if __name__ == "__main__":
    day1 = Day1()
    day1.run(include_test_data=True)
