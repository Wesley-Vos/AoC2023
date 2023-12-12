import re
import math


filename = "day6.in"
# filename = "part1.test"


class Day6:
    time_str = None
    distance_str = None

    def __init__(self):
        with open(filename) as f:
            data = f.read().splitlines()
            self.time_str = data[0].split("Time:")[1].strip()
            self.distance_str = data[1].split("Distance:")[1].strip()

    @staticmethod
    def solve_eq(max_time, distance_record):
        discriminant = math.sqrt(max_time ** 2 - 4 * distance_record)
        return math.ceil((max_time - discriminant) / 2), math.floor((max_time + discriminant) / 2)

    def determine_number_of_ways(self, times, distances):
        number_of_ways_prd = 1
        for i in range(len(times)):
            t1, t2 = self.solve_eq(times[i], distances[i])
            number_of_ways_prd *= (t2 - t1 + 1)

        return number_of_ways_prd

    def solve_part1(self):
        _extract_numbers = lambda line: [int(num) for num in re.findall(r'\d+', line)]
        times, distances = (_extract_numbers(self.time_str), _extract_numbers(self.distance_str))

        return self.determine_number_of_ways(times, distances)

    def solve_part2(self):
        times = [int(self.time_str.replace(' ', ''))]
        distances = [int(self.distance_str.replace(' ', ''))]

        return self.determine_number_of_ways(times, distances)

    def run(self):
        print("Part 1: ", self.solve_part1())
        print("Part 2: ", self.solve_part2())


if __name__ == "__main__":
    day = Day6()
    day.run()
