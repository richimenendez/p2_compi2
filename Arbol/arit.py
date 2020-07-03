from Arbol.valores import *
from Arbol.value import * 


# -------------------------------------------------- SUMA  ---------------------------------------------------------------------
class Suma():
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
            return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+"\n"+str(temp) +" = "+str(val1.temporal) + " + "+str(val2.temporal)+";", temp, tipo,str(val1.temporal)+",+,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver Entero"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  :  Suma (+)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTa: "+str(e))
            return "error\n"

    def gramAsc(self):
        pass 

# -------------------------------------------------- Resta  ---------------------------------------------------------------------
class Resta():
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
            tipo = operarNumerico(val1,val2)
            if(tipo==TIPO.ERROR):
                 return valorTemporal(TIPO_TEMP.ERROR, "TIPOS INCOMPATIBLES","",TIPO.ERROR,"","")
            return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+ "\n"+str(temp) +" = "+str(val1.temporal) + " - "+str(val2.temporal)+";", temp, tipo,str(val1.temporal)+",-,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver Entero"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  :  Resta (-)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTb: "+str(e))
            return "error\n"

    def gramAsc(self):
        pass 

# -------------------------------------------------- Multi  ---------------------------------------------------------------------
class Multi():
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
            tipo = operarNumerico(val1,val2)
            if(tipo==TIPO.ERROR):
                 return valorTemporal(TIPO_TEMP.ERROR, "TIPOS INCOMPATIBLES","",TIPO.ERROR,"","")
            return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+ "\n"+str(temp) +" = "+str(val1.temporal) + " * "+str(val2.temporal)+";", temp, tipo,str(val1.temporal)+",*,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver Entero"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  :  Multi (*)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTc: "+str(e))
            return "error\n"

    def gramAsc(self):
        pass 

# -------------------------------------------------- Divi  ---------------------------------------------------------------------
class Divi():
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
            tipo = operarNumerico(val1,val2)
            if(tipo==TIPO.ERROR):
                 return valorTemporal(TIPO_TEMP.ERROR, "TIPOS INCOMPATIBLES","",TIPO.ERROR,"","")
            return valorTemporal(TIPO_TEMP.EXPRESION,  val1.cadena+val2.cadena+"\n"+str(temp) +" = "+str(val1.temporal) + " / "+str(val2.temporal)+";", temp, tipo,str(val1.temporal)+",/,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver Entero"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  :  Division (/)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTd: "+str(e))
            return "error\n"

    def gramAsc(self):
        pass 

# -------------------------------------------------- mODULO  ---------------------------------------------------------------------
class Modulo():
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
            tipo = operarNumerico(val1,val2)
            if(tipo==TIPO.ERROR):
                 return valorTemporal(TIPO_TEMP.ERROR, val1.cadena+val2.cadena+ "TIPOS INCOMPATIBLES","",TIPO.ERROR,"","")
            return valorTemporal(TIPO_TEMP.EXPRESION, "\n"+str(temp) +" = "+str(val1.temporal) + " % "+str(val2.temporal)+";", temp, tipo,str(val1.temporal)+",%,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver Entero"),"","")
    
    def ast(self):
        try:    
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  :  Modulo (%)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTe: "+str(e))
            return "error\n"

    def gramAsc(self):
        pass 

# -------------------------------------------------- CAST  ---------------------------------------------------------------------
class Casteo():
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2

    def ejecutar(self,ts,ex): 
        val2 = self.v2.ejecutar(ts,ex)
        if(val2.tipo==TIPO_TEMP.ERROR):
            return val2
        try:
            temp = ts.generarTemporal()
            tipo = TIPO.ERROR
            if(self.v1 == "int"):
                tipo = TIPO.ENTERO 
            elif(self.v1 == "char"):
                tipo = TIPO.STRING 
            elif(self.v1 == "double"):
                tipo = TIPO.DOUBLE 
            elif(self.v1 == "float"):
                tipo = TIPO.FLOAT 
                self.v1 = "double"
            
            if(tipo==TIPO.ERROR):
                 return valorTemporal(TIPO_TEMP.ERROR, "TIPOS INCOMPATIBLES","",TIPO.ERROR,"","")
            return valorTemporal(TIPO_TEMP.EXPRESION,   val2.cadena+"\n"+str(temp) +" = (" +self.v1 +")"+str(val2.temporal)  +";", temp, tipo,"","") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver Entero"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  :  Casteo ()\"]\nn"+node+"-> "+self.v2.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTf: "+str(e))
            return "error\n"

    def gramAsc(self):
        pass 

# -------------------------------------------------- INCREMENTABLE  ---------------------------------------------------------------------
class Incremento():
    def __init__(self,v1,v2):
        self.v1 = v1

    def ejecutar(self,ts,ex):
        val1 = self.v1.ejecutar(ts,ex)
        if(val1.tipo==TIPO_TEMP.ERROR):
            return val1
        try:
            return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+"\n"+str(val1.temporal) +" = "+str(val1.temporal) + " + 1;", temp, val1.value,str(val1.temporal) + ",+,1","") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver Entero"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  :  Incremento ()\"]\nn"+node+"-> "+self.v1.ast() 
            return v
        
        except Exception as e:
            print("ERROR-ASTg: "+str(e))
            return "error\n"

    def gramAsc(self):
        pass 

# -------------------------------------------------- DECREMENTO  ---------------------------------------------------------------------
class Decremento():
    def __init__(self,v1,v2):
        self.v1 = v1

    def ejecutar(self,ts,ex):
        val1 = self.v1.ejecutar(ts,ex)
        if(val1.tipo==TIPO_TEMP.ERROR):
            return val1
        try:
            return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+"\n"+str(val1.temporal) +" = "+str(val1.temporal) + " - 1;", temp, val1.value,str(val1.temporal) + ",-,1","") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver Entero"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  :  Decremento \"]\nn"+node+"-> "+self.v1.ast() 
            return v
        
        except Exception as e:
            print("ERROR-ASTh: "+str(e))
            return "error\n"

    def gramAsc(self):
        pass 

# -------------------------------------------------- Resta2  ---------------------------------------------------------------------
class Resta2():
    def __init__(self,v1,v2):
        self.v1 = v1

    def ejecutar(self,ts,ex):
        val1 = self.v1.ejecutar(ts,ex)
        temp = ts.generarTemporal()
        if(val1.tipo==TIPO_TEMP.ERROR):
            return val1
        try:
            return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+"\n"+str(temp) +" = - "+str(val1.temporal) + ";", temp, val1.value,"-,"+str(val1.temporal) + ",","") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver negar" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver negar"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  :  Resta2 (-) Exp\"]\nn"+node+"-> "+self.v1.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTi: "+str(e))
            return "error\n"

    def gramAsc(self):
        pass 

# -------------------------------------------------- Sizeof  ---------------------------------------------------------------------
class Tamano():
    def __init__(self,v1,v2):
        self.v1 = v1

    def ejecutar(self,ts,ex):
        val1 = self.v1.ejecutar(ts,ex)
        temp = ts.generarTemporal()
        val = ""
        if(val1.tipo==TIPO_TEMP.ERROR):
            return val1
        if(val1.value == TIPO.ENTERO):
            val = "4"
        elif(val1.value == TIPO.STRING):
            val = "1"
        elif(val1.value == TIPO.FLOAT):
            val = "2"
        try:
            return valorTemporal(TIPO_TEMP.VALOR, val1.cadena, val, TIPO.ENTERO,"","") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver negar" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver negar"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  :  SizeOf (-) Exp\"]\nn"+node+"-> "+self.v1.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTj: "+str(e))
            return "error\n"

    def gramAsc(self):
        pass 
