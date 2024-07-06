from dataclasses import dataclass

import noorm.psycopg2 as nm


@dataclass
class DbPost:
    id: int
    title: str
    description: str
    meta_info: str
    raw_content: str
    mark: str
    feed_id: int
    source_id: int


@nm.sql_fetch_all(DbPost, "SELECT id, title, description, meta_info, raw_content, mark, feed_id, source_id FROM dt_post")
def get_all_users():
    ...


@nm.sql_one_or_none(
    DbPost, "SELECT id, title, description, meta_info, raw_content, mark, feed_id, source_id FROM dt_post id = :id"
)
def get_post_by_id(id: int):
    return nm.params(id=id)


@nm.sql_execute("INSERT INTO dt_post (title, description, meta_info, raw_content, mark, feed_id, source_id) VALUES (%s, %s, %s, '-', true, 2, 1)")
def create_new_post(
    title: str,
    description: str,
    meta_info: str,
    # TODO: собирать поля
    # raw_content: str,
    # mark: str,
    # feed_id: int,
    # source_id: int,
):
    return nm.params(title, description, meta_info)
