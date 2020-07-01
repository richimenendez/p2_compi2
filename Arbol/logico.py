from Arbol.valores import *
from Arbol.value import * 

# -------------------------------------------------- OR  ---------------------------------------------------------------------
class Or():
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
            return valorTemporal(TIPO_TEMP.EXPRESION, "\n"+str(temp) +" = "+str(val1.temporal) + " || "+str(val2.temporal)+";", temp, tipo, tipo,str(val1.temporal)+",||,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo resolver el OR"),"","")
    
    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" Exp  : Or (||)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
        return v

    def gramAsc(self):
        pass 


# -------------------------------------------------- AND  ---------------------------------------------------------------------
class And():
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
            return valorTemporal(TIPO_TEMP.EXPRESION, "\n"+str(temp) +" = "+str(val1.temporal) + " && "+str(val2.temporal)+";", temp, tipo, tipo,str(val1.temporal)+",&&,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver AND" + str(exp),"", Valor(TIPO.ERROR,"No se pudo resolver el AND"),"","")
    
    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" Exp  : And (&&)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
        return v

    def gramAsc(self):
        pass 


# -------------------------------------------------- BAND  ---------------------------------------------------------------------
class BAnd():
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
            return valorTemporal(TIPO_TEMP.EXPRESION, "\n"+str(temp) +" = "+str(val1.temporal) + " & "+str(val2.temporal)+";", temp, tipo, tipo,str(val1.temporal)+",&,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver bAND" + str(exp),"", Valor(TIPO.ERROR,"No se pudo resolver el bAND"),"","")
    
    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" Exp  : And (&&)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
        return v

    def gramAsc(self):
        pass 




# -------------------------------------------------- BOR  ---------------------------------------------------------------------
class BOr():
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
            return valorTemporal(TIPO_TEMP.EXPRESION, "\n"+str(temp) +" = "+str(val1.temporal) + " | "+str(val2.temporal)+";", temp, tipo, tipo,str(val1.temporal)+",|,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver bOR" + str(exp),"", Valor(TIPO.ERROR,"No se pudo resolver el bOR"),"","")
    
    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" Exp  : BOr (|)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
        return v

    def gramAsc(self):
        pass 

    


# -------------------------------------------------- Left  ---------------------------------------------------------------------
class Left():
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
            return valorTemporal(TIPO_TEMP.EXPRESION, "\n"+str(temp) +" = "+str(val1.temporal) + " << "+str(val2.temporal)+";", temp, tipo, tipo,str(val1.temporal)+",<<,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Left" + str(exp),"", Valor(TIPO.ERROR,"No se pudo resolver el Left"),"","")
    
    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" Exp  : Left (<<)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
        return v

    def gramAsc(self):
        pass 


    


# -------------------------------------------------- Right  ---------------------------------------------------------------------
class Right():
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
            return valorTemporal(TIPO_TEMP.EXPRESION, "\n"+str(temp) +" = "+str(val1.temporal) + " >> "+str(val2.temporal)+";", temp, tipo, tipo,str(val1.temporal)+",>>,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Right" + str(exp),"", Valor(TIPO.ERROR,"No se pudo resolver el Right"),"","")
    
    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" Exp  : Right (>>)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
        return v

    def gramAsc(self):
        pass 


# -------------------------------------------------- Not  ---------------------------------------------------------------------
class Not():
    def __init__(self,v1,v2):
        self.v1 = v1

    def ejecutar(self,ts,ex):
        val1 = self.v1.ejecutar(ts,ex)
        if(val1.tipo==TIPO_TEMP.ERROR):
            return val1
        try:
            return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+"\n"+str(val1.temporal) +" = ! "+str(val1.temporal) + ";", temp, val1.tipo,"!,"+str(val1.temporal)+",","") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver negar" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver negar"),"","")
    
    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" Exp  :  Not (!) Exp\"]\nn"+node+"-> "+self.v1.ast()
        return v

    def gramAsc(self):
        pass 

# -------------------------------------------------- BNot  ---------------------------------------------------------------------
class BNot():
    def __init__(self,v1,v2):
        self.v1 = v1

    def ejecutar(self,ts,ex):
        val1 = self.v1.ejecutar(ts,ex)
        if(val1.tipo==TIPO_TEMP.ERROR):
            return val1
        try:
            return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+"\n"+str(val1.temporal) +" = ~ "+str(val1.temporal) + ";", temp, val1.tipo,"~,"+str(val1.temporal)+",","") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver negar" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver negar"),"","")
    
    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" Exp  :  BNot (~) Exp\"]\nn"+node+"-> "+self.v1.ast()
        return v

    def gramAsc(self):
        pass 



