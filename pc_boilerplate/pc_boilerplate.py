import pynecone as pc
from logic.script import script
from logic.states import State

from routes import *


app = pc.App(state=State)
app.compile()
script(app)
