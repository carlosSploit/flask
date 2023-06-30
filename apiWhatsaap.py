# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''ApiWhatsaap
import requests
import json
from heyoo import WhatsApp
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''env
import os


def sendMessegeWhatsaapp(messege, telefonoCliente):
    # TOKEN DE ACCESO DE FACEBOOK
    token = os.getenv('TOKEN')
    # IDENTIFICADOR DE NÚMERO DE TELÉFONO
    idNumeroTeléfono = os.getenv('IDWHATSAPP')
    # TELEFONO QUE RECIBE (EL DE NOSOTROS QUE DIMOS DE ALTA)
    telefonoEnvia = telefonoCliente
    # MENSAJE A ENVIAR
    textoMensaje = messege
    # '''''''''''''''''''''''''''''''''''''''''''' Enviamos el mensaje
    # INICIALIZAMOS ENVIO DE MENSAJES
    mensajeWa = WhatsApp(token, idNumeroTeléfono)
    # ENVIAMOS UN MENSAJE DE TEXTO
    mensajeWa.send_message(textoMensaje, telefonoEnvia)
