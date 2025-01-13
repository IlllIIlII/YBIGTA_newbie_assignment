from __future__ import annotations
import copy


"""
TODO:
- __setitem__ 구현하기
- __pow__ 구현하기 (__matmul__을 활용해봅시다)
- __repr__ 구현하기
"""


class Matrix:
    MOD = 1000

    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix = matrix

    @staticmethod
    def full(n: int, shape: tuple[int, int]) -> Matrix:
        return Matrix([[n] * shape[1] for _ in range(shape[0])])

    @staticmethod
    def zeros(shape: tuple[int, int]) -> Matrix:
        return Matrix.full(0, shape)

    @staticmethod
    def ones(shape: tuple[int, int]) -> Matrix:
        return Matrix.full(1, shape)

    @staticmethod
    def eye(n: int) -> Matrix:
        matrix = Matrix.zeros((n, n))
        for i in range(n):
            matrix[i, i] = 1
        return matrix

    @property
    def shape(self) -> tuple[int, int]:
        return (len(self.matrix), len(self.matrix[0]))

    def clone(self) -> Matrix:
        return Matrix(copy.deepcopy(self.matrix))

    def __getitem__(self, key: tuple[int, int]) -> int:
        return self.matrix[key[0]][key[1]]
    """
    이 메소드는 행렬의 특정 부분에 특정 값을 넣기 위한 것입니다.
    Args:
        - key : 특정 부분이 어디인지 특정하는 튜플입니다.
        - value: 행렬에 넣을 값입니다.
    Result:
        key에 해당하는 행렬 자리에 value값이 들어갑니다.
    """
    def __setitem__(self, key: tuple[int, int], value: int) -> None:
        self.matrix[key[0]][key[1]] = value
       
        

    def __matmul__(self, matrix: Matrix) -> Matrix:
        x, m = self.shape
        m1, y = matrix.shape
        assert m == m1

        result = self.zeros((x, y))

        for i in range(x):
            for j in range(y):
                for k in range(m):
                    result[i, j] += self[i, k] * matrix[k, j]
                    result[i, j] %= self.MOD  

        return result
    """
    이 메소드는 분할 정복을 이용한 행렬의 거듭제곱을 수행하는 메소드입니다.
    Args:
          - n : 몇 제곱을 할지 정하는 숫자입니다.
    result:
         행렬의 거듭제곱이 실행됩니다. (0일경우 단위행렬)
    """
    def __pow__(self, n: int) -> Matrix:
        M = self
        result = Matrix.eye(self.shape[0])

        while n > 0:
            if n % 2 == 1:
                result = result.__matmul__(M)
            M = M.__matmul__(M)
            n //= 2

        for i in range(result.shape[0]):
            for j in range(result.shape[0]):
                result[i, j] %= self.MOD 

        return result
        pass
    """
    행렬을 문자열로 바꾸는 메소드입니다.
    result:
           map을 이용해 각 행을 문자열로 바꾸고 공백으로 join시킨 뒤, 모든 줄들을 줄바꿈으로 join시켜 하나의 문자열로 만듭니다. 
    """
    def __repr__(self) -> str:
        
        return "\n".join(" ".join(map(str, row)) for row in self.matrix)
         
        pass


from typing import Callable
import sys


"""
아무것도 수정하지 마세요!
"""


def main() -> None:
    
    intify: Callable[[str], list[int]] = lambda l: [*map(int, l.split())]

    lines: list[str] = sys.stdin.readlines()

    N, B = intify(lines[0])
    matrix: list[list[int]] = [*map(intify, lines[1:])]

    Matrix.MOD = 1000
    modmat = Matrix(matrix)

    print(modmat ** B)



if __name__ == "__main__":
    main()