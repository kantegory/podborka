import feedparser
from dataclasses import dataclass, asdict

import psycopg2
import json

from db.posts import create_new_post



@dataclass
class Post:
    title: str
    description: str
    meta_info: dict[str, any]


def parse(link):
    feed = feedparser.parse(link)

    posts = []

    for post in feed.entries:
        posts.append(
            Post(
                title=post.title,
                description=post.summary,
                meta_info={
                    'published_at': post.published,
                    'author': post.author,
                    'tags': list(map(lambda tag: tag['term'], post.tags)),
                    'link': post.link,
                    # TODO: добавить поля
                    # 'raw_content': '-',
                    # 'mark': '-',
                    # 'feed_id': 1,
                    # 'source_id': 1,
                }
            )
        )

    return posts


def generate_feed(sources):
    posts = []

    for source in sources:
        posts_by_source = parse(source)

        posts.extend(posts_by_source)

    return posts


def save_posts(posts):
    with psycopg2.connect(database='maindb', user='maindb', password='maindb', host='localhost', port='15432') as conn:
        for post in posts:
            create_new_post(conn, **{ **asdict(post), 'meta_info': json.dumps(post.meta_info) })

        conn.commit()


def load_posts(sources):
    results = generate_feed(sources)

    print('First result:', results[0])

    print('Length of posts:', len(results))

    save_posts(results)
