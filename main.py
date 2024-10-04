from validaciones import *
from funciones import *

"""
Mostrar una lista de productos disponibles (nombre, precio y cantidad). #Si cantidad > 0 
• El usuario podrá seleccionar un producto y la cantidad que desea comprar. 
• Verificar que haya suficiente stock del producto seleccionado. 
• Restar la cantidad comprada del inventario. 
• Mostrar el total a pagar al cliente por la venta. 
• Si no hay suficiente stock, mostrar un mensaje que indique que no se puede 
realizar la venta. #Si cantidad_a_comprar < cantidad
"""

inventario = [
  ["Chupetin Sable de Luz", 50, 200],
  ["Agua La Fuerza", 35, 3200],
  ["Gomitas Holocubo", 25, 990],
  ["Barrita de Cereal Wookie", 48, 2500],
  ["Galletitas R2D2", 25, 15800],
]

def mostrar_inventario(inventario, titulo, solo_disponbiles = False):
  print(f" {titulo:^65} ")
  print(f"{'Producto':^30} {'Cantidad':^25} {'Precio':^15}")
  print("------------------------------------------------------------------------")
  for producto in inventario:
    for _ in producto:
      nombre = producto[0]
      cantidad = producto[1]
      precio = producto[2]
    if solo_disponbiles == True:
      if cantidad > 0:
        print(f"{nombre:^30} {cantidad:^25} {precio:^15}")
    else:
       print(f"{nombre:^30} {cantidad:^25} {precio:^15}")
  print("------------------------------------------------------------------------")

respuesta = "no"
while respuesta == "no":
  match menu():
    case "1":
      inventario.append(agregar_producto())

    case "2":
      mostrar_inventario(inventario, "PRODUCTOS EN STOCK", solo_disponbiles=True)
      
      flag_producto = False
      producto_a_comprar = input("Ingrese el producto a comprar: ").lower()
      
      cantidad_a_comprar = input("Ingrese la cantidad que desea comprar: ")
      
      
      realizar_venta(inventario, producto_a_comprar, validar_entero(cantidad_a_comprar))      

    case "3":
      mostrar_inventario(inventario, "LISTADO DE PRODUCTOS")  
    
    case "4":
      respuesta = input("¿Está seguro que desea salir? (si/no): ")

    case _:
      print("Ingrese una opción correcta")