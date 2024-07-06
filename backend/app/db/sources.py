from dataclasses import dataclass

import noorm.psycopg2 as nm


@dataclass
class DbSource:
    id: int
    name: str
    link: str
    type: str


@nm.sql_fetch_all(DbSource, "SELECT id, name, link, type FROM dt_source")
def get_all_sources():
    ...


@nm.sql_one_or_none(
    DbSource, "SELECT id, name, link, type FROM dt_source id = :id"
)
def get_source_by_id(id: int):
    return nm.params(id=id)


@nm.sql_execute("INSERT INTO dt_source (name, link, type) VALUES (%s, %s, %s)")
def create_new_source(
    name: str,
    link: str,
    type: str
):
    return nm.params(name, link, type)
