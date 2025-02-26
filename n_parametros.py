'''#1 Funciones con n parámetros 
Escribir un programa que contenga una función que reciba n parámetros de tipo numérico y calcule el producto total. '''
from typing import List
lista = list()
def calcularProductoTotal(listaNumeros:List):
    productoTotal = 0
    for numero in listaNumeros:
        productoTotal += numero
    
    return productoTotal

while True:
    Argumento = float(input('Ingrese numero: '))
    lista.append(Argumento)
    opcion = input('Desea agregar otro argumento? S/N: ')
    if opcion == 'N':
        break;


print('El producto total es: '+str(calcularProductoTotal(lista)))


