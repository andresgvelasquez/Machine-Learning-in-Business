from rest_framework import serializers

class CorrelationMatrixSerializer(serializers.Serializer):
    # Define el formato del JSON de salida. Puedes ajustar esto según la estructura de tu JSON.
    correlation_matrix = serializers.DictField()