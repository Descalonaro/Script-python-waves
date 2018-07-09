#!/usr/bin/env python3
# encoding: utf-8

import pywaves
import math
import sys
import csv

if (len(sys.argv) > 1 ):

	# Asigno parametros de entrada del comando
	privKey = sys.argv[1]
	# token = sys.argv[2] # Si quisiera introducir token por parametro
 
	# Inicializo parametros (direccion y token a enviar)
	myAddress = pywaves.Address(privateKey=""+privKey+"")
	myToken = pywaves.Asset("AFUG6HXViGfAnobd41H1sAeASUEmjF7dHsgt5K1XFcfM")
	waves = pywaves.

	print("\n- Se esta usando su cuenta:")
	print(myAddress)	

	print("\n- El token a enviar sera (junto con Waves):")
	print(myToken)


	print("\n- Se van a realizar las siguientes transacciones:")
	csvarchivo = open("inputDirecciones.csv")
	direcciones = csv.reader(csvarchivo)
	reg = next(direcciones)
	print(reg)


	for row in direcciones:
		print(row)
		direccion,teftok,waves,texto = row # Parametros de cada fila
		destinoAddress = pywaves.Address(direccion) # Formato destino
		
		# Enviar tokens a cada direccion de forma individualizada
		myAddress.sendAsset(recipient=destinoAddress, asset=myToken, amount=int(teftok), attachment=texto)

		# Enviar waves de forma masiva
		

		# Enviar tokens de forma masiva
		# ----

else:

	print("\nIntroduce tu privateKey como parametro para enviar la transferencia masiva.\n\n")
	