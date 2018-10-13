# Por favor complete con su nombre y RUT.
# NOMBRE Y APELLIDO: Roberto Tapia
# RUT: 19.668.622-3

# Run the file as "python SAT.py -v"

# Add further needed modules
import unittest

# To implement the functions below, you are allowed
# to define auxiliary functions, if convenient.


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

"""           
def IsSatisfiable(formula):
    if(formulaVacia(formula)):
        return True
    if(clausulaVacia(formula)):
        return False
    if(IsSatisfiable(SetLiteral(formula,formula[0][0]))==False):
        return IsSatisfiable(SetLiteral(formula,-(formula[0][0])))
    else:
        return IsSatisfiable(SetLiteral(formula,formula[0][0]))
"""

def IsSatisfiable(formula):
        original=formula.copy()
        if(formulaVacia(formula)):
                formula=original
                return True
        if(clausulaVacia(formula)):
                formula=original
                return False
        literales=encontrarLiterales(formula)
        formula=original
        for literal in literales:
                if satisfacible(formula,literal)==True:
                        formula=original
                        return True
        formula=original
        return False
        
def satisfacible(formula,literal):
        if(formulaVacia(formula)):
                return True
        if(clausulaVacia(formula)):
                return False
        else:
                literal=(formula[0][0])
                formula=SetLiteral(formula,literal)
                return satisfacible(formula,literal)

def camino(formula):
    original=formula
    if IsSatisfiable(formula)==False:
        return False
    else:
        camino={}
        literales=encontrarLiterales(original)
        print(formula)
        for literal in encontrarLiterales(formula):
            if literal>0:
                camino[literal]=0
        for llave in camino.keys():
            if IsSatisfiable(SetLiteral(formula,camino[llave])):
                camino[llave]=True
            else:
                camino[llave]=False
    print(camino)
    return camino
        
def BuildModel(formula):
    print(formula)
    original=formula
    print(original)
    if( IsSatisfiable(formula)==False):
        return(False,{})
    else:
        print("asdf")
        print(formula)
        valuacion=camino(original)
        
        return(True,valuacion)
            

"""   
def satisfacible(formula,literal):
        if(formulaVacia(formula)):
                return True
        if(ClausulaVacia(formula)):
                return False
        else:
                literal=(formula[0][0])
                formula=SetLiteral(formula,literal)
                return satisfacible(formula,literal)
"""


#Entrega una lista con todos los literales distintos en la formula,
#estos son los literales a los que se les deben asignar valores para
#la funcion IsSatisfiable.
def encontrarLiterales(formula):
        listaLiterales=[]
        for clausula in formula:
                for literal in clausula:
                        if literal not in listaLiterales:
                                listaLiterales.append(literal)

        return listaLiterales

#print (encontrarLiterales([[-2, 4], [1], [-4,-1]]))

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

#def BuildModel(formula):

#print(BuildModel([[-2, 4], [1], [-4,-1]]))
a=[[-2, 4], [1], [-4, -1]]
print(a)
print(IsSatisfiable(a))
print(a)
"""
class Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_SetLiteral(self):
        self.assertEqual(SetLiteral([[1, 2, -3], [-1, -2, 4], [3, 4]], 1), [[-2, 4], [3, 4]])
        self.assertEqual(SetLiteral([[1, 2, -3], [-1, -2, 4], [3, 4]], -1), [[2, -3], [3, 4]])

    def test_IsSatisfiable(self):
        self.assertEqual(IsSatisfiable([[1, 2, -3], [-1, -2, 4], [3, 4]]), True)
        self.assertEqual(IsSatisfiable([[1, 2], [1, -2], [], [-1]]), False)
        self.assertEqual(IsSatisfiable([]), True)
        self.assertEqual(IsSatisfiable([[-2,4],[1],[-4,-1]]), True)
        #self.assertEqual(IsSatisfiable([[-3,1],[-4],[3,4]]),True)
        self.assertEqual(IsSatisfiable([[3,4],[-3,1],[-4]]),True)

    #def test_encontrarLiterales(self):
     #       self.assertEqual(encontrarLiterales(),[1,2,3,-1,-4,

    def test_BuildModel(self):
        self.assertEqual(BuildModel([[-2, 4], [1], [-4,-1]]), (True, {1: True, 2: False, 4: False}))
        self.assertEqual(BuildModel([[1,2], [-1,-2], [-1,2], [1,-2]]), (False, {}))
"""
"""FUNCIONA A MEDIAS
def IsSatisfiable(formula):
        if(formulaVacia(formula)):
                return True
        if(ClausulaVacia(formula)):
                return False
        else:
                literal=abs(formula[0][0])
                formula=SetLiteral(formula,literal)
                return IsSatisfiable(formula)
"""
###
"""

def IsSatisfiable(formula):
        if(formulaVacia(formula)):
                return True
        if(ClausulaVacia(formula)):
                return False
        literales=encontrarLiterales(formula)
        original=formula
        for literal in literales:
                if satisfacible(formula,literal)==True:
                        return True
        return False
        #if(formulaVacia(formula)):
        #        return True
        #if(ClausulaVacia(formula)):
        #        return False
        #else:
        #        literal=abs(formula[0][0])
        #        formula=SetLiteral(formula,literal)
        #        return IsSatisfiable(formula)
    
def satisfacible(formula,literal):
        if(formulaVacia(formula)):
                return True
        if(ClausulaVacia(formula)):
                return False
        else:
                literal=(formula[0][0])
                formula=SetLiteral(formula,literal)
                return satisfacible(formula,literal)


# Perform the tests when runing the file
if __name__ == '__main__':
    unittest.main()
"""
