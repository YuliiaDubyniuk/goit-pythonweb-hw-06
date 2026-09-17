import random
from faker import Faker
from src.database import SessionLocal
from src.models import Group, Student, Teacher, Subject, Grade


fake = Faker()


def seed_database():
    with SessionLocal() as session:
        groups = []
        for i in range(3):
            group = Group(
                name=f"Group {i + 1}"
            )
            groups.append(group)

        session.add_all(groups)
        session.flush()

        teachers = []
        for _ in range(5):
            teacher = Teacher(
                full_name=fake.name()
            )
            teachers.append(teacher)

        session.add_all(teachers)
        session.flush()

        subject_names = [
            "Mathematics",
            "Physics",
            "Chemistry",
            "Biology",
            "History",
            "English",
            "Computer Science",
            "Geography",
        ]

        subjects = []
        for name in subject_names:
            subject = Subject(
                name=name,
                teacher=random.choice(teachers),
            )
            subjects.append(subject)

        session.add_all(subjects)
        session.flush()

        
        students = []
        for _ in range(30):
            student = Student(
                full_name=fake.name(),
                group=random.choice(groups),
            )
            students.append(student)

        session.add_all(students)
        session.flush()

        grades = []
        for student in students:
            for subject in random.sample(subjects, k=random.randint(3, 6)):
                grade = Grade(
                    grade=random.randint(1, 12),
                    student=student,
                    subject=subject,
                )
                grades.append(grade)

        session.add_all(grades)

        session.commit()

        print("Database seeded successfully!")
        print(f"Groups: {len(groups)}")
        print(f"Teachers: {len(teachers)}")
        print(f"Subjects: {len(subjects)}")
        print(f"Students: {len(students)}")
        print(f"Grades: {len(grades)}")


if __name__ == "__main__":
    seed_database()