from Arbol.value import *

class valorTemporal():
    def __init__(self, tipo, cadena, temporal,valueT):
        self.tipo = tipo
        self.cadena = cadena
        self.temporal = temporal
        self.value = value 
        self.true = []
        self.false = []

    def __init__(self, tipo, cadena, temporal,value, true,false):
        self.tipo = tipo
        self.cadena = cadena
        self.temporal = temporal
        self.value = value 
        self.true = true
        self.false = false



# -------------------------------------------------- NODO ENTERO  ---------------------------------------------------------------------
class ValorEntero():
    def __init__(self,valor):
        self.valor = valor

    def ejecutar(self,ts,ex):
        try:
            v= int(self.valor)
            return valorTemporal(TIPO_TEMP.VALOR, "", str(self.valor), TIPO.ENTERO,"","") 
        except:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero","",TIPO.ERROR,"","")
    
    def ast(self):
        node = str(getHash(self))
        v = "n"+node+"\n n"+node+"[label = \" Entero : "+str(self.valor)+"\"]"
        return v    

    def gda(self,nodo):
        node = str(nodo) + str(getHash(self.valor))
        v = "n"+node+"\n n"+node+"[label = \" Entero : "+str(self.valor)+"\"]"
        return v



    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  entero <br/> </p></td> 
        <td><p>
        t[0]  = ValorEntero(t[1]) </p></td> 
        </tr>''' )
        return v


# -------------------------------------------------- NODO DOBLE  ---------------------------------------------------------------------
class ValorDoble():
    def __init__(self,valor):
        self.valor = valor

    def ejecutar(self,ts,ex):
        try:
            v= float(self.valor)
            return valorTemporal(TIPO_TEMP.VALOR, "", str(self.valor), TIPO.DOUBLE,"","") 
        except:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero","", TIPO.ERROR,"","")
    
    def ast(self):
        node = str(getHash(self))
        v = "n"+node+"\n n"+node+"[label = \" Doble : "+str(self.valor)+"\"]"
        return v

    def gda(self,nodo):
        node = str(nodo) + str(getHash(self.valor))
        v = "n"+node+"\n n"+node+"[label = \" Doble : "+str(self.valor)+"\"]"
        return v

    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  double <br/> </p></td> 
        <td><p>
        t[0]  = ValorDouble(t[1]) </p></td> 
        </tr>''' )
        return v



# -------------------------------------------------- NODO DOBLE  ---------------------------------------------------------------------
class ValorString():
    def __init__(self,valor):
        self.valor = valor

    def ejecutar(self,ts,ex):
        try:
            return valorTemporal(TIPO_TEMP.VALOR, "", str(self.valor), TIPO.STRING,"","") 
        except:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver String","", TIPO.ERROR,"","")
    
    def ast(self):
        node = str(getHash(self))
        v = "n"+node+"\n n"+node+"[label = \" STRING : "+str(self.valor).replace("\"","")+"\"]"
        return v

    def gda(self,nodo):
        node = str(nodo) + str(getHash(self.valor))
        v = "n"+node+"\n n"+node+"[label = \" String : "+str(self.valor)+"\"]"
        return v
 

    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  String <br/> </p></td> 
        <td><p>
        t[0]  = ValorString(t[1]) </p></td> 
        </tr>''' )
        return v


# -------------------------------------------------- NODO Float  ---------------------------------------------------------------------
class ValorFloat():    
    def __init__(self,valor):
        self.valor = valor

    def ejecutar(self,ts,ex):
        try:
            return valorTemporal(TIPO_TEMP.VALOR, "", str(self.valor), TIPO.FLOAT,"","") 
        except:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero","",TIPO.ERROR,"","")
    
    def ast(self):
        node = str(getHash(self))
        v = "n"+node+"\n n"+node+"[label = \" Float : "+str(self.valor)+"\"]"
        return v

    def gda(self,nodo):
        node = str(nodo) + str(getHash(self.valor))
        v = "n"+node+"\n n"+node+"[label = \" Float : "+str(self.valor)+"\"]"
        return v


    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  float <br/> </p></td> 
        <td><p>
        t[0]  = valorFloat(t[1]) </p></td> 
        </tr>''' )
        return v


# -------------------------------------------------- NODO Varibvle   ---------------------------------------------------------------------
class ValorVariable():
    def __init__(self,valor, access):
        self.valor = valor
        self.access = access

    def ejecutar(self,ts,ex):
        v=""
        flag = 0
        try:
            for dic in reversed(ts.variables):
                if self.valor in dic:
                    flag = 1
                    v = dic[self.valor]
                    break

            if flag==0:
                return valorTemporal(TIPO_TEMP.ERROR, "No existe la variable!!!","", TIPO.ERROR,"","")
            
            cad = ""
            acs = ""
            index = list() 
            tp = None 
            if(self.access != None):
                for x in self.access:
                    if(isinstance(x, ValorAcceso)):
                        acs += "['"+x.valor+"']"
                    else:
                        z = x.ejecutar(ts,ex)
                        cad += z.cadena
                        acs += "["+z.temporal+"]" 
            return valorTemporal(TIPO_TEMP.VALOR, cad, v.temp+acs, v.tipo,"","") 
        except Exception as e:
            print("Error:  "+str(e))
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver la variable","", TIPO.ERROR,"","")
    
    def ast(self):
        node = str(getHash(self))
        v = "n"+node+"\n n"+node+"[label = \" Variable : "+str(self.valor)+"\"]"
        return v

    def gda(self,nodo):
        node = str(nodo) + str(getHash(self.valor))
        v = "n"+node+"\n n"+node+"[label = \" Variable : "+str(self.valor)+"\"]"
        return v
 

    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  id Lacs <br/> </p></td> 
        <td><p>
        t[0]  = ValorVariable(t[1],t[2]) </p></td> 
        </tr>''' )
        return v




# -------------------------------------------------- NODO ARRAY  ---------------------------------------------------------------------
class ValorArray2():    
    def __init__(self,valor):
        self.valor = valor

    def ejecutar(self,ts,ex):
        try:
            a = self.valor.ejecutar(ts,ex)
            return valorTemporal(TIPO_TEMP.VALOR, a.cadena, a.temporal, a.tipo,"","") 
        except:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero","",TIPO.ERROR,"","")
    
    def ast(self):
        node = str(getHash(self))
        v = "n"+node+"\n n"+node+"[label = \" [] : \"]"
        return v

    def gda(self,nodo):
        node = str(nodo) + str(getHash(self.valor))
        v = "n"+node+"\n n"+node+"[label = \" []\"]"
        return v
 

    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  { Lexp } <br/> </p></td> 
        <td><p>
        t[0]  = ValorArray(t[1]) </p></td> 
        </tr>''' )
        return v



# -------------------------------------------------- NODO ARRAY  ---------------------------------------------------------------------
class ValorArray():    
    def __init__(self,valores):
        self.valor = valores

    def ejecutar(self,ts,ex):
        try: 
            return valorTemporal(TIPO_TEMP.VALOR,"", "", TIPO.ARRAY,"","") 
        except:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero","",TIPO.ERROR,"","")
    
    def ast(self):
        node = str(getHash(self))
        v = "n"+node+"\n n"+node+"[label = \" .X : \"]"
        return v

    def gda(self,nodo):
        node = str(nodo) + str(getHash(self.valor))
        v = "n"+node+"\n n"+node+"[label = \" .X \"]"
        return v

    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  [exp] <br/> </p></td> 
        <td><p>
        t[0]  = ValorArray(t[1]) </p></td> 
        </tr>''' )
        return v


# ------------------------
# -------------------------------------------------- NODO Acceso  ---------------------------------------------------------------------
class ValorAcceso():    
    def __init__(self,valor):
        self.valor = valor

    def ejecutar(self,ts,ex):
        try:
            a = self.valor.ejecutar()

            return valorTemporal(TIPO_TEMP.VALOR, "", a.temporal, a.temporal,"","") 
        except:
            return valorTemporal(TIPO_TEMP.ERROR, "No se pudo volver Entero","",TIPO.ERROR,"","")
    
    def ast(self):
        node = str(getHash(self))
        v = "n"+node+"\n n"+node+"[label = \" Acceso : \"]"
        return v
    def gda(self,nodo):
        node = str(nodo) + str(getHash(self.valor))
        v = "n"+node+"\n n"+node+"[label = \" Acceso :\"]"
        return v



    def grammar(self):
        v =('''
        <tr> 
        <td> <p>EXP  =>  .id <br/> </p></td> 
        <td><p>
        t[0]  = Acceso(t[1]) </p></td> 
        </tr>''' )
        return v







