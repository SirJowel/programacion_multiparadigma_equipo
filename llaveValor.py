diccionario = {}
def mostrarLlaveValor(**kargs):
    for llave,valor in kargs.items():
        print('Llave: '+str(llave)+', Valor: '+str(valor))


while True:
    llave = input('Ingrese la llave: ')
    valor = input('Ingrese el valor de la llave: ')
    diccionario[llave] = valor
    opcion = input('Desea ingresar otra llave y valor?(S/N): ')
    if opcion =='N':
        break

mostrarLlaveValor(**diccionario)