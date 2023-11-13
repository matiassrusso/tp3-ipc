#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:45:24 2023

@author: Benicio y Matias
"""

#TP3 IPC
simbolo_excluye="~"  #Cuando la deuda se reparte entre todos, menos los que le siguen al "~"
simboolo_nuevo = '*' #Cuado esta este simbolo y un nombre a su derecha, significa un nuevo integrante en el departamento

lista=[]

with open("corto.txt","r") as corto:
    for linea in corto:
        texto=linea.strip().split(",")
        lista.extend(texto) #Lista es un array que guarda todas las lineas del texto.
        
                    
deuda = {}
for nombre in lista[0].split(" "): #Nombramos las claves del diccionario
    deuda[nombre]=0
#print(deuda)

inquilinos = list(deuda.keys())
def inquilino_nuevo(nuevo):
    inquilinos.append(nuevo)
    deuda[nuevo]=0
    

lista2 = []
for i in range(len(lista)):
    lista2.append(lista[i].split(' '))

#print(deuda)

for lineas in lista2[1:]:
    if simbolo_excluye in lineas:
        deuda[lineas[1]] = deuda[lineas[1]]-int(lineas[2])
        pagan=int(lineas[2])/(len(deuda)-len(lineas[4:]))
        deudores = []
        for nombres in inquilinos:
            if nombres not in lineas[4:]:
                deudores.append(nombres)
                for nombre in deudores:
                    deuda[nombre]+=int(pagan)
    elif simboolo_nuevo in lineas:
        inquilino_nuevo(lineas[2])
        

                    
            
    else:
        deuda[lineas[1]]=deuda[lineas[1]]-int(lineas[2])
        pagan=int(lineas[2])/int(len(lineas[3:]))
        for nombres in lineas[3:]:
            deuda[nombres]+=int(pagan)
print(deuda)
    













"""
def calculo_deuda(fecha):#Que reciba como argumento fecha (nose bien como hacer para que calcule hasta tal fecha)
    i = 1
    m = lista2[i][0]
    while m != fecha:
        i += 1 #salteo la primer lista dentro de lista2
        if simbolo_excluye in lista[i]:
        
"""       
    
