from flask import Flask, jsonify, request, render_template, current_app
from unipath import Path
from datetime import datetime
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''ApiWhatsaap
import requests
import json
from heyoo import WhatsApp
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''chatbot
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''inicializar la ruta
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

    pares = [
        #[
        #    r"(.*) metodos (.*) publicar (.*)|",
        #    ["Tenemos el metodo particular o profecional", ]
        #],
        [
            r"Hola (.*)|Hola",
            ["Hola, en que podemos ayudarte.....", ]
        ]
    ]

initdatares()

def conversacionbot(messeg):
    #print(mis_reflexions)
    #print(pares)
    chat = Chat(pares, mis_reflexions)
    # chat.converse()
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

#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
@app.before_request
def log_requests():
    print("Debug log level")

#inicializar la ruta
@app.route("/", methods =["POST", "GET"])
def index():
    print('Arranque de la aplicacion')
    return jsonify({"status": "success","messege": "Conexion satisfactoriamente."}, 200)

# https://developers.facebook.com/docs/whatsapp/api/messages/text
#def sendMessegeWhatsaap(messege):
#    token = "EAANMM1aAZBp4BAGHGZB8v4GrTfn3s7B5YbIlj0SLWs6yZA4n1jKB6EdZA2Tg2futo7qhUjtufwLvGi9FRYovf4FwJ80S6LzYWNCiiC93nkN3rI29pzmj8XqJnQJtQ5K29cp62oh8w9Lb1hk0M7cCdGYCLXW0t53l6p0KjErivy1vyerbmfmMdBE41jObartJkjqwZAc8kTwZDZD"
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
def sendMessegeWhatsaapp(messege):
    #TOKEN DE ACCESO DE FACEBOOK
    token = "EAANMM1aAZBp4BAAHBJZBNHvJnXHXQondzBMnQJ9ypUhaaIi0K3CheKEgiKHfTw8uYnPgZAviYe3JyQdIUDEmnqZA2VRGkIjohxWl8dfs2dDFhQlXWwuoRzhbWkgZCYtXNgqSjbIZCIU7ytN7VEGKiXXANVrYv5h9zkucD1t4kIIUr7cIqODwdlWeN8psTjN0qB0eVrQicqcxTAQuFH1sXbKbWo66Ra3agZD"
    #IDENTIFICADOR DE NÚMERO DE TELÉFONO
    idNumeroTeléfono = '116250248175966'
    #TELEFONO QUE RECIBE (EL DE NOSOTROS QUE DIMOS DE ALTA)
    telefonoEnvia='51997585922'
    #MENSAJE A ENVIAR
    textoMensaje = messege
    #'''''''''''''''''''''''''''''''''''''''''''' Enviamos el mensaje
    #INICIALIZAMOS ENVIO DE MENSAJES
    mensajeWa=WhatsApp(token,idNumeroTeléfono)
    #ENVIAMOS UN MENSAJE DE TEXTO
    mensajeWa.send_message(textoMensaje,telefonoEnvia)

#cuando recibimos las peticiones en esta ruta
@app.route("/webhook/", methods =["POST", "GET"])
def webhook_whatsapp():
    #Si hay datos recibimos via get
    if request.method == "GET":
        #Si el toke es igual al que recibimos
        #hub.verify_token
        #print(request.args)
        if request.args.get('hub.verify_token') == "HolaAlvarezBohl":
            #Escribimos en el navegador
            #hub.challenge
            return request.args.get('hub.challenge') 
        else:
            return "Error de autenticación."
    #print(request.get_json())
    #RECIBIMOS TODOS LOS DATOS ENVIADO VIA JSON
    data = request.get_json()
    #EXTRAEMOS EL NUMERO DE TELEFONO Y EL MANSAJE
    telefonoCliente = data ['entry'][0]['changes'][0]['value']['messages'][0]['from']
    #EXTRAEMOS EL TELEFONO DEL CLIENTE
    mensajes = data ['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
    #EXTRAEMOS EL ID DE WHATSAPP DEL ARRAY
    idWA = data ['entry'][0]['changes'][0]['value']['messages'][0]['id']
    #EXTRAEMOS EL TIEMPO DE WHATSAPP DEL ARRAY
    timestamp = data ['entry'][0]['changes'][0]['value']['messages'][0]['timestamp']
    #ESCRIBIMOS EL NUMERO DE TELEFONO Y EL MENSAJE EN EL ARCHIVO TEXTO
    #SI HAY UN MENSAJE
    #if mensajes is not None:
    #    print({"mensajes": mensajes,"telefonoCliente": telefonoCliente,"idWA": idWA,"timestamp": timestamp})
    #    respuesta = conversacionbot(mensajes)
    #    print(respuesta)
    #    # bot = RiveScript()
    #    # bot.sort_replies()
    #    # bot.load_file('./distribuidoraab.rive')
    #    # respuesta = bot.reply("localuser", mensajes)
    #    # print(respuesta)
    #    # respuesta = bot.reply("localuser", mensajes)
    #    # respuesta = respuesta.replace("\\n","\\\n")
    #    # respuesta = respuesta.replace("\\","")

        # f = open("texto.txt", "w")
        # f.write(mensajes)
        # f.close()
        # return jsonify({"status": "success"}, 200)
    #mensajes = request.args.get('messege')
    #telefonoCliente = '00000000000'
    
    response = conversacionbot(mensajes)
    sendMessegeWhatsaapp(response['messeg'])
    # historial de peticiones al chatbot
    fe = Path('./text.txt')
    if (fe.exists()) :
        with open("text.txt","a") as filetextw:
            fechaActual = datetime.now()
            fechaFormat = datetime.strftime(fechaActual,'%b %d %Y %H:%M:%S')
            historyFormat = "time: {0}|telefonoCliente: {1}|messege: {2}|response: {3}".format(fechaFormat,telefonoCliente, mensajes,response['messeg'])
            filetextw.write(historyFormat)
            
        with open("text.txt","r") as filetext:
            for line in filetext:
                print(line)

    return jsonify({"status": "success"}, 200)

if __name__ == "__main__":
    app.run(debug = true)
