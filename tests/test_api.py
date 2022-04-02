# module imports
import pytest
import json
import os

from app import create_app
from models import Base, engine
import fixtures


@pytest.fixture()
def app():
    """
    This fixture generates the app object from the
    factory. We can update the config as per the test
    requirements.
    """
    app = create_app('config.py')
    app.config.update(
        {
            'TESTING': True,
            'DEBUG': True,
            'FLASK_ENV': "development"
        }
    )
    yield app


@pytest.fixture()
def db_conn():
    """
    This fixture first removes the existing test db under tests folder,
    and the creates a new one.
    """
    # remove the already existing test db under tests folder
    os.remove("db.sqlite3")
    Base.metadata.create_all(bind=engine)
    fixtures.test_fixtures()


@pytest.fixture()
def client(app):
    """
    This fixture returns the test client
    """
    return app.test_client()


def test_get_all_characters(client, db_conn):
    """
    This test runs a GraphQl query to get all characters
    """
    query_get_all_characters = """
                              {
                            allCharacters {
                              name
                              status
                              species
                              type
                              episodes {
                                name
                                airDate
                              }
                            }
                          }
    """
    response_all_characters = {
        "data": {
            "allCharacters": [
                {
                    "name": "Rick Sanchez",
                    "status": "ALIVE",
                    "species": "Human",
                    "type": "",
                    "episodes": [
                        {
                            "name": "Pilot",
                            "airDate": "2013-12-02T00:00:00"
                        },
                        {
                            "name": "Lawnmover Dog",
                            "airDate": "2013-12-09T00:00:00"
                        },
                        {
                            "name": "Anatomy Park",
                            "airDate": "2013-12-16T00:00:00"
                        },
                        {
                            "name": "M. Night Shaym-Alients!",
                            "airDate": "2014-01-13T00:00:00"
                        },
                        {
                            "name": "Meeseeks and Destroy",
                            "airDate": "2014-01-20T00:00:00"
                        }
                    ]
                },
                {
                    "name": "Morty Smith",
                    "status": "ALIVE",
                    "species": "Human",
                    "type": "",
                    "episodes": [
                        {
                            "name": "Pilot",
                            "airDate": "2013-12-02T00:00:00"
                        },
                        {
                            "name": "Lawnmover Dog",
                            "airDate": "2013-12-09T00:00:00"
                        },
                        {
                            "name": "Anatomy Park",
                            "airDate": "2013-12-16T00:00:00"
                        },
                        {
                            "name": "M. Night Shaym-Alients!",
                            "airDate": "2014-01-13T00:00:00"
                        }
                    ]
                },
                {
                    "name": "Summer Smith",
                    "status": "ALIVE",
                    "species": "Human",
                    "type": "",
                    "episodes": [
                        {
                            "name": "Pilot",
                            "airDate": "2013-12-02T00:00:00"
                        },
                        {
                            "name": "Lawnmover Dog",
                            "airDate": "2013-12-09T00:00:00"
                        },
                        {
                            "name": "Anatomy Park",
                            "airDate": "2013-12-16T00:00:00"
                        },
                        {
                            "name": "M. Night Shaym-Alients!",
                            "airDate": "2014-01-13T00:00:00"
                        },
                        {
                            "name": "Meeseeks and Destroy",
                            "airDate": "2014-01-20T00:00:00"
                        }
                    ]
                },
                {
                    "name": "Beth Smith",
                    "status": "ALIVE",
                    "species": "Human",
                    "type": "",
                    "episodes": [
                        {
                            "name": "Pilot",
                            "airDate": "2013-12-02T00:00:00"
                        },
                        {
                            "name": "Lawnmover Dog",
                            "airDate": "2013-12-09T00:00:00"
                        },
                        {
                            "name": "Anatomy Park",
                            "airDate": "2013-12-16T00:00:00"
                        },
                        {
                            "name": "M. Night Shaym-Alients!",
                            "airDate": "2014-01-13T00:00:00"
                        }
                    ]
                },
                {
                    "name": "Jerry Smith",
                    "status": "ALIVE",
                    "species": "Human",
                    "type": "",
                    "episodes": [
                        {
                            "name": "Pilot",
                            "airDate": "2013-12-02T00:00:00"
                        },
                        {
                            "name": "Lawnmover Dog",
                            "airDate": "2013-12-09T00:00:00"
                        },
                        {
                            "name": "M. Night Shaym-Alients!",
                            "airDate": "2014-01-13T00:00:00"
                        },
                        {
                            "name": "Meeseeks and Destroy",
                            "airDate": "2014-01-20T00:00:00"
                        }
                    ]
                }
            ]
        }
    }
    response = client.post('/graphql', json={'query': query_get_all_characters})
    data = json.loads(response.get_data())
    assert response.status_code == 200
    assert data == response_all_characters


def test_get_all_characters_name(client, db_conn):
    """
    This test runs a Graphql query to get all the characters with only
    name as the field
    """
    query_get_all_characters_name = """
                                        {
                                      allCharacters {
                                        name
                                      }
                                    }
                                    """
    response_all_characters_name = {
        "data": {
            "allCharacters": [
                {
                    "name": "Rick Sanchez"
                },
                {
                    "name": "Morty Smith"
                },
                {
                    "name": "Summer Smith"
                },
                {
                    "name": "Beth Smith"
                },
                {
                    "name": "Jerry Smith"
                }
            ]
        }
    }

    response = client.post('/graphql', json={'query': query_get_all_characters_name})
    data = json.loads(response.get_data())
    assert response.status_code == 200
    assert data == response_all_characters_name


def test_get_character_by_name(client, db_conn):
    """
    This test runs a Graphql query to get a character by name
    """
    query_get_character_by_name = """
                                  {
                                    getCharacterByName(name: "Beth Smith") {
                                      name
                                    }
                                  }
                                  """
    response_get_character_by_name = {
                                          "data": {
                                            "getCharacterByName": {
                                              "name": "Beth Smith"
                                            }
                                          }
                                     }
    response = client.post('/graphql', json={'query': query_get_character_by_name})
    data = json.loads(response.get_data())
    assert response.status_code == 200
    assert data == response_get_character_by_name