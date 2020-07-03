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
            if(val2.temporal == "0"):
                ts.optimizacion.append("REGLA 12:   X + 0 PASA A SER X  entre:  "+str(val1.temporal) + "   y   " + str(val2.temporal))
                return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+"\n"+str(temp) +" = "+str(val1.temporal)+";", temp, tipo,str(val1.temporal)+",+,"+str(val2.temporal),"") 
            if(val1.temporal == "0"):
                ts.optimizacion.append("REGLA 12:   X + 0 PASA A SER X  entre:  "+str(val1.temporal) + "   y   " + str(val2.temporal))
                return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+"\n"+str(temp) +" = "+str(val2.temporal)+";", temp, tipo,str(val1.temporal)+",+,"+str(val2.temporal),"")                 
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

    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : +\"]\nn"+node+"-> "+self.v1.gda(nodo)+"\n n"+node+" -> "+self.v2.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"

    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E + E <br/> </p></td> 
        <td><p> if(t[2]=="+")<br>
        t[0]  = Suma(t[1],t[3]) </p></td> 
        </tr>'''+self.v1.grammar()+self.v2.grammar())
        return v

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
            if(val2.temporal == "0"):
                ts.optimizacion.append("REGLA 13:   X - 0 PASA A SER X  entre:  "+str(val1.temporal) + "   y   " + str(val2.temporal))
                return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+"\n"+str(temp) +" = "+str(val1.temporal)+";", temp, tipo,str(val1.temporal)+",+,"+str(val2.temporal),"") 
            if(val1.temporal == "0"):
                ts.optimizacion.append("REGLA 13:   X - 0 PASA A SER X  entre:  "+str(val1.temporal) + "   y   " + str(val2.temporal))
                return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+"\n"+str(temp) +" = "+str(val2.temporal)+";", temp, tipo,str(val1.temporal)+",+,"+str(val2.temporal),"")       
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

    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : -\"]\nn"+node+"-> "+self.v1.gda(nodo)+"\n n"+node+" -> "+self.v2.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"

    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E - E <br/> </p></td> 
        <td><p> if(t[2]=="-")<br>
        t[0]  = Resta(t[1],t[3]) </p></td> 
        </tr>'''+self.v1.grammar()+self.v2.grammar())
        return v

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
            if(val2.temporal == "1"):
                ts.optimizacion.append("REGLA 14:   X * 1 PASA A SER X  entre:  "+str(val1.temporal) + "   y   " + str(val2.temporal))
                return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+"\n"+str(temp) +" = "+str(val1.temporal)+";", temp, tipo,str(val1.temporal)+",+,"+str(val2.temporal),"") 
            if(val1.temporal == "1"):
                ts.optimizacion.append("REGLA 14:   1 * x PASA A SER X  entre:  "+str(val1.temporal) + "   y   " + str(val2.temporal))
                return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+"\n"+str(temp) +" = "+str(val2.temporal)+";", temp, tipo,str(val1.temporal)+",+,"+str(val2.temporal),"")
            if(val2.temporal == "0"):
                ts.optimizacion.append("REGLA 17:   X * 0 PASA A SER 0  entre:  "+str(val1.temporal) + "   y   " + str(val2.temporal))
                return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+"\n"+str(temp) +" = 0;", temp, tipo,str(val1.temporal)+",+,"+str(val2.temporal),"") 
            if(val1.temporal == "0"):
                ts.optimizacion.append("REGLA 17:   0 * x PASA A SER 0  entre:  "+str(val1.temporal) + "   y   " + str(val2.temporal))
                return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+"\n"+str(temp) +" = 0;", temp, tipo,str(val1.temporal)+",+,"+str(val2.temporal),"")  
            if(val2.temporal == "2"):
                ts.optimizacion.append("REGLA 16:   X * 2 PASA A SER X + X  entre:  "+str(val1.temporal) + "   y   " + str(val2.temporal))
                return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+"\n"+str(temp) +" = "+ str(val1.temporal) +" + "+ str(val1.temporal) +";", temp, tipo,str(val1.temporal)+",+,"+str(val2.temporal),"") 
            if(val1.temporal == "2"):
                ts.optimizacion.append("REGLA 16:   2 * x PASA A SER X + X  entre:  "+str(val1.temporal) + "   y   " + str(val2.temporal))
                return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+"\n"+str(temp)  +" = "+ str(val2.temporal) +" + "+ str(val2.temporal) +";", temp, tipo,str(val1.temporal)+",+,"+str(val2.temporal),"")  
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
            

    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : *\"]\nn"+node+"-> "+self.v1.gda(nodo)+"\n n"+node+" -> "+self.v2.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"

    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E * E <br/> </p></td> 
        <td><p> if(t[2]=="*")<br>
        t[0]  = Multi(t[1],t[3]) </p></td> 
        </tr>'''+self.v1.grammar()+self.v2.grammar())
        return v

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
            if(val2.temporal == "1"):
                ts.optimizacion.append("REGLA 15:   X / 1 PASA A SER X  entre:  "+str(val1.temporal) + "   y   " + str(val2.temporal))
                return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+"\n"+str(temp) +" = "+str(val1.temporal)+";", temp, tipo,str(val1.temporal)+",+,"+str(val2.temporal),"") 
            if(val1.temporal == "0"):
                ts.optimizacion.append("REGLA 18:    0 / x PASA A SER 0  entre:  "+str(val1.temporal) + "   y   " + str(val2.temporal))
                return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+"\n"+str(temp) +" = 0;", temp, tipo,str(val1.temporal)+",+,"+str(val2.temporal),"")  
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


    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : /\"]\nn"+node+"-> "+self.v1.gda(nodo)+"\n n"+node+" -> "+self.v2.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"

    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E / E <br/> </p></td> 
        <td><p> if(t[2]=="/")<br>
        t[0]  = Divi(t[1],t[3]) </p></td> 
        </tr>'''+self.v1.grammar()+self.v2.grammar())
        return v
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
            return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+"\n"+str(temp) +" = "+str(val1.temporal) + " % "+str(val2.temporal)+";", temp, tipo,str(val1.temporal)+",%,"+str(val2.temporal),"") 
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

    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : %\"]\nn"+node+"-> "+self.v1.gda(nodo)+"\n n"+node+" -> "+self.v2.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"

    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E MOD E <br/> </p></td> 
        <td><p> if(t[2]=="%")<br>
        t[0]  = Modulo(t[1],t[3]) </p></td> 
        </tr>'''+self.v1.grammar()+self.v2.grammar())
        return v

# -------------------------------------------------- Ternario  ---------------------------------------------------------------------
class Ternario():
    def __init__(self,v1,v2,v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def ejecutar(self,ts,ex):
        val1 = self.v1.ejecutar(ts,ex)
        if(val1.tipo==TIPO_TEMP.ERROR):
            return val1
        val2 = self.v2.ejecutar(ts,ex)
        if(val2.tipo==TIPO_TEMP.ERROR):
            return val2
        val3 = self.v3.ejecutar(ts,ex)
        if(val3.tipo==TIPO_TEMP.ERROR):
            return val3
        
        try:
            temp = ts.generarEtiqueta()
            temp2 = ts.generarEtiqueta()
            temp3 = ts.generarTemporal()
            return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena + "\nif ("+str(val1.temporal) +")  goto "+str(temp) + "; \n "+val3.cadena+"\n"+temp3+" = "+val3.temporal+";\ngoto "+temp2+";\n"+temp+":"+val2.cadena+"\n"+temp3+" = "+val2.temporal+";\n"+temp2+":", temp3, val2.value,"","") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver Entero"),"","")
    
    def ast(self):
        try:    
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  :  Ternario (?:)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTe: "+str(e))
            return "error\n"

    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : Tenario (?:) \"]\nn"+node+"-> "+self.v1.gda(nodo)+"\n n"+node+" -> "+self.v2.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"

    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E ? E : E <br/> </p></td> 
        <td><p> if(t[2]=="?")<br>
        t[0]  = Ternario(t[1],t[3]) </p></td> 
        </tr>''')
        return v
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


    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : Casteo()\"]\nn"+node+"-> "+self.v2.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"
    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  LEFTPAR "("  int   DERPAR ")"  Exp <br/> </p></td> 
        <td><p> t[0]  = Cast2Int(t[2]) </p></td> 
        </tr>'''+self.v2.grammar())
        return v

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

    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : - E\"]\nn"+node+"-> "+self.v1.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"


    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  => - E <br/> </p></td> 
        <td><p> if(t[1]=="-")<br>
        t[0]  = Resta2(t[2]) </p></td> 
        </tr>'''+self.v1.grammar())
        return v

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

    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : SizeOf\"]\nn"+node+"-> "+self.v1.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"

    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  sizeof E <br/> </p></td> 
        <td><p> if(t[1]=="sizeof")<br>
        t[0]  = Sizeof(t[2]) </p></td> 
        </tr>'''+self.v1.grammar() )
        return v
