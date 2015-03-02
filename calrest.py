#!/usr/bin/python


import webapp #para importar el webapp


class servidor(webapp.webApp):   #va a separar lo que va arriba
	def parse(self, request):
		opcion = request.split()[0]
		recuerso = request.split()[1].split("/")[1] #coge lo segundo hasta la siguiente barra
		dato = request.split()[-1] #coge el resto
		return(opcion, recurso, dato)

	def process(self, parsedRequest):
		if (opcion == "PUT"):
			self.operacion = dato
			return ("200 OK","<html><body>Operacion"
							+ body + "</body></html>")
		elif(opcion == "GET"):
			
			if  len(self.opercion.split("+")) == 2:
				solucion = (float(self.operacion.split("+")[0]) 
							+ float(self.operacion.split("+")[1]))
				return ("200 OK", "<html><body>Solucion:  " +str(result) + "</body></html>")
			elif  len(self.opercion.split("-")) == 2:
				solucion = (float(self.operacion.split("-")[0])
							- float(self.operacion.split("-")[1]))
				return ("200 OK", "<html><body>Solucion:  " +str(result) + "</body></html>")
			elif  len(self.opercion.split("*")) == 2:
				solucion = (float(self.operacion.split("*")[0])
							* float(self.operacion.split("*")[1]))
				return ("200 OK", "<html><body>Solucion:  " +str(result) + "</body></html>")
			elif  len(self.opercion.split("/")) == 2:
				solucion = (float(self.operacion.split("/")[0])
							/ float(self.operacion.split("/")[1]))
				return ("200 OK", "<html><body>Solucion:  " +str(result) + "</body></html>")
		else:
			return ("404 Non Found","<html><body>Operacion no aceptada</body></html>")

if __name__ == "__main__":
	servaleat = servidor("localhost", 1234)










		











		
