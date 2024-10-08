import tkinter as tk

def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea != "":
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)

def eliminar_tarea():
    try:
        tarea_seleccionada = lista_tareas.curselection()
        lista_tareas.delete(tarea_seleccionada)
    except:
        pass

def marcar_completada():
    try:
        tarea_seleccionada = lista_tareas.curselection()
        tarea = lista_tareas.get(tarea_seleccionada)
        lista_tareas.delete(tarea_seleccionada)
        lista_tareas.insert(tk.END, f"{tarea} - Completada")
    except:
        pass

root = tk.Tk()
root.title("Aplicación de Lista de Tareas")
root.geometry("400x400")

# Widgets
titulo = tk.Label(root, text="Lista de Tareas", font=("Helvetica", 16))
entrada_tarea = tk.Entry(root, width=30)
lista_tareas = tk.Listbox(root, width=30, height=10)
boton_agregar = tk.Button(root, text="Añadir Tarea", command=agregar_tarea)
boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
boton_completar = tk.Button(root, text="Marcar como Completada", command=marcar_completada)

# Layout
titulo.pack(pady=10)
entrada_tarea.pack(pady=10)
boton_agregar.pack(pady=10)
lista_tareas.pack(pady=10)
boton_eliminar.pack(pady=10)
boton_completar.pack(pady=10)

root.mainloop()
#Tuve que ver en foros y aclarar dudas con chatGPT del correcto funcionamiento, ya que al intentar hacerlo en distintos archivos e importarlos al main, no me dejaba. Así que quedó todo en el main