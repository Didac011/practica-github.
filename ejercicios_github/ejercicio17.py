'''Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el
peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado
es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.'''
peso = float(input("introduce tu peso: "))
estatura = float(input("introduce tu estatura: "))
indice_masa = peso/estatura**2
print("tu IMC es de: ", round(indice_masa,2))
if indice_masa >= 25:
    print("Tienes sobrepeso") 
    
