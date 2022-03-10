from rest_framework import serializers

from profiles.models import Profiles

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