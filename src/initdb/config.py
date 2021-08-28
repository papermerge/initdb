
__all__ = [
    'config', 'Config'
]


class Config:
    def __init__(self):
        self.host = "postgres"
        self.user = "postgres"
        self.database = "postgres"
        self.port = 5432

    def setup(self, configfile, **kwargs):
        pass

    def __str__(self):
        return f"Config(host={self.host}, user={self.user})"


config = Config()
