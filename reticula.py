'''#4 Entrada de datos y estructuración. Revisar su retícula para escribir un programa que cree un diccionario vacío para que el usuario capture las materias y créditos de su semestre preferido (inferior a 8vo) al final imprimir en el formato “{asignatura}” tiene “{créditos}” créditos. Y la suma de todos los créditos del semestre '''


reticula = {}
totalCreditosSemestre = 0
semestre = input('Ingrese el semestre a capturar: ')
while True:
    materia = input('Ingresar materia: ')
    creditos = int(input('Cantidad de creditos de la materia: '))
    reticula[materia] = creditos
    opcion = input('Deseas agregar otra materia?(S/N): ')
    if opcion =='N':
        break;

for materia,creditos in reticula.items():
    print(materia+' tiene '+str(creditos)+' creditos')
    totalCreditosSemestre +=creditos

print('Los creditos totales del semestre '+semestre+ ' son: '+ str(totalCreditosSemestre))
    

