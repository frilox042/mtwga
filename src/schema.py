import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from models import Flux as FluxModel
from models import FluxGroup as FluxGroupModel
from models import FluxContent as FluxContentModel
from models import FluxLog as FluxLogModel


class FluxGroup(SQLAlchemyObjectType):

    class Meta:
        model = FluxGroupModel
        interfaces = (relay.Node, )


class Flux(SQLAlchemyObjectType):

    class Meta:
        model = FluxModel
        interfaces = (relay.Node, )


class FluxContent(SQLAlchemyObjectType):

    class Meta:
        model = FluxContentModel
        interfaces = (relay.Node, )


class FluxLog(SQLAlchemyObjectType):

    class Meta:
        model = FluxLogModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_groups = SQLAlchemyConnectionField(FluxGroup)
    all_fluxs = SQLAlchemyConnectionField(Flux)
    all_flux_contents = SQLAlchemyConnectionField(FluxContent)
    all_flux_logs = SQLAlchemyConnectionField(FluxLog)


schema = graphene.Schema(query=Query, types=[FluxGroup, Flux,
                                             FluxContent, FluxLog])
