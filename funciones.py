from validaciones import *

def menu()->str:
  """
  Imprime el menú en pantalla

  Returns:
      input: para seleccionar la opción que querramos
  """
  
  print(f"{'Menú de opciones':^50}")
  print("1 - Agregar producto al inventario")
  print("2 - Realizar una venta")
  print("3 - Mostrar inventario")
  print("4 - Salir")

  return input("Ingrese opción: ")

def agregar_producto():
  nuevo_producto = []
  
  producto = input("Ingrese nombre del producto: ").title()
  nuevo_producto.append(producto)
  
  cantidad = input("Ingrese la cantidad: ")
  nuevo_producto.append(validar_entero(cantidad))
  
  precio = input("Ingrese el precio del producto: ")
  nuevo_producto.append(validar_entero(precio))

  return nuevo_producto

def realizar_venta(inventario, producto_a_comprar, cantidad_a_comprar, disponible=False):
  for producto in inventario:
    for _ in producto:
      nombre = producto[0]

      if producto_a_comprar == nombre.lower():
        disponible = True
        cantidad = producto[1]
        precio = producto[2]
        
        if cantidad == 0:
          print("No hay stock")
          break

        elif cantidad < cantidad_a_comprar:
          print("No se puede realizar la venta")
          break

        else:
          print(f"El total a pagar es de ${cantidad_a_comprar * precio}")
          producto[1] -= cantidad_a_comprar
          break
  
  if disponible == False:
    print("No existe ese producto en nuestro inventario")