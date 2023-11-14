#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:45:24 2023

@author: Benicio y Matias
"""

#TP3 IPC
simbolo_excluye = "~"  #Cuando la deuda se reparte entre todos, menos los que le siguen al "~"
simboolo_nuevo = '*' #Cuado esta este simbolo y un nombre a su derecha, significa un nuevo integrante en el departamento

fecha = [2022, 1, 2]


lista=[]

with open("corto.txt","r") as corto:
    for linea in corto:
        texto=linea.strip().split(",")
        lista.extend(texto) #Lista es un array que guarda todas las lineas del texto.
        
                    
deuda = {}
for nombre in lista[0].split(" "): #Nombramos las claves del diccionario
    deuda[nombre]=0
#print(deuda)

inquilinos = list(deuda.keys()) #Saco las claves del diccionario para anotar los nombres

def inquilino_nuevo(nuevo): #Funcion que agrega el nuevo inquilino cuando aparece el signo: '*'
    inquilinos.append(nuevo)
    deuda[nuevo]=0
    

lista2 = [] #Esta segunda lista va a guardar todas las lineas del texto pero cada linea es una lista
for i in range(len(lista)):
    lista2.append(lista[i].split(' '))

#print(deuda)

#def calculo_deuda(fecha):   #Que recibe como argumento fecha

fechas = []
for dias in lista2[1:]:
    fechas.append(dias[0].split('-'))
i=0
for fecha in fechas:
    print(fecha)
    num=fecha.pop(i)
    num1 = int(num)
    
    i+=1
    #fecha = int(fecha)
    
    #years.append(int(fechas[0]))
    #months.append(int(fechas[1]))
    #day.append(int(fechas[2]))
    
print(fechas)   
 

"""
for anos in years:
    if fecha[0]>=anos:
        for meses in months:
            if fecha[1]>=meses:
                for dias in day:
                    if fecha[2]>=dias:
                        print('god')
 """       

for lineas in lista2[1:]:
    
    if simbolo_excluye in lineas:
        deuda[lineas[1]] = round (deuda[lineas[1]]-int(lineas[2]),2) #Se le resta al que pago en el diccionario
        pagan=int(lineas[2])/(len(deuda)-len(lineas[4:])) #Se calcula en cada linea cuanto se debe pagar por persona
        deudores = []
        for nombres in inquilinos:
            if nombres not in lineas[4:]:
                deudores.append(nombres)
        for nombre in deudores:
            deuda[nombre]+=round (pagan,2)
    
    elif simboolo_nuevo in lineas:
        inquilino_nuevo(lineas[2])
                                    
    else:
        deuda[lineas[1]]= round (deuda[lineas[1]]-int(lineas[2]), 2)
        pagan=int(lineas[2])/int(len(lineas[3:]))
        for nombres in lineas[3:]:
            deuda[nombres]+=round (pagan,2)
print(deuda)
    




        
        
       
    
