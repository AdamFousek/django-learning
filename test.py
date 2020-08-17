"""
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
"""
NOT_STARTED = 'not-started'
IN_PROGRESS = 'in-progress'
STUCK = 'stuck'
DONE = 'done'
STATUS_CHOICES = [
    (NOT_STARTED, 'Not started'),
    (IN_PROGRESS, 'In progress'),
    (STUCK, 'Stuck'),
    (DONE, 'Done'),
]

list_of_tuples = [(1, 2), (3, 4)]
for (x, y) in STATUS_CHOICES:
    print(x, y)
