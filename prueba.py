# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 13:18:29 2023

@author: matia
"""

from collections import defaultdict

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    return lineas

def procesar_linea(linea, inquilinos, deudas):
    partes = linea.split()
    
    if '*' in partes:  # Agregar nuevo inquilino
        nuevo_inquilino = partes[2]
        inquilinos.add(nuevo_inquilino)
    else:
        fecha = partes[0]
        pagador = partes[1]
        monto = int(partes[2])
        
        if '~' in partes:  # Repartir deuda entre inquilinos
            no_pagan = set(partes[4:])
            pagan = inquilinos - no_pagan
            monto_por_persona = monto / len(pagan)
            
            for persona in pagan:
                deudas[persona] += monto_por_persona
        else:
            involucrados = set(partes[3:])
            monto_por_persona = monto / len(involucrados)
            
            for persona in involucrados:
                deudas[persona] += monto_por_persona

def main():
    archivo_largo = "transacciones_largo.txt"
    archivo_corto = "transacciones_corto.txt"
    
    inquilinos = set()
    deudas = defaultdict(float)
    
    for archivo in [archivo_largo, archivo_corto]:
        lineas = leer_archivo(archivo)
        
        for linea in lineas[1:]:  # Ignorar la primera línea con los nombres
            procesar_linea(linea, inquilinos, deudas)

    print("Total deudas por inquilino:")
    for persona, deuda in deudas.items():
        print(f"{persona}: ${deuda:.2f}")



if __name__ == "__main__":
    main()
