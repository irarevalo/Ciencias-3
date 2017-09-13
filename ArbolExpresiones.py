class Nodo():
    def __init__(self, val, izq=None, der=None):
        self.valor = val
        self.izq = izq
        self.der = der

class Pila:
    def __init__(self):
        self.pila = []
    def agregar(self, elemento):
        self.pila.append(elemento)
    def sacar(self):
        if self.vacia()==False:
            return self.pila.pop()
        else:
            return "Pila vacia"
    def vacia(self):
        return self.pila == []

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.sacar()
            nodo_izq = pila.sacar()
            pila.agregar(Nodo(lista[0],nodo_izq,nodo_der))
        elif lista[0] in variables:
                valor = variables[lista[0]]
                pila.agregar(Nodo(valor[0]))
        elif lista[0]=="=":
            variable = pila.sacar().valor
            variables[variable] = [evaluar(pila.sacar())]
            print(variable+" = "+str(variables[variable][0]))
        else:
            pila.agregar(Nodo(lista[0]))
        return convertir(lista[1:],pila)

def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)

if __name__ == "__main__":
    pila = Pila()
    opcion = "y"
    variables = {}
    variable = ""
    while(opcion == "y" or opcion == "Y"):
        exp = input("Ingrese la expresion en formato posfijo: ").split(" ")
        convertir(exp,pila)
        opcion = input("Desea ingresar otra expresion?:(y,N)")
