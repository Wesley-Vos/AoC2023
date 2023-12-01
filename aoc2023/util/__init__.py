class Day:
    data = None
    part1_testdata = None
    part2_testdata = None

    def __init__(self, filename_input, filename_part1_test, filename_part2_test, split=True):
        self.read_files(filename_input, filename_part1_test, filename_part2_test, split)

    def read_files(self, filename_input, filename_part1_test, filename_part2_test, split):
        self.data = self._read(filename_input, split)
        self.part1_testdata = self._read(filename_part1_test, split)
        self.part2_testdata = self._read(filename_part2_test, split)

    @staticmethod
    def _read(filename: str, split):
        with open(filename) as input_file:
            data = input_file.read()
            if split:
                data = data.splitlines()
        return data

    def solve_part1(self, data):
        return "Answer part 1: still unknown"

    def solve_part2(self, data):
        return "Answer part 2: still unknown"

    def run(self, test_data=False):
        if test_data:
            print(f"Answer test part 1: {self.solve_part1(self.part1_testdata)}")
            print(f"Answer test part 2: {self.solve_part2(self.part2_testdata)}")
        else:
            print(f"Answer part 1: {self.solve_part1(self.data)}")
            print(f"Answer part 2: {self.solve_part2(self.data)}")
