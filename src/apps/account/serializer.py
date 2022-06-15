from dataclasses import fields
from rest_framework import serializers
from account.models import User
from fcm_django.models import FCMDevice
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username","password","id",)

    def create(self,validated_data):
        
        u,c = User.objects.update_or_create(
            username=validated_data["username"],        
        )
        print(c)
        if c:
            u.set_password(validated_data["password"])
            u.save()
        return u


class FcmDeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = FCMDevice
        fields = ("registration_id","name","device_id","type","user",)

    def create(cls,validated_data):
        a,c = FCMDevice.objects.update_or_create(
            user=validated_data["user"],
            defaults={
                "registration_id":validated_data["registration_id"],
                "device_id": validated_data["device_id"],
                "type": validated_data["type"],
                "name": validated_data["name"]
            }
        )
        return a    

class RestAuthSerializer(serializers.ModelSerializer):

    key = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("username","key",)
        read_only_fields = ("username",)

    def get_key(self,obj):
        return obj.token.key        



class NewRegisterSerializer(serializers.ModelSerializer):
    #username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username","password","id",)

    def create(self,validated_data):
        
        u = User.objects.create(
            username=validated_data["username"],        
        )
        
        if u:
            u.set_password(validated_data["password"])
            u.save()
        return u   

class NewRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ("username","password","id",)

    def create(self,validated_data):
        u = User.objects.get(
            username=validated_data["username"],        
        )
        return u    

class GoogleSignInSerializer(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("username","token",)


    @classmethod
    def get_query(cls,pk):
        try:
            return User.objects.get(username=pk)
        except Exception as e:
            print(e)
            return None    


    def get_token(self,obj):
        return obj.token.key                      