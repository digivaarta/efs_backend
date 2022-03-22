from re import L
from rest_framework import serializers

from support.models import Ticket,Support


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ("subject","id",)

    def create(self,validated_data):
        user = self.context["request"].user
        v = Ticket.objects.create(
            user=user,
            **validated_data
        )    
        return v

class TicketUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ("status",)

    def get_object(self,pk):
        try:
            return Ticket.objects.get(pk=pk)
        except Exception as e:
            return None

class SupportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Support
        fields = ("ticket","message",)
    

    def create(self,validated_data):
        user = self.context["request"].user
        v = Support.objects.create(
            sender=user,
            **validated_data
        )    
        return v


class TicketListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        exclude = ("user",)


    @classmethod
    def get_query(cls,user):
        return Ticket.objects.filter(user=user)

class SupportListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Support
        exclude = ("sender",)


    @classmethod
    def get_query(cls):
        return Support.objects.all()

    @classmethod
    def get_none(cls):
        return Support.objects.none()    
            


