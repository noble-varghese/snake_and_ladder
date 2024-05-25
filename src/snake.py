

class Snake:
    def __init__(self, head, tail) -> None:
        self.name = "Snake"
        self.head = head
        self.tail = tail

    def object_type(self):
        return self.name

    def next_position(self, new_position):
        return self.tail
