#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:45:24 2023

@author: Benicio y Matias
"""

#TP3 IPC
simbolo_excluye="~"  #Cuando la deuda se reparte entre todos, menos los que le siguen al "~"

lista=[]

with open("corto.txt","r") as corto:
    for linea in corto:
        texto=linea.strip().split(",")
        lista.extend(texto) #Lista es un array que guarda todas las lineas del texto.
        
    
               
deuda={}
for nombre in lista[0].split(" "):
    deuda[nombre]=0


#print(my_dic)

for i in range(len(lista)):
    lista[i] = lista[i].split()
        
    
