from rest_framework import serializers

from utility.models import MetaContent

class MetaContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = MetaContent
        exclude = ("user",)

    @classmethod
    def get_query(cls,slug):
        return MetaContent.objects.get(slug=slug,is_active=True)    