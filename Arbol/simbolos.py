class Error():
    def __init__(self,valor,linea):
        self.valor = valor 
        self.linea = linea

class Simbolo():
    def __init__(self,name,valor,temp,linea):
        self.nombre= name
        self.tipo = valor 
        self.linea = linea
        self.temp  = temp

class Metodo():
    def __init__(self, name, instr):
        self.nombre = name 
        self.inst   = instr 
        self. linea = linea 

class TablaSimbolos():
    def __init__(self):
        self.contadorTemp = 0
        self.contadorTag = 0 
        self.errorSemantico = []
        self.mensajes = []
        self.variables = []
        self.variables.append(dict())
        self.metodos = {}
        self.optimizacion = []

    def addError(self, mensaje, linea):
        self.errorSemantico.append(Error(mensaje,linea)) 

    def addMensaje(self,mensaje):
        self.mensajes.append(mensaje)

    def addVariable(self,name, val, temp, linea):
        self.variables[-1][name] = Simbolo(name,val,temp,linea)

    def generarTemporal(self):
        self.contadorTemp +=1
        return "$t"+str(self.contadorTemp)

    def getLastTemporal(self):
        return "$t"+str(self.contadorTemp)

    def generarEtiqueta(self):
        self.contadorTag +=1
        return "tag"+str(self.contadorTag)

    def getLastEtiqueta(self):
        return "tag"+str(self.contadorTag)

    def addEntorno(self):
        self.variables = self.variables.append(dict()) 

    def popEntorno(self):
        self.variables.pop()
    