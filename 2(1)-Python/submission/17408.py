from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Callable




T = TypeVar("T")
U = TypeVar("U")


class SegmentTree(Generic[T, U]):
    
    pass


import sys





class Pair(tuple[int, int]):
    
    def __new__(cls, a: int, b: int) -> 'Pair':
        return super().__new__(cls, (a, b))

    @staticmethod
    def default() -> 'Pair':
      
        return Pair(0, 0)

    @staticmethod
    def f_conv(w: int) -> 'Pair':
     
        return Pair(w, 0)

    @staticmethod
    def f_merge(a: Pair, b: Pair) -> 'Pair':
       
        return Pair(*sorted([*a, *b], reverse=True)[:2])

    def sum(self) -> int:
        return self[0] + self[1]


def main() -> None:
    pass


if __name__ == "__main__":
    main()