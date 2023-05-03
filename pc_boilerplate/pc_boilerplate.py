import pynecone as pc
from logic.script import script

from routes import *


class State(pc.State):
    """The app state."""

    pass


app = pc.App(state=State)
script(app)
app.compile()
