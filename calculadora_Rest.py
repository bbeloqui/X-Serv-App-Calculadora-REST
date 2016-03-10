#!/usr/bin/python
# -*- coding: utf-8 -*


import webapp
import random


class calculadora(webapp.webApp):

    def parse(self, request):
        verb = request.split()[0]
        recurso = request.split()[1].split("/")[1]
        cuerpo = request.split("\r\n\r\n")[1]
        return (verb,recurso,cuerpo)


    def process(self, parsedRequest):
        (verb, recurso, cuerpo)=parsedRequest
        if verb == "GET":
            try:
                if len(self.operacion.split("+")) == 2:
                    suma = float(self.operacion.split("+")[0]) + float(self.operacion.split("+")[1])
                    return ("200 OK", "<html><body><p>Suma: " + str(suma) + "</p></body></html>")
                if len(self.operacion.split("-")) == 2:
                    resta = float(self.operacion.split("-")[0]) - float(self.operacion.split("-")[1])
                    return ("200 OK", "<html><body><p>Resta: " + str(resta) + "</p></body></html>")
                if len(self.operacion.split("*")) == 2:
                    suma = float(self.operacion.split("*")[0]) * float(self.operacion.split("*")[1])
                    return ("200 OK", "<html><body><p>Multiplicacion: " + str(suma) + "</p></body></html>")
                if len(self.operacion.split("/")) == 2:
                    division = float(self.operacion.split("/")[0]) / float(self.operacion.split("/")[1])
                    return ("200 OK", "<html><body><p>Division: " + str(division) + "</p></body></html>")
            except AttributeError:
                #Todavia no se ha iniciado self.operacion
                return ("404 Not Found", "<html><body><p>Introduce primero la operacion con el PUT</p></body></html>")
            except ValueError:
                #Operacion con algun fallo
                return ("404 Not Found", "<html><body><p>La operacion no es correcta</p></body></html>")

        elif verb == "PUT":
            self.operacion = cuerpo
            print self.operacion
            return ("200 OK", "<html><body><p>La operacion es " + cuerpo + "</p></body></html>")

if __name__ == "__main__":
    servaleat = calculadora("localhost", 1234)
