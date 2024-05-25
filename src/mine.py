

class Mine:
    def __init__(self, location, turns=2) -> None:
        self.name = "Mine"
        self.location = location
        # number of turns before movement.
        self.turns_held = turns

    def get_turns_held(self):
        return self.turns_held

    def next_position(self, new_position):
        # Mine doesn't allow movement. So returns no position change.
        return new_position

    def object_type(self):
        return self.name
