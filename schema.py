# module imports
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import Character as CharacterModel, Location as LocationModel,\
    Origin as OriginModel, Episode as EpisodeModel


class Character(SQLAlchemyObjectType):
    """
    The SQLAlchemyObjectType for the Model Character
    """
    class Meta:
        model = CharacterModel


class Origin(SQLAlchemyObjectType):
    """
    The SQLAlchemyObjectType for the Model Origin
    """
    class Meta:
        model = OriginModel


class Location(SQLAlchemyObjectType):
    """
    The SQLAlchemyObjectType for the Model Location
    """
    class Meta:
        model = LocationModel


class Episode(SQLAlchemyObjectType):
    """
    The SQLAlchemyObjectType for the Model Episode
    """
    class Meta:
        model = EpisodeModel


class Query(graphene.ObjectType):
    """
    The root Query for Graphql
    """
    all_characters = graphene.List(Character)
    all_episodes = graphene.List(Episode)
    get_character_by_name = graphene.Field(Character, name=graphene.String())

    def resolve_get_character_by_name(self, info, name):
        """
        Resolver method for get_character_by_name query
        """
        return CharacterModel.query.filter_by(name=name).first()

    def resolve_all_characters(self, info, **kwargs):
        """
        Resolver method for all_characters query
        """
        return CharacterModel.query.all()

    def resolve_all_episodes(self, info, **kwargs):
        """
        Resolver method for all_episodes query
        """
        return EpisodeModel.query.all()


# create the schema object with the root Query
schema = graphene.Schema(query=Query)