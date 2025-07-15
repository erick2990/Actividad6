from PIL.features import version_feature
from babel.dates import match_skeleton

Cod = {}

fin = True

def agregar():
    codigos = ["J", "P", "B","S"]

    print('Funcion para añadir productos: ')
    print('Inicio de codigo clave: J= Pantalones P = Playeras B = Blusas S = Sueter')
    cantidad = int(input('Ingrese la cantidad de prendas que desea añadir: '))
    for i in range(cantidad):
        cod_prenda = input(f'Ingrese el codigo de {i+1} prenda: ').upper() #se recibe el codigp de prenda para ser añadido

        if cod_prenda[0] not in codigos:
            print('Codigo invalido por favor intentelo de nuevo')
            continue

        nombre_producto = input('Nombre del producto: ')
        categoria = input('H=Hombre, M=mujer y N=niño: ').upper()
        talla = input('Ingrese la talla S/M/L/XL: ').upper()
        precio = float(input('Ingrese el precio de la prenda: '))
        stock_r = int(input('Ingrese la existencia de prendas: '))

        # Diccionario que contiene codigo  todos los atributos
        Cod[cod_prenda] = {
            "Nombre": nombre_producto,
            "Categoria": categoria,
            "Talla": talla,
            "Precio": precio,
            "Stock": stock_r
        }



def view_items():
    print('Productos disponibles')

    if not Cod:
        print('No hay productos disponibles aún')

    else:
        for prop, camp in Cod.items():
            print(prop, ' : ', camp)


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
