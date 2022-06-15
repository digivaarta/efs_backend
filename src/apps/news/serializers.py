from rest_framework import serializers

from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = News
        fields = ("title","description","content","image",)

    @classmethod
    def get_query(cls):
        return News.objects.filter(is_active=True)   