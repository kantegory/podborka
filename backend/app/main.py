from parser.rss import load_posts

habr_all_publications = 'https://habr.com/ru/rss/articles/?fl=ru'
habr_best_publications = 'https://habr.com/ru/rss/articles/top/daily/?fl=ru'

sources = [habr_all_publications, habr_best_publications]

load_posts(sources)
