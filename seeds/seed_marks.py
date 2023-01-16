from faker import Faker
from random import randint

from database.db import session
from database.models import Mark

NUMBER_STUDENTS = 39
NUMBER_SUBJECTS = 6
NUMBER_MARKS = 16
MAX_MARK = 12

fake = Faker("uk_Ua")


def create_marks():
    for _ in range(NUMBER_STUDENTS * NUMBER_MARKS):
        mark = Mark(
            student_id=randint(1, NUMBER_STUDENTS - 1),
            subject_id=randint(1, NUMBER_SUBJECTS),
            mark=randint(1, MAX_MARK),
            date=fake.date_between(start_date="-1y"),
        )
        session.add(mark)
    session.commit()


if __name__ == "__main__":
    create_marks()
