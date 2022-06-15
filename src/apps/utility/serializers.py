from rest_framework import serializers

from utility.models import MetaContent,Suggestion

class MetaContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = MetaContent
        fields = ("title","content","extra",)

    @classmethod
    def get_query(cls,slug):
        return MetaContent.objects.get(slug=slug,is_active=True)    


class MetaContentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = MetaContent
        fields = ("title","content","extra",)

    @classmethod
    def get_query(cls):
        return MetaContent.objects.filter(is_active=True)        


class SuggestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Suggestion
        fields = ("title","content",)

    def create(self,validated_data):
        user = self.context["request"].user
        v = Suggestion.objects.create(
            user=user,**validated_data
        )    
        return v