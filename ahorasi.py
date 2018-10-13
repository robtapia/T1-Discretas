


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

        for literal in range(len(listaLiterales)):
            if (listaLiterales[literal]<0):
                listaLiterales[literal]=abs(listaLiterales[literal])
        lista=list(set(listaLiterales))
        lista.sort()
        return lista
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
    if clausulaVacia(formula):
        return
    if formulaVacia(formula):
        return True

    print("formula:")
    print(formula)
    #print(encontrarLiterales(formula)[0])
    s=first(formula)
    #print(formula)
    while(s!= None):
        #IsSatisfiable(s)
        #print(formula)
        #print("b")
        #print("-"+str(encontrarLiterales(formula)[0]))
        if(IsSatisfiable(s)):
            return IsSatisfiable(s)
        else:
            s=next(formula)

    #return False


def first(formula):
    if encontrarLiterales(formula)==[]:
        return
    print("literal seteado:"+ str(encontrarLiterales(formula)[0]))
    return SetLiteral(formula,encontrarLiterales(formula)[0])
def next(formula):
    if encontrarLiterales(formula)==[]:
        return
    print("literal seteado:" + str(-encontrarLiterales(formula)[0]))
    return SetLiteral(formula,0-(encontrarLiterales(formula)[0]))

a=[[1, 2, -3], [-1, -2, 4], [3, 4]]
b=[[1, 2], [1, -2], [], [-1]] #False
c=[]
d=[[-2,4],[1],[-4,-1]]
e=[[-3,1],[-4],[3,4]]
f=[[3,4],[-3,1],[-4]]
g=[[3,4],[-3,1],[-4]]

#print(IsSatisfiable(a))
#print(IsSatisfiable(b))
#print(IsSatisfiable(c))
#print(IsSatisfiable(d))
print(IsSatisfiable(e))
#print(IsSatisfiable(f))
#print(IsSatisfiable(g))
#print(a)
