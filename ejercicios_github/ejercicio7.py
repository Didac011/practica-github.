'''programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes 
forzar que el resultado de la división tenga 2 decimales?'''
operador1 = int(input("introduce un numero: "))
operador2 = int(input("introduce otro numero: "))
print("la suma de operador1 y operador2 es: ", operador1 + operador2)
print("la resta de operador1 y operador2 es: ", operador1 - operador2)
print("la multiplicacion de operador1 y operador2 es: ", operador1 * operador2)
print("la divison de operador1 y operador2 es: ", round(operador1 / operador2, 2))
print("la divison de operador1 y operador2 es: ", operador1 % operador2)