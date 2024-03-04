from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///chinook")

base = declarative_base()

class Artist(base):
    __tablename__="artist"
    artist_id = Column(Integer, primary_key=True)
    name = Column(String)

class Album(base):
    __tablename__ = "album"
    album_id = Column(Integer, primary_key=True)
    title = Column(String)
    artist_id = Column(Integer, ForeignKey("Artist.artist_id"))

class Track(base):
    __tablename__ = "track"
    track_id = Column(Integer, primary_key=True)
    name = Column(String)
    album_id = Column(Integer, ForeignKey("Album.album_id"))
    media_type_id = Column(Integer, primary_key=False)
    genre_id = Column(Integer, primary_key=False)
    composer = Column(String)
    miliseconds = Column(Integer, primary_key=False)
    bytes = Column(Integer, primary_key=False)
    unit_price = Column (Float)


Session = sessionmaker(db)

session = Session()

base.metadata.create_all(db)

# artists = session.query(Artist)
# for artist in artists:
#     print(artist.artist_id, artist.name, sep=" / ")

# artists = session.query(Artist)
# for artist in artists:
#     print( artist.name)

# artist = session.query(Artist).filter_by(name= "Queen").first()
# print(artist.artist_id, artist.name, sep=" / ")

# artist = session.query(Artist).filter_by(artist_id = 51).first()
# print(artist.artist_id, artist.name, sep=" / ")

# albums = session.query(Album).filter_by(artist_id = 51)
# for album in albums:
#     print(album.album_id, album.title, album.artist_id, sep= " / ")

tracks = session.query(Track).filter_by(composer = "Queen")
for track in tracks:
    print(track.track_id, track.name, track.album_id, track.media_type_id, track.genre_id, track.composer, track.miliseconds, track.bytes, track.unit_price)