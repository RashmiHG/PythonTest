from django.db.models.aggregates import Count
from django.db.models.fields import IntegerField, SlugField
from django.db.models.lookups import In
from rest_framework import serializers
from report.models import Student, Subject, Mark



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','firstname','lastname']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id','code','name']


class MarkSerializer(serializers.ModelSerializer):

    subject = serializers.SlugRelatedField(slug_field="code",queryset=Subject.objects.all())
    student = serializers.SlugRelatedField(slug_field="firstname",queryset=Student.objects.all())

    class Meta:
        model = Mark
        fields = ['id','score','subject','student']



class TotalMarksSerializer(serializers.Serializer):
    student = StudentSerializer()
    total = serializers.IntegerField()
    totalSubjects = serializers.IntegerField()

class AverageMarksSerializer(serializers.Serializer):
    subject = SubjectSerializer()
    avg = serializers.DecimalField(max_digits=15,decimal_places=2)
    count = serializers.IntegerField()


# class ReadMarkSerializer(serializers.ModelSerializer):

#     subject = SubjectSerializer()

#     class Meta:
#         model = Mark
#         fields = ['id','score','subject','student']
    
    
