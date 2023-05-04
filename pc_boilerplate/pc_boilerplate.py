import pynecone as pc


from logic.script import script


app = pc.App()
script(app)
app.compile()
