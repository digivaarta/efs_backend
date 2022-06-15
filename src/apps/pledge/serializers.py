from rest_framework import serializers

from pledge.models import Pledge,PledgeData,UserPledge


class PledgeDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = PledgeData
        fields = ("title","slug","content","slug","cover_image",)


class PledgeListSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Pledge
        fields = "__all__"
    @classmethod
    def get_query(cls):
        return Pledge.objects.filter(is_active=True)    



class PledgeDetailSerializer(serializers.ModelSerializer):

    pledge_data = PledgeDataSerializer(many=True)


    class Meta:
        model = Pledge
        fields = ("title","slug","cover_image","pledge_data",)

    @classmethod
    def get_query(cls,pk):
        try:
            return Pledge.objects.get(pk=pk)
        except Exception as e:
            return None

class UserPledgeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPledge
        exclude = ("user",)

    def create(self,validated_data):
        user = self.context["request"].user
        v,c = UserPledge.objects.update_or_create(
            user=user,pledge=validated_data["pledge"],
            defaults={}
        )
        return v

    @classmethod
    def get_user(self,user):
        try:
            return UserPledge.objects.get(user=user)
        except Exception as e:
            print(e)
            return None    


