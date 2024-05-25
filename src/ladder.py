

class Ladder:
    def __init__(self, start, end) -> None:
        self.name = "Ladder"
        self.start = start
        self.end = end

    def next_position(self, new_position):
        return self.end

    def object_type(self):
        return self.name
