"""Examples of "vectorized" operations via magic methods."""

from __future__ import annotations
from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items
    
    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        result: StrArray = StrArray([])
        if type(rhs) == str:
            for i in self.items:
                result.items.append(i + rhs)
        else:
            i: int = 0
            while i < len(self.items) and i < len(rhs.items):
                result.items.append(self.items[i] + rhs.items[i])
                i += 1
        return result

a: StrArray = StrArray(["Armando", "Pete", "Leaky"])
b: StrArray = StrArray(["Bacot", "Nance", "Black"])
print(a)
print(a + "!")
print(a + b)