
import math


class Day2:
    def __init__(self):
        with open('day2.in', 'r') as f:
            self.data = f.read().splitlines()
        
        self.games = []
        for line in self.data:
            _, game = line.split(': ') 
            turns = [[item.split(' ') for item in turn.split(', ')] for turn in game.split('; ')]
            self.games.append(turns)
   
    def solve_part1(self):
        max_cubes = {'red': 12, 'green': 13, 'blue': 14}
        sum_val = sum(((game_id + 1) * all([all([int(cnt) <= max_cubes[color] for (cnt, color) in turn]) for turn in game])) for game_id, game in enumerate(self.games))

        print(sum_val)

    def solve_part2(self):
        sum_val = 0
        for game in self.games:
            min_cubes = {'red': 0,'green': 0,'blue': 0}

            for turn in game:
                for cnt, clr in turn:
                    min_cubes[clr] = max(min_cubes[clr], int(cnt))
            sum_val += math.prod(min_cubes.values())
        print(sum_val)

    def run(self):
        self.solve_part1()
        self.solve_part2()


if __name__ == "__main__":
    day = Day2()
    day.run()
