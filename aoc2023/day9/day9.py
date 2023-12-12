filename = "day9.in"
# filename = "part1.test"


class Day9:
    data = None

    def __init__(self):
        with open(filename) as f:
            data = f.read().splitlines()
        self.data = [[int(el) for el in line.split(' ')] for line in data]

    def predict_value(self, measurement):
        diff_list = measurement
        lists = [diff_list]
        while not all([val == 0 for val in diff_list]):
            diff_list = [val - prev for prev, val in zip(diff_list, diff_list[1:])]
            lists.append(diff_list)

        len_lists = len(lists)
        latest_numb = None

        for i in range(len_lists):
            j = len_lists - i - 1
            list = lists[j]

            if latest_numb is not None:
                next_val = list[-1] + latest_numb
                lists[j].append(next_val)

            latest_numb = list[-1]

        return lists[0][-1]

    def predict_value_backward(self, measurement):
        diff_list = measurement
        lists = [diff_list]
        while not all([val == 0 for val in diff_list]):
            diff_list = [val - prev for prev, val in zip(diff_list, diff_list[1:])]
            lists.append(diff_list)

        len_lists = len(lists)
        latest_numb = None

        for i in range(len_lists):
            j = len_lists - i - 1
            list = lists[j]

            if latest_numb is not None:
                next_val = list[0] - latest_numb
                lists[j] = [next_val] + lists[j]

            latest_numb = lists[j][0]

        return lists[0][0]

    def solve_part1(self):
        return sum([self.predict_value(measurement) for measurement in self.data])

    def solve_part2(self):
        return sum([self.predict_value_backward(measurement) for measurement in self.data])

    def run(self):
        print("Part 1: ", self.solve_part1())
        print("Part 2: ", self.solve_part2())


if __name__ == "__main__":
    day = Day9()
    day.run()
