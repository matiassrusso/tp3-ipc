#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:45:24 2023

@author: Benicio y Matias
"""

#TP3 IPC
simbolo_excluye = "~"  #Cuando la deuda se reparte entre todos, menos los que le siguen al "~"
simboolo_nuevo = '*' #Cuado esta este simbolo y un nombre a su derecha, significa un nuevo integrante en el departamento

import matplotlib.pyplot as plt

lista=[]

with open("transacciones_largo.txt","r") as corto:
    for linea in corto:
        texto=linea.strip().split(",")
        lista.extend(texto) #Lista es un array que guarda todas las lineas del texto.
        
         
deuda = {} #Un diccionario para ir sumando y restando la deuda de cada persona
registro = {} #Otro diccionario que vaya conteniendo en dos listas la fecha y la suma a medida que avanzan las transacciones (para luego graficar)
for nombre in lista[0].split(" "): #Nombramos las claves del diccionario
    deuda[nombre]=0
    registro[nombre] = 0
#print(deuda)

inquilinos = list(deuda.keys()) #Saco las claves del diccionario para anotar los nombres

def inquilino_nuevo(nuevo): #Funcion que agrega el nuevo inquilino cuando aparece el signo: '*'
    inquilinos.append(nuevo)
    deuda[nuevo]=0
    

lista2 = [] #Esta segunda lista va a guardar todas las lineas del texto pero cada linea es una lista
for i in range(len(lista)):
    lista2.append(lista[i].split(' '))



fechas_str = []
for dias in lista2[1:]:
    fechas_str.append(dias[0].split('-'))
fechas_int = [[int(numero) for numero in sublist] for sublist in fechas_str]


def calculo_deuda(year, month, day):   #Que recibe como argumento fecha    
    u=1
    for fechas in fechas_int:
        if year == fechas[0]: #Chequea años
            if month >= fechas[1]: #Chequea meses
                if day >= fechas[2]: #Chequea dias
                    u+=1
        elif year > fechas[0]:
            u += 1
    return u
        

prueba = calculo_deuda(2029, 9, 13)
#print(prueba)

#<<<<<<< HEAD
#=======
prueba = calculo_deuda(2023, 9, 13)


#>>>>>>> 129cfa91bbc145e2cf1d0b7a911a159586d06d6d
k=0

for lineas in lista2[1:prueba]: #calcula la deuda hasta el valor de u (cantidad de lineas hasta la fecha)

    if simbolo_excluye in lineas:
        deuda[lineas[1]] = round (deuda[lineas[1]]-int(lineas[2]),2) #Se le resta al que pago en el diccionario
        pagan= round (int(lineas[2])/(len(deuda)-len(lineas[4:])),2) #Se calcula en cada linea cuanto se debe pagar por persona
        deudores = []
        for nombres in inquilinos:  
            if nombres not in lineas[4:]:
                deudores.append(nombres)
        for nombre in deudores:
            deuda[nombre]+= round(pagan,2)
    
    elif simboolo_nuevo in lineas:
        inquilino_nuevo(lineas[2])
                                    
    else:
        deuda[lineas[1]]= round(deuda[lineas[1]]-int(lineas[2]), 2)
        pagan = round(int(lineas[2])/int(len(lineas[3:])),2)
        for nombres in lineas[3:]:
            deuda[nombres]+= round(pagan,2)
    
#<<<<<<< HEAD
#=======
    for key in deuda:
       registro[key][0].append(prueba)
       registro[key][1].append(deuda[key])

print(registro)
    

#>>>>>>> 129cfa91bbc145e2cf1d0b7a911a159586d06d6d
    
#print(deuda)




import pandas as pd

# Crear un DataFrame con los datos
datos = pd.DataFrame({
    'Fecha': pd.to_datetime(['-'.join(fecha) for fecha in fechas_str]),
    'Nombre': inquilinos
})

# Graficar
plt.figure(figsize=(10, 6))
for nombre in inquilinos:
    subset = datos[datos['Nombre'] == nombre]
    plt.plot(subset['Fecha'], label=nombre)

plt.title('Gráfico de Transacciones')
plt.xlabel('Fecha')
plt.ylabel('Valor')
plt.legend()
plt.show()



"""
plt.figure()
plt.plot (fechas_int[k], deuda['Jennifer'], label = 'Azul')

plt.plot(fechas_int[k][0], deuda['Jennifer'], 'bo', label='Azul')  # 'bo' means blue color and circle marker
k+= 1
plt.xlim([2022,1,1],[2022,3,1])
plt.ylim([-300000,200000])
plt.show()
"""


        
       
    
