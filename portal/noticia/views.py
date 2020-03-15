from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Noticia
from .serializers import NoticiaSerializer


class NoticiaView(APIView):
    def get(self, request):
        noticias = Noticia.objects.all()
        serializers = NoticiaSerializer(noticias, many=True)
        return Response({"noticias": serializers.data})

    def post(self, request):
        noticia = request.data
        serializer = NoticiaSerializer(data=noticia)
        if serializer.is_valid(raise_exception=True):
            noticia_salva = serializer.save()
        return Response(
            {"Notícia '{}' gravada com sucesso.".format(noticia_salva.titulo)}
        )

    def put(self, request, pk):
        noticia = get_object_or_404(Noticia.objects.all(), pk=pk)
        data = request.data
        serializer = NoticiaSerializer(instance=noticia, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            noticia = serializer.save()
        return Response({"Noticia '{}' atualizada com sucesso.".format(noticia.titulo)})

    def delete(self, request, pk):
        noticia = get_object_or_404(Noticia.objects.all(), pk=pk)
        noticia.delete()
        return Response({"Noticia '{}' excluida com sucesso.".format(pk)}, status=204,)

