from words.models import Words
from rest_framework import serializers

class WordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = ('__all__')