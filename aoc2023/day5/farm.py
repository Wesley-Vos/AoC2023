class SeedRange:
    start: int
    length: int
    end: int

    def __init__(self, start: int, length: int) -> None:
        self.start = start
        self.length = length
        self.end = start + length - 1

    def is_subset(self, other) -> bool:
        return self.start >= other.start and self.end <= other.end

    def is_superset(self, other) -> bool:
        return self.start < other.start and self.end > other.end

    def is_partially_overlapping_left(self, other) -> bool:
        return self.start < other.start <= self.end <= other.end

    def is_partially_overlapping_right(self, other) -> bool:
        return self.end > other.end >= self.start >= other.start

    def is_non_overlapping(self, other) -> bool:
        return (self.start < other.start and self.end < other.end) or (self.start > other.start and self.end > other.end)

    def split_range(self, range_to_extract) -> (any, any, any):
        left, middle, right = None, None, None

        if self.is_superset(range_to_extract):
            # larger left and right
            left = SeedRange(self.start, range_to_extract.start - self.start)
            middle = SeedRange(range_to_extract.start, range_to_extract.length)
            right = SeedRange(range_to_extract.end + 1, self.end - range_to_extract.end)
        elif self.is_subset(range_to_extract):
            # fully subset
            middle = SeedRange(self.start, self.length)
        elif self.is_partially_overlapping_left(range_to_extract):
            # larger on the left side
            left = SeedRange(self.start, range_to_extract.start - self.start)
            middle = SeedRange(range_to_extract.start, self.end - range_to_extract.start + 1)
        elif self.is_partially_overlapping_right(range_to_extract):
            # larger on the right side
            middle = SeedRange(self.start, range_to_extract.end - self.start + 1)
            right = SeedRange(range_to_extract.end + 1, self.end - range_to_extract.end)
        elif self.is_non_overlapping(range_to_extract):
            if self.start < range_to_extract.start:
                # all on left, no middle
                left = SeedRange(self.start, self.length)
            else:
                # all on right, no middle
                right = SeedRange(self.start, self.length)

        return left, middle, right

    def __repr__(self) -> str:
        return f"Range start at {self.start}, end at {self.end} (length {self.length})"

    def __eq__(self, other) -> int:
        return self.start == other.start and self.end == other.end

    def __lt__(self, other) -> int:
        if self.start == other.start:
            return self.length < other.length
        else:
            return self.start < other.start

    def __gt__(self, other) -> int:
        if self.start == other.start:
            return self.length > other.length
        else:
            return self.start > other.start


class Mapping:
    source_range: SeedRange
    destination_range: SeedRange
    offset: int

    def __init__(self, line):
        destination_start, source_start, range_length = list(map(int, line.split(' ')))
        self.source_range = SeedRange(source_start, range_length)
        self.destination_range = SeedRange(destination_start, range_length)
        self.offset = self.destination_range.start - self.source_range.start

    def map_range(self, seed_ranges: [SeedRange]) -> ([SeedRange], [SeedRange]):
        to_do, done = [], []

        for seed_range in seed_ranges:
            left, middle, right = seed_range.split_range(self.source_range)
            if left is not None:
                to_do.append(left)
            if middle is not None:
                middle = SeedRange(middle.start + self.offset, middle.length)       # map it to destination range
                done.append(middle)
            if right is not None:
                to_do.append(right)

        return done, to_do


class FarmMap:
    mappings: [Mapping] = []
    from_to_str: str = ""

    def __init__(self, mapping_input) -> None:
        self.from_to_str = mapping_input[0].split(' map:')[0]
        self.mappings = [Mapping(line) for line in mapping_input[1:]]

    def map_range(self, to_do: [SeedRange]) -> [SeedRange]:
        glob_done = []
        for mapping in self.mappings:
            done, to_do = mapping.map_range(to_do)
            glob_done += done

        glob_done += to_do
        return glob_done


class Farm:
    maps: {str: FarmMap} = {}
    seeds = [int]

    def __init__(self, filename: str) -> None:
        with open(filename) as f:
            data = f.read().splitlines()

        mapping_input = []
        for row in data:
            if row.startswith("seeds"):
                self.seeds = list(map(int, row.split("seeds: ")[1].split(' ')))
                continue

            if row == "":
                continue

            if row.endswith("map:"):
                if len(mapping_input) > 0:
                    new_map = FarmMap(mapping_input)
                    self.maps[new_map.from_to_str] = new_map
                mapping_input = []

            mapping_input.append(row)

        if len(mapping_input) > 0:
            new_map = FarmMap(mapping_input)
            self.maps[new_map.from_to_str] = new_map

    def map_seed_range_to_closet_location(self, seed_range: SeedRange) -> int:
        mapping_order = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
        seed_ranges = [seed_range]

        for mapping_from, mapping_to in zip(mapping_order, mapping_order[1:]):
            mapper_key = f"{mapping_from}-to-{mapping_to}"
            seed_ranges = self.maps[mapper_key].map_range(seed_ranges)
        return sorted(seed_ranges)[0].start

    def find_closest_location_simple(self) -> int:
        return min([self.map_seed_range_to_closet_location(seed_range) for seed_range in
                    [SeedRange(seed, 1) for seed in self.seeds]])

    def find_closest_location_ranges(self) -> int:
        return min([self.map_seed_range_to_closet_location(seed_range) for seed_range in
                    [SeedRange(self.seeds[i], self.seeds[i + 1]) for i in range(0, len(self.seeds), 2)]])
