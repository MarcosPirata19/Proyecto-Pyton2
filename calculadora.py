"""Este módulo contiene funciones para realizar operaciones matemáticas básicas."""

import tkinter as tk


def sumar(a, b):
    """Suma dos números."""
    return a + b


def restar(a, b):
    """Resta dos números."""
    return a - b


def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b


def dividir(a, b):
    """Divide dos números. Maneja la división por cero."""
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b


def main():
    ventana = tk.Tk()
    ventana.title("Calculadora Gráfica")

    # Pantalla de visualización
    pantalla = tk.Entry(ventana, width=35, borderwidth=5)
    pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Variables para almacenar el primer número y la operación
    primer_numero = 0
    operacion = ""

    # Función para manejar los clics de los botones numéricos y la entrada del teclado
    def boton_click(numero):
        actual = pantalla.get()
        if numero == "." and "." in actual:
            return  # No permite agregar más de un punto decimal
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str(actual) + str(numero))

    # Función para manejar los clics de los botones de operación y la entrada del teclado
    def boton_operacion(op):
        nonlocal primer_numero, operacion
        primer_numero = float(pantalla.get())
        operacion = op
        pantalla.delete(0, tk.END)

    # Función para manejar el clic del botón "=" y la entrada del teclado
    def boton_igual():
        nonlocal primer_numero, operacion
        segundo_numero = float(pantalla.get())
        if operacion == "+":
            resultado = sumar(primer_numero, segundo_numero)
        elif operacion == "-":
            resultado = restar(primer_numero, segundo_numero)
        elif operacion == "*":
            resultado = multiplicar(primer_numero, segundo_numero)
        elif operacion == "/":
            resultado = dividir(primer_numero, segundo_numero)
        else:
            resultado = "Error"
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str(resultado))

    def boton_borrar():
        """Borra el último carácter de la pantalla."""
        actual = pantalla.get()
        pantalla.delete(len(actual) - 1, tk.END)

    def boton_limpiar():
        """Borra todo el contenido de la pantalla y restablece las variables."""
        global primer_numero, operacion
        pantalla.delete(0, tk.END)
        primer_numero = 0
        operacion = ""

    # Botones numéricos
    boton_1 = tk.Button(
        ventana, text="1", padx=40, pady=20, command=lambda: boton_click(1)
    )
    boton_2 = tk.Button(
        ventana, text="2", padx=40, pady=20, command=lambda: boton_click(2)
    )
    boton_3 = tk.Button(
        ventana, text="3", padx=40, pady=20, command=lambda: boton_click(3)
    )
    boton_4 = tk.Button(
        ventana, text="4", padx=40, pady=20, command=lambda: boton_click(4)
    )
    boton_5 = tk.Button(
        ventana, text="5", padx=40, pady=20, command=lambda: boton_click(5)
    )
    boton_6 = tk.Button(
        ventana, text="6", padx=40, pady=20, command=lambda: boton_click(6)
    )
    boton_7 = tk.Button(
        ventana, text="7", padx=40, pady=20, command=lambda: boton_click(7)
    )
    boton_8 = tk.Button(
        ventana, text="8", padx=40, pady=20, command=lambda: boton_click(8)
    )
    boton_9 = tk.Button(
        ventana, text="9", padx=40, pady=20, command=lambda: boton_click(9)
    )
    boton_0 = tk.Button(
        ventana, text="0", padx=40, pady=20, command=lambda: boton_click(0)
    )
    # Botón para el punto decimal
    boton_punto = tk.Button(
        ventana, text=".", padx=41, pady=20, command=lambda: boton_click(".")
    )

    # Botones de operaciones
    boton_suma = tk.Button(
        ventana, text="+", padx=39, pady=20, command=lambda: boton_operacion("+")
    )
    boton_resta = tk.Button(
        ventana, text="-", padx=41, pady=20, command=lambda: boton_operacion("-")
    )
    boton_multi = tk.Button(
        ventana, text="*", padx=39, pady=20, command=lambda: boton_operacion("*")
    )
    boton_division = tk.Button(
        ventana, text="/", padx=41, pady=20, command=lambda: boton_operacion("/")
    )
    boton_igual = tk.Button(ventana, text="=", padx=40, pady=60, command=boton_igual)

    # Botones de borrar y limpiar
    boton_borra = tk.Button(
        ventana, text="Borrar", padx=39, pady=20, command=boton_borrar
    )
    boton_limpia = tk.Button(
        ventana, text="Limpiar", padx=41, pady=20, command=boton_limpiar
    )

    # Colocar los botones en la cuadrícula
    boton_1.grid(row=1, column=0)
    boton_2.grid(row=1, column=1)
    boton_3.grid(row=1, column=2)
    boton_4.grid(row=2, column=0)
    boton_5.grid(row=2, column=1)
    boton_6.grid(row=2, column=2)
    boton_7.grid(row=3, column=0)
    boton_8.grid(row=3, column=1)
    boton_9.grid(row=3, column=2)
    boton_0.grid(row=4, column=0)
    boton_punto.grid(row=4, column=2)
    boton_suma.grid(row=4, column=1)
    boton_resta.grid(row=4, column=2)
    boton_multi.grid(row=5, column=0)
    boton_division.grid(row=5, column=1)
    boton_igual.grid(row=5, column=2, rowspan=2)

    # Colocar los botones en la cuadrícula
    # ... (resto de los botones)
    boton_borra.grid(row=6, column=0)
    boton_limpia.grid(row=6, column=1)

    # Asociar eventos de teclado
    ventana.bind("<Key-1>", lambda event: boton_click(1))
    ventana.bind("<Key-2>", lambda event: boton_click(2))
    ventana.bind("<Key-3>", lambda event: boton_click(3))
    ventana.bind("<Key-4>", lambda event: boton_click(4))
    ventana.bind("<Key-5>", lambda event: boton_click(5))
    ventana.bind("<Key-6>", lambda event: boton_click(6))
    ventana.bind("<Key-7>", lambda event: boton_click(7))
    ventana.bind("<Key-8>", lambda event: boton_click(8))
    ventana.bind("<Key-9>", lambda event: boton_click(9))
    ventana.bind("<Key-0>", lambda event: boton_click(0))
    ventana.bind("<plus>", lambda event: boton_operacion("+0"))
    ventana.bind("<minus>", lambda event: boton_operacion("-"))
    ventana.bind("<asterisk>", lambda event: boton_operacion("*"))
    ventana.bind("<slash>", lambda event: boton_operacion("/"))
    ventana.bind("<Return>", lambda event: boton_igual)

    ventana.mainloop()


if __name__ == "__main__":
    main()
