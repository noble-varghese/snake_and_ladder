

class Crocodile:
    def __init__(self, position, steps_back=5) -> None:
        self.name = "Crocodile"
        self.position = position
        self.steps_back = steps_back

    def next_position(self, new_position):
        return max(0, self.position - self.steps_back)

    def object_type(self):
        return self.name
