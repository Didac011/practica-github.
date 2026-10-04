'''Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor
y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.'''
base_menor = int(input("introduce el valor de la base menor: "))
base_mayor = int(input("introduce el valor de la base mayor: "))
altura = int(input("inroduce el valor de la altura: "))
lado = int(input("introduce el valor del lado: "))
perimetro = base_mayor+base_menor+2*lado
area = ((base_mayor+base_menor)*altura)/2
print("el perimetro del trapecio es: ", perimetro,"y el area es: ", area,) 