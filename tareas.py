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
