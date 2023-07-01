from flask import Flask, jsonify, request, render_template, current_app
import chatboot as ctt
import apiWhatsaap as apwha
import history as hist
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
ctt.initdatares()

# # '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''inicializar la ruta
# # datos para el entrenamiento del chatbot
# mis_reflexions = {}
# pares = []


# def initdatares():

#     global mis_reflexions
#     global pares

#     mis_reflexions = {
#         "ir": "fui",
#         "hola": "hey",
#         "caido": "cayo",
#         "cayo": "caido"
#     }

#     pares = [
#         # [
#         #    r"(.*) metodos (.*) publicar (.*)|",
#         #    ["Tenemos el metodo particular o profecional", ]
#         # ],
#         # pepito 58
#         [
#             r"Hola (.*)|Hola",
#             ["Hola, en que podemos ayudarte.....", ]
#         ]
#     ]


# initdatares()


# def conversacionbot(messeg):
#     # print(mis_reflexions)
#     # print(pares)
#     chat = Chat(pares, mis_reflexions)
#     # chat.converse()
#     # Ingresar los datos para que de una respuesta el bot segun lo aprendido
#     respont = chat.respond(str(messeg))
#     meseg = str(respont)
#     resul = {}  # captara el mensaje en forma de json
#     rejson = ''  # captara el mensaje en forma de string o cadena

#     if ((meseg == 'None') or (meseg == '') or (meseg == None)):
#         resul['messeg'] = 'No entiendo lo que me estas escribiendo.'
#     else:
#         resul['messeg'] = meseg

#     return resul

# # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# @app.before_request
# def log_requests():
#     print("Debug log level")
# inicializar la ruta

@app.route("/", methods=["POST", "GET"])
def index():
    # print(os.getenv('TOKEN'))
    # print(os.getenv('IDWHATSAPP'))
    # print('Arranque de la aplicacion')
    return jsonify({"status": "success", "messege": "Conexion satisfactoriamente."}, 200)

# https://developers.facebook.com/docs/whatsapp/api/messages/text
# def sendMessegeWhatsaap(messege):
#    token = os.getenv('TOKEN')
#    headeToken = "Bearer {0}".format(token)
#    print(headeToken)
#    url = "https://graph.facebook.com/v17.0/116250248175966/messages"
#    headers = {"Authorization": headeToken,"Content-Type": "application/json;"}
#    print(headers)
#    data = {
#        "messaging_product": "whatsapp",
#        "to": "51997585922",
#        "type": "text",
#        "text": {
#            "body": messege
#        }
#    }
#    print("JSON", data)
#    response = requests.post(url, headers=headers, json=data)
#    print("JSON Response ", response.json())
#    print("Status Code", response.status_code)

# Libreria Heyoo


# def sendMessegeWhatsaapp(messege):
#     # TOKEN DE ACCESO DE FACEBOOK
#     token = os.getenv('TOKEN')
#     # IDENTIFICADOR DE NÚMERO DE TELÉFONO
#     idNumeroTeléfono = os.getenv('IDWHATSAPP')
#     # TELEFONO QUE RECIBE (EL DE NOSOTROS QUE DIMOS DE ALTA)
#     telefonoEnvia = '51997585922'
#     # MENSAJE A ENVIAR
#     textoMensaje = messege
#     # '''''''''''''''''''''''''''''''''''''''''''' Enviamos el mensaje
#     # INICIALIZAMOS ENVIO DE MENSAJES
#     mensajeWa = WhatsApp(token, idNumeroTeléfono)
#     # ENVIAMOS UN MENSAJE DE TEXTO
#     mensajeWa.send_message(textoMensaje, telefonoEnvia)

# cuando recibimos las peticiones en esta ruta


@app.route("/webhook/", methods=["POST", "GET"])
def webhook_whatsapp():
    # Si hay datos recibimos via get
    if request.method == "GET":
        # Si el toke es igual al que recibimos
        # hub.verify_token
        # print(request.args)
        if request.args.get('hub.verify_token') == "HolaAlvarezBohl":
            # Escribimos en el navegador
            # hub.challenge
            print(request.args.get('hub.challenge'))
            return request.args.get('hub.challenge')
        else:
            return "Error de autenticación."
    # print(request.get_json())
    # RECIBIMOS TODOS LOS DATOS ENVIADO VIA JSON
    data = request.get_json()
    # COMPRUEBA SI EL MENSAJE EXISTE DENTRO DE LO QUE ENVIA EL SERVIDOR
    if 'messages' in data['entry'][0]['changes'][0]['value']:
        print(data)
        # EXTRAEMOS EL NUMERO DE TELEFONO Y EL MANSAJE
        telefonoCliente = data['entry'][0]['changes'][0]['value']['messages'][0]['from']
        # EXTRAEMOS EL TELEFONO DEL CLIENTE
        mensajes = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
        # EXTRAEMOS EL ID DE WHATSAPP DEL ARRAY
        idWA = data['entry'][0]['changes'][0]['value']['messages'][0]['id']
        # EXTRAEMOS EL TIEMPO DE WHATSAPP DEL ARRAY
        timestamp = data['entry'][0]['changes'][0]['value']['messages'][0]['timestamp']
        # ESCRIBIMOS EL NUMERO DE TELEFONO Y EL MENSAJE EN EL ARCHIVO TEXTO
        # SI HAY UN MENSAJE

        response = ctt.conversacionbot(mensajes)

        if (hist.isUserHistory(telefonoCliente)):
            response['messeg'] = 'Bienvenido al chatbo, parece ser que es tu primera interaccion. Escribe ´hola´ para empezar con la interaccion.'

        apwha.sendMessegeWhatsaapp(response['messeg'], telefonoCliente)
        # historial de peticiones al chatbot
        hist.historyPeticion(telefonoCliente, mensajes, response)

    return jsonify({"status": "success"}, 200)


if __name__ == "__main__":
    app.run(debug=True)
