# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''chatbot
from nltk.chat.util import Chat, reflections

# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''inicializar la ruta
# datos para el entrenamiento del chatbot
mis_reflexions = {}
pares = []


def initdatares():

    global mis_reflexions
    global pares

    mis_reflexions = {
        "ir": "fui",
        "hola": "hey",
        "caido": "cayo",
        "cayo": "caido"
    }
    # r"(.*) metodos (.*) publicar (.*)|" -> Emisor o lo que enviara el usuario
    # r"(.*) metodos (.*) publicar (.*)|" -> Emisor o lo que enviara el usuario
    pares = [
        # [
        #    r"(.*) metodos (.*) publicar (.*)|",
        #    ["Tenemos el metodo particular o profecional", ]
        # ],
        # pepito 58
        [
            r"Hola (.*)|Hola",
            ["Hola, en que podemos ayudarte.....", ]
        ]
    ]


def conversacionbot(messeg):
    # print(mis_reflexions)
    # print(pares)
    chat = Chat(pares, mis_reflexions)
    # Ingresar los datos para que de una respuesta el bot segun lo aprendido
    respont = chat.respond(str(messeg))
    meseg = str(respont)
    resul = {}  # captara el mensaje en forma de json
    rejson = ''  # captara el mensaje en forma de string o cadena

    if ((meseg == 'None') or (meseg == '') or (meseg == None)):
        resul['messeg'] = 'No entiendo lo que me estas escribiendo.'
    else:
        resul['messeg'] = meseg

    return resul

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
