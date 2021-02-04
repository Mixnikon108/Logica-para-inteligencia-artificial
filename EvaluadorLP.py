'''
          LOGICA PARA INTELIGENCIA ARTIFICIAL

Este programa ha sido desarrollado por Jorge de la Rosa Padrón
a fecha 24/10/2020. En el se encuentran los ejercicios del 1 al
4 de la hoja de prácticas.

'''




'''
EJERCICIO 1.

Implementar una función de Python evaluarVerdadFND que, dada una
lista de listas formula y un diccionario asignacion verdad, devuelva 
la asignación de verdad de la FND representada por formula mediante 
asignacion verdad. 
'''



#Condiciones dadas
formula = [["p", "!q", "r"], ["p", "q", "r"]]
asignacion_verdad = {"p": 1, "q": 0, "r":1}

#Funcion solicitada
def evaluarVerdadFND(formula:list, asignacion_verdad:dict):
	'''
		Input:

	formula --> lista de la forma normal disyuntiva 
	asignacion_verdad --> diccionario con la asignacion de verdad deseada

		Funcionamiento:

	En la primera linea pasa nuestra formula de literales a una lista directamente con las asignaciones
	de verdad de los literales.
	En nuestro caso:

	formula = [[1,1,1],[1,0,1]]
	
	Luego,creando otra lista, se evalua si se encuentra algun 0 dentro de las listas.
	Si es el caso, se añade un 1 a la lista, si no, añade un 0.
	En nuestro caso: 

	verdad = [0, 1]
	
	Finalmente, como para que se cumpla la formula al menos una de las clausulas tiene que tener todo 1s,
	si hay algun 0 en la lista de verdad, devuelve un 1.

		Output:
	Devuelve un numero tipo int.
	1 si es cierto
	0 si es falso
	'''

	formula = [[int(not(asignacion_verdad[j[1:]])) if '!' in j else asignacion_verdad[j] for j in i] for i in formula]
	verdad = [1 if 0 in i else 0 for i in formula]
	return 1 if 0 in verdad else 0


#Print de ejemplo para ver el resultado
print('La formula {} es {}'.format(formula, evaluarVerdadFND(formula, asignacion_verdad)))







'''
EJERCICIO 2.

Repetir la función anterior pero para fórmulas en Forma Normal
Conjuntiva, para implementar la función evaluarVerdadFNC.
'''


#Condiciones dadas
formula = [["p", "!q", "r"], ["p", "q", "r"]]
asignacion_verdad = {"p": 1, "q": 0, "r":1}


#Funcion solicitada
def evaluarVerdadFNC(formula:list, asignacion_verdad:dict):
	'''
		Input:

	formula --> lista de la forma normal conjuntiva 
	asignacion_verdad --> diccionario con la asignacion de verdad deseada

		Funcionamiento:

	En la primera linea pasa nuestra formula de literales a una lista directamente con las asignaciones
	de verdad de los literales.
	En nuestro caso:

	formula = [[1,1,1],[1,0,1]]
	
	Luego,creando otra lista, se evalua si se encuentra algun 0 dentro de las listas.
	Si es el caso, se añade un 1 a la lista, si no, añade un 0.
	En nuestro caso: 

	verdad = [0, 1]
	
	Finalmente, como para que se cumpla la formula todas las clausulas deben cumplirse, en caso de 
	encontrar algun 0 en la lista de verdad, devolverá un 0.

		Output:
	Devuelve un numero tipo int.
	1 si es cierto
	0 si es falso
	'''

	formula = [[int(not(asignacion_verdad[j[1:]])) if '!' in j else asignacion_verdad[j] for j in i] for i in formula]
	verdad = [1 if 1 in i else 0 for i in formula]
	return 0 if 0 in verdad else 1


#Print de ejemplo para ver el resultado
print('La formula {} es {}'.format(formula, evaluarVerdadFNC(formula, asignacion_verdad)))






'''
EJERCICIO 3.

Implementar una función en Python, llamada evaluarVerdadLP que,
dada una cadena de texto formula representando una fórmula bien 
formada de lógica proposicional y un diccionario asignacion verdad, 
representando una asignación de verdad, devuelva la asignación
de verdad de la fórmula formula.
'''



'''
Aclaracion de como escribir las formulas de verdad.
Para construir cualquier formula de manera que la funcion la entienda se tiene que utilizar el maximo
numero de corchetes posible, reduciendo la ambugüedad a nula. De manera que si tenemos la formula, por 
ejemplo
			
			        p ∨ ¬p

se traduciria de la siguente forma

	     [ ['p'],  '∨',   ['¬', ['p']] ]




La estructura de las listas tendrá la forma

		[[formula 1],   'operador',  [formula 2]]

donde para el caso del negado '¬' seguiría la estructura

		['¬',  [formula 1]]

Un ultimo ejemplo mas para ayudar al lector en la comprension del mismo.
Ej.

formula original                                 ((¬p ∨ q) ∧ r) → (p ↔ ¬q)
Ayuda visual a la estructura      ((¬p        ∨    q)    ∧    r)     →      (p    ↔       ¬q)
formula traducida            [[[['¬',['p']], '∨',['q']],'∧', ['r']],  '→',  [['p'],'↔',['¬',['p']]]]

'''

#Condiciones dadas
formula = [[[['¬',['p']], '∨',['q']],'∧', ['r']],  '→',  [['p'],'↔',['¬',['p']]]]
asignacion_verdad = {"p": 1, "q": 0, "r":1}



#Funcion solicitada
def evaluarVerdadLP(formula:list, asignacion_verdad:dict):
	'''
		Input:

	formula --> lista con la formula 
	asignacion_verdad --> diccionario con la asignacion de verdad deseada

		Funcionamiento:

	Recursividad.

		Output:
	Devuelve un numero tipo int.
	1 si es cierto
	0 si es falso
	'''
	if len(formula) == 1:
		j = formula[0]
		return asignacion_verdad[j]
		
	if len(formula) == 2:
		for1 = evaluarVerdadLP(formula[1], asignacion_verdad)
		return int(not(for1))

	else:
		for1 = evaluarVerdadLP(formula[0], asignacion_verdad)
		for2 = evaluarVerdadLP(formula[2], asignacion_verdad)

		if formula[1] == '∧':
			return 1 if for1 == 1 and for2 == 1 else 0

		elif formula[1] == '∨':
			return 1 if for1 == 1 or for2 == 1 else 0
			
		elif formula[1] == '→':
			return 0 if for1 == 1 and for2 == 0 else 1
			
		elif formula[1] == '↔':
			return 1 if for1 == for2  else 0
	

#Print de ejemplo para ver el resultado
print('La formula {} es {}'.format(formula, evaluarVerdadLP(formula, asignacion_verdad)))


'''
EJERCICIO 4.

Extender la función anterior para implementar una función 
esTautologia que, dada una fórmula formula y una lista con 
sus literales literales , devuelva si la fórmula es una
tautología o no.
'''

#Condiciones dadas
formula = [['p'],'∨',['¬',['p']]]
literales = ['p']


#Funcion solicitada
def esTautologia(formula: list, literales: list):
	'''
		Input:

	formula --> lista de la forma normal conjuntiva 
	asignacion_verdad --> lista de literales

		Funcionamiento:

	Creamos una lista con el mismo numero de 0 que de literales haya
	x = [0,0,0,0]

	A continuacion, hacemos un bucle for con 2**numero de literales
	ya que son las posibles combinaciones que pueda haber con esos literales.
	n = [1,1]

	Simplemente sustituimos los dos ultimos valores de x con los de n.


		Output:
	Devuelve un numero tipo bool.
	True si es cierto
	False si es falso
	'''
	numero_de_literales = len(literales)
	flag = 0

	for k in range(2**numero_de_literales):

		n = str(bin(k)[2:])
		n = [int(i) for i in n]

		x = '0' * numero_de_literales
		x = [int(i) for i in x]
		
		x[-len(n):] = n

		d = {literales[i] : x[i] for i in range(len(literales))}
		
		if evaluarVerdadLP(formula, d) == 0:
			flag = 1
			break

	return True if flag == 0 else False

#Print de ejemplo para ver el resultado
print('El hecho de que la formula {} es una tautologia es {}'.format(formula, esTautologia(formula, literales)))
