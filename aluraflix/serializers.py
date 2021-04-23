from rest_framework import serializers
from aluraflix.models import Filme

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = ['id','nome', 'likes','dislikes']