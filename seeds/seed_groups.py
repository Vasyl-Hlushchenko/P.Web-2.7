from faker import Faker

from database.db import session
from database.models import Group

NUMBER_GROUPS = 3

fake = Faker("uk_Ua")


def create_groups():
    for i in range(NUMBER_GROUPS):
        group = Group(group_name=f"group- {i+1}")
        session.add(group)
    session.commit()


if __name__ == "__main__":
    create_groups()
