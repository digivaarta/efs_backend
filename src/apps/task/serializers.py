from pyexpat import model
from rest_framework import serializers

from task.models import Curriculum,UserTask

class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curriculum
        exclude = ("user",)

    @classmethod
    def get_query(cls):
        return Curriculum.objects.filter(is_active=True)  

class UserTaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserTask
        fields = ("attachment","content","curriculum",)

    def create(self,validated_data):
        user = self.content["request"].user
        v = UserTask.objects.create(
            user=user,**validated_data
        )
        return v


class TaskDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curriculum
        fields = ("id","title",)


class UserTaskListSerializer(serializers.ModelSerializer):

    curriculum = TaskDetailSerializer()

    class Meta:
        model = UserTask
        exclude = ("user","is_active",)
        depth = 1
        

    @classmethod
    def get_query(cls,user):
        return UserTask.objects.filter(user=user)      

        

