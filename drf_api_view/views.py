from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
# from .throttless import JackThrottle

from blog import serializers
from drf.models import Student
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status

# @api_view(['GET','POST','PUT','DELETE','PATCH'])
# def employee_view(request,pk=None):
#     if request.method == 'GET':
#         id=pk
#         if id is not None:
#             employee=Employee.objects.get(id=id)
#             serializer=EmployeeSerializer(employee)
#             return Response(serializer.data)
#         else:
#             employees=Employee.objects.all()
#             serializer=EmployeeSerializer(employees,many=True)
#             return Response(serializer.data)
#     if request.method == 'POST':
#         data=request.data
#         serializer=EmployeeSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message":"Employee saved successfully"},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)
#
#     if request.method == 'PUT':
#         id=pk
#
#         employee=Employee.objects.get(id=id)
#         serializer=EmployeeSerializer(employee,data=request.data,partial=True)  #IF partial = True is given. It can work as patch also (for partial editing data ).
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message":"Edited successfully"})
#         return Response(serializer.errors)
#


# We can also use the generic API views as below.
from rest_framework.generics import ListAPIView,GenericAPIView
from rest_framework.mixins import RetrieveModelMixin,UpdateModelMixin,ListModelMixin,DestroyModelMixin,CreateModelMixin

# class List_create(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset = Employee.objects.all()
#     serializer_class =EmployeeSerializer
#     def get(self,request,format=None):
#         return self.list(request,format)
#
#     def post(self,request,format=None):
#         return self.create(request,format)
#
#
# class retrieve_update_delete(GenericAPIView,RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin):
#     queryset = Employee.objects.all()
#     serializer_class =EmployeeSerializer
#     def get(self,request,pk,format=None):
#         return self.retrieve(request,pk)
#
#     def put(self, request, pk, format=None):
#         return self.update(request, pk)
#
#     def delete(self, request, pk, format=None):
#         return self.destroy(request,pk)






# Another easy way to to is using VIEWSET.IN this method we don't have to define the url for each and every action . We just use the router method.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, BaseAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.throttling import AnonRateThrottle,ScopedRateThrottle

class EmployeeViewSet(viewsets.ViewSet):



    # authentication_classes = [BasicAuthentication]  #this is autentication code.
    # permission_classes=[IsAdminUser]  # The Is_adminUser authentication allow only the users with is_staff status=True .  The Is_authenticated will allow any type of user.

    # Session authentication
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]

    # # Tokenauthentication
    # authentication_classes = [TokenAuthentication]
    # # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]

    #JWT authentication
    # authentication_classes = [JWTAuthentication]
    #
    # permission_classes = [IsAuthenticated]

    # NOW THE CONCEPT OF THROTTLING
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    from .throttless import JackThrottle
    throttle_classes = [JackThrottle]
    # or
    # throttle_classes=[ScopedRateThrottle]
    # throttle_scope = 'jack'





    def list(self,request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset,many=True)
        return Response(serializer.data)
    def post(self,request):
        data=request.data
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Employee added successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(queryset,partial=True)
        return Response(serializer.data)

    def update(self,request,pk=None):
        queryset = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(queryset, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Employee updated successfully"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        data=Employee.objects.get(id=pk)
        if data is not None:
            data.delete()
            return Response({"message":"Employee deleted successfully"},status=status.HTTP_200_OK)
        return Response({"message":"Data deleted successfully"},status=status.HTTP_400_BAD_REQUEST)



# We can also use VIEWSET.MODELVIEWSET to create complete CRUD ONLY ON 3 lines

# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class =EmployeeSerializer(queryset,many=True)


# Read only model viewset can only list and retrieve.
# class StudentViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class =EmployeeSerializer(queryset,many=True)


