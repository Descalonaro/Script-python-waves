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
	

	print("\n- Se esta usando su cuenta:")
	print(myAddress)	

	print("\n- El token a enviar sera (junto con Waves):")
	print(myToken)


	print("\n- Se van a realizar las siguientes transacciones:")
	csvarchivo = open("inputDirecciones.csv")
	direcciones = csv.reader(csvarchivo)
	reg = next(direcciones)
	print(reg)


	transfersToken = []
	transfersWaves = []

	for row in direcciones:
		print(row)
		direccion,teftok,waves,texto = row # Parametros de cada fila
		destinoAddress = pywaves.Address(direccion) # Formato destino
		
		# Enviar tokens a cada direccion de forma individualizada
		#myAddress.sendAsset(recipient=destinoAddress, asset=myToken, amount=int(teftok), attachment=texto)

		# Para enviar waves de forma masiva
		transfersWaves.append({'recipient':direccion, 'amount': int(waves)}) # Se crea el transfer masivo para waves

		# Para enviar tokens de forma masiva
		transfersToken.append({'recipient':direccion, 'amount': int(teftok)}) # Se crea el transfer masivo para tokens
		

	print(transfersToken)
	print(transfersWaves)

	print(type(transfersToken))
	print(type(transfersWaves))	

	print("\n- Transaccion masiva de Token TEFTOK")
	myAddress.massTransferAssets(transfersToken, myToken, texto,0) # No funciona
	#pywaves.Address.massTransferAssets(myAddress, transfersToken, myToken)
	#print("\nTransaccion realizada")

	#print("\nTransaccion masiva de WAVES")
	#myAddress.massTransferWaves(transfersWaves,"Envio masivo de Waves")
	#print("\nTransaccion realizada")


else:

	print("\nIntroduce tu privateKey como parametro para enviar la transferencia masiva.\n\n")
	