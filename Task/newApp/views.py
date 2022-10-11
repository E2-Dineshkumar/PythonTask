from rest_framework import viewsets
from newApp.models import Student
from rest_framework import filters
from newApp.serializers import StudentSerializer
# Create your views here.

class StudentViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[filters.OrderingFilter]
    ordering_fields=['marks']
    # marks=queryset.values_list('marks',flat=True)
    # student_detail=queryset.filter('id',flat=True)
    # print(student_detail)
    # # for  in student_detail:
    # #     print(i)
