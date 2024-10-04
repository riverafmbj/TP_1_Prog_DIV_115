def validar_entero(entero:str) -> int:
  """
  Valida que el entero sea un digito

  Args:
      entero(str): el entero a validar
  
  Returns:
      entero(int): devuelve el entero validado
  """   
  while not entero.isdigit() or int(entero) <= 0:
      entero = input(f"Error. Ingrese el dato correctamente: ")
  return int(entero)