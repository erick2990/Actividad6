from babel.dates import match_skeleton

Cod = {}

fin = True


while fin:
    try:
        print("\r\t\tInventario de tienda de ropa: ")
        print('1. Mostrar lista de productos \r\n2. Solicitar codio de producto y existencia ')
        print('3. Calcular valor total del inventario \r\n4.Mostrar productos por categoria \r\n5. Salir')
        opcion = int(input('Ingrese el numero de opcion que deseea: '))

        match opcion:
            case 1:
            case 2:
            case 3:
            case 4:
            case 5:
            case _:
                print('Opcion invalida ')

    except ValueError:
        print('Ingreso un dato incorrecto vuelva a intentarlo ..... \n\n')
