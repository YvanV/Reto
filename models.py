from django.db import models
from django.urls import reverse, reverse_lazy

# Create your models here.

# ---------------------------------------------------------------
# Clase Planeta
# ---------------------------------------------------------------

class Planeta(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    diametro = models.IntegerField(null=True, blank=True)
    periodo_rotacion = models.IntegerField(null=True, blank=True)
    fecha_creacion = models.DateTimeField("creado", auto_now_add=True, null=True)
    fecha_actualizacion = models.DateTimeField("editado", auto_now=True)
    clima = models.CharField(max_length=10, null=True, blank=True)
    gravedad = models.CharField(max_length=10, null=True, blank=True)
    poblacion = models.CharField(max_length=10, null=True, blank=True)
    periodo_orbita = models.CharField(max_length=10, null=True, blank=True)
    agua_superficie = models.CharField(max_length=10, null=True, blank=True)
    terreno  = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):  
        return self.nombre

# ---------------------------------------------------------------
# Clase Persona
# ---------------------------------------------------------------

class Persona(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    anho_nacimiento = models.CharField(max_length=50, null=True, blank=True)
    color_ojos = models.CharField(max_length=50, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    planeta_natal = models.ForeignKey(Planeta, null=True, blank=True, on_delete=models.PROTECT, related_name="residentes")
    # especie = models.ForeignKey(Especie, null=True, blank=True, on_delete=models.PROTECT, related_name="especies")
    genero = models.CharField(max_length=10, null=True, blank=True)
    color_cabello = models.CharField(max_length=10, null=True, blank=True)
    estatura = models.CharField(max_length=10, null=True, blank=True)
    peso = models.CharField(max_length=10, null=True, blank=True)
    color_piel = models.CharField(max_length=10, null=True, blank=True)
    
    def __str__(self):  
        return "{0}".format(self.nombre)

    def get_absolute_url(self):
        return reverse("persona-list")        
        
# ---------------------------------------------------------------
# Clase Especie
# ---------------------------------------------------------------

class Especie(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    esperanza_vida = models.CharField(max_length=10, null=True, blank=True)
    clasificacion = models.CharField(max_length=10, null=True, blank=True)
    designacion = models.CharField(max_length=10, null=True, blank=True)
    color_ojos = models.CharField(max_length=50, null=True, blank=True)
    color_piel = models.CharField(max_length=50, null=True, blank=True)
    color_cabello = models.CharField(max_length=10, null=True, blank=True)
    lenguaje = models.CharField(max_length=10, null=True, blank=True)
    estatura_promedio = models.CharField(max_length=10, null=True, blank=True)
    planeta_natal = models.ForeignKey(Planeta, null=True, blank=True, on_delete=models.PROTECT, related_name="especies")
    personas = models.ManyToManyField(Persona, related_name='especies')
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):  
        return "{0}".format(self.nombre)

# ---------------------------------------------------------------
# Clase Vehiculo
# ---------------------------------------------------------------

class Vehiculo(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    capacidad_carga = models.CharField(max_length=10, null=True, blank=True)
    consumbibles = models.CharField(max_length=10, null=True, blank=True)
    costo_en_creditos = models.CharField(max_length=10, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    tripulacion = models.CharField(max_length=10, null=True, blank=True)
    longitud = models.CharField(max_length=10, null=True, blank=True)
    fabricante = models.CharField(max_length=50, null=True, blank=True)
    maxima_velocidad = models.CharField(max_length=10, null=True, blank=True)
    modelo = models.CharField(max_length=50, null=True, blank=True)
    pasajeros = models.CharField(max_length=10, null=True, blank=True)
    clase_vehiculo = models.CharField(max_length=10, null=True, blank=True)
    pilotos = models.ManyToManyField(Persona, related_name="vehiculos")

    def __str__(self):  
        return self.nombre

# ---------------------------------------------------------------
# Clase Nave
# ---------------------------------------------------------------

class Nave(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    MGLT = models.CharField(max_length=10, null=True, blank=True)
    consumibles = models.CharField(max_length=10, null=True, blank=True)
    costo_en_creditos = models.CharField(max_length=10, null=True, blank=True)
    tripulacion = models.CharField(max_length=10, null=True, blank=True)
    puntaje_hyperdrive = models.CharField(max_length=10, null=True, blank=True)
    longitud = models.CharField(max_length=10, null=True, blank=True)
    fabricante = models.CharField(max_length=50, null=True, blank=True)
    maxima_velocidad = models.CharField(max_length=10, null=True, blank=True)
    modelo = models.CharField(max_length=50, null=True, blank=True)
    pasajeros = models.CharField(max_length=10, null=True, blank=True)
    clase_nave = models.CharField(max_length=50, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    capacidad_carga = models.CharField(max_length=10, null=True, blank=True)
    pilotos = models.ManyToManyField(Persona, related_name="naves")

    def __str__(self):  
        return self.nombre

# ---------------------------------------------------------------
# Clase Pelicula
# ---------------------------------------------------------------

class Pelicula(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    director = models.CharField(max_length=50, null=True, blank=True)
    codigo_episodio = models.CharField(max_length=50, null=True, blank=True)
    texto_apertura = models.CharField(max_length=200, null=True, blank=True)
    productor = models.CharField(max_length=50, null=True, blank=True)
    fecha_emision = models.CharField(max_length=50, null=True, blank=True)
    planetas = models.ManyToManyField(Planeta, related_name='peliculas')
    personajes = models.ManyToManyField(Persona, related_name="peliculas")
    especies = models.ManyToManyField(Especie, related_name="peliculas")
    naves = models.ManyToManyField(Nave, related_name="peliculas")
    vehiculos = models.ManyToManyField(Vehiculo, related_name="peliculas")

    def __str__(self):  
        return self.titulo

