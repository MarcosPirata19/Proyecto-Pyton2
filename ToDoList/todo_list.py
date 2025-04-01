tareas = []

def mostrar_tareas(): # Corrección: sin espacios al principio
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("Tareas:")
        for indice, tarea in enumerate(tareas):
            print(f"{indice + 1}. {tarea}")

def agregar_tarea(tarea):
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada.")

def eliminar_tarea(indice):
    if 1 <= indice <= len(tareas):
        tarea_eliminada = tareas.pop(indice - 1)
        print(f"Tarea '{tarea_eliminada}' eliminada.")
    else:
        print("Índice de tarea inválido.")

# Menu principal.
while True:
    print("\nOpciones:")
    print("1. Mostrar tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_tareas()
    elif opcion == "2":
        tarea = input("Introduce la nueva tarea: ")
        agregar_tarea(tarea)
    elif opcion == "3":
        indice = int(input("Introduce el índice de la tarea a eliminar: "))
        eliminar_tarea(indice)
    elif opcion == "4":
        break
    else:
        print("Opción inválida. Inténtalo de nuevo.")

print("¡Hasta luego!")