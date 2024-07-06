from dataclasses import dataclass

import noorm.psycopg2 as nm


@dataclass
class DbFeed:
    id: int
    name: str
    created_at: str
    user_id: int


@nm.sql_fetch_all(DbFeed, "SELECT id, name, created_at, user_id FROM dt_feed")
def get_all_feeds():
    ...


@nm.sql_one_or_none(
    DbFeed, "SELECT id, name, link, type FROM dt_feed id = :id"
)
def get_feed_by_id(id: int):
    return nm.params(id=id)


@nm.sql_execute("INSERT INTO dt_feed (name, user_id) VALUES (%s, %s)")
def create_new_feed(
    name: str,
    user_id: int,
):
    return nm.params(name, user_id)
