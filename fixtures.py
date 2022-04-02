# module import
import datetime
from models import engine, db_session, Base, Character, Episode,\
    Origin, Location

# create all db's
Base.metadata.create_all(bind=engine)


def test_fixtures():
    """
    This test fixture creates 3 Origin objects, 2 Location objects,
    5 Character Objects and 5 Episode Objects
    """
    # create 3 origin objects
    origin_1 = Origin(
        name='Earth (C-137)',
        type='Planet'
    )
    origin_2 = Origin(
        name='unknown',
        type=None
    )
    origin_3 = Origin(
        name='Earth (Replacement Dimension)',
        type='Planet'
    )

    db_session.add_all([origin_1, origin_2, origin_3])
    db_session.commit()

    # create 3 location objects
    location_1 = Location(
        name='Citadel of Ricks',
        type='Space station'
    )

    location_2 = Location(
        name='Earth (Replacement Dimension)',
        type='Planet'
    )

    db_session.add_all([location_1, location_2])
    db_session.commit()

    # create 5 episode objects
    episode_1 = Episode(
        name='Pilot',
        air_date=datetime.datetime(year=2013, day=2, month=12)
    )

    episode_2 = Episode(
        name='Lawnmover Dog',
        air_date=datetime.datetime(year=2013, day=9, month=12)
    )

    episode_3 = Episode(
        name='Anatomy Park',
        air_date=datetime.datetime(year=2013, day=16, month=12)
    )

    episode_4 = Episode(
        name='M. Night Shaym-Alients!',
        air_date=datetime.datetime(year=2014, day=13, month=1)
    )

    episode_5 = Episode(
        name='Meeseeks and Destroy',
        air_date=datetime.datetime(year=2014, day=20, month=1)
    )


    db_session.add_all([episode_1, episode_2, episode_3, episode_4, episode_5])
    db_session.commit()

    # create 5 character objects
    character_1 = Character(
        name='Rick Sanchez',
        status='Alive',
        species='Human',
        type='',
        gender='Male',
        origin=origin_1.id,
        location=location_1.id,
        image='https://rickandmortyapi.com/api/character/avatar/1.jpeg',
        created=datetime.datetime.now()
    )

    character_2 = Character(
        name='Morty Smith',
        status='Alive',
        species='Human',
        type='',
        gender='Male',
        origin=origin_2.id,
        location=location_1.id,
        image='https://rickandmortyapi.com/api/character/avatar/2.jpeg',
        created=datetime.datetime.now()
    )

    character_3 = Character(
        name='Summer Smith',
        status='Alive',
        species='Human',
        type='',
        gender='Female',
        origin=origin_3.id,
        location=location_2.id,
        image='https://rickandmortyapi.com/api/character/avatar/3.jpeg',
        created=datetime.datetime.now()
    )

    character_4 = Character(
        name='Beth Smith',
        status='Alive',
        species='Human',
        type='',
        gender='Female',
        origin=origin_2.id,
        location=location_2.id,
        image='https://rickandmortyapi.com/api/character/avatar/4.jpeg',
        created=datetime.datetime.now()
    )

    character_5 = Character(
        name='Jerry Smith',
        status='Alive',
        species='Human',
        type='',
        gender='Male',
        origin=origin_2.id,
        location=location_2.id,
        image='https://rickandmortyapi.com/api/character/avatar/5.jpeg',
        created=datetime.datetime.now()
    )

    db_session.add_all([character_1, character_2, character_3, character_4, character_5])
    db_session.commit()

    # add episodes to each character
    character_1.episodes.append(episode_1)
    character_1.episodes.append(episode_2)
    character_1.episodes.append(episode_3)
    character_1.episodes.append(episode_4)
    character_1.episodes.append(episode_5)

    character_2.episodes.append(episode_1)
    character_2.episodes.append(episode_2)
    character_2.episodes.append(episode_3)
    character_2.episodes.append(episode_4)

    character_3.episodes.append(episode_1)
    character_3.episodes.append(episode_2)
    character_3.episodes.append(episode_3)
    character_3.episodes.append(episode_4)
    character_3.episodes.append(episode_5)


    character_4.episodes.append(episode_1)
    character_4.episodes.append(episode_2)
    character_4.episodes.append(episode_3)
    character_4.episodes.append(episode_4)

    character_5.episodes.append(episode_1)
    character_5.episodes.append(episode_2)
    character_5.episodes.append(episode_4)
    character_5.episodes.append(episode_5)

    db_session.commit()