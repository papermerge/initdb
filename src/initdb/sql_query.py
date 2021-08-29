from psycopg2 import sql


class SqlQuery:
    def __init__(self, connection, config):
        self.connection = connection
        self.config = config

    def create_user(self):
        query = sql.SQL(
            "CREATE USER {user} WITH ENCRYPTED PASSWORD '{password}';"
        ).format(
            user=sql.Identifier(self.config.user),
            password=sql.Identifier(self.config.password)
        )

        cursor = self.connection.cursor()
        cursor.execute(query)
        cursor.close()
        self.connection.commit()

    def create_db(self):
        query = sql.SQL(
            "CREATE DATABASE {database} WITH OWNER {user}"
        ).format(
            user=sql.Identifier(self.config.user),
            database=sql.Identifier(self.config.database)
        )
        self.connection.autocommit = True
        with self.connection.cursor() as cursor:
            cursor.execute(query)

        self._grant_all_priv()

    def _grant_all_priv(self):
        query = sql.SQL(
            "GRANT ALL PRIVILEGES ON DATABASE {database} TO {user};"
        ).format(
            database=sql.Identifier(self.config.database),
            user=sql.Identifier(self.config.user)
        )

        with self.connection.cursor() as cursor:
            cursor.execute(query)
