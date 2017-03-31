from django.db import models

# Create your models here.
class Poblacion(models.Model):
    #lo que va a contener la tabla Poblacion
    comuna = models.CharField(max_length=250)
    nino = '0-14'
    adolecente = '15-24'
    adulto = '25-34'
    mediana_edad = '35-54'
    tercera_edad = '55-80'
    ochentamas = '80 y más'
    elegiredad =(
        (nino, '0-14'),
        (adolecente, '15-24'),
        (adulto, '25-34'),
        (mediana_edad, '35-54'),
        (tercera_edad, '55-80'),
        (ochentamas, '80 y mas'),
    )
    edad = models.CharField(
            max_length=10,
            choices=elegiredad,
            default=nino,
    )
    ano1 = '2011'
    ano2 = '2015'
    elegirano =(
        (ano1, '2011'),
        (ano2, '2015'),
    )
    poblacion_año = models.CharField(
        max_length=5,
        choices=elegirano,
        default=ano1,
        )
    numero_poblacion = models.IntegerField(default=0)

    def __str__(self):
        return self.comuna
