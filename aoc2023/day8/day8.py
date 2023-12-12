import re
from math import lcm

filename = "day8.in"
# filename = "part1.test"


class Day8:
    data = None
    instructions: [str] = []
    network = {}

    def __init__(self):
        with open(filename) as f:
            self.data = f.read().splitlines()
            self.instructions = [instr for instr in self.data[0]]
            for line in self.data[2:]:
                el, first, second = re.findall(r'\b\w+\b', line)
                self.network[el] = [first, second]

    def play(self, start, dest):
        cur = start
        cnt = 0
        number_of_instructions = len(self.instructions)
        instruction_to_idx_mapping = {'L': 0, 'R': 1}

        while cur != dest:
            instruction = self.instructions[cnt % number_of_instructions]
            cnt += 1
            cur = self.network[cur][instruction_to_idx_mapping[instruction]]

        return cnt

    def play2(self, ):
        curs = [el for el in self.network.keys() if el.endswith('A')]
        cnt = 0
        number_of_instructions = len(self.instructions)
        mapping = {'L': 0, 'R': 1}

        result = []

        while curs:
            instruction = self.instructions[cnt % number_of_instructions]
            idx_diff = mapping[instruction]
            cnt += 1
            new_curs = [self.network[cur][idx_diff] for cur in curs if not self.network[cur][idx_diff].endswith('Z')]
            if (len(curs) - len(new_curs)) > 0:
                result.append(cnt)
            curs = new_curs

        return lcm(*result)

    def solve_part1(self):
        return self.play('AAA', 'ZZZ')

    def solve_part2(self):
        return self.play2()

    def run(self):
        print("Part 1: ", self.solve_part1())
        print("Part 2: ", self.solve_part2())


if __name__ == "__main__":
    day = Day8()
    day.run()
