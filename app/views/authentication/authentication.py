from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.generics import ListAPIView,RetrieveDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.serializers.authentication.auth_serializer import RegisterSerializer,AllUsersSerializers
from app.utils.utils import get_tokens_for_user,send_messege,verify
from django.contrib.auth import login, logout
import json
from django.db.models import Q

from app.models.usermodel import User


class RegisterView(APIView):
    def post(self,request):
        post_data = request.data
        serializer = RegisterSerializer(data=post_data)
        if serializer.is_valid():
            serializer.create(validated_data=post_data)
            return Response({"msg":"User is created","data":serializer.data,"status":status.HTTP_201_CREATED})
        else:
            return Response({"msg":"Invaild credentials","data":[],"status":status.HTTP_400_BAD_REQUEST})


class SignInView(APIView):
    def post(self,request):
        verified_user = verify(phone_number=request.data["phone"])
        if verified_user!=None:
            login(request,user=verified_user)
            authtoken = get_tokens_for_user(user=verified_user)
            data ={
                "id":verified_user.id,
                "phone":verified_user.phone,
                "firstname":verified_user.first_name,
                "lastname":verified_user.last_name,
            }
            return Response({'msg': 'Login Success',"data":data, **authtoken}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class SendOtpView(APIView):
    def get(self,request):
        phone = self.request.query_params.get("phone")
        phone_number = "{0}{1}".format("+91",phone)
        otp = send_messege(phone_number=phone_number)
        if otp!=None:
            return Response({"msg":"your otp is {0}".format(otp),"data":otp,"status":status.HTTP_200_OK})
        else:
            return Response({"msg":"Your Phone Number is not Valid","data":otp,"status":status.HTTP_404_NOT_FOUND})


class Logout(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        logout(request)
        return Response({"msg":"User is Logged out Now"})

class AllUsers(ListAPIView):
    queryset=User.objects.all()
    serializer_class=AllUsersSerializers
    permission_classes=[IsAdminUser]

class RetriveOrDeleteUser(RetrieveDestroyAPIView):
    permission_classes=[IsAdminUser]
    queryset=User.objects.all()
    serializer_class=AllUsersSerializers
    lookup_field="pk"


            


