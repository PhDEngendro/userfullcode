#!/usr/bin/python3
import sys
from progress.bar import IncrementalBar
## RUT Maker.

## la idea general es crear ruts entre el A millones y el B millones como diccionario para prosesar handshake.

#calculadora de opciones


def opt(optNum):
	op4 = int(optNum // 8)
	if op4 == 1 :
		optNum -= 8
	op3 = int(optNum // 4)
	if op3 == 1 :
		optNum -= 4
	op2 = int(optNum // 2)
	if op2 == 1 :
		optNum -= 2
	op1 = int(optNum // 1)
	if op1 == 1 :
		optNum -= 1
	return op1, op2, op3, op4

# definir funcion para calcular el verificador

def calc_hash(seed):
	suma = 0
	mult = 2
	while True:
		if mult > 7:
			mult = 2
		suma += ((int(seed) % 10) * int(mult))
		mult += 1
		seed = int( seed // 10 )

		if int(seed) == 0:
			break
	ver = 11 - (suma % 11)
	if (ver == 10):
	    ver = 0
	elif (ver == 11):
	    ver = "k"
	return ver


# definir funcion para juntar ambos valores en varios arreglos

def arreglos(seed, ver):
	millones = str(seed // 1000000)
	miles = str((int(seed % 1000000) - int(seed % 1000)) // 1000)
	cientos = str(seed % 1000)
	if len(str(miles)) < 4:
		agregar = 3 - len(str(miles))
		for n in range(0,agregar,1):
			miles = "0"+miles
	if len(str(cientos)) < 4:
		agregar = 3 - len(str(cientos))
		for m in range(0,agregar,1):
			cientos = "0"+cientos
	arreglo1 = str(seed)
	arreglo2 = (str(seed)+str(ver))
	arreglo3 = (str(seed)+"-"+str(ver))
	arreglo4 = (str(millones)+"."+str(miles)+"."+str(cientos)+"-"+str(ver))
	return arreglo1, arreglo2, arreglo3, arreglo4


# definir funcion main

print("""


Generador de diccionario de R.U.T.


""")


if len(sys.argv) > 1 :
    inicio = int(sys.argv[1])
    finall = int(sys.argv[2])
    opcion = int(sys.argv[3])
    finame = str(sys.argv[4])
    
    print("Inicio   ",inicio)
    print("Final    ",finall)
    print("Opcion   ",opcion)
    print("Nombre   ",(finame+".txt"))
print("""




	""")    


opc1, opc2, opc3, opc4 = opt(opcion)

diccionario = open((str(finame+".txt")), "w")
cont = 0

Lamda = (finall - inicio) // 1000

bar = IncrementalBar('Peocesando', max=Lamda, suffix='%(percent).1f%% - %(eta_td)s')

for rut in range(inicio, finall, 1):
	
	verif = calc_hash(rut)
	
	rut1, rut2, rut3, rut4 = arreglos(rut, verif)
	
	if int(opc1) == 1:
		diccionario.writelines(str(rut1))
		diccionario.writelines(str("\n"))
		#print(rut1)
	
	if int(opc2) == 1:
		diccionario.writelines(str(rut2))
		diccionario.writelines(str("\n"))
		#print(rut2)
	
	if int(opc3) == 1:
		diccionario.writelines(str(rut3))
		diccionario.writelines(str("\n"))
		#print(rut3)
	
	if int(opc4) == 1:
		diccionario.writelines(str(rut4))
		diccionario.writelines(str("\n"))
		#print(rut4)
	if cont >=1000:
		bar.next()
		cont=0

	cont += 1

diccionario.close()
print("Archivo",finame+".txt","creado")
bar.finish()
