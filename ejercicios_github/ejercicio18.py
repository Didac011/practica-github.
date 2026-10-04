'''Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan
importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores
de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por
teclado el número de menores y el número de adultos que asisten al cine.'''
precio = 12
adultos = int(input("cuantos adultos vais a asistir: "))
memores_18 = int(input("cuantos menores vais a asistir: "))
descuento_adultos = precio*0.90
descuento_menores = precio*0.50
total_adultos = (adultos*descuento_adultos) 
total_menores = (memores_18*descuento_menores)
total = (total_adultos+total_menores)
print("por cada menor teneis que pagar ", descuento_menores, "en total los menores van a pagar ", total_menores)
print("por cada adulto teneis que pagar ", descuento_adultos, "en total los adultos teneis que pagar ", total_adultos)
print("en total teneis que pagar ",total,)