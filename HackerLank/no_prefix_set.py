# 트라이의 노드를 정의하는 클래스
class TrieNode:
    def __init__(self):
        self.children = {}  # 자식 노드를 저장하는 딕셔너리
        self.is_end_of_word = False  # 이 노드가 단어의 끝인지 표시

# 트라이 자료구조를 정의하는 클래스
class Trie:
    def __init__(self):
        self.root = TrieNode()  # 루트 노드 생성

    # 단어를 트라이에 삽입하면서 접두사 관계를 검사하는 메소드
    def insert_and_check(self, word):
        current_node = self.root
        for char in word:  # 단어의 각 문자에 대해
            if char not in current_node.children:
                current_node.children[char] = TrieNode()  # 자식 노드가 없으면 생성
            current_node = current_node.children[char]  # 다음 노드로 이동

            # 현재 노드가 단어의 끝이면, 현재 삽입하는 단어가 이전 단어의 접두사임
            if current_node.is_end_of_word:
                return False
        
        # 삽입하는 단어의 마지막 노드에 도달한 후, 자식이 있으면 현재 단어는 다른 단어의 접두사임
        if current_node.children:
            return False

        # 단어 삽입 완료, 현재 노드를 단어의 끝으로 표시
        current_node.is_end_of_word = True
        return True

# 주어진 단어 목록에서 접두사 관계를 검사하는 함수
def noPrefix(words):
    trie = Trie()  # 트라이 객체 생성
    for word in words:  # 모든 단어에 대해
        if not trie.insert_and_check(word):  # 트라이에 단어 삽입 및 검사
            print("BAD SET")  # 접두사 관계 발견
            print(word)
            return
    print("GOOD SET")  # 접두사 관계 없음

# 메인 실행 부분
if __name__ == '__main__':
    n = int(input().strip())  # 입력 받을 단어 수
    words = []
    for _ in range(n):
        words_item = input()  # 단어 입력 받기
        words.append(words_item)
    noPrefix(words)  # 함수 호출
