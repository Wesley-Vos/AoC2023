class ScratchCardGame:
    cards: list

    def __init__(self, filename: str) -> None:
        with open(filename) as f:
            self.cards = [self.parse(row) for row in f.read().splitlines()]
    
    def parse(self, row):
        card_id, numbers = row.split(": ")
        winning_numbers, my_numbers = (set(int(el[i:(i + 2)]) for i in range(0, len(el), 3)) for el in
                                       numbers.split("| "))
        number_of_winning_numbers = len(winning_numbers.intersection(my_numbers))
        return [int(card_id.split("Card ")[1]), number_of_winning_numbers, 1]

    def count_points(self) -> int:
        return sum(2 ** (card[1] - 1) if card[1] > 0 else 0 for card in self.cards)

    def play(self) -> int:
        for card in self.cards:
            for i in range(card[0] + 1, card[0] + card[1] + 1):
                self.cards[i - 1][2] += card[2]

        return sum(card[2] for card in self.cards)
