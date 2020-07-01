from Arbol.valores import *
from Arbol.value import * 

# -------------------------------------------------- Mayor  ---------------------------------------------------------------------
class Mayor():
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2

    def ejecutar(self,ts,ex):
        val1 = self.v1.ejecutar(ts,ex)
        if(val1.tipo==TIPO_TEMP.ERROR):
            return val1
        val2 = self.v2.ejecutar(ts,ex)
        if(val2.tipo==TIPO_TEMP.ERROR):
            return val2
        try:
            temp = ts.generarTemporal()
            tipo = operarSuma(val1,val2)
            if(tipo==TIPO.ERROR):
                 return valorTemporal(TIPO_TEMP.ERROR, "TIPOS INCOMPATIBLES","",TIPO.ERROR,"","")
            return valorTemporal(TIPO_TEMP.EXPRESION, "\n"+str(temp) +" = "+str(val1.temporal) + " > "+str(val2.temporal)+";", temp, tipo, tipo,str(val1.temporal)+",>,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver Entero"),"","")
    
    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" Exp  : Mayor (>)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
        return v

    def gramAsc(self):
        pass 

# -------------------------------------------------- Menor  ---------------------------------------------------------------------
class Menor():
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2

    def ejecutar(self,ts,ex):
        val1 = self.v1.ejecutar(ts,ex)
        if(val1.tipo==TIPO_TEMP.ERROR):
            return val1
        val2 = self.v2.ejecutar(ts,ex)
        if(val2.tipo==TIPO_TEMP.ERROR):
            return val2
        try:
            temp = ts.generarTemporal()
            tipo = operarSuma(val1,val2)
            if(tipo==TIPO.ERROR):
                 return valorTemporal(TIPO_TEMP.ERROR, "TIPOS INCOMPATIBLES","",TIPO.ERROR,"","")
            return valorTemporal(TIPO_TEMP.EXPRESION, "\n"+str(temp) +" = "+str(val1.temporal) + " < "+str(val2.temporal)+";", temp, tipo, tipo,str(val1.temporal)+",<,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver Entero"),"","")
    
    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" Exp  : Menor (<)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
        return v

    def gramAsc(self):
        pass 

# -------------------------------------------------- MayorQue  ---------------------------------------------------------------------
class MayorQue():
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2

    def ejecutar(self,ts,ex):
        val1 = self.v1.ejecutar(ts,ex)
        if(val1.tipo==TIPO_TEMP.ERROR):
            return val1
        val2 = self.v2.ejecutar(ts,ex)
        if(val2.tipo==TIPO_TEMP.ERROR):
            return val2
        try:
            temp = ts.generarTemporal()
            tipo = operarSuma(val1,val2)
            if(tipo==TIPO.ERROR):
                 return valorTemporal(TIPO_TEMP.ERROR, "TIPOS INCOMPATIBLES","",TIPO.ERROR,"","")
            return valorTemporal(TIPO_TEMP.EXPRESION, "\n"+str(temp) +" = "+str(val1.temporal) + " >= "+str(val2.temporal)+";", temp, tipo, tipo,str(val1.temporal)+",>=,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver Entero"),"","")
    
    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" Exp  : MayorQue (>=)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
        return v

    def gramAsc(self):
        pass 

# -------------------------------------------------- MenorQue  ---------------------------------------------------------------------
class MenorQue():
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2

    def ejecutar(self,ts,ex):
        val1 = self.v1.ejecutar(ts,ex)
        if(val1.tipo==TIPO_TEMP.ERROR):
            return val1
        val2 = self.v2.ejecutar(ts,ex)
        if(val2.tipo==TIPO_TEMP.ERROR):
            return val2
        try:
            temp = ts.generarTemporal()
            tipo = operarSuma(val1,val2)
            if(tipo==TIPO.ERROR):
                 return valorTemporal(TIPO_TEMP.ERROR, "TIPOS INCOMPATIBLES","",TIPO.ERROR,"","")
            return valorTemporal(TIPO_TEMP.EXPRESION, "\n"+str(temp) +" = "+str(val1.temporal) + " <= "+str(val2.temporal)+";", temp, tipo, tipo,str(val1.temporal)+",<=,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver Entero"),"","")
    
    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" Exp  : MenorQue (<=)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
        return v

    def gramAsc(self):
        pass 

# -------------------------------------------------- Igual  ---------------------------------------------------------------------
class Igual():
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2

    def ejecutar(self,ts,ex):
        val1 = self.v1.ejecutar(ts,ex)
        if(val1.tipo==TIPO_TEMP.ERROR):
            return val1
        val2 = self.v2.ejecutar(ts,ex)
        if(val2.tipo==TIPO_TEMP.ERROR):
            return val2
        try:
            temp = ts.generarTemporal()
            tipo = operarSuma(val1,val2)
            if(tipo==TIPO.ERROR):
                 return valorTemporal(TIPO_TEMP.ERROR, "TIPOS INCOMPATIBLES","",TIPO.ERROR,"","")
            return valorTemporal(TIPO_TEMP.EXPRESION, "\n"+str(temp) +" = "+str(val1.temporal) + " == "+str(val2.temporal)+";", temp, tipo, tipo,str(val1.temporal)+",==,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver Entero"),"","")
    
    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" Exp  : Igual (==)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
        return v

    def gramAsc(self):
        pass 

# -------------------------------------------------- Desigual  ---------------------------------------------------------------------
class Desigual():
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2

    def ejecutar(self,ts,ex):
        val1 = self.v1.ejecutar(ts,ex)
        if(val1.tipo==TIPO_TEMP.ERROR):
            return val1
        val2 = self.v2.ejecutar(ts,ex)
        if(val2.tipo==TIPO_TEMP.ERROR):
            return val2
        try:
            temp = ts.generarTemporal()
            tipo = operarSuma(val1,val2)
            if(tipo==TIPO.ERROR):
                 return valorTemporal(TIPO_TEMP.ERROR, "TIPOS INCOMPATIBLES","",TIPO.ERROR,"","")
            return valorTemporal(TIPO_TEMP.EXPRESION, "\n"+str(temp) +" = "+str(val1.temporal) + " != "+str(val2.temporal)+";", temp, tipo, tipo,str(val1.temporal)+",!=,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver Entero"),"","")
    
    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" Exp  : Desigual (!=)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
        return v

    def gramAsc(self):
        pass 
