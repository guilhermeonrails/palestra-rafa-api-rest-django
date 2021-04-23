from aluraflix.models import Filme
from aluraflix.serializers import FilmeSerializer
from rest_framework import viewsets

class FilmeViewSet(viewsets.ModelViewSet):
    serializer_class = FilmeSerializer
    queryset = Filme.objects.all()