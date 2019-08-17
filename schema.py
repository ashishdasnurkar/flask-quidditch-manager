from models import Team
from models import Player
from models import Game
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

class PlayerObject(SQLAlchemyObjectType):
    class Meta:
        model = Player
        interfaces = (graphene.relay.Node, )

class TeamObject(SQLAlchemyObjectType):
    class Meta:
        model = Team
        interfaces = (graphene.relay.Node, )

class GameObject(SQLAlchemyObjectType):
    class Meta:
        model = Game
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_players = SQLAlchemyConnectionField(PlayerObject)
    all_teams = SQLAlchemyConnectionField(TeamObject)
    all_games = SQLAlchemyConnectionField(GameObject)

schema = graphene.Schema(query=Query)