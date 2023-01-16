from sqlalchemy import func, desc

from database.db import session
from database.models import Mark, Student, Subject, Teacher, Group


def get_query_1():
    result = (
        session.query(
            Student.full_name, func.round(func.avg(Mark.mark), 2).label("avg")
        )
        .select_from(Mark)
        .join(Student)
        .group_by(Student.id)
        .order_by(desc("avg"))
        .limit(5)
        .all()
    )

    for res in result:
        print(f"{res[0]}: {res[1]}")


def get_query_2():
    subject_id = int(input("Enter subject_id: "))
    result = (
        session.query(
            Student.full_name,
            func.round(func.avg(Mark.mark), 2).label("avg"),
            Subject.subject_name,
        )
        .select_from(Mark)
        .join(Student)
        .join(Subject)
        .filter(Subject.id == subject_id)
        .group_by(Subject.id, Student.id)
        .order_by(desc("avg"))
        .first()
    )

    result_list = []
    for res in result:
        result_list.append(str(res))
    print(f"{result_list[0]}, {result_list[1]}, {result_list[2]}")


def get_query_3():
    subject_id = int(input("Enter subject_id: "))
    group_id = int(input("Enter group_id: "))
    result = (
        session.query(
            Subject.subject_name,
            Group.group_name,
            func.round(func.avg(Mark.mark), 2).label("avg"),
        )
        .select_from(Mark)
        .join(Student)
        .join(Group)
        .join(Subject)
        .filter(Subject.id == subject_id, Group.id == group_id)
        .group_by(Group.id, Subject.id)
        .order_by(desc("avg"))
        .first()
    )

    for res in result:
        print(res)


def get_query_4():
    result = session.query(func.round(func.avg(Mark.mark), 2)).select_from(Mark).one()

    print(result)


def get_query_5():
    teacher_id = int(input("Enter teacher_id: "))
    result = (
        session.query(Teacher.full_name, Subject.subject_name)
        .select_from(Subject)
        .join(Teacher)
        .filter(Teacher.id == teacher_id)
        .all()
    )

    result_list = []
    for res in result:
        result_list.append(res[1])

    print(f"{res[0]}: {result_list}")


def get_query_6():
    group_id = int(input("Enter group_id: "))
    result = (
        session.query(Student.full_name)
        .select_from(Student)
        .join(Group)
        .filter(Group.id == group_id)
        .all()
    )

    print(result)


def get_query_7():
    group_id = int(input("Enter group_id: "))
    subject_id = int(input("Enter subject_id: "))
    result = (
        session.query(Mark.mark)
        .select_from(Mark)
        .join(Subject)
        .join(Student)
        .join(Group)
        .filter(Group.id == group_id, Subject.id == subject_id)
        .all()
    )

    print(result)


def get_query_8():
    teacher_id = int(input("Enter teacher_id: "))
    result = (
        session.query(func.round(func.avg(Mark.mark), 2))
        .select_from(Mark)
        .join(Subject)
        .join(Teacher)
        .group_by(Teacher.id)
        .filter(Subject.teacher_id == teacher_id)
        .all()
    )

    print(result)


def get_query_9():
    student_id = int(input("Enter student_id: "))
    result = (
        session.query(Subject.subject_name)
        .select_from(Student)
        .join(Mark)
        .join(Subject)
        .group_by(Subject.subject_name)
        .filter(Student.id == student_id)
        .all()
    )

    print(result)


def get_query_10():
    student_id = int(input("Enter student_id: "))
    teacher_id = int(input("Enter teacher_id: "))
    result = (
        session.query(Subject.subject_name)
        .select_from(Student)
        .join(Mark)
        .join(Subject)
        .join(Teacher)
        .group_by(Subject.subject_name)
        .filter(Student.id == student_id, Teacher.id == teacher_id)
        .all()
    )

    print(result)


if __name__ == "__main__":
    # get_query_1()
    # get_query_2()
    # get_query_3()
    # get_query_4()
    # get_query_5()
    # get_query_6()
    # get_query_7()
    # get_query_8()
    # get_query_9()
    get_query_10()
