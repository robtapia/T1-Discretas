


def SetLiteral(formula, lit):
    if(formula==[]):
        return formula
    clausula=0
    while(clausula<len(formula)):
        if lit in formula[clausula]:
            del formula[clausula]
        elif -lit in formula[clausula]:
            formula[clausula].remove(-lit)
        else:
            clausula=clausula+1
    return formula

def encontrarLiterales(formula):
        listaLiterales=[]
        for clausula in formula:
                for literal in clausula:
                        if literal not in listaLiterales:
                                listaLiterales.append(literal)

        return listaLiterales

def formulaVacia(formula):
        if formula==[]:
                return True
        else:
                return False
def clausulaVacia(formula):
        for clausula in formula:
                if clausula==[]:
                        return True
                else:
                        continue
        return False

def IsSatisfiable(formula):
    #Caso Base:
    if(formulaVacia(formula)):
        return True
    if(clausulaVacia():
    original=formula.copy() #Para poder restaurar formula a su valor original luego de iterar sobre el
    

IsSatisfiable([[1,2]])
