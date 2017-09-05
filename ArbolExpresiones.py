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
class Variable():
    def __init__(self, identificador, valor):
        self.identificador = identificador
        self.valor = valor
def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.sacar()
            nodo_izq = pila.sacar()
            pila.agregar(Nodo(lista[0],nodo_izq,nodo_der))
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
def main():
    pila = Pila()
    opcion = "y"
    variables = []
    control=0
    while(opcion == "y" or opcion == "Y"):
        exp = raw_input("ingrese la expresion en formato posfijo: ").split(" ") 
        convertir(exp[:len(exp)-2],pila)
        variable = Variable(exp[len(exp)-1],evaluar(pila.sacar()))
        print(variable.identificador," ",variable.valor)
        variables.append(variable)
        opcion = raw_input("Desea ingresar otra expresion?:(y,N)")
        if(opcion == "N" or opcion == "n"):
            exp = raw_input("ingrese la expresion  fianl en formato posfijo: ").split(" ")
            for i in exp[:len(exp)-2]:
                if(i.isalpha()):
                    for j in variables:
                        if(j.identificador==i):
                             exp[control] = str(j.valor)
                control=control+1
            convertir(exp[:len(exp)-2],pila)
            variable = Variable(exp[len(exp)-1],evaluar(pila.sacar()))
            print(variable.identificador," ",variable.valor)
            
            
if __name__ == "__main__":
    main()
