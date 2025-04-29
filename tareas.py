def agregar_tarea(lista, tarea):
 lista.append(tarea)
 return lista


def listar_tareas(lista):
 if not lista:
  print("No hay tareas pendientes.")
 else:
  print("Lista de tareas:")
  for i, tarea in enumerate(lista, start=1):
   print(f"{i}. {tarea}")

   def eliminar_tarea(lista, indice):
    if 0 <= indice < len(lista):
     eliminada = lista.pop(indice)
     print(f"Tarea eliminada: {eliminada}")
    else:
     print("Índice inválido.")
