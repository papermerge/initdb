

class SqlQuery:
    def __init__(self, connection, config):
        self.connection = connection
        self.cursor = connection.cursor()
        self.config = config

    def create_user(self):
        sql = "CREATE USER %s WITH PASSWORD '%s';"
        self.cursor.execute(
            sql,
            (self.config.user, self.config.password)
        )
        self.cursor.commit()

    def create_db(self):
        sql = "CREATE DATABASE %s WITH OWNER '%s';"
        self.cursor.execute(
            sql,
            (self.config.database, self.config.owner)
        )
        self.cursor.commit()
        self._grant_all_priv()

    def _grant_all_priv(self):
        sql = "GRANT ALL PRIVILEGES ON DATABASE %s TO %s;"
        self.cursor.execute(
            sql,
            (self.config.database, self.config.owner)
        )
        self.cursor.commit()
