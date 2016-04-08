# Links para ejecutarlo Online  en repl.it ==>  https://repl.it/CDii
# Links para ejecutarlo Online en codeskulptor ==>  http://www.codeskulptor.org/#user41_ZCUq6srWo7_0.py
# Unefa Núcleo Mérida 
# Materia: Programación 2
class reproductor:
	encendido=False #Sirve para Encender(True) o Apagar(False) el Reproductor
	radio=True      #Sirve para cambiar a MODO RADIO
	frecuencia_FM=True #Sirve para Cambiar de Frecuencia entre FM y AM
	cd=False     #Sirve para cambiar a MODO CD
	compuerta=False   #Sirve para abrir(True) o para cerrar(False) la compuerta del Reproductor
	usb=False	#Sirve para cambiar a MODO USB
	radial_FM=100.1    #Emisora FM
	radial_AM=54.1     #Emisora AM
	volumen=0     #Sirve para Subir o bajar volumen
	vol_max=100	#Limite de volumen
	reproduciendo_cd=1   #Sirve Para cambiar de pista del CD
	reproduciendo_usb=1   #Sirve para cambiar de pista de la USB
	cds=False          #Sirve para Saber si hay un cd puesto en el reproductor
	cantidad_musica=0  #Sirve para tener la Cantidad de cansiones que tiene el CD o USB
	usb_activo=False  # Sirve para saber si hay un USB puesto en el reproductor
	Pausa=False

	def apagar(self):
		if (self.encendido== True):
			self.encendido=False
			print "Apagado"

	def encender(self):
		if (self.encendido==False):
			self.encendido=True
			print "Encendido"

	
	
	def sel_radio(self):
		if (self.encendido==True):
			self.radio=True
			self.cd=False
			self.usb=False
			print "Modo Radio"

	def cambiar_frecuencia(self):
		if (self.encendido==True):
			if (self.radio==True):
				if (self.frecuencia_FM==True):
					self.frecuencia_FM=False
					print "Se ha cambiado a la Frecuencia AM"
				else:
					if (self.frecuencia_FM==False):
						self.frecuencia_FM=True
						print "Se ha cambiado a la Frecuencia FM"
	

	def sel_cd(self):
		if (self.encendido==True):
			self.radio=False
			self.cd=True
			self.usb=False
			print "Se ha cambiado a Modo CD"

	def abrir_compuerta(self):
		if (self.encendido==True):
			if (self.cd==True):
				self.compuerta=True
				print "Compuerta Abierta puede Ingresar CD" 
	
	def cerrar_compuerta(self):
		if (self.encendido==True):
			if (self.cd==True):
				if (self.compuerta==True):
					self.compuerta=False
					print "Compuerta Cerrada"
		

	def sel_usb(self):
		if (self.encendido==True):
			self.radio=False
			self.cd=False
			self.usb=True
			print "Se ha cambiado a Modo USB"

	def subir_volumen(self):
		if (self.encendido==True):
			if (self.volumen <= self.vol_max):
				self.volumen = self.volumen + 1
				print "Se ha incrementado el volumen de 1 en 1   "
				print "El Volumen Actual es: ",self.volumen
				

	def bajar_volumen(self):
		if (self.encendido==True):
			if(self.volumen > 0):
				self.volumen = self.volumen -1
				print "Se ha disminuido el Volumen de 1 en 1   "
				print "El Volumen Actual es: ",self.volumen


	def ingresar_cd(self):
		if (self.encendido==True):
			if (self.compuerta==True):
				if (self.cds==False):
					self.cds=True
					print " CD Ingresado "

	def pausa(self):
		if (self.encendido==True):
			if (self.cd==True):
				if (self.cds==True):
					self.Pausa=True
					print "se ha pausado el CD en la Pista ",self.reproduciendo_cd
					
			if (self.usb==True):
				if (self.usb_activo==True):
					self.Pausa=True
					print "se ha pausado el USB en la pista ",self.reproduciendo_usb


	def play(self):
		if (self.encendido==True):
			if (self.cd==True):
				if (self.Pausa==True):
					self.Pausa=False
					print "Reproduciendo CD en la Pista  ",self.reproduciendo_cd
			if (self.usb==True):
				if (self.usb_activo==True):
					if (self.Pausa==True):
						self.Pausa=False
						print "Reproduciendo USB en la Pista  ",self.reproduciendo_usb
					
					
	
	def leer(self,cantidad):
		if (self.encendido==True):
			if (self.cd==True):
				if (self.compuerta==False):
					if (self.cds==True):
						self.cantidad_musica=cantidad
						print "CD listo para usar"
					if (self.cds==False):
						print "error al Leer el CD"
			if (self.usb==True):
				if (self.usb_activo==True):
					self.cantidad_musica=cantidad
					print "Dispositivo USB listo para usar"
				if (self.usb_activo==False):
					print "Error al Leer el dispositivo USB"
				
						
					
	
	def sacar_cd(self):
		if (self.encendido==True):
			if (self.compuerta==True):
				if (self.cds==True):
					self.cds=False
					print "retirar CD"	

	def ingresar_usb(self):
		if (self.encendido==True):
			if (self.usb==True):
				self.usb_activo=True
				print "USB Ingresado"
	


	def siguiente(self):
		if (self.encendido==True):

			#Radio
			if (self.radio==True):
				#Frecuencia FM
				if (self.frecuencia_FM==True):
					self.radial_FM=self.radial_FM+0.2
					print "Se ha Cambiado a la Estacion",self.radial_FM
				if (self.radial_FM > 200.1):
					self.radial_FM=84.1
					print "Se ha Cambiado a la Estacion",self.radial_FM
				
				#Frecuencia AM
				if (self.frecuencia_FM==False):
					self.radial_AM=self.radial_AM+0.2
					print "Se ha Cambiado a la Estacion",self.radial_AM
				if (self.radial_AM > 160.1):
					self.radial_AM=54.1
					print "Se ha Cambiado a la Estacion",self.radial_AM

			#CD
			if (self.cd==True):
				if (self.cds==True):
					if (self.reproduciendo_cd <  self.cantidad_musica):
						self.reproduciendo_cd=self.reproduciendo_cd+1
						print "El CD se ha Cambiado a la  Pista ",self.reproduciendo_cd
					if (self.reproduciendo_cd >= self.cantidad_musica):
						return 

			#USB
			if (self.usb==True):
				if (self.usb_activo==True):
					if (self.reproduciendo_usb >= self.cantidad_musica):
						return
					
					if (self.cantidad_musica > self.reproduciendo_usb ):
						self.reproduciendo_usb=self.reproduciendo_usb+1
						print "El USB se ha Cambiado a la  Pista  ",self.reproduciendo_usb

	
	

	def anterior(self):
		if (self.encendido==True):

			#Radio			
			if (self.radio==True):
				#Frecuencia FM
				if (self.frecuencia_FM==True):
					self.radial_FM=self.radial_FM-0.2
					print "Se ha Cambiado a la Estacion",self.radial_FM
				if (self.radial_FM < 84.1):
					self.radial_FM=200.1
					print "Se ha Cambiado a la Estacion",self.radial_FM

				#Frecuencia AM
				if (self.frecuencia_FM==False):
					self.radial_AM=self.radial_AM-0.2
					print "Se ha Cambiado a la Estacion",self.radial_AM
				if (self.radial_AM < 54.1):
					self.radial_AM=160.1
					print "Se ha Cambiado a la Estacion",self.radial_AM

			#cd
			if (self.cd==True):
				if (self.cds==True):
					if (self.reproduciendo_cd <=  self.cantidad_musica):
						self.reproduciendo_cd=self.reproduciendo_cd-1
						print "El CD se ha Cambiado a la  Pista ",self.reproduciendo_cd
					if (self.reproduciendo_cd == 0):
						return 

			#USB
			if (self.usb==True):
				if (self.usb_activo==True):
					if (self.reproduciendo_usb == 0):
						return
					
					if (self.reproduciendo_usb <=self.cantidad_musica):
						self.reproduciendo_usb=self.reproduciendo_usb-1
						print "El USB se ha Cambiado a la  Pista ",self.reproduciendo_usb

				
			


#PRINCIPAL
a=reproductor()
a.encender()

#radio
a.cambiar_frecuencia()
a.siguiente()
a.anterior()
a.cambiar_frecuencia()
a.siguiente()
a.anterior()

#CD
a.sel_cd()
a.abrir_compuerta()
a.ingresar_cd()
a.cerrar_compuerta()
a.leer(3)
a.pausa()
a.play()
a.siguiente()
a.anterior()
a.abrir_compuerta()
a.sacar_cd()
a.cerrar_compuerta()

#USB
a.sel_usb()
a.ingresar_usb()
a.leer(6)
a.pausa()
a.play()
a.siguiente()
a.siguiente()
a.anterior()
a.anterior()
a.subir_volumen()
a.subir_volumen()
a.bajar_volumen()


#radio
a.sel_radio()
a.apagar()
