import random

RANKS = "23456789TJQKA"   # rank index 0 = deuce ... 12 = ace
SUITS = "cdhs"

def rank(card: int) -> int:
    return card // 4

def suit(card: int) -> int:
    return card % 4

def to_str(card: int) -> str:
    return RANKS[rank(card)] + SUITS[suit(card)]

def from_str(s: str) -> int:
    """'As' -> ace of spades"""
    return RANKS.index(s[0]) * 4 + SUITS.index(s[1])

class Deck:
    def __init__(self, rng: random.Random | None = None):
        self.rng = rng or random.Random()
        self.cards = list(range(52))
        self.rng.shuffle(self.cards)

    def deal(self, n: int) -> list[int]:
        dealt, self.cards = self.cards[:n], self.cards[n:]
        return dealt