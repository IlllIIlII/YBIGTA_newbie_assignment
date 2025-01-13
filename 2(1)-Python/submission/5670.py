from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Iterable


"""
TODO:
- Trie.push �����ϱ�
- (�ʿ��� ���) Trie�� �߰� method �����ϱ�
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
        seq: T�� �� (list[int]�� ���� �ְ� str�� ���� �ְ� ���...)

        action: trie�� seq�� �����ϱ�
        """
        # �����ϼ���!
        current_node = self[0]
        for char in seq:
            if char not in current_node.children:
                new_node = TrieNode(body=char)
                self.append(new_node)
                current_node.children.append(len(self) - 1)
            current_node = self[current_node.children[-1]]
        current_node.is_end = True
        pass
            
       

    # �����ϼ���!
    def calculate_order(self, node_idx: int = 0, mod: int = 1000000007) -> int:
        """
        node_idx: ���� ��� ���� ����� �ε���
        mod: ��� �߿� ����� ���� �� 1000000007
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


"""
TODO:
- �ϴ� Trie���� �����ϱ�
- count �����ϱ�
- main �����ϱ�
"""


def count(trie: Trie, query_seq: str) -> int:
    """
    trie - �̸� �״�� trie
    query_seq - �ܾ� ("hello", "goodbye", "structures" ��)

    returns: query_seq�� �ܾ �Է��ϱ� ���� ��ư�� ������ �ϴ� Ƚ��
    """
    pointer = 0
    cnt = 0

    for element in query_seq:
        if len(trie[pointer].children) > 1 or trie[pointer].is_end:
            cnt += 1

        new_index = None # �����ϼ���!

        pointer = new_index

    return cnt + int(len(trie[0].children) == 1)


def main() -> None:
    # �����ϼ���!
    pass


if __name__ == "__main__":
    main()