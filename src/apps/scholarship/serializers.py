from rest_framework import serializers
from scholarship.models import Scholarship,ScholarshipTask,ScholarshipSubTask,UserScholarshipTask


class ScholarshipSubTaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScholarshipSubTask
        fields = ("title","id",)

class ScholarshipTaskListSerializer(serializers.ModelSerializer):

    sch_scholarship_task = ScholarshipSubTaskListSerializer(many=True)

    class Meta:
        model = ScholarshipTask
        fields = ("id","title","minimum_age","maximum_age","sch_scholarship_task",)


class ScholarshipListSerializers(serializers.ModelSerializer):

    sch_scholarship = ScholarshipTaskListSerializer(many=True)

    class Meta:
        model = Scholarship
        fields = ("id","title","content","sch_scholarship",)


    @classmethod
    def get_query(self):
        return Scholarship.objects.filter(is_active=True)    

class UserScholarshipTaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserScholarshipTask
        exclude = ("user",)

    def create(self,validated_data):
        user = self.context["request"].user
        v = UserScholarshipTask.objects.create(user=user,**validated_data)    
        return v   

class UserScholarshipTaskListSerializer(serializers.ModelSerializer):

    sub_task = serializers.SerializerMethodField()

    class Meta:
        model = UserScholarshipTask
        fields = ("content","attachment_one","attachment_two","status","sub_task",)

    @classmethod
    def get_query(cls,user):
        return UserScholarshipTask.objects.filter(user=user) 

    def get_sub_task(self,obj):
        return obj.sub_task.title     