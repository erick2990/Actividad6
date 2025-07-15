from babel.dates import match_skeleton

Cod = {}

fin = True

def agregar():
    print('Funcion para añadir productos: ')

def view_items():
    print('Productos disponibles')

def existencia():
    print('Existencia de productos')

def total():
    print('Este es el total del inventario')

def categoria():
    print('Productos por categoria')

while fin:
    try:
        print("\r\t\tInventario de tienda de ropa: ")
        print('1. Agregar producto \r\n2. Mostrar lista de productos \r\n3. Solicitar codio de producto y existencia ')
        print('4. Calcular valor total del inventario \r\n5.Mostrar productos por categoria \r\n6. Salir')
        opcion = int(input('Ingrese el numero de opcion que deseea: '))

        match opcion:
            case 1:
                agregar()
            case 2:
                view_items()
            case 3:
                existencia()
            case 4:
                total()
            case 5:
                categoria()
            case 6:
                print('Gracias por usar el sistema :)')
                fin = False
            case _:
                print('Opcion invalida ')

    except ValueError:
        print('Ingreso un dato incorrecto vuelva a intentarlo ..... \n\n')
