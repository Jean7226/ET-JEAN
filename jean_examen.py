
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
'123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
'342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050']
}
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]
}

def stock_marca(marca):
    total = 0
    for codigo, datos in productos.items():
        if datos[0].lower() == marca.lower():
             if codigo in stock:
                 total += stock[codigo][1]
    print(f"El stock total para {marca} es: {total} ")

def búsqueda_precio(precio_min, precio_max):
    resultado = []
    for codigo, datos in productos.items():
        precio = datos[0]
        if precio >= precio_min and precio_max and stock[codigo][1] > 0:
            resultado.append(codigo + '--' + datos[2])
    if resultado:
        resultado.sort()
        print("producto encontrado: ", resultado)
    else:
        print("no hay producto con ese rango de precio.")

def ordenar_productos():
    listadoproductos = []
    i = 0
    for codigo, datos in productos.items():
       orden = datos[0]+ '--' + codigo+ '--'+ datos[2]+'--'+ datos[4]
       listadoproductos.append(orden)
    print("------- Listado de Notebooks Ordenados --------")
    for a in listadoproductos:
       print(f"{listadoproductos[i]}")
       i += 1

def main():
    while True:
        print("*****menu principal*****")
        print("Stock marca.")
        print("Búsqueda por precio.")
        print("Listado de productos.")
        print("Salir.")
        try:
            opc = int(input("ingrese opcion: "))
            if opc == 1:
                marca = input("ingrese una marca: ")
                stock_marca(marca)
            elif opc == 2:
                while True:
                    try:
                        precio_max = int(input("ingrese la cantidad maxima de precio: "))
                        precio_min = int(input("ingrese la cantidad minima de precio: "))
                        búsqueda_precio(precio_min, precio_max)
                    except ValueError:
                        print("el valor ingresado debe ser entero")
            elif opc == 3:
                ordenar_productos()
             
            elif opc == 4:
                print("programa finalizado.")
                break
            else:
                print("debe seleccionar una opcion valida!!!")


        except ValueError:
            print("opcion no valida")
        print("")

        
if __name__ == "__main__":
    main()



