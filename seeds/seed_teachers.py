from faker import Faker

from database.db import session
from database.models import Teacher

NUMBER_TEACHERS = 4

fake = Faker("uk_Ua")


def create_teachers():
    for _ in range(NUMBER_TEACHERS):
        teacher = Teacher(full_name=fake.name())
        session.add(teacher)
    session.commit()


if __name__ == "__main__":
    create_teachers()
