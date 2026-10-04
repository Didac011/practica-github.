'''Introduce por teclado dos números y muestre por pantalla la siguiente información:
cociente, resto y si el dividendo es par o impar.'''
dividendo = int(input("introduce el dividendo: "))
divisor = int(input("introduce el divisor: "))
cociente = dividendo//divisor
resto = dividendo % divisor
if dividendo % 2==0:
    par_impar = "par"
else:
    par_impar = "impar"
print("el cociente es: ", cociente,)
print("el resto es: ", resto,)
print("el dividendo es: ", par_impar,)