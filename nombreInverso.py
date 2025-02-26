'''#3 Entrada de datos y manipulación. 
Escribir un programa que permita al usuario capturar su nombre completo e imprima su nombre de manera inversa letra por letra '''

nombreCompleto = input('Ingrese su nombre completo: ')
nombreInverso = reversed(nombreCompleto.replace(' ',''))
print(','.join(nombreInverso))