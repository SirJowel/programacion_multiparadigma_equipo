import datetime
contador = 1
while contador != 0:
    print('Menu Principal: \n 1.- Imprimir YYYY/MM/DD \n 2.- Imprimir MM/DD/YYYY \n 0.- Salir')
    contador = input('Ingrese el numero de la opcion que desea utilizar: ')
    try: contador = int(contador)
    except ValueError:
       print('\n Favor de no ingresar caracteres, solo numeros validos. \n')
       contador = -1
       continue

    if contador == 1:
       fecha_actual1 = datetime.datetime.now()
       fecha_actual2 = datetime.datetime.strftime(fecha_actual1, '%y/%m/%d')
       print('\n',fecha_actual2, '\n')
    elif contador == 2:
       fecha_actual1 = datetime.datetime.now()
       fecha_actual2 = datetime.datetime.strftime(fecha_actual1, '%m/%d/%Y')
       print('\n',fecha_actual2,'\n')
    elif contador == 0:
       print('Vuelva pronto :)','\n')
    else:   
       print('\n Favor de ingresar correctamente la opcion que desea usar. \n')
     

