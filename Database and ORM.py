import sqlalchemy as sq
from sqlalchemy import desc, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.testing import in_

Base = declarative_base()

engine = sq.create_engine('postgresql+psycopg2://netology:netology@localhost:5432/music')
Session = sessionmaker(bind=engine)


class Artist(Base):
    __tablename__ = 'artist'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)
    albums = relationship('Album', back_populates='artist')


class Album(Base):
    __tablename__ = 'album'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    tracks = relationship('Track', backref='album',  cascade="all,delete")
    published = sq.Column(sq.Date)
    id_artist = sq.Column(sq.Integer, sq.ForeignKey('artist.id'))
    artist = relationship(Artist)

    def __str__(self):
        return self.title


class Genre(Base):
    __tablename__ = 'genre'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    tracks = relationship('Track', secondary='track_to_genre', back_populates='genres', cascade="all,delete", cascade_backrefs=True)

    def __repr__(self):
        return self.title

class Track(Base):
    __tablename__ = 'track'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    duration = sq.Column(sq.Integer, nullable=False)
    genres = relationship(Genre, secondary='track_to_genre', back_populates='tracks', cascade="all,delete")
    id_album = sq.Column(sq.Integer, sq.ForeignKey('album.id', ondelete="CASCADE"))

    @classmethod
    def list(cls):
        return Session().query(cls).all()

    def __repr__(self):
        return self.title


track_to_genre = sq.Table(
    'track_to_genre', Base.metadata,
    sq.Column('genre_id', sq.Integer, sq.ForeignKey('genre.id')),
    sq.Column('track_id', sq.Integer, sq.ForeignKey('track.id')),
)


if __name__ == '__main__':
    session = Session()
    # Init scheme
    # Base.metadata.create_all(engine)

    # Example data
    date_ar1 = {
        'Album 1': [
            {'name': 'Track 1_1', 'dur': 60},
            {'name': 'Track 1_2', 'dur': 30},
            {'name': 'Track 1_3', 'dur': 45}
        ],
        'Album 2': [
            {'name': 'Track 2_1', 'dur': 60},
            {'name': 'Track 2_2', 'dur': 30},
            {'name': 'Track 2_3', 'dur': 45}
        ]
    }

    ## Example add dates
    # artist_1 = session.query(Artist).filter_by(name="Artist 1").one()
    # for album_name, raw_tracks in date_ar1.items():
    #     item_album = Album(title=album_name, artist=artist_1)
    #     for item_track in raw_tracks:
    #         _track = Track(title=item_track['name'], duration=item_track['dur'])
    #         item_album.tracks.append(_track)
    #
    #     session.add(item_album)
    # session.commit()

    # session.query(Artist).filter_by(Artist.name="asd")

    # artist = Artist(name='Artist 2')
    # session.add(artist)
    # ...
    # session.commit()


    ## Example 1
    # artist_list = ["Artist 1", "Artist 2"]
    # q1 = session.query(Artist).filter_by(name="Artist 2").filter_by(name="Artist 1")
    # q2 = session.query(Artist).filter(Artist.name.in_(artist_list))

    # Example 2
    query_tracks = session.query(Track).filter(Track.duration > 40)
    query_tracks2 = session.query(Track).filter(Track.duration <= 40)
    blues = Genre(title="Blues")
    folk = Genre(title="Folk")

    # Update 1
    for t in query_tracks.all():
        t.genres.append(blues)
        t.genres.append(folk)

    # Update 2
    query_tracks2.update({"duration": 41})

    session.commit()
    print([t.genres for t in query_tracks.all()])



    print('Finish')