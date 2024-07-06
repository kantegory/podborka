CREATE TABLE IF NOT EXISTS dt_user (
    id SERIAL PRIMARY KEY,
    login VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS dt_feed (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER REFERENCES dt_user(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS dt_source (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    link VARCHAR(255) NOT NULL,
    type VARCHAR(10) NOT NULL CHECK (type = 'RSS' OR type = 'ATOM')
);

CREATE TABLE IF NOT EXISTS dt_post (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    meta_info JSONB, -- JSONB поддерживает индексацию и поиск
    raw_content TEXT,
    mark BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    feed_id INTEGER REFERENCES dt_feed(id) ON DELETE CASCADE,
    source_id INTEGER REFERENCES dt_source(id) ON DELETE RESTRICT
);
