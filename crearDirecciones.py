#!/usr/bin/env python3
# encoding: utf-8

import pywaves
import math
import sys
import subprocess

# if len( sys.argv) < .......  compruebo que el fichero pasado como parametro existe

# Generar nueva direccion... address = pywaves.Address()

# bucle for, que recorre hasta el numero de direcciones pasadas como parametro

if (len(sys.argv) > 1 ) :
	print(len(sys.argv))
	
	print(int(sys.argv[1]))

	numberAccounts = int(sys.argv[1])

	if ( numberAccounts <= 1 ):
		numberAccounts = int(1)
		print("Se va a generar 1 cuenta \n")
	else:
		print("Se va a generar " +sys.argv[1]+ " cuentas \n")

	f = open("fichero.txt","w") # Para reiniciar el fichero output
	f.close()

	for i in range(1,numberAccounts+1):
		
		createdAddress = pywaves.Address()  # Genera la nueva direccion

		f = open("fichero.txt","a")
		f.write("- [Cuenta numero "+str(i)+"]  ")      	# Se llena el fichero con las direcciones de cada cuenta creada
		f.write("Address: " +createdAddress.address)
		f.write("  Seed: " +createdAddress.seed+"\n\n")



		print("Cuenta numero "+str(i)+" generada.")
		i=i+1

	f.close()


else:

	print("\nIntroduzca un numero de cuentas valido como parametro \n(Debe ser un numero entero) \n")
	



