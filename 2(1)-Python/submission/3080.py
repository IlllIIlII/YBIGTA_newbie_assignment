from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Iterable


"""
TODO:
- Trie.push 구현하기
- (필요할 경우) Trie에 추가 method 구현하기
"""


T = TypeVar("T")


@dataclass
class TrieNode(Generic[T]):
    body: Optional[T] = None
    children: list[int] = field(default_factory=lambda: [])
    is_end: bool = False


class Trie(list[TrieNode[T]]):
    def __init__(self) -> None:
        super().__init__()
        self.append(TrieNode(body=None))

    def push(self, seq: Iterable[T]) -> None:
        """
        seq: T의 열 (list[int]일 수도 있고 str일 수도 있고 등등...)

        action: trie에 seq을 저장하기
        """
        # 구현하세요!
        current_node = self[0]
        for char in seq:
            if char not in current_node.children:
                new_node = TrieNode(body=char)
                self.append(new_node)
                current_node.children.append(len(self) - 1)
            current_node = self[current_node.children[-1]]
        current_node.is_end = True
        pass
            
       

    # 구현하세요!
    def calculate_order(self, node_idx: int = 0, mod: int = 1000000007) -> int:
        """
        node_idx: 현재 계산 중인 노드의 인덱스
        mod: 계산 중에 결과를 나눌 값 1000000007
        """
        current_node = self[node_idx]
        result = 1

        for child_idx in current_node.children:
            result *= self.calculate_order(child_idx, mod)
            result %= mod

    
        child_count = len(current_node.children)
        if child_count > 1:  
            for i in range(1, child_count + 1):
                result *= i
                result %= mod

        return result



import sys

MOD = 1000000007
"""
TODO:
- 일단 Trie부터 구현하기
- main 구현하기

힌트: 한 글자짜리 자료에도 그냥 str을 쓰기에는 메모리가 아깝다...
"""


def main() -> None:
    # 구현하세요!
    N = int(sys.stdin.readline()) 
    names = [sys.stdin.readline().strip() for _ in range(N)] 

    # 트라이 생성
    trie = Trie()

    # 이름을 트라이에 삽입
    for name in names:
        trie.push(name)

    answer = trie.calculate_order(0, MOD)
    print(answer)


    
    
    pass


if __name__ == "__main__":
    main()