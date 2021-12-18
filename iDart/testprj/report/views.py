from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from report.models import Student, Subject, Mark
from report.serializers import StudentSerializer, SubjectSerializer, MarkSerializer, TotalMarksSerializer
from report.reports import TotalMarks

from report.reports import total_marks_per_student, avg_marks_per_subject
from report.serializers import AverageMarksSerializer

# Create your views here.

# API to just view the students
class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SubjectModelViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class MarkModelViewSet(ModelViewSet):
    queryset = Mark.objects.all()
    filter_backends = [OrderingFilter,DjangoFilterBackend]
    ordering_fields = ['student','score']
    filterset_fields = ['student__firstname']
    serializer_class = MarkSerializer

    # def get_serializer_class(self):
    #     if self.action in ("list","retrieve"):
    #         return ReadMarkSerializer
    #     return WriteMarkSerializer

class TotalMarksAPIView(APIView):
    def get(self,request):
        data = total_marks_per_student()
        serializer = TotalMarksSerializer(instance=data,many=True)
        return Response(data=serializer.data)

class AverageMarksAPIView(APIView):
    def get(self,request):
        data = avg_marks_per_subject()
        serializer = AverageMarksSerializer(instance=data,many=True)
        return Response(data=serializer.data)

