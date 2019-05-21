'''lista=[3,5,6,7,8]


longitud=len(lista)
for i in range(longitud):
	print(lista[longitud-i-1])


for item in reversed(lista):
	print(item)'''


###################### DECIMAL A BINARIO  ###########################

def decimal_bin():
	num_d_b=int(input("Por favor, Ingrese un número decimal a convertir :D : "))

	modulo=[]


	while True:
		cociente=num_d_b//2
		modu=int(num_d_b%2)
		num_d_b=cociente
		modulo.append(modu)
		
		if cociente<=0:
			break

	binario=[]

	for i in reversed(modulo):
		binario.append(i)

	print(*binario)

	
######################## BINARIO A DECIMAL ############################# 

''' lista de potencias en base 2'''

def bin_decimal():
	n=input("Por favor, Ingrese el número de binario a convertir :D : ")

	num=str(n)
	cantidad_potencia=len(num)
	
	''' lista de potencias en base 2'''

	lista_pot_base2=[]

	for i in range(0,cantidad_potencia):
		lista_pot_base2.append(2**i)

	'''número ingresado convertido en una lista para poder recorrerlo y saber cuantos unos hay'''

	lista_n=[]

	for b in reversed(n):
		lista_n.append(b)

	'''bucle para determinar la posicion de los unos'''

	resultado=0

	for i in range(0,len(lista_n)):
		if lista_n[i]=='1':
			posicion=i+1
			resultado+=lista_pot_base2[posicion-1]

	print(resultado)

######################### DECIMAL A OCTAL ##########################


def decimal_oct():
	num_d_o=int(input("Por favor, Ingrese un número decimal a convertir :D : "))

	modulo=[]


	while True:
		cociente=num_d_o//8
		modu=int(num_d_o%8)
		num_d_o=cociente
		modulo.append(modu)
		
		if cociente<=0:
			break

	octal=[]

	for i in reversed(modulo):
		octal.append(i)

	
	print(*octal)

########################## OCTAL A DECIMAL ################################

def oct_decimal():
	num_o_d=input("Por favor, Ingrese un número de base 8 a convertir :D : ")

	n_o_d=str(num_o_d)
	long_num_o_d=len(n_o_d)


	'''Lista de potendias de base 8'''
	pot_octal=[]

	for i in range(0,long_num_o_d):
		pot_octal.append(8**i)

	'''Se revierte el número para multiplicarlo con su posicion correspondiente'''
	num_octal=[]

	for j in reversed(n_o_d):
		num_octal.append(j)

	'''Se convierte la lista de strings en una lista de enteros para poder multiplicarlos'''
	ints=[]
	for l in num_octal:
		ints.append(int(l))

	resultado=0
	for m in range(0,len(num_octal)):
		result+=pot_octal[m]*ints[m]

	
	print(resultado)

##################### DECIMAL A HEXADECIMAL ########################

def decimal_hexa():
	num_d_h=int(input("Por favor, Ingrese un número decimal a convertir :D : "))


	modulo=[]


	while True:
		cociente=num_d_h//16
		modu=int(num_d_h%16)
		num_d_h=cociente
		modulo.append(modu)
		
		if cociente<=0:
			break

	hexadecimal=[]

	for i in reversed(modulo):
		hexadecimal.append(i)

	conver_hexa=[]
	
	for j in hexadecimal:
		if j==10:
			j='A'
		elif j==11:
			j='B'
		elif j==12:
			j='C'
		elif j==13:
			j='D'
		elif j==14:
			j='E'
		elif j==15:
			j='F'
		conver_hexa.append(j)

	print(*conver_hexa)

########################### HEXADECIMAL A DECIMAL ################################

def hexa_deci():
	num_h_d=input("Por favor, Ingrese el número de base 16 a convertir :D : ")

	n_h_d=str(num_h_d)

	lista_pot_h=[]

	'''Potencias de 16'''
	for j in range(0,len(n_h_d)):
		lista_pot_h.append(16**j)

	
	lista_h_d=[]

	'''Se convierte el número en una lista para poder recorrerlo'''
	for i in reversed(n_h_d):
		lista_h_d.append(i)

	
	conver=[]

	for h in lista_h_d:
		if h=='0':
			conver.append(h)
		elif h=='1':
			conver.append(h)
		elif h=='2':
			conver.append(h)
		elif h=='3':
			conver.append(h)
		elif h=='4':
			conver.append(h)
		elif h=='5':
			conver.append(h)
		elif h=='6':
			conver.append(h)
		elif h=='7':
			conver.append(h)
		elif h=='8':
			conver.append(h)
		elif h=='9':
			conver.append(h)
		elif h=='A':
			conver.append('10')
		elif h=='B':
			conver.append('11')
		elif h=='C':
			conver.append('12')
		elif h=='D':
			conver.append('13')
		elif h=='E':
			conver.append('14')
		elif h=='F':
			conver.append('15') 
	
	'''se convierte de lista de strings a lista de enteros para poder multiplicarlos'''
	int_conver=[]

	for m in conver:
		int_conver.append(int(m))

	num_convertido=[]

	for l in range(0,len(int_conver)):
		num_convertido.append(lista_pot_h[l]*int_conver[l])

	'''Se suma todos los elementos de la lista'''

	num_deci=0
	for k in num_convertido:
		num_deci+=k

	print(  num_deci)

##############################################################################################################3

opcion=int(input("""Por favor elija una de las opciones de convers  ión :D
Decimal a Binario ---> 1 
Decimal a Octal ---> 2
Decimal a Hexadecimal ---> 3
Binario a Decimal ---> 4
Binario a Octal ---> 5
Binario a Hexadecimal ---> 6
Octal a Decimal ---> 7
Octal a Binario ---> 8
Octal a Hexadecimal ---> 9
Hexadecimal a Decimal ---> 10
Hexadecimal a Binario ---> 11
Hexadecimal a Octal ---> 12"""))

if opcion==1:
	print(decimal_bin())
elif opcion==2:
	print(decimal_oct())
elif opcion==3:
	print(decimal_hexa())
elif opcion==4:
	print(bin_decimal())
elif opcion==5:
	bin_oct=decimal_oct()











decimal_a_binario=decimal_bin(num_d_b)






























































































































































		







































































		



