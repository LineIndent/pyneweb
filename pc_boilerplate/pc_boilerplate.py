import pynecone as pc


from logic.script import script

# from logic.states import State
# from routes import *


# class State(pc.State):
#     """The app state."""

#     show_left: bool = False

#     def right(self):
#         self.show_left = not (self.show_left)


app = pc.App()
script(app)
app.compile()
