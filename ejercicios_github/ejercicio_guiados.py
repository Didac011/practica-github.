var_grados=float(input("introduce los grados: "))
'''F=Cx5/9+32'''

calculo=var_grados * 5/9 + 32
print("temperatura: ", calculo, "ºF")

#otra manera de presentar la informacion con print

print(f"2ª manera de presentar Temperatura: ")
#primer método de redondeo
print(round(calculo,2))
print(f"método roura {calculo:.2f}")