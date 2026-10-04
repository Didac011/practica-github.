'''Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro,
introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.'''
import math
radio = float(input("introduce el radio del cilindro: "))
altura = float(input("introduce la altura: "))
area = 2*math.pi*radio*(radio+altura)
volumen = math.pi*radio**2*altura
print("el area del cilindro es: ",round(area,2), "y el volumen es:",round(volumen,2))