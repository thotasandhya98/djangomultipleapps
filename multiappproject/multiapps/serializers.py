from rest_framework import serializers

from .models import UserDetails


class UserDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['username','email','display_name']
