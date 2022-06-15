from rest_framework import serializers
from django.utils import timezone
from task.models import Curriculum,UserTask,TaskChoice
import datetime
class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curriculum
        fields = ("title","content","creation_date","attachment_type",)

    @classmethod
    def get_query(cls):
        return Curriculum.objects.filter(is_active=True)  

class UserTaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserTask
        fields = ("attachment","content","curriculum",)

    def create(self,validated_data):
        user = self.context["request"].user
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

        

class UserTaskStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserTask
        fields = ("id",)

    @classmethod
    def get_object(cls,pk,user):
        curriculum = Curriculum.objects.get(pk=pk)
        try:
            return cls.get_query(cls,curriculum,user)
        except Exception as e:
            print(e)
            return None 

    def get_query(self,curriculum,user):
        now = timezone.now()
        print("Now")
        print(now)
        if(TaskChoice.DAILY == curriculum.task_type):
            return UserTask.objects.filter(user=user,curriculum=curriculum,creation_date__date=now.date()).first()
            # if v:
            #     raise serializers.ValidationError({'message':'Data Available'}, code=200)
            # else:  
            #     raise serializers.ValidationError({'message':'Data Available'}, code=200)  
        elif(TaskChoice.MONTHLY == curriculum.task_type):
            return UserTask.objects.filter(user=user,curriculum=curriculum,creation_date__year=now.year,creation_date__month=now.month).first()
        elif(TaskChoice.ONE_TIME == curriculum.task_type):
            return UserTask.objects.filter(user=user,curriculum=curriculum).first()
        return None               

