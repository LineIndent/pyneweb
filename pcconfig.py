import pynecone as pc

class PcboilerplateConfig(pc.Config):
    pass

config = PcboilerplateConfig(
    app_name="pc_boilerplate",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
