from rest_framework import serializers

from profiles.models import Profiles,UserOtp

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True,default=serializers.CurrentUserDefault())

    class Meta:
        model = Profiles
        exclude = ("last_update",)

    def get_object(self,pk):
        try:
            return Profiles.objects.get(pk=pk)
        except Exception:
            return None

class UserOTPSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = UserOtp
        fields = ("email","otp",)

    def create(self,validated_data):
        
        u,c = UserOtp.objects.update_or_create(
            email=validated_data["email"],        
        )
       
        if u:
            u.save()
        return u            