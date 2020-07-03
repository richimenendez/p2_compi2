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
            return valorTemporal(TIPO_TEMP.EXPRESION,  val1.cadena+val2.cadena+"\n"+str(temp) +" = "+str(val1.temporal) + " > "+str(val2.temporal)+";", temp, tipo, str(val1.temporal)+",>,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver Entero"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : Mayor (>)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTt: "+str(e))
            return "error\n"
 
    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : Mayor (>)\"]\nn"+node+"-> "+self.v1.gda(nodo)+"\n n"+node+" -> "+self.v2.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"



    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E > E <br/> </p></td> 
        <td><p> if(t[2]==">")<br>
        t[0]  = May(t[1],t[3]) </p></td> 
        </tr>'''+self.v1.grammar()+self.v2.grammar())
        return v
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
            return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+ "\n"+str(temp) +" = "+str(val1.temporal) + " < "+str(val2.temporal)+";", temp, tipo,str(val1.temporal)+",<,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver Entero"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : Menor (<)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTu: "+str(e))
            return "error\n"
    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : Mayor (<)\"]\nn"+node+"-> "+self.v1.gda(nodo)+"\n n"+node+" -> "+self.v2.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"


    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E < E <br/> </p></td> 
        <td><p> if(t[2]=="<")<br>
        t[0]  = Men(t[1],t[3]) </p></td> 
        </tr>'''+self.v1.grammar()+self.v2.grammar())
        return v

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
            return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+ "\n"+str(temp) +" = "+str(val1.temporal) + " >= "+str(val2.temporal)+";", temp,   tipo,str(val1.temporal)+",>=,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver Entero"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : MayorQue (>=)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTv: "+str(e))
            return "error\n"

    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  :  (>=)\"]\nn"+node+"-> "+self.v1.gda(nodo)+"\n n"+node+" -> "+self.v2.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"

    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E <= E <br/> </p></td> 
        <td><p> if(t[2]=="<=")<br>
        t[0]  = MeI(t[1],t[3]) </p></td> 
        </tr>'''+self.v1.grammar()+self.v2.grammar())
        return v

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
            return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+ "\n"+str(temp) +" = "+str(val1.temporal) + " <= "+str(val2.temporal)+";", temp, tipo,str(val1.temporal)+",<=,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver Entero"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : MenorQue (<=)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTw: "+str(e))
            return "error\n"
    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  :<=\"]\nn"+node+"-> "+self.v1.gda(nodo)+"\n n"+node+" -> "+self.v2.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"


    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E >= E <br/> </p></td> 
        <td><p> if(t[2]==">=")<br>
        t[0]  = MaI(t[1],t[3]) </p></td> 
        </tr>'''+self.v1.grammar()+self.v2.grammar())
        return v

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
            return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+ "\n"+str(temp) +" = "+str(val1.temporal) + " == "+str(val2.temporal)+";", temp, tipo,str(val1.temporal)+",==,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver Entero"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : Igual (==)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTx: "+str(e))
            return "error\n"

    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  :==\"]\nn"+node+"-> "+self.v1.gda(nodo)+"\n n"+node+" -> "+self.v2.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"


    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E == E <br/> </p></td> 
        <td><p> if(t[2]=="==")<br>
        t[0]  = Igual(t[1],t[3]) </p></td> 
        </tr>'''+self.v1.grammar()+self.v2.grammar())
        return v
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
            return valorTemporal(TIPO_TEMP.EXPRESION,  val1.cadena+val2.cadena+"\n"+str(temp) +" = "+str(val1.temporal) + " != "+str(val2.temporal)+";", temp, tipo,str(val1.temporal)+",!=,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver Entero"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : Desigual (!=)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTy: "+str(e))
            return "error\n"

    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : !=\"]\nn"+node+"-> "+self.v1.gda(nodo)+"\n n"+node+" -> "+self.v2.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"


    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E != E <br/> </p></td> 
        <td><p> if(t[2]=="!=")<br>
        t[0]  = Desigual(t[1],t[3]) </p></td> 
        </tr>'''+self.v1.grammar()+self.v2.grammar())
        return v
