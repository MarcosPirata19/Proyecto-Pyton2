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
    """Función principal de la calculadora."""
    print("Calculadora Simple")
    print("Operaciones disponibles: +, -, *, /")

    try:
        num1 = float(input("Ingrese el primer número: "))
        operacion = input("Ingrese la operación (+, -, *, /): ")
        num2 = float(input("Ingrese el segundo número: "))

        if operacion == "+":
            resultado = sumar(num1, num2)
        elif operacion == "-":
            resultado = restar(num1, num2)
        elif operacion == "*":
            resultado = multiplicar(num1, num2)
        elif operacion == "/":
            resultado = dividir(num1, num2)
        else:
            resultado = "Operación no válida"

        print("Resultado:", resultado)

    except ValueError:
        print("Error: Ingrese números válidos")


if __name__ == "__main__":
    main()
