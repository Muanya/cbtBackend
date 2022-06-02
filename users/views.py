from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import Students
from users.serializers import StudentRegistrationSerializer, StudentSerializer


class RegistrationView(APIView):
    def post(self, req):
        serializer = StudentRegistrationSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, req):
        students = Students.objects.all()
        res = []
        for student in students:
            res.append(StudentSerializer(student).data)
        return Response(res)


class LoginView(APIView):
    def post(self, req):
        print(req.data)
        if 'reg_no' not in req.data or 'password' not in req.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        reg_no = req.data['reg_no']
        password = req.data['password']
        user = authenticate(req, reg_no=reg_no, password=password)
        if user is not None:
            login(req, user)
            auth_data = get_tokens_for_user(req.user)
            return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, req):
        logout(req)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)


class AuthenticatedView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, req):
        return Response({'data': 'data'})


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
