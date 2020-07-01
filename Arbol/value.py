from enum import Enum

temp = 0
   
def getHash(var):
    return hash(var)

def esNumerico(v1):
    if(v1.value==TIPO.DOUBLE or v1.value==TIPO.ENTERO or v1.value == TIPO.FLOAT):
        return True
    return False

class TIPO(Enum):
    ERROR = 0
    ENTERO = 1
    DOUBLE = 2
    STRING = 3
    FLOAT = 4
    ARRAY = 5
    PUNTERO = 6

class TIPO_TEMP(Enum):
    ERROR = 0
    VALOR = 1
    EXPRESION = 2
    INSTRUCCION = 3

class Valor():
    def __init__(self,tipo,value):
        self.tipo = tipo 
        self.value = value 


def operarSuma(v,b):
    if(v.value==TIPO.ENTERO):
        if(b.value == TIPO.ENTERO):
            return TIPO.ENTERO
        elif(b.value == TIPO.FLOAT):
            return TIPO.FLOAT
        elif(b.value == TIPO.DOUBLE):
            return TIPO.DOUBLE
        else:
            return TIPO.ERROR
    elif(v.value==TIPO.FLOAT):
        if(b.value == TIPO.ENTERO):
            return TIPO.FLOAT
        elif(b.value == TIPO.FLOAT):
            return TIPO.FLOAT
        elif(b.value == TIPO.DOUBLE):
            return TIPO.FLOAT
        else:
            return TIPO.ERROR
    elif(v.value==TIPO.DOUBLE):
        if(b.value == TIPO.ENTERO):
            return TIPO.DOUBLE
        elif(b.value == TIPO.FLOAT):
            return TIPO.FLOAT
        elif(b.value == TIPO.DOUBLE):
            return TIPO.DOUBLE
        else:
            return TIPO.ERROR
    elif(v.value==TIPO.STRING):
        if(b.value == TIPO.STRING):
            return TIPO.STRING
        else:
            return TIPO.ERROR
    return TIPO.ERROR

 
 
def operarNumerico(v,b):
    if(v.value==TIPO.ENTERO):
        if(b.value == TIPO.ENTERO):
            return TIPO.ENTERO
        elif(b.value == TIPO.FLOAT):
            return TIPO.FLOAT
        elif(b.value == TIPO.DOUBLE):
            return TIPO.DOUBLE
        else:
            return TIPO.ERROR
    elif(v.value==TIPO.FLOAT):
        if(b.value == TIPO.ENTERO):
            return TIPO.FLOAT
        elif(b.value == TIPO.FLOAT):
            return TIPO.FLOAT
        elif(b.value == TIPO.DOUBLE):
            return TIPO.FLOAT
        else:
            return TIPO.ERROR
    elif(v.value==TIPO.DOUBLE):
        if(b.value == TIPO.ENTERO):
            return TIPO.DOUBLE
        elif(b.value == TIPO.FLOAT):
            return TIPO.FLOAT
        elif(b.value == TIPO.DOUBLE):
            return TIPO.DOUBLE
        else:
            return TIPO.ERROR
    return TIPO.ERROR

 