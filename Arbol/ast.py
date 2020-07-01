from Arbol.valores import *


#----------------------------------------------------- METODO     ------------------------------------------------------------
class Metodo():
    def __init__(self,name,body,linea):
        self.name = name
        self.body = body 
        self.linea = linea
    
    def ejecutar(self,ts,ex):
        cadena = ""
        for a in self.body:
            try:
                b = a.ejecutar(ts,ex)
                cadena+=b.cadena
            except:
                pass
        return valorTemporal(TIPO_TEMP.INSTRUCCION,self.name+":"+cadena,"","","","")

#----------------------------------------------------- ASIGNACION     ------------------------------------------------------------
class Asignacion():

    def __init__(self,name,exp,linea):
        self.name = name
        self.exp = exp 
        self.linea = linea
    
    def ejecutar(self,ts,ex):
        # TD ARREGLO
        #.-.-.-.-.-
        temp=None
        flag = 0
        for dic in reversed(ts.variables):
            if self.name in dic:
                    flag = 1
                    temp = dic[self.name]
                    break
        if flag==0:
                #error
                print("NO SE ENCONTRO LA VARIABLE")
                return None
        a = self.exp.ejecutar(ts,ex)
        cad = ""
        if(a.tipo==TIPO_TEMP.VALOR):
            cad = "\n"+temp.temp+" = "+a.temporal+";"
        else: 
            cad = "\n"+a.cadena+"\n"+temp.temp+" = "+a.temporal +";"
        ts.addVariable(self.name,a.value,temp, str(self.linea))
        return valorTemporal(TIPO_TEMP.INSTRUCCION,cad,"","","","")

    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" Asignacion  : "+ self.name+"\"]\nn"+node+"-> "+self.exp.ast()
        return v

#----------------------------------------------------- DECLARACION     ------------------------------------------------------------
class Declaracion():

    def __init__(self,name,exp,linea):
        self.name = name
        self.exp = exp 
        self.linea = linea
    
    def ejecutar(self,ts,ex):
        # TD ARREGLO
        #.-.-.-.-.-
        temp = ts.generarTemporal()
        a = self.exp.ejecutar(ts,ex)
        cad = ""
        if(a.tipo==TIPO_TEMP.VALOR):
            cad = "\n"+temp+" = "+a.temporal+";"
        else: 
            cad = "\n"+a.cadena+"\n"+temp+" = "+a.temporal +";"
        ts.addVariable(self.name,a.value,temp, str(self.linea))
        return valorTemporal(TIPO_TEMP.INSTRUCCION,cad,"","","","")

    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" Asignacion  : "+ self.name+"\"]\nn"+node+"-> "+self.exp.ast()
        return v

#----------------------------------------------------- IF     ------------------------------------------------------------
class Si():
    def __init__(self,exp,cuerpo, elsif, els,linea):
        self.exp = exp 
        self.cuerpo = cuerpo
        self.linea = linea
        self.elsif = elsif
        self.els = els
    
    def ejecutar(self,ts,ex):
        # TD ARREGLO
        #.-.-.-.-.-
        tempT = ts.generarEtiqueta()
        tempF = ts.generarEtiqueta()
        a = self.exp.ejecutar(ts,ex)
        tempEnd = ts.generarEtiqueta()
        cadena = ""
        for c in self.cuerpo:
            try:
                b = c.ejecutar(ts,ex)
                cadena+=b.cadena
            except:
                pass
        v= a.cadena+"\n if ("+a.temporal+") goto "+tempT +";\n goto "+tempF+"; \n"+tempT+":\n"+cadena +"\ngoto "+tempEnd +";\n "+tempF+":\n" 
        if(self.elsif!=None):
            for c in self.elsif:
                try:
                    b =c.ejecutar(ts,tempEnd)
                    v += b.cadena
                except:
                    pass
        if(self.els!=None):
            for c in self.els:
                try:
                    b = c.ejecutar(ts,ex)
                    v+=b.cadena
                except:
                    pass
        v += "\n"+tempEnd+":"      
        return valorTemporal(TIPO_TEMP.INSTRUCCION,v,"","","","")
        
    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" Asignacion  : "+ self.name+"\"]\nn"+node+"-> "+self.exp.ast()
        return v

#----------------------------------------------------- ELSE IF     ------------------------------------------------------------
class ElseSi():
    def __init__(self,exp,cuerpo, elsif, els,linea):
        self.exp = exp 
        self.cuerpo = cuerpo
        self.linea = linea
        self.elsif = elsif
        self.els = els
    
    def ejecutar(self,ts,ex):
        # TD ARREGLO
        tempT = ts.generarEtiqueta()
        tempF = ts.generarEtiqueta()
        a = self.exp.ejecutar(ts,ex)
        tempEnd = ex
        cadena = ""
        for c in self.cuerpo:
            try:
                b = c.ejecutar(ts,ex)
                cadena+=b.cadena
            except:
                pass
        v= a.cadena+"\n if ("+a.temporal+") goto "+tempT +";\n goto "+tempF+"; \n"+tempT+":\n"+cadena +"\ngoto "+tempEnd +";\n "+tempF+":\n"  
        return valorTemporal(TIPO_TEMP.INSTRUCCION,v,"","","","")
        
    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" Asignacion  : "+ self.name+"\"]\nn"+node+"-> "+self.exp.ast()
        return v

#----------------------------------------------------- While     ------------------------------------------------------------
class Para():
    def __init__(self,exp,cuerpo,linea):
        self.exp = exp 
        self.cuerpo = cuerpo
        self.linea = linea
    
    def ejecutar(self,ts,ex):
        # TD ARREGLO
        #.-.-.-.-.-
        tempT = ts.generarEtiqueta()
        tempF = ts.generarEtiqueta()
        tempC = ts.generarEtiqueta()
        a = self.exp.ejecutar(ts,ex)
        
        cadena = ""
        for c in self.cuerpo:
            try:
                b = c.ejecutar(ts,ex)
                cadena+=b.cadena
            except:
                pass
        v="\n"+tempC + ":\n"+a.cadena+"\n if ("+a.temporal+") goto "+tempT +";\ngoto "+tempF+"; \n"+tempT+":\n"+cadena +"\ngoto "+ tempC+";\n "+tempF+":\n"       
        return valorTemporal(TIPO_TEMP.INSTRUCCION,v,"","","","")
        
    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" While  : "+ self.name+"\"]\nn"+node+"-> "+self.exp.ast()
        return v

#----------------------------------------------------- Do While     ------------------------------------------------------------
class NekoPara():
    def __init__(self,exp,cuerpo,linea):
        self.exp = exp 
        self.cuerpo = cuerpo
        self.linea = linea
    
    def ejecutar(self,ts,ex):
        # TD ARREGLO
        #.-.-.-.-.-
        tempT = ts.generarEtiqueta()
        tempF = ts.generarEtiqueta()
        tempC = ts.generarEtiqueta()
        a = self.exp.ejecutar(ts,ex)
        
        cadena = ""
        for c in self.cuerpo:
            try:
                b = c.ejecutar(ts,ex)
                cadena+=b.cadena
            except:
                pass
        v="\n"+ tempC + ":\n"+cadena+a.cadena+"\n if ("+a.temporal+") goto "+tempC +";\ngoto "+tempF+"; "+"\n "+tempF+":\n"       
        return valorTemporal(TIPO_TEMP.INSTRUCCION,v,"","","","")
        
    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" While  : "+ self.name+"\"]\nn"+node+"-> "+self.exp.ast()
        return v

#----------------------------------------------------- Switch     ------------------------------------------------------------
class Cual():
    def __init__(self,exp,cuerpo,linea):
        self.exp = exp 
        self.cuerpo = cuerpo
        self.linea = linea
    
    def ejecutar(self,ts,ex):
        # TD ARREGLO
        #.-.-.-.-.-
        tempT = ts.generarEtiqueta()
        tempF = ts.generarEtiqueta()
        tempC = ts.generarEtiqueta()
        a = self.exp.ejecutar(ts,ex)
        
        cadena = ""
        for c in self.cuerpo:
            try:
                b = c.ejecutar(ts,ex)
                cadena+=b.cadena
            except:
                pass
        v="\n"+ tempC + ":\n"+cadena+a.cadena+"\n if ("+a.temporal+") goto "+tempC +";\ngoto "+tempF+"; "+"\n "+tempF+":\n"       
        return valorTemporal(TIPO_TEMP.INSTRUCCION,v,"","","","")
        
    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" While  : "+ self.name+"\"]\nn"+node+"-> "+self.exp.ast()
        return v


#----------------------------------------------------- PrintF     ------------------------------------------------------------
import re
class Printf():
    def __init__(self,exp,cuerpo,linea):
        self.exp = exp 
        self.cuerpo = cuerpo
        self.linea = linea
    
    def ejecutar(self,ts,ex):
        # TD ARREGLO
        #.-.-.-.-.-
        cadena = ""
        prints=""
        if self.cuerpo != None:
            for x in self.cuerpo:
                try:
                    v = x.ejecutar(ts,ex)
                    cadena+=v.cadena
                    print(cadena)
                    self.exp = re.sub(r"[\%][a-zA-Z]","",self.exp,1)
                    prints  += "\nprint("+v.temporal+");"
                except Exception as e:
                    print("ERROR: " + e)           
        else:
            print("No hay params")

        v2="\n"+cadena+"\n print (\'"+self.exp+"\');"+prints       
        return valorTemporal(TIPO_TEMP.INSTRUCCION,v2,"","","","")
        
    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" While  : "+ self.name+"\"]\nn"+node+"-> "+self.exp.ast()
        return v


#----------------------------------------------------- ReadF     ------------------------------------------------------------
class Readf():
    def __init__(self,linea):
        self.linea = linea
    
    def ejecutar(self,ts,ex):
        # TD ARREGLO
        #.-.-.-.-.-
        cadena = ""
        prints=""
        return valorTemporal(TIPO_TEMP.VALOR,"","read()",TIPO.ENTERO,"","")
        
    def ast(self):
        node = getHash(self)
        v = "n"+node+"\n n"+node+"[label=\" While  : "+ self.name+"\"]\nn"+node+"-> "+self.exp.ast()
        return v
