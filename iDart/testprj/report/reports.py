
from django.db.models.fields import IntegerField
from dataclasses import dataclass
from report.models import Mark

from decimal import Decimal

from django.db.models import Sum, Count, Avg

from report.models import Student
from report.models import Subject

# def student_mark_details():
#     queryset = Mark.objects.values("student").annotate(
#         score = "score",
#         subject = "subject"
#     )
#     return queryset

@dataclass
class TotalMarks:
    student: Student
    total: int
    totalSubjects: int

def total_marks_per_student():
    data = []
    queryset = Mark.objects.values("student").annotate(
        total=Sum("score"),
        totalSubjects=Count("subject")
    )

    for row in queryset:
        student = Student.objects.get(pk=row["student"])
        total_marks = TotalMarks(student,row["total"],row["totalSubjects"])
        data.append(total_marks)
    return data

@dataclass
class AvgMarks:
    subject:Subject
    avg:Decimal
    count:int


def avg_marks_per_subject():
    data = []
    queryset = Mark.objects.values("subject").annotate(
        avg=Avg("score"),
        count=Count("student")
    )

    for row in queryset:
        subject = Subject.objects.get(pk=row["subject"])
        avg_marks = AvgMarks(subject,row["avg"],row["count"])
        data.append(avg_marks)
    return data