from enum import Enum
from collections import Counter


class SortedEnum(Enum):
    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __hash__(self):
        return self.value

    def __repr__(self):
        return str(self.name)


class HandType(SortedEnum):
    FIVE_OAK = 7
    FOUR_OAK = 6
    FH = 5
    THREE_OAK = 4
    TP = 3
    OP = 2
    HC = 1


class Card(SortedEnum):
    A = 13
    K = 12
    Q = 11
    J = 10
    T = 9
    NINE = 8
    EIGHT = 7
    SEVEN = 6
    SIX = 5
    FIVE = 4
    FOUR = 3
    THREE = 2
    TWO = 1


class Card2(SortedEnum):
    A = 13
    K = 12
    Q = 11
    T = 10
    NINE = 9
    EIGHT = 8
    SEVEN = 7
    SIX = 6
    FIVE = 5
    FOUR = 4
    THREE = 3
    TWO = 2
    J = 1


class Hand:
    cards: [Card]
    bid: int
    type: HandType | None = None
    rank: int = 0
    joker: bool
    input_cards: str

    def __init__(self, row: str, joker=False):
        self.joker = joker
        cards, bid = row.split(' ')
        self.input_cards = cards
        self.bid = int(bid)
        self.type = None
        self.rank = 0

        if self.joker:
            self.cards = [Card2(int(card)) if card.isdigit() else Card2[card] for card in cards]
        else:
            self.cards = [Card(int(card) - 1) if card.isdigit() else Card[card] for card in cards]
        self.determine_hand_type()

    def __repr__(self):
        return f"Hand: type {self.type} rank {self.rank} and bid {self.bid} [" + ", ".join([str(card) for card in self.cards]) + "]"

    def determine_hand_type(self):
        counted_hand = Counter(self.cards)
        if self.joker:
            if 'J' in self.input_cards:
                most_frequent_card = None
                for card, cnt in counted_hand.most_common(2):
                    if card is not Card2.J:
                        most_frequent_card = card
                        break
                cards = [most_frequent_card if card == Card2.J else card for card in self.cards]
                counted_hand = Counter(cards)

        sorted_counted_hand = sorted(counted_hand.values())

        if len(counted_hand) == 1:
            self.type = HandType.FIVE_OAK
        elif any(count == 4 for count in counted_hand.values()):
            self.type = HandType.FOUR_OAK
        elif sorted_counted_hand == [2, 3]:
            self.type = HandType.FH
        elif sorted_counted_hand == [1, 1, 3]:
            self.type = HandType.THREE_OAK
        elif sorted_counted_hand == [1, 2, 2]:
            self.type = HandType.TP
        elif 2 in counted_hand.values():
            self.type = HandType.OP
        else:
            self.type = HandType.HC

    def winning(self):
        return self.rank * self.bid

    def __lt__(self, other):
        if self.type != other.type:
            return self.type < other.type
        else:
            return self.cards < other.cards

    def __eq__(self, other):
        return self.type == other.type and self.cards == other.cards

    def __gt__(self, other):
        if self.type != other.type:
            return self.type > other.type
        else:
            return self.cards > other.cards


class CamelCard:
    hands: [Hand] = []
    joker: bool

    def __init__(self, data, joker=False):
        self.joker = joker
        self.hands = []
        for row in data:
            self.hands.append(Hand(row, joker))
        self.rank_hands()

    def rank_hands(self):
        rank = 1
        for hand in sorted(self.hands):
            hand.rank = rank
            rank += 1

    def calc_total_winnings(self) -> int:
        return sum(hand.winning() for hand in self.hands)

