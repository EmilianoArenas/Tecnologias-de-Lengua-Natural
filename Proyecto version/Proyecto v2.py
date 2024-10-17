palabrasClave = ['hola', 'cuanto es 5+6?', 'cuanto es 10*6?', 'cuanto es 5/6?', 'gracias']
respuestas = [
    '¡Hola! Soy tu sistema experto de soluciones de operaciones básicas, ¿En qué puedo ayudarte?', 
    'El resultado es 11. Imagina que tienes 5 manzanas en una canasta y agregas 6, ¿cuántas tenemos? Pues el resultado es 11.',
    'El resultado es 60. Si tienes 10 grupos de 6 objetos, en total tendrás 60 objetos.',
    'El resultado es aproximadamente 0.833. Es como si dividieras 5 chocolates entre 6 personas; cada uno recibiría un poco del chocolate.',
    'De nada, siempre aquí para ayudar.'
]

def responder(palabra):
    if palabra in palabrasClave:
        indice = palabrasClave.index(palabra)
        return respuestas[indice]
    else:
        return "Lo siento, no entiendo lo que dices."

print("¡Hola! Soy tu asistente virtual. Escribe 'salir' para terminar la conversación.")

while True:
    palabra = input("\nTú: ").lower()
    if palabra == 'salir':
        print("Sistema: ¡Adiós! Gracias por charlar conmigo.")
        break    
    respuesta = responder(palabra)
    print(f"Asistente: {respuesta}")