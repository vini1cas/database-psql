from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# connect to the chinook database (db)

db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable for "artist" table

artist_table = Table(
    "artist", meta,
    Column("artist_id", Integer, primary_key=True),
    Column("name", String)
)

# create variable for "album" table

album_table = Table(
    "album", meta,
    Column("album_id", Integer, primary_key=True),
    Column("title", String),
    Column("artist_id", Integer, ForeignKey("artist_table.artist_id"))
)

# create variable for "track" table

track_table = Table(
    Column("track_id", Integer, primary_key=True),
    Column("name", String),
    Column("album_id", String, ForeignKey("album_table.album_id")),
    Column("media_type_id", Integer, primary_key=False),
    Column("genre_id", Integer, primary_key=False),
    Column("composer", String),
    Column("milisecons", Integer),
    Column("bytes", Integer),
    Column("unit_price", Float),
)

# making connection

with db.connect() as connection:
    # Query 1 Select all all records form the "artist" table

    # select_query = artist_table.select()

    # select_query = artist_table.select().with_only_columns([artist_table.c.name])

    # select_query = artist_table.select().where([artist_table.c.name == "Queen"])

    # select_query = artist_table.select().where([artist_table.c.artist_id == 51])

    # select_query = album_table.select().where([album_table.c.artist_id == 51])

    select_query = track_table.select().where([track_table.c.composer == "Queen"])

    results = connection.execute(select_query)
    for result in results:
        print(result)
