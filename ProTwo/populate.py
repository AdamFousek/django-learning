from faker import Faker
import random
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')
django.setup()
from AppTwo.models import User
fakegen = Faker()


def populate(N=5):

    for i in range(N):
        u = User()
        u.first_name = fakegen.name()
        u.last_name = fakegen.name()
        u.email = fakegen.email()
        u.save()


if __name__ == "__main__":
    populate()
