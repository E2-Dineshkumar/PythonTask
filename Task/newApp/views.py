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
    marks=queryset.values_list('marks',flat=True)
    student_detail=queryset.values_list('id',flat=True)
#     category=[]
#     for i in marks:
#         if i>70:
#             excellent=[]
#             sid=student_detail.filter(marks=i)
#             print(excellent.append(sid))
#         elif i<=70 and i>40:
#             good=[]
#             sid=student_detail.filter(marks=i)
#             print(good.append(sid))
#             print('Good')
#         else:
#             sid=student_detail.filter(marks=i)
#             print(good.append(sid))
#             print('Average')

# class StudentCategory(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer