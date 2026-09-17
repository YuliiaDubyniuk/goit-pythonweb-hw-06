from sqlalchemy import select, func, desc
from src.database import SessionLocal
from src.models import Student, Group, Teacher, Subject, Grade


def select_1():
    with SessionLocal() as session:
        stmt = (
            select(
                Student.full_name, func.round(func.avg(Grade.grade), 2)
                .label("average_grade"),
            )
            .join(Grade, Grade.student_id == Student.id)
            .group_by(Student.id)
            .order_by(desc("average_grade"))
            .limit(5)
        )

        result = session.execute(stmt)
        return result.all()


def select_2(subject_name):
    with SessionLocal() as session:
        stmt = (
            select(
                Student.full_name,
                func.round(func.avg(Grade.grade), 2).label("average_subject_grade"),
            )
            .join(Grade, Grade.student_id == Student.id)
            .join(Subject, Subject.id == Grade.subject_id)
            .where(Subject.name == subject_name)
            .group_by(Student.id)
            .order_by(desc("average_subject_grade"))
            .limit(1)
        )

        result = session.execute(stmt)

        return result.first()


def select_3(subject_name):
    with SessionLocal() as session:
        stmt = (
            select(
                Group.name, func.round(func.avg(Grade.grade), 2)
                .label("average_grade"),
            )
            .join(Student, Student.group_id == Group.id)
            .join(Grade, Grade.student_id == Student.id)
            .join(Subject, Subject.id == Grade.subject_id)
            .where(Subject.name == subject_name)
            .group_by(Group.id)
        )

        result = session.execute(stmt)
        return result.all()


def select_4():
    with SessionLocal() as session:
        stmt = select(
            func.round(func.avg(Grade.grade), 2).label("average_grade")
        )

        result = session.execute(stmt)
        return result.scalar()


def select_5(teacher_name):
    with SessionLocal() as session:
        stmt = (
            select(Subject.name)
            .join(Teacher, Teacher.id == Subject.teacher_id)
            .where(Teacher.full_name == teacher_name)
        )

        result = session.execute(stmt)
        return result.scalars().all()


def select_6(group_name):
    with SessionLocal() as session:
        stmt = (
            select(Student.full_name)
            .join(Group, Group.id == Student.group_id)
            .where(Group.name == group_name)
        )

        result = session.execute(stmt)
        return result.scalars().all()


def select_7(group_name, subject_name):
    with SessionLocal() as session:
        stmt = (
            select(
                Student.full_name,
                Grade.grade,
            )
            .join(Group, Group.id == Student.group_id)
            .join(Grade, Grade.student_id == Student.id)
            .join(Subject, Subject.id == Grade.subject_id)
            .where(
                Group.name == group_name,
                Subject.name == subject_name,
            )
            .order_by(Student.full_name)
        )

        result = session.execute(stmt)

        return result.all()


def select_8(teacher_name):
    with SessionLocal() as session:
        stmt = (
            select(
                Teacher.full_name, func.round(func.avg(Grade.grade), 2)
                .label("average_grade"),
            )
            .join(Subject, Subject.teacher_id == Teacher.id)
            .join(Grade, Grade.subject_id == Subject.id)
            .where(Teacher.full_name == teacher_name)
            .group_by(Teacher.id)
        )

        result = session.execute(stmt)
        return result.first()


def select_9(student_name):
    with SessionLocal() as session:
        stmt = (
            select(Subject.name)
            .join(Grade, Grade.subject_id == Subject.id)
            .join(Student, Student.id == Grade.student_id)
            .where(Student.full_name == student_name)
            .distinct()
        )

        result = session.execute(stmt)
        return result.scalars().all()


def select_10(student_name, teacher_name):
    with SessionLocal() as session:
        stmt = (
            select(Subject.name)
            .join(Grade, Grade.subject_id == Subject.id)
            .join(Student, Student.id == Grade.student_id)
            .join(Teacher, Teacher.id == Subject.teacher_id)
            .where(
                Student.full_name == student_name,
                Teacher.full_name == teacher_name,
            )
            .distinct()
        )

        result = session.execute(stmt)

        return result.scalars().all()



if __name__ == "__main__":
    print(select_1())
    print(select_2("Physics"))
    print(select_3("History"))
    print(select_4())
    print(select_5("David White"))
    print(select_6("Group 2"))
    print(select_7("Group 1", "English"))
    print(select_8("Samuel Cohen"))
    print(select_9("Joseph Rogers"))
    print(select_10("Zoe Williams", "Caroline Jones"))