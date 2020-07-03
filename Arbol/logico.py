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
            return valorTemporal(TIPO_TEMP.EXPRESION,  val1.cadena+val2.cadena+"\n"+str(temp) +" = "+str(val1.temporal) + " || "+str(val2.temporal)+";", temp,  tipo,str(val1.temporal)+",||,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero" + str(exp),"", Valor(TIPO.ERROR,"No se pudo resolver el OR"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : Or (||)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTk: "+str(e))
            return "error\n"

    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : ||\"]\nn"+node+"-> "+self.v1.gda(nodo)+"\n n"+node+" -> "+self.v2.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"


    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E || E <br/> </p></td> 
        <td><p> if(t[2]=="||")<br>
        t[0]  = Suma(t[1],t[3]) </p></td> 
        </tr>'''+self.v1.grammar()+self.v2.grammar())
        return v


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
            return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+ "\n"+str(temp) +" = "+str(val1.temporal) + " && "+str(val2.temporal)+";", temp,   tipo,str(val1.temporal)+",&&,"+str(val2.temporal),"" ) 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver AND" + str(exp),"", Valor(TIPO.ERROR,"No se pudo resolver el AND"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : And (&&)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTl: "+str(e))
            return "error\n"

    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : &&\"]\nn"+node+"-> "+self.v1.gda(nodo)+"\n n"+node+" -> "+self.v2.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"


    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E && E <br/> </p></td> 
        <td><p> if(t[2]=="&&")<br>
        t[0]  = Suma(t[1],t[3]) </p></td> 
        </tr>'''+self.v1.grammar()+self.v2.grammar())
        return v

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
            return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+ "\n"+str(temp) +" = "+str(val1.temporal) + " & "+str(val2.temporal)+";", temp,  tipo,str(val1.temporal)+",&,"+str(val2.temporal),"" ) 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver bAND" + str(exp),"", Valor(TIPO.ERROR,"No se pudo resolver el bAND"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : And (&)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTm: "+str(e))
            return "error\n"

    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : &\"]\nn"+node+"-> "+self.v1.gda(nodo)+"\n n"+node+" -> "+self.v2.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"

    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E & E <br/> </p></td> 
        <td><p> if(t[2]=="&")<br>
        t[0]  = Suma(t[1],t[3]) </p></td> 
        </tr>'''+self.v1.grammar()+self.v2.grammar())
        return v




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
            return valorTemporal(TIPO_TEMP.EXPRESION,  val1.cadena+val2.cadena+"\n"+str(temp) +" = "+str(val1.temporal) + " | "+str(val2.temporal)+";", temp, tipo,  str(val1.temporal)+",|,"+str(val2.temporal),"" ) 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver bOR" + str(exp),"", Valor(TIPO.ERROR,"No se pudo resolver el bOR"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : BOr (|)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTn: "+str(e))
            return "error\n"


    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : |\"]\nn"+node+"-> "+self.v1.gda(nodo)+"\n n"+node+" -> "+self.v2.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"

    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E | E <br/> </p></td> 
        <td><p> if(t[2]=="|")<br>
        t[0]  = Suma(t[1],t[3]) </p></td> 
        </tr>'''+self.v1.grammar()+self.v2.grammar())
        return v
    
# -------------------------------------------------- BOR  ---------------------------------------------------------------------
class Xor():
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
            return valorTemporal(TIPO_TEMP.EXPRESION,  val1.cadena+val2.cadena+"\n"+str(temp) +" = "+str(val1.temporal) + " ^ "+str(val2.temporal)+";", temp, tipo,  str(val1.temporal)+",|,"+str(val2.temporal),"" ) 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Xor" + str(exp),"", Valor(TIPO.ERROR,"No se pudo resolver el bOR"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : BOr (|)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTo: "+str(e))
            return "error\n"

    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : ^\"]\nn"+node+"-> "+self.v1.gda(nodo)+"\n n"+node+" -> "+self.v2.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"

    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E ^ E <br/> </p></td> 
        <td><p> if(t[2]=="^")<br>
        t[0]  = Suma(t[1],t[3]) </p></td> 
        </tr>'''+self.v1.grammar()+self.v2.grammar())
        return v

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
            return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+val2.cadena+ "\n"+str(temp) +" = "+str(val1.temporal) + " << "+str(val2.temporal)+";", temp, tipo, str(val1.temporal)+",<<,"+str(val2.temporal),"" ) 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Left" + str(exp),"", Valor(TIPO.ERROR,"No se pudo resolver el Left"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : Left (<<)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTp: "+str(e))
            return "error\n"


    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : <<\"]\nn"+node+"-> "+self.v1.gda(nodo)+"\n n"+node+" -> "+self.v2.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"

    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E << E <br/> </p></td> 
        <td><p> if(t[2]=="<<")<br>
        t[0]  = Suma(t[1],t[3]) </p></td> 
        </tr>'''+self.v1.grammar()+self.v2.grammar())
        return v

    


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
            return valorTemporal(TIPO_TEMP.EXPRESION,  val1.cadena+val2.cadena+"\n"+str(temp) +" = "+str(val1.temporal) + " >> "+str(val2.temporal)+";", temp, tipo, str(val1.temporal)+",>>,"+str(val2.temporal),"") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Right" + str(exp),"", Valor(TIPO.ERROR,"No se pudo resolver el Right"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : Right (>>)\"]\nn"+node+"-> "+self.v1.ast()+"\n n"+node+" -> "+self.v2.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTq: "+str(e))
            return "error\n"


    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : >>\"]\nn"+node+"-> "+self.v1.gda(nodo)+"\n n"+node+" -> "+self.v2.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"

    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  E >> E <br/> </p></td> 
        <td><p> if(t[2]>>"+")<br>
        t[0]  = Suma(t[1],t[3]) </p></td> 
        </tr>'''+self.v1.grammar()+self.v2.grammar())
        return v


# -------------------------------------------------- Not  ---------------------------------------------------------------------
class Not():
    def __init__(self,v1,v2):
        self.v1 = v1

    def ejecutar(self,ts,ex):
        val1 = self.v1.ejecutar(ts,ex)
        temp = ts.generarTemporal()
        if(val1.tipo==TIPO_TEMP.ERROR):
            return val1
        try:
            return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+"\n"+str(temp) +" = ! "+str(val1.temporal) + ";", temp, val1.value,"!,"+str(val1.temporal)+",","") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver negar" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver negar"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  :  Not (!) Exp\"]\nn"+node+"-> "+self.v1.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTr: "+str(e))
            return "error\n"


    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : !\"]\nn"+node+"-> "+self.v1.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"

    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  ! E <br/> </p></td> 
        <td><p> if(t[1]=="!")<br>
        t[0]  = Suma(t[1]) </p></td> 
        </tr>'''+self.v1.grammar() )
        return v
# -------------------------------------------------- BNot  ---------------------------------------------------------------------
class BNot():
    def __init__(self,v1,v2):
        self.v1 = v1

    def ejecutar(self,ts,ex):
        val1 = self.v1.ejecutar(ts,ex)
        temp = ts.generarTemporal()
        if(val1.tipo==TIPO_TEMP.ERROR):
            return val1
        try:
            return valorTemporal(TIPO_TEMP.EXPRESION, val1.cadena+"\n"+str(temp) +" = ~ "+str(val1.temporal) + ";", temp, val1.value,"~,"+str(val1.temporal)+",","") 
        except Exception as exp:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver negar" + str(exp),"", Valor(TIPO.ERROR,"No se pudo volver negar"),"","")
    
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  :  BNot (~) Exp\"]\nn"+node+"-> "+self.v1.ast()
            return v
        
        except Exception as e:
            print("ERROR-ASTs: "+str(e))
            return "error\n"
    def gda(self,nodo):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Exp  : ~\"]\nn"+node+"-> "+self.v1.gda(nodo)
            return v
        
        except Exception as e:
            print("ERROR-GDA: "+str(e))
            return "error\n"



    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  ~ E <br/> </p></td> 
        <td><p> if(t[1]=="~")<br>
        t[0]  = Suma(t[1]) </p></td> 
        </tr>'''+self.v1.grammar() )
        return v


