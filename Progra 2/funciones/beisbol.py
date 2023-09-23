from math import *
def distancia_maxima_horizontal(velocidad_inicial, angulo_salida):
  angulito = radians(angulo_salida)
  GRAVEDAD = 9.8
  distancia_horizontal_max = ((velocidad_inicial)**2) * (sin(2 * angulito)) / (GRAVEDAD)
  return distancia_horizontal_max

def altura_maxima(altura_bateo, velocidad_inicial, angulo_salida, distancia_horizontal_max):
  angulito = radians(angulo_salida)
  GRAVEDAD = 9.8
  alturisima_maxima = altura_bateo + (distancia_horizontal_max * tan(angulito)) - ((GRAVEDAD * distancia_horizontal_max**2) / (2 * velocidad_inicial**2 * cos(angulito**2)))
  return altura_maxima

