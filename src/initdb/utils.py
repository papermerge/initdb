import time
import psycopg2

from .sql_query import SqlQuery


def connect(host, port, database, user, password):
    try:
        conn = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )
    except Exception as e:
        print(e)
        raise

    return conn


def db_is_ready(conf):
    """
    Is database up and running ?

    This is blocking function, which means that
    it will block entire script execution until database
    will be available - i.e. it will be able to connect
    with initial_user + initial_password + host to the database
    """
    while(True):
        try:
            conn = connect(
                user=conf.initial_user,
                password=conf.initial_password,
                host=conf.host,
                port=conf.port
            )
            conn.close()
        except Exception:
            time.sleep(1)

    return True


def create_user(conf):
    connection = connect(
        user=conf.initial_user,
        password=conf.initial_password,
        host=conf.host,
        port=conf.port
    )
    sql_query = SqlQuery(
        connection=connection,
        config=conf
    )
    sql_query.create_user()


def create_db(conf):
    connection = connect(
        user=conf.initial_user,
        password=conf.initial_password,
        host=conf.host,
        port=conf.port
    )
    sql_query = SqlQuery(
        connection=connection,
        config=conf
    )
    sql_query.create_db()
