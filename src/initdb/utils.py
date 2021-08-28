import time
import psycopg2


def connect(conf):
    try:
        conn = psycopg2.connect(
            database=conf.database,
            user=conf.user,
            password=conf.password,
            host=conf.host,
            port=conf.port
        )
    except Exception as e:
        print(e)
        raise

    return conn


def db_is_ready(conf):
    while(True):
        try:
            conn = connect(conf)
            conn.close()
        except Exception:
            time.sleep(1)

    return True
