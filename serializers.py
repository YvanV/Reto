from rest_framework import serializers

from .models import *


class PersonaSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name = "persona-detail")
    peliculas = serializers.HyperlinkedRelatedField(many=True, queryset=Pelicula.objects.all(), view_name="pelicula-detail")
    especies = serializers.HyperlinkedRelatedField(many=True, queryset=Especie.objects.all(), view_name="especie-detail")
    planeta_natal = serializers.HyperlinkedRelatedField(queryset=Planeta.objects.all(), view_name="planeta-detail")
    naves = serializers.HyperlinkedRelatedField(many=True, queryset=Nave.objects.all(), view_name="nave-detail")
    vehiculos = serializers.HyperlinkedRelatedField(many=True, queryset=Vehiculo.objects.all(), view_name="vehiculo-detail")
    creado = serializers.CharField(source="fecha_creacion")
    editado = serializers.CharField(source="fecha_actualizacion")

    class Meta:
        model = Persona
        fields = [ "anho_nacimiento", "color_ojos",  "peliculas","genero", "color_cabello", 
        "estatura", "planeta_natal", "peso", "nombre", "color_piel", "creado", 
        "editado", "especies", "naves", "url", "vehiculos"]   


class PlanetaSerializer(serializers.ModelSerializer):
    residentes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="persona-detail")
    peliculas = serializers.HyperlinkedRelatedField(many=True, queryset=Pelicula.objects.all(), view_name="pelicula-detail")
    url = serializers.HyperlinkedIdentityField(view_name = "planeta-detail")
    creado = serializers.CharField(source="fecha_creacion")
    editado = serializers.CharField(source="fecha_actualizacion")

    class Meta:
        model = Planeta
        fields = ["clima", "creado", "diametro",  "editado", "peliculas", "gravedad", 
        "nombre", "periodo_orbita", "poblacion", "residentes", "periodo_rotacion", 
        "agua_superficie", "terreno", "url"
        ]

    
class EspecieSerializer(serializers.ModelSerializer):
    personas = serializers.HyperlinkedRelatedField(many=True, queryset=Persona.objects.all(), view_name="persona-detail")
    peliculas = serializers.HyperlinkedRelatedField(many=True, queryset=Pelicula.objects.all(), view_name="pelicula-detail")
    url = serializers.HyperlinkedIdentityField(view_name = "especie-detail")
    creado = serializers.CharField(source="fecha_creacion")
    editado = serializers.CharField(source="fecha_actualizacion")

    class Meta:
        model = Especie
        fields = ["estatura_promedio", "esperanza_vida", "clasificacion", "creado", 
        "designacion", "editado", "color_ojos", "color_cabello", "planeta_natal", 
        "lenguaje", "nombre","personas", "peliculas", "color_piel",  "url", ]
    

class VehiculoSerializer(serializers.ModelSerializer):
    pilotos = serializers.HyperlinkedRelatedField(many=True, queryset=Persona.objects.all(), view_name="persona-detail")
    peliculas = serializers.HyperlinkedRelatedField(many=True, queryset=Pelicula.objects.all(), view_name="pelicula-detail")
    creado = serializers.CharField(source="fecha_creacion")
    editado = serializers.CharField(source="fecha_actualizacion")
    url = serializers.HyperlinkedIdentityField(view_name = "vehiculo-detail")

    class Meta:
        model = Vehiculo
        fields = ["capacidad_carga", "consumbibles", "costo_en_creditos", "creado",
        "tripulacion", "editado", "longitud", "fabricante", "maxima_velocidad", 
        "modelo", "nombre", "pasajeros", "pilotos", "peliculas", "url", "clase_vehiculo"]

class NaveSerializer(serializers.ModelSerializer):
    pilotos = serializers.HyperlinkedRelatedField(many=True, queryset=Persona.objects.all(), view_name="persona-detail")
    peliculas = serializers.HyperlinkedRelatedField(many=True, queryset=Pelicula.objects.all(), view_name="pelicula-detail")
    url = serializers.HyperlinkedIdentityField(view_name = "nave-detail")
    creado = serializers.CharField(source="fecha_creacion")
    editado = serializers.CharField(source="fecha_actualizacion")

    class Meta:
        model = Nave
        fields = ["MGLT", "capacidad_carga", "consumibles", "costo_en_creditos",
        "creado", "tripulacion", "editado", "puntaje_hyperdrive", "longitud", 
        "fabricante", "maxima_velocidad", "modelo", "nombre", 
        "pasajeros", "peliculas", "pilotos", "clase_nave", "url"
        ]

class PeliculaSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name = "pelicula-detail")
    personajes = serializers.HyperlinkedRelatedField(many=True, queryset=Persona.objects.all(), view_name="persona-detail")
    planetas = serializers.HyperlinkedRelatedField(many=True, queryset=Planeta.objects.all(), view_name="planeta-detail")
    especies = serializers.HyperlinkedRelatedField(many=True, queryset=Especie.objects.all(), view_name="especie-detail")
    creado = serializers.CharField(source="fecha_creacion")
    editado = serializers.CharField(source="fecha_actualizacion")
    naves = serializers.HyperlinkedRelatedField(many=True, queryset=Nave.objects.all(), view_name="nave-detail")
    vehiculos = serializers.HyperlinkedRelatedField(many=True, queryset=Vehiculo.objects.all(), view_name="vehiculo-detail")

    class Meta:
        model = Pelicula
        fields = ["personajes", "creado", "director", "editado", 
        "codigo_episodio", "texto_apertura", "planetas", "productor", 
        "fecha_emision", "especies", "naves", "titulo","url", "vehiculos"
        ]


