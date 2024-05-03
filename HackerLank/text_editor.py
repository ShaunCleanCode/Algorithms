class TextEditor:
    def __init__(self):
        self.current_string = ""
        self.stack = []

    def append(self, char_to_append):
        self.stack.append(self.current_string)
        self.current_string += char_to_append

    def delete(self, num_chars_to_delete):
        self.stack.append(self.current_string)
        self.current_string = self.current_string[:-int(num_chars_to_delete)]

    def print_char(self, position):
        print(self.current_string[int(position) - 1])

    def undo(self):
        if self.stack:
            self.current_string = self.stack.pop()

    def process_query(self, query):
        if query[0] == "1":
            self.append(query[1])
        elif query[0] == "2":
            self.delete(query[1])
        elif query[0] == "3":
            self.print_char(query[1])
        elif query[0] == "4":
            self.undo()


if __name__ == "__main__":
    editor = TextEditor()
    num_queries = int(input())

    for _ in range(num_queries):
        query = input().split()
        editor.process_query(query)


# String 은 문자열로 , 변경 불가능한(immutable) 객체이므로 문자열은 변경이 아니라 새롭게 할당되고 , 기존에 존재하는 스트링은 파이썬의 가비지 컬렉터에 의해서 제거됌

