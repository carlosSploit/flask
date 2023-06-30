from unipath import Path
from datetime import datetime


def historyPeticion(telefonoCliente, mensajes, response):
    fe = Path('./text.txt')
    if (fe.exists()):
        with open("text.txt", "a") as filetextw:
            fechaActual = datetime.now()
            fechaFormat = datetime.strftime(fechaActual, '%b %d %Y %H:%M:%S')
            historyFormat = "time: {0}|telefonoCliente: {1}|messege: {2}|response: {3}\n".format(
                fechaFormat, telefonoCliente, mensajes, response['messeg'].replace("\n", "!"))
            filetextw.write(historyFormat)

        with open("text.txt", "r") as filetext:
            for line in filetext:
                print(line)
