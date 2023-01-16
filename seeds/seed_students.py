from faker import Faker
from random import randint

from database.db import session
from database.models import Student

NUMBER_STUDENTS = 39
NUMBER_GROUPS = 3

fake = Faker("uk_Ua")


def create_students():
    for _ in range(1, NUMBER_STUDENTS):
        student = Student(full_name=fake.name(), group_id=randint(1, NUMBER_GROUPS))
        session.add(student)
    session.commit()


if __name__ == "__main__":
    create_students()
