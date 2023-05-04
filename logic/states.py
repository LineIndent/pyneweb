import pynecone as pc


class State(pc.State):
    # Main state where all other states inherit from.#
    show_left: bool = False

    def left(self):
        self.show_left = not (self.show_left)
