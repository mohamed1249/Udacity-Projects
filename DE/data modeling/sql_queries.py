# DROP TABLES

songplay_table_drop = "DROP IF EXIST TABLE songplay"
user_table_drop = "DROP IF EXIST TABLE user"
song_table_drop = "DROP IF EXIST TABLE song"
artist_table_drop = "DROP IF EXIST TABLE artist"
time_table_drop = "DROP IF EXIST TABLE time"

# CREATE TABLES

songplay_table_create = (""" CREATE TABLE songplay (songplay_id TEXT, start_time TIME, user_id TEXT, level INT, song_id TEXT, artist_id TEXT, session_id TEXT, location TEXT, user_agent TEXT)
""")

user_table_create = ("""  CREATE TABLE user (user_id TEXT, first_name TEXT, last_name TEXT, gender TEXT, level INT)
""")

song_table_create = (""" CREATE TABLE song (song_id TEXT, title TEXT, artist_id TEXT, year INT, duration decimal)
""")

artist_table_create = (""" CREATE TABLE artist (artist_id TEXT, name TEXT, location TEXT, latitude float8, longitude float8)
""")

time_table_create = (""" CREATE TABLE time (start_time TIME, hour INT, day TEXT, week INT, month TEXT, year INT, weekday TEXT)
""")

# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplay(songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {});
""")

user_table_insert = ("""INSERT INTO user(user_id, first_name, last_name, gender, level)
VALUES ({}, {}, {}, {}, {});
""")

song_table_insert = ("""INSERT INTO song(song_id, title, artist_id, year, duration)
VALUES ({}, {}, {}, {}, {});
""")

artist_table_insert = ("""INSERT INTO artist(artist_id, name, location, latitude, longitude)
VALUES ({}, {}, {}, {}, {});
""")


time_table_insert = ("""INSERT INTO time(start_time, hour, day, week, month, year, weekday)
VALUES ({}, {}, {}, {}, {}, {}, {});
""")

# FIND SONGS

song_select = (""" SELECT {} FROM song;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]