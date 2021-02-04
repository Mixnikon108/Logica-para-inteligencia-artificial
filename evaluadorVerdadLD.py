#!/usr/bin/env python
# coding: utf-8


'''
          LOGICA PARA INTELIGENCIA ARTIFICIAL

Este programa ha sido desarrollado por Jorge de la Rosa Padrón
a fecha 08/01/2021. En el se encuentran los ejercicios del 1 al
4 de la hoja de prácticas.

'''





# ADAPTACION A LOGICA DIFUSA POR GÖDEL-DUMMETT
def evaluarVerdadGodelDummetFNC(formula:list, asignacion_verdad:dict):
	aux1 = list()
	aux2 = list()
	aux3 = list()

	for lista in formula:
		for atomo in lista:
			if '!' in atomo:
				valor_verdad = 1 - asignacion_verdad[atomo[1:]]
				aux1.append(valor_verdad)
			else:
				aux1.append(asignacion_verdad[atomo])
		
		  
		aux2.append(aux1)
		aux1 = [] 
   
	for lista in aux2:
		aux3.append(max(lista))

	return min(aux3)



formula = [["p", "!q"], ["q", "r"]]
asignacion_verdad = {"p": 0.7, "q": 0.6, "r":0.1}


evaluarVerdadGodelDummetFNC(formula, asignacion_verdad)





# ADAPTACION A LOGICA DIFUSA POR GÖDEL-DUMMETT
def parseFormula(formula):
    
    if formula[1] == '!': # La formula empieza por ! -> es un NOT.
        return ["!", parseFormula(formula[2:-1])]
    
    elif formula[1] != '(': # La formula no tiene parentesis interno -> es un literal
        return [formula[1:-1]]
    
    
    
    n_parentesis = 1     
                         
    index = 2  
    
    while n_parentesis > 0:        # Aun no estan balanceados los parentesis
        if formula[index] == "(": 
            n_parentesis += 1      # Nuevo parentesis de apertura
        elif formula[index] == ")":
            n_parentesis -= 1      # Parentesis de apertura cerrado
        
        index += 1
    

    return [formula[index], 
            parseFormula(formula[1:index]), 
            parseFormula(formula[index + 1:-1])]


def evaluarAnd(operando1, operando2, asignacion_verdad):
    
        
    resultado1 = evaluarVerdadLDLista(operando1, asignacion_verdad)
    resultado2 = evaluarVerdadLDLista(operando2, asignacion_verdad)
    
    # ADAPTACION A LOGICA DIFUSA POR GÖDEL-DUMMETT 

    # TABLA DE VERDAD DEL AND
    return min(resultado1, resultado2)
    
    
def evaluarOr(operando1, operando2, asignacion_verdad):
    
        
    resultado1 = evaluarVerdadLDLista(operando1, asignacion_verdad)
    resultado2 = evaluarVerdadLDLista(operando2, asignacion_verdad)
    
    # ADAPTACION A LOGICA DIFUSA POR GÖDEL-DUMMETT 

    # TABLA DE VERDAD DEL OR
    return max(resultado1, resultado2)
    
def evaluarImplicacion(operando1, operando2, asignacion_verdad):
    
        
    resultado1 = evaluarVerdadLDLista(operando1, asignacion_verdad) #Ψ
    resultado2 = evaluarVerdadLDLista(operando2, asignacion_verdad) #φ

    # ADAPTACION A LOGICA DIFUSA POR GÖDEL-DUMMETT 
    
    # TABLA DE VERDAD DEL LA IMPLICACION
    return 1 if resultado1 <= resultado2 else resultado2

def evaluarNot(operando, asignacion_verdad):
    
    
    resultado = evaluarVerdadLDLista(operando, asignacion_verdad)
    
    # ADAPTACION A LOGICA DIFUSA POR GÖDEL-DUMMETT 

    # TABLA DE VERDAD DEL NOT
    return 1 if resultado == 0 else 0




def evaluarVerdadGodelDummett(formula, asignacion_verdad):
    
    # Se convierte la formula a una lista de listas
    formula_lista = parseFormula(formula) 
    # Se llama a la funcion auxiliar evaluarVerdadLPLista que es igual
    # a esta funcion, pero acepta una formula escrita como lista de listas.
    return evaluarVerdadLDLista(formula_lista, asignacion_verdad)

def evaluarVerdadLDLista(formula_lista, asignacion_verdad):
    

    # La lista solo contiene un elemento: Es un literal
    if len(formula_lista) < 2:
        return asignacion_verdad[formula_lista[0]] # Devolvemos el valor de literal segun el diccionario
    
    # La formula es un AND
    elif formula_lista[0] == '&':
        return evaluarAnd(formula_lista[1], formula_lista[2], asignacion_verdad)

    # La formula es un OR
    elif formula_lista[0] == '|':
        return evaluarOr(formula_lista[1], formula_lista[2], asignacion_verdad)
    
    # La formula es una IMPLICACION
    elif formula_lista[0] == '>':
        return evaluarImplicacion(formula_lista[1], formula_lista[2], asignacion_verdad)
    
    # La formula es un NOT
    elif formula_lista[0] == '!':        
        return evaluarNot(formula_lista[1], asignacion_verdad)




# Ejemplo de uso
formula = "(((p)|(!(q)))&((q)|(r)))"
asignacion_verdad = {"p": 0.7, "q": 0.6, "r":0.1}

evaluarVerdadGodelDummett(formula, asignacion_verdad)





# ADAPTACION A LOGICA DIFUSA POR LUKASIEWICZ

def evaluarAndL(operando1, operando2, asignacion_verdad):
    
        
    resultado1 = evaluarVerdadLDListaL(operando1, asignacion_verdad)
    resultado2 = evaluarVerdadLDListaL(operando2, asignacion_verdad)
    
    # ADAPTACION A LOGICA DIFUSA POR LUKASIEWICZ

    # TABLA DE VERDAD DEL AND
    return min(resultado1, resultado2)
    
    
def evaluarOrL(operando1, operando2, asignacion_verdad):
    
        
    resultado1 = evaluarVerdadLDListaL(operando1, asignacion_verdad)
    resultado2 = evaluarVerdadLDListaL(operando2, asignacion_verdad)
    
    # ADAPTACION A LOGICA DIFUSA POR LUKASIEWICZ 

    # TABLA DE VERDAD DEL OR
    return max(resultado1, resultado2)
    
def evaluarImplicacionL(operando1, operando2, asignacion_verdad):
    
        
    resultado1 = evaluarVerdadLDListaL(operando1, asignacion_verdad) #Ψ
    resultado2 = evaluarVerdadLDListaL(operando2, asignacion_verdad) #φ

    # ADAPTACION A LOGICA DIFUSA POR LUKASIEWICZ 
    
    # TABLA DE VERDAD DEL LA IMPLICACION
    return 1 if resultado1 <= resultado2 else 1 - (resultado1 - resultado2)

def evaluarNotL(operando, asignacion_verdad):
    
    
    resultado = evaluarVerdadLDListaL(operando, asignacion_verdad)
    
    # ADAPTACION A LOGICA DIFUSA POR LUKASIEWICZ 

    # TABLA DE VERDAD DEL NOT
    return 1 - resultado




def evaluarVerdadLukasiewicz(formula, asignacion_verdad):
    
    # Se convierte la formula a una lista de listas
    formula_lista = parseFormula(formula) 
    # Se llama a la funcion auxiliar evaluarVerdadLPLista que es igual
    # a esta funcion, pero acepta una formula escrita como lista de listas.
    return evaluarVerdadLDListaL(formula_lista, asignacion_verdad)

def evaluarVerdadLDListaL(formula_lista, asignacion_verdad):
    
    
    # La lista solo contiene un elemento: Es un literal
    if len(formula_lista) < 2:
        return asignacion_verdad[formula_lista[0]] # Devolvemos el valor de literal segun el diccionario
    
    # La formula es un AND
    elif formula_lista[0] == '&':
        return evaluarAndL(formula_lista[1], formula_lista[2], asignacion_verdad)

    # La formula es un OR
    elif formula_lista[0] == '|':
        return evaluarOrL(formula_lista[1], formula_lista[2], asignacion_verdad)
    
    # La formula es una IMPLICACION
    elif formula_lista[0] == '>':
        return evaluarImplicacionL(formula_lista[1], formula_lista[2], asignacion_verdad)
    
    # La formula es un NOT
    elif formula_lista[0] == '!':        
        return evaluarNotL(formula_lista[1], asignacion_verdad)




# Ejemplo de uso
formula = "((((!(p))|(q))&(r))>((p)&(!(q))))"
asignacion_verdad = {"p": 0.4, "q": 0.1, "r":0.6}

evaluarVerdadLukasiewicz(formula, asignacion_verdad)

