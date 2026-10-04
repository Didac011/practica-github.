'''Realiza un programa que introduciendo el valor del lado de un cuadrado nos devuelva
por pantalla en el área y el perímetro.'''
lado = int(input("introduce el valor del lado de un cuadrado: "))
area = lado*lado
perimetro = lado+lado+lado+lado
print("el area del cuadrado es: ", area," y el perimetro es: ", perimetro,)