from rest_framework import serializers
from materias.models import Materia
from niveles.models import Nivel


class MateriaSerializer(serializers.ModelSerializer):
    nivel_descripcion = serializers.CharField(
        source='nivel.descripcion', read_only=True)

    class Meta:
        model = Materia
        fields = ['id', 'codigo', 'nombre',
                  'carga_horaria', 'nivel', 'nivel_descripcion']
