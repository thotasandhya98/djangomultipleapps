from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import UserDetails
from .serializers import UserDetailsSerializers


class UserDetailsRcu(APIView):
    permission_classes = [permissions.IsAuthenticated]
    # serializers_class= UserDetailsSerializers
    # queryset=UserDetails.objects.all()

    def get(self, request, pk=None, format=None):
        if pk:
            user_details = get_object_or_404(UserDetails, id=pk)
            user_details_serializers = UserDetailsSerializers(user_details)
            return Response(user_details_serializers.data, status=status.HTTP_200_OK)
        else:
            user_details_qs = UserDetails.objects.all()
            user_details_serializers = UserDetailsSerializers(user_details_qs, many=True)
            return Response(user_details_serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        user_details_serializers = UserDetailsSerializers(data=request.data)
        user_details_serializers.is_valid(raise_exception=True)
        user_details_serializers.save()
        return Response(user_details_serializers.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None, format=None):
        user_details = get_object_or_404(UserDetails, id=pk)
        user_details_serializers = UserDetailsSerializers(instance=user_details, data=request.data)
        user_details_serializers.is_valid(raise_exception=True)
        user_details_serializers.save()
        return Response(user_details_serializers.data, status=status.HTTP_200_OK)

class AuthenticatedView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        msg = {'message': f'Hi {request.user.username}! Congo on being authenticated!'}
        return Response(msg, status=status.HTTP_200_OK)
