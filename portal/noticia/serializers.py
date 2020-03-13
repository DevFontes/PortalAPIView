from rest_framework import serializers

from .models import Noticia, Autor


class NoticiaSerializer(serializers.Serializer):
    titulo = serializers.CharField(max_length=125)
    texto = serializers.CharField()
    autor_id = serializers.IntegerField()

    def create(self, validate_data):
        return Noticia.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.titulo = validate_data.get("titulo", instance.titulo)
        instance.texto = validate_data.get("texto", instance.texto)
        instance.autor_id = validate_data.get("autor_id", instance.autor_id)
        instance.save()
        return instance
