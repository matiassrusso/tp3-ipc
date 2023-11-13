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

lista2 = []
for i in range(len(lista)):
    lista2.append(lista[i].split(' '))

#print (lista2)

def calculo_deuda(fecha)#Que reciba como argumento fecha (nose bien como hacer para que calcule hasta tal fecha)
    i = 0
    m = lista2[i][0]
    while m != fecha:
        i += 1 #salteo la primer lista dentro de lista2
        if simbolo_excluye in lista[i]
        
         
    
    
