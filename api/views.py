import imp
from re import L
from rest_framework.response import Response
from api.serializers import *
from api.models import *
from rest_framework.views import APIView
from rest_framework import status

class ProfileView(APIView):
    def post(self,request,format=None):
        # format =None means that NO SPECIFIED FORMAT IS REQUIRED, ALL ARE ALLOWED
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Resume Uploaded Sucessfully','status': 'sucess','candidate':serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    def get(self,request,format=None):
        candidates = Profile.objects.all()
        serializer = ProfileSerializer(candidates,many=True)
        return Response({'status':'success','candidates':serializer.data},status=status.HTTP_200_OK)
        