import tkinter as tk
from tkinter import messagebox


tareas = []


def mostrar_tareas():
    lista_tareas.delete(0, tk.END)
    for tarea in tareas:
        lista_tareas.insert(tk.END, tarea)


def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        tareas.append(tarea)
        mostrar_tareas()
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Introduce una tarea.")


def eliminar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        tareas.pop(indice)
        mostrar_tareas()
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")


ventana = tk.Tk()
ventana.title("To-Do List")

frame_tareas = tk.Frame(ventana)
frame_tareas.pack(pady=10)

lista_tareas = tk.Listbox(frame_tareas, width=50, height=10)
lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar_tareas = tk.Scrollbar(frame_tareas)
scrollbar_tareas.pack(side=tk.RIGHT, fill=tk.BOTH)

lista_tareas.config(yscrollcommand=scrollbar_tareas.set)
scrollbar_tareas.config(command=lista_tareas.yview)

frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

entrada_tarea = tk.Entry(frame_entrada, width=40)
entrada_tarea.pack(side=tk.LEFT)

boton_agregar = tk.Button(frame_entrada, text="Agregar", command=agregar_tarea)
boton_agregar.pack(side=tk.LEFT)

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

boton_eliminar = tk.Button(frame_botones, text="Eliminar", command=eliminar_tarea)
boton_eliminar.pack()

ventana.mainloop()
