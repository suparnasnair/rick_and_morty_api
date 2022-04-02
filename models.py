# module imports
import enum
from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker,
                            relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

# create the db engine
engine = create_engine('sqlite:///db.sqlite3')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class Status(enum.Enum):
    """
    This enum represents the Status field of a Rick&Morty Character
    """
    Unknown = 0
    Alive = 1
    Dead = 2


class Gender(enum.Enum):
    """
    This enum represents the Gender field of a Rick&Morty Character
    """
    Unknown = 0
    Female = 1
    Male = 2
    Genderless = 3


class Origin(Base):
    """
    This is the Model for Origin object, one of the fields of Rick&Morty Character.
    """
    __tablename__ = 'origin'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)


class Location(Base):
    """
    This is the Model for Location object, one of the fields of Rick&Morty Character.
    """
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)


# following is a many to many association between Episode and Character Tables
episode_char_link = Table(
    'episode_char_link',
    Base.metadata,
    Column('character_id', Integer(), ForeignKey('character.id')),
    Column('episode_id', Integer(), ForeignKey('episode.id'))
)


class Episode(Base):
    """
    This is the Model for Episode object, one of the fields of Rick&Morty Character.
    """
    __tablename__ = 'episode'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    air_date = Column(DateTime)


class Character(Base):
    """
    This is the Model for a Rick&Morty Character.
    """
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(Enum(Status))
    species = Column(String)
    type = Column(String)
    gender = Column(Enum(Gender))
    origin = Column(ForeignKey('origin.id'))
    location = Column(ForeignKey('location.id'))
    image = Column(String)
    created = Column(DateTime)
    episodes = relationship(
        'Episode', secondary=episode_char_link,
        backref='characters'
    )

