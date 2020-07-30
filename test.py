import graphene
import json


class Query(graphene.ObjectType):
    is_staff = graphene.Boolean(name="is_staff")

    def resolve_is_staff(self, info):
        return True


schema = graphene.Schema(query=Query)

result = schema.execute()

items = dict(result.data.items())
print(json.dumps(items, indent=4))
