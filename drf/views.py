from django.shortcuts import render,HttpResponse

from drf.models import Student
from drf.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


# Create your views here.
def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    serialized=StudentSerializer(stu)
    print(serialized)
    json_data=JSONRenderer().render(serialized.data)
    return HttpResponse(json_data)

def all_student(request):
    stu=Student.objects.all()
    serialized=StudentSerializer(stu,many=True)
    print(serialized)
    json_data=JSONRenderer().render(serialized.data)
    return HttpResponse(json_data)
@csrf_exempt
def student_create(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        print(f"This is Stream ===== {stream}")
        pythondata=JSONParser().parse(stream)
        print(f"This is python data===== {pythondata}")

        serializer=StudentSerializer(data=pythondata)
        print(f"This is Serialized data===== {serializer}")

        if serializer.is_valid():
            serializer.save()
            msg="Student created successfully"
            res={"msg":msg}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type="application/json")

        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/json")


def student_api(request):
    if request.method=='GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get("id",None)

        if id is not None:
            student=Student.objects.get(id=id)
            serializer=StudentSerializer(student)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type="application/json")

        student=Student.objects.all()
        serializer=StudentSerializer(student,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type="application/json")







