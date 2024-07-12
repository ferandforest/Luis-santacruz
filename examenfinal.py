import random

trabajadores_lista=[]



def sueldos_del_trabajador():
    nombres = ['Juan Perez', 'Maria Garcia', 'Carlos Lopez', 'Ana Martinez', 
               'Pedro Rodriguez', 'Laura Hernandez', 'Miguel Sánchez', 
               'Isabel Gómez', 'Francisco Díaz', 'Elena Fernández']
    
    for nombre in nombres:
        sueldo = random.randrange(300000, 2600000)
        trabajadores_lista.append((nombre, sueldo))
        print(f'{nombre}: ${sueldo}')
   
def clasificacion_de_trabajadores():
    print('Sueldos menores a $800.000:')
    total_bajo = 0
  
    for nombre, sueldo in trabajadores_lista:
        if sueldo < 800000:
            print(f'{nombre}: ${sueldo}')
            total_bajo += sueldo
    print(f'Total de sueldos menores a $800.000: ${total_bajo}')
    
    
def clasificacion_de_trabajadores2():
    print('Sueldos entre $800.000 y $2.000.000:')
    
    total_medio=800000
    for nombre, sueldo in trabajadores_lista:
        if sueldo < 2000000:
            print(f'{nombre}: ${sueldo}')
            total_medio += sueldo
    
        

def clasificacion_de_trabajadores3():
    print('Sueldos mayor a $2.000.000:')
    
    total_mayor=0
    for nombre, sueldo in trabajadores_lista:
        if sueldo > 2000000:
            print(f'{nombre}: ${sueldo}')
            total_mayor += sueldo
    
        
def total_de_sueldos():
    
    total=0
    for nombre, sueldo in trabajadores_lista:
        if sueldo>300000:
            f'{nombre}: ${sueldo}'
            total+=sueldo
    print(f'el total de todos los sueldos es de:{total}')
    


def descuento_de_vida():
    
    print()
    
   

def sueldo_mas_alto():
    
    for sueldo in trabajadores_lista:
       
        str(max(sueldo))
    

    
    
    
while True:
    print('menu')
    print('1-Asignar sueldos aleatorios')
    print('2-Clasificar sueldos')
    print('3-Ver estadísticas.')
    print('4-Reporte de sueldos')
    print('5-Salir del programa')
    opcion = input('ingrese del (1-5):'+' ')


    if opcion=='1':
        print('ha seleccionado la opcion 1')
        sueldos_del_trabajador()
        
    elif opcion=='2':
        print('ha seleccionado la opcion 2')
        
        clasificacion_de_trabajadores()       
        print()
        print()
        clasificacion_de_trabajadores2()

        print()
        print()
        clasificacion_de_trabajadores3()
        print()
        print()
        total_de_sueldos()
    elif opcion=='3':
        print('ha seleccionado la opcion 3')
        sueldo_mas_alto()
    elif opcion=='4':
        print('ha seleccionado la opcion 4')
        
    else:
        opcion=='5'
            
        print('ha seleccionado la opcion 5')
        print('Finalizando programa...')
        print('desarrollado por Luis santa cruz')
        print('rut:24.336.968-1')
        break