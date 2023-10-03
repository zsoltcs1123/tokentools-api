from datetime import date
from typing import Tuple

BIRTH_CARDS = {
    19: (0, "Sun / Wheel of Fortune / Magician"),
    18: (9, "Moon / Hermit"),
    17: (8, "Star / Strength"),
    16: (7, "Tower / Chariot"),
    15: (6, "Devil / Lovers"),
    14: (5, "Temperance / Hierophant"),
    13: (4, "Death / Emperor"),
    12: (3, "Hanged Man / Empress"),
    11: (2, "Justice / High Priestess"),
    10: (1, "Wheel of Fortune / Magician"),
    20: (2, "Judgement / High Priestess"),
    21: (3, "World / Empress")
}

def numerological_reduction(mm: int, dd: int, yyyy: int) -> int:
    constant = 20 if 2000 <= yyyy <= 2099 else 19
    total_sum = mm + dd + constant + (yyyy % 100)
    reduced_sum = sum(int(digit) for digit in str(total_sum))
    return reduced_sum if reduced_sum >= 10 else reduced_sum + 9 

def get_birth_card(dt: date) -> Tuple[int, int, str]:
    nr = numerological_reduction(dt.month, dt.day, dt.year)
    return (nr, BIRTH_CARDS[nr][0], BIRTH_CARDS[nr][1])

