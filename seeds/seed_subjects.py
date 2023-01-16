from faker import Faker
from random import randint

from database.db import session
from database.models import Subject

NUMBER_SUBJECTS = 6
NUMBER_TEACHERS = 4

fake = Faker("uk_Ua")


def create_subjects():
    for i in range(NUMBER_SUBJECTS):
        subject = Subject(
            subject_name=fake.job(), teacher_id=randint(1, NUMBER_TEACHERS)
        )
        session.add(subject)
    session.commit()


if __name__ == "__main__":
    create_subjects()
