import graphene
from graphene_django import DjangoObjectType
from my_app.models import Restaurant

class RestaurantType(DjangoObjectType):
  class Meta:
    model = Restaurant
    fields = ("id", "name", "address")

class Query(graphene.ObjectType):
  """
  Queries for the Restaurant model
  """
  restaurants = graphene.List(RestaurantType)

  def resolve_restaurants(self, info, **kwargs):
    return Restaurant.objects.all()