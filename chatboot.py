# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''chatbot
from nltk.chat.util import Chat, reflections
from unipath import Path

# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''inicializar la ruta
# datos para el entrenamiento del chatbot
mis_reflexions = {}
pares = []


def load_conver_data():
    paresAux = []
    fe = Path('./conversation.txt')
    if (fe.exists()):
        with open("conversation.txt", "r") as filetext:
            positAnalis = -1
            itemAux = []
            for line in filetext:
                # recorre todas las lineas
                if (line[0] == '+'):
                    itemAux = []
                    positAnalis = positAnalis + 1
                    # Ingreso del input
                    input = line[1:]
                    itemAux = [input.replace("\n", ""), []]
                    paresAux.append(itemAux)
                else:
                    # Ingresa los ouput.
                    ouput = line[1:]
                    itemAux[1].append(ouput.replace("\n", ""))
                    paresAux[positAnalis] = itemAux
    return paresAux


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
    # print(load_conver_data())
    pares = load_conver_data()
    # pares = [
    #     # [
    #     #    r"(.*) metodos (.*) publicar (.*)|",
    #     #    ["Tenemos el metodo particular o profecional", ]
    #     # ],
    #     # pepito 58
    #     [
    #         "Hola (.*)|Hola",
    #         ["Hola, en que podemos ayudarte.....", ]
    #     ],
    #     [
    #         "Ayuda (.*)|Ayuda",
    #         ["Que consulta tienes para nosotros: !- No se como pagar. !- No entiendo una operacion", ]
    #     ],
    #     [
    #         "Contacto (.*)|Contacto",
    #         ["Se puede contactarnos con nosotros.", ]
    #     ]
    # ]


def conversacionbot(messeg):
    # print(mis_reflexions)
    # print(pares)
    chat = Chat(pares, mis_reflexions)
    # Ingresar los datos para que de una respuesta el bot segun lo aprendido
    respont = chat.respond(str(messeg).lower())
    meseg = str(respont)
    resul = {}  # captara el mensaje en forma de json
    rejson = ''  # captara el mensaje en forma de string o cadena

    if ((meseg == 'None') or (meseg == '') or (meseg == None)):
        resul['messeg'] = 'No entiendo lo que me estas escribiendo.'
    else:
        resul['messeg'] = meseg
    # si hay saltos de linea, los da, sino imprime talcual
    if ("!" in resul['messeg']):
        resul['messeg'] = resul['messeg'].replace("!", "\n")
        return resul
    else:
        return resul

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
