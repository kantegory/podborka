from dataclasses import dataclass

import noorm.psycopg2 as nm


@dataclass
class DbUser:
    id: int
    login: str


@nm.sql_fetch_all(DbUser, "SELECT id, login FROM dt_user")
def get_all_users():
    ...


@nm.sql_one_or_none(
    DbUser, "SELECT id, login FROM dt_user id = :id"
)
def get_user_by_id(id: int):
    return nm.params(id=id)


@nm.sql_execute("INSERT INTO dt_user (login, password) VALUES (%s, %s)")
def create_new_user(login: str, password: str):
    return nm.params(login, password)


def main():
    import psycopg2
    with psycopg2.connect(database='maindb', user='maindb', password='maindb', host='localhost', port='15432') as conn:
        create_new_user(conn, 'test', 'test')
        conn.commit()

main()
