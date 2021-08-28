from .config import config
from .utils import db_is_ready as _db_is_ready
from .utils import connect
from .sql_query import SqlQuery


print("this is __init__.py")

__all__ = [
    'db_is_ready',
    'create_db',
    'create_user'
]


def db_is_ready():
    return _db_is_ready(config)


def create_user():
    connection = connect(config)
    sql_query = SqlQuery(connection)
    sql_query.create_user()


def create_db():
    connection = connect(config)
    sql_query = SqlQuery(connection)
    sql_query.create_db()
