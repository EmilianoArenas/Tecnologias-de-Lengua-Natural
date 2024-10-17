class CalculadoraChatbot:
    def __init__(self):
        pass

    def explicar(self, operacion, a, b, resultado):
        if operacion == "suma":
            return f"Si tienes {a} cosas y luego consigues {b} más, entonces ahora tienes {resultado} cosas en total."
        elif operacion == "resta":
            return f"Si tienes {a} cosas y le quitas {b}, entonces te quedas con {resultado} cosas."
        elif operacion == "multiplicacion":
            return f"Multiplicar es como sumar muchas veces. Si tienes {a} grupos con {b} cosas en cada grupo, en total tendrás {resultado} cosas."
        elif operacion == "division":
            if b == 0:
                return "No se puede dividir entre cero, es como intentar repartir nada entre amigos."
            return f"Dividir es como repartir. Si tienes {a} cosas y las repartes entre {b} amigos, cada uno recibirá {resultado} cosas."

    def sumar(self, a, b):
        resultado = a + b
        explicacion = self.explicar("suma", a, b, resultado)
        return explicacion

    def restar(self, a, b):
        resultado = a - b
        explicacion = self.explicar("resta", a, b, resultado)
        return explicacion

    def multiplicar(self, a, b):
        resultado = a * b
        explicacion = self.explicar("multiplicacion", a, b, resultado)
        return explicacion

    def dividir(self, a, b):
        if b == 0:
            return "No se puede dividir entre cero. Imagina que intentas repartir algo entre nadie, no tiene sentido."
        resultado = a / b
        explicacion = self.explicar("division", a, b, resultado)
        return explicacion

    def resolver(self, operacion, a, b):
        if operacion == "suma":
            return self.sumar(a, b)
        elif operacion == "resta":
            return self.restar(a, b)
        elif operacion == "multiplicacion":
            return self.multiplicar(a, b)
        elif operacion == "division":
            return self.dividir(a, b)
        else:
            return f"Operación '{operacion}' no soportada."

    def iniciar(self):
        print("Hola! Soy tu calculadora inteligente. Vamos a aprender matemáticas juntos.")
        
        while True:
            operacion = input("¿Qué operación deseas hacer? (suma, resta, multiplicacion, division) o escribe 'salir' para terminar: ").lower()
            if operacion == "salir":
                print("Gracias por jugar conmigo! ¡Hasta pronto!")
                break

            try:
                a = float(input("Introduce el primer número (a): "))
                b = float(input("Introduce el segundo número (b): "))
            except ValueError:
                print("Ups, parece que eso no es un número. Vamos a intentarlo otra vez.")
                continue

            resultado = self.resolver(operacion, a, b)
            print(resultado)
            print("-" * 40)

# Ejecutar el chatbot
calculadora = CalculadoraChatbot()
calculadora.iniciar()
