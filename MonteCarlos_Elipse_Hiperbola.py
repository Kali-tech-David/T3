import math
import random
 
 
def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("El valor debe ser mayor que 0.")
        except ValueError:
            print("Ingrese un numero valido.")
 
 
def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("El valor debe ser mayor que 0.")
        except ValueError:
            print("Ingrese un numero entero valido.")
 
 
def main():

    a = pedir_float("Ingrese a (elipse): ")
    b = pedir_float("Ingrese b (elipse): ")
    c = pedir_float("Ingrese c (hiperbola): ")
    d = pedir_float("Ingrese d (hiperbola): ")
    cantidad = pedir_entero("Ingrese la cantidad de puntos aleatorios: ")
 
    puntos_en_elipse = 0
    puntos_en_interseccion = 0
 
    for _ in range(cantidad):

        x = random.uniform(-a, a)
        y = random.uniform(-b, b)
 

        dentro_elipse = (x ** 2) / (a ** 2) + (y ** 2) / (b ** 2) <= 1
 

        dentro_hiperbola = (x ** 2) / (c ** 2) - (y ** 2) / (d ** 2) >= 1
 
        if dentro_elipse:
            puntos_en_elipse = puntos_en_elipse + 1
 
            if dentro_hiperbola:
                puntos_en_interseccion = puntos_en_interseccion + 1
 
    area_elipse = math.pi * a * b
 
    if puntos_en_elipse > 0:
        proporcion = puntos_en_interseccion / puntos_en_elipse
    else:
        proporcion = 0
 
    area_interseccion = proporcion * area_elipse
 
    print()
    print("Puntos aleatorios dentro de la elipse:", puntos_en_elipse)
    print("Puntos aleatorios en la interseccion de la hiperbola con la elipse:", puntos_en_interseccion)
    print("Area aproximada de la zona de la elipse que se interseca con la hiperbola:", round(area_interseccion, 4))
 
 
main()