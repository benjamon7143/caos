from webCaos.models import Mercaderia
from rest_framework import serializers

class mercaderiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mercaderia
        fields = ["IDMerca","NombreMerca","PrecioVenta","CantidadStock",]
