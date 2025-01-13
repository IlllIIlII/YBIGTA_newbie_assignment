from lib import Trie
import sys

MOD = 1000000007
"""
TODO:
- 일단 Trie부터 구현하기
- main 구현하기

힌트: 한 글자짜리 자료에도 그냥 str을 쓰기에는 메모리가 아깝다...
"""


def main() -> None:
    
    N = int(sys.stdin.readline()) 
    names = [sys.stdin.readline().strip() for _ in range(N)] 

    
    trie = Trie()

    
    for name in names:
        trie.push(name)

    answer = trie.calculate_order(0, MOD)
    print(answer)


    
    
    pass


if __name__ == "__main__":
    main()