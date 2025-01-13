from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Iterable





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
        
        
        current_node = self[0]
        for char in seq:
            if char not in current_node.children:
                new_node = TrieNode(body=char)
                self.append(new_node)
                current_node.children.append(len(self) - 1)
            current_node = self[current_node.children[-1]]
        current_node.is_end = True
        pass
            
       

    
    def calculate_order(self, node_idx: int = 0, mod: int = 1000000007) -> int:
        
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



def main() -> None:
    
    N = int(sys.stdin.readline()) 
    names = [sys.stdin.readline().strip() for _ in range(N)] 

   
    trie: Trie[str] = Trie()

    
    for name in names:
        trie.push(name)

    answer = trie.calculate_order(0, MOD)
    print(answer)


    
    
    pass


if __name__ == "__main__":
    main()