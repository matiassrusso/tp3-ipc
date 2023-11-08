#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:45:24 2023

@author: Benicio y Matias
"""

#TP3 IPC
simbolo_repartida="~"
lista=[]


with open("corto.txt","r") as corto:
    for linea in corto:
        texto=linea.strip().split(",")
        lista.extend(texto) #Lista es un array que guarda todas las lineas del texto.
        
    
               
my_dic={}
for nombre in lista[0].split(" "):
    my_dic[nombre]=0


#print(my_dic)

for linea in lista:
    linea=linea.split(" ")
    if simbolo_repartida in linea:
        print("god")
#print(lista[1])