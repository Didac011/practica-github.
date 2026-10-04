'''Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El
resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un
resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso
(raíz y división).'''
import math
numero = float(input("introduce un valor: "))
raiz= math.sqrt(numero)
division = raiz//2
print("el resultado de la raiz es: ",raiz,"y el resultado de la division es: ", division,)