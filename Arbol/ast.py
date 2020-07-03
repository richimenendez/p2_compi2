from Arbol.valores import *
from Arbol.simbolos import *

def asignarArray(arreglo,   cadena,temporal,ts,ex):
    if (isinstance(arreglo,ValorArray)):
        cad = "\n"+temporal +" = array();"
        for i in range(len(arreglo.valor)):
            if(isinstance(arreglo.valor[i],ValorArray)):
                cad2 = asignarArray(arreglo.valor[i], "",temporal+"["+str(i)+"]",ts,ex)
                cad += cad2
            else:
                v = arreglo.valor[i].ejecutar(ts,ex)
                cad+= v.cadena+ "\n"+temporal+"["+str(i)+"]"+" = "+ v.temporal+";"
        return cad
    else:
        return ""

#----------------------------------------------------- METODO     ------------------------------------------------------------
class Metodo():
    def __init__(self,name,linst,body,linea):
        self.name = name
        self.linst = linst
        self.body = body 
        self.linea = linea
    
    def ejecutar(self,ts,ex):
        ts.addEntorno()
        cadena = ""
        for a in self.body:
            try:
                b = a.ejecutar(ts,ex)
                cadena+=b.cadena
            except Exception as e:
                print("ERROR: "+str(e) +"  en  "+ self.linea)
        return valorTemporal(TIPO_TEMP.INSTRUCCION,self.name+":"+cadena,"","","","")

    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\nn"+node+"[label=\"Main\"]\n"
            for x in self.body:
                try:
                    v+="\nn"+node+" -> "+x.ast()
                except Exception as e:
                    print("AST-ERROR: ERROR GENERANDO LIENA AST - "+e )
            return v
        
        except Exception as e:
            print("ERROR-AST1: "+str(e))
            return "error\n"
#----------------------------------------------------- METODO     ------------------------------------------------------------
class AddMetodo():
    def __init__(self,name,linst,body,linea):
        self.name = name
        self.linst = linst
        self.body = body 
        self.linea = linea
    
    def ejecutar(self,ts,ex):
        cadena = ""
        ts.metodos[self.name] = Metodos(self.name, self.linst, self.body, self.linea)

    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\nn"+node+"[label=\"Metodo:"+ str(self.name)+"\"]\n"
            for x in self.body:
                try:
                    v+="\nn"+node+" -> "+x.ast()
                except Exception as e:
                    print("AST-ERROR: ERROR GENERANDO LIENA AST - "+e )
            return v
        except:
            return "error\n"
            

#----------------------------------------------------- ASIGNACION     ------------------------------------------------------------
class Asignacion():

    def __init__(self,name,arr,exp,linea):
        self.name = name
        self.exp = exp
        self.arr = arr 
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
        if(a.tipo == TIPO_TEMP.ERROR):
            ts.addError("Error Asignacion: "+a.cadena,self.linea)
            return ""
        cad = "" 
        acs = ""
        index = list()  
        if(self.arr != None):
            for x in self.arr:
                if(isinstance(x, ValorAcceso)):
                    acs += "['"+x.valor+"']"
                else:
                    z = x.ejecutar(ts,ex)
                    cad += z.cadena
                    acs += "["+z.temporal+"]" 
        if (isinstance(self.exp,ValorArray)):
            cad += asignarArray(self.exp,"",temp.temp,ts,ex) 
        elif(a.tipo==TIPO_TEMP.VALOR): 
            cad += a.cadena+"\n"+temp.temp + acs+" = "+a.temporal+";"
        else: 
            cad += "\n"+a.cadena+"\n"+temp.temp+acs+" = "+a.temporal +";"
        ts.addVariable(self.name,a.value,temp.temp, str(self.linea))
        return valorTemporal(TIPO_TEMP.INSTRUCCION,cad,"","","","")

    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Asignacion  : "+ str(self.name)+"\"]\nn"+node+"-> "+self.exp.ast()
            return v
        except:
            return "error\n"

#----------------------------------------------------- DECLARACION     ------------------------------------------------------------
class Declaracion():

    def __init__(self,name,arr,exp,linea):
        self.name = name
        self.exp = exp
        self.arr = arr 
        self.linea = linea
    
    def ejecutar(self,ts,ex):
        # TD ARREGLO
        #.-.-.-.-.-
        temp = ts.generarTemporal()
        a = self.exp.ejecutar(ts,ex)
        if(a.tipo == TIPO_TEMP.ERROR):
            ts.addError("Error Declaracion: "+a.cadena,self.linea)
            return ""
        cad = ""
        acs = ""
        index = list() 
        tp = None 
        if(self.arr != None):
            for x in self.arr:
                if(isinstance(x, ValorAcceso)):
                    acs += "['"+x.valor+"']"
                else:
                    z = x.ejecutar(ts,ex)
                    cad += z.cadena
                    acs += "["+z.temporal+"]" 

        if (isinstance(self.exp,ValorArray)):
            cad += asignarArray(self.exp,"",temp,ts,ex) 
        elif(a.tipo==TIPO_TEMP.VALOR):
            cad += a.cadena+"\n"+temp+acs+" = "+a.temporal+";" 
        else: 
            cad += "\n"+a.cadena+"\n"+temp+acs+" = "+a.temporal +";"
        ts.addVariable(self.name,a.value,temp, str(self.linea))
        ts.addVariable2(self.name,a.value,temp, str(self.linea))
        return valorTemporal(TIPO_TEMP.INSTRUCCION,cad,"","","","")

    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Declaracion  : "+ str(self.name)+"\"]\nn"+node+"-> "+self.exp.ast()
            return v
        except Exception as e:
            print("ERROR-AST2: "+str(e))
            return "error\n"

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
        if(a.tipo == TIPO_TEMP.ERROR):
            ts.addError("Error IF: "+str(a.cadena),self.linea)
            return ""
        tempEnd = ts.generarEtiqueta()
        cadena = ""
        ts.addEntorno()
        for c in self.cuerpo:
            try:
                b = c.ejecutar(ts,ex) 
                cadena+=b.cadena
            except Exception as e:
                print("ERROR EN IF:  "+str(e))  
        ts.popEntorno()
        v= a.cadena+"\n if ("+a.temporal+") goto "+tempT +";\n goto "+tempF+"; \n"+tempT+":\n"+cadena +"\ngoto "+tempEnd +";\n "+tempF+":\n" 
        if(self.elsif!=None):
            for c in self.elsif:
                try:
                    b =c.ejecutar(ts,tempEnd) 
                except:
                    pass
        if(self.els!=None):
            ts.addEntorno()
            for c in self.els:
                try:
                    b = c.ejecutar(ts,ex) 
                    v+=b.cadena
                except:
                    pass
            ts.popEntorno()
        v += "\n"+tempEnd+":"      
        return valorTemporal(TIPO_TEMP.INSTRUCCION,v,"","","","")
        
    def ast(self):
        node = str(getHash(self))
        try:
            v = "n"+node+"\n n"+node+"[label=\" If   \"]\nn"+node+"-> "+self.exp.ast()
            for x in (self.cuerpo):
                try:
                    v+="\nn"+node+"->"+x.ast()
                except:
                    pass
            if(self.elsif!=None):
                for x in self.elsif:
                    v+="\nn"+node+" -> "+x.ast()
            if(self.els!=None):
                v+="\nne"+node+"[label=\"Else\"]\nn"+node+"->ne"+node
                for z in self.els:
                    try:
                        v+="\nne"+node+"->"+z.ast()
                    except:
                        pass
            return v
        
        except Exception as e:
            print("ERROR-AST3: "+str(e))
            return "error"

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
        if(a.tipo == TIPO_TEMP.ERROR):
            ts.addError("Error ELse If: "+a.cadena,self.linea)
            return ""
        tempEnd = ex
        cadena = ""
        ts.addEntorno()
        for c in self.cuerpo:
            try:
                b = c.ejecutar(ts,ex) 
                     
                cadena+=b.cadena
            
            except:
                pass
            
        ts.popEntorno()
        v= a.cadena+"\n if ("+a.temporal+") goto "+tempT +";\n goto "+tempF+"; \n"+tempT+":\n"+cadena +"\ngoto "+tempEnd +";\n "+tempF+":\n"  
        return valorTemporal(TIPO_TEMP.INSTRUCCION,v,"","","","")
        
    def ast(self):
        node = str(getHash(self))
        try:
            v = "n"+node+"\n n"+node+"[label=\" Else If  :  \"]\nn"+node+"-> "+self.exp.ast()
            for x in (self.cuerpo):
                v+="\nn"+node+"->"+x.ast() 
            return v
        
        except Exception as e:
            print("ERROR-AST4: "+str(e))
            return "error"


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
        
        if(a.tipo == TIPO_TEMP.ERROR):
            ts.addError("Error FOR: "+a.cadena,self.linea)
            return ""
        cadena = ""
        ts.addEntorno()
        for c in self.cuerpo:  
            try:
                b = c.ejecutar(ts,ex)
                cadena+=b.cadena
            except:
                pass
            
        ts.popEntorno()
        v="\n"+tempC + ":\n"+a.cadena+"\n if ("+a.temporal+") goto "+tempT +";\ngoto "+tempF+"; \n"+tempT+":\n"+cadena +"\ngoto "+ tempC+";\n "+tempF+":\n"       
        return valorTemporal(TIPO_TEMP.INSTRUCCION,v,"","","","")
        
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" While  :  \"]\nn"+node+"-> "+self.exp.ast()
            for x in self.cuerpo:
                try:
                    v+="n"+node+"->"+x.ast()
                except:
                    pass
            return v
        
        except Exception as e:
            print("ERROR-AST5: "+str(e))
            return "error"
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
        
        if(a.tipo == TIPO_TEMP.ERROR):
            ts.addError("Error DoWhile: "+a.cadena,self.linea)
            return ""
        cadena = ""
        ts.addEntorno()
        for c in self.cuerpo:
            try:
                b = c.ejecutar(ts,ex)
                cadena+=b.cadena
            except:
                pass
        ts.popEntorno()
        v="\n"+ tempC + ":\n"+cadena+a.cadena+"\n if ("+a.temporal+") goto "+tempC +";\ngoto "+tempF+"; "+"\n "+tempF+":\n"       
        return valorTemporal(TIPO_TEMP.INSTRUCCION,v,"","","","")
        
        def ast(self):
            try:
                node = str(getHash(self))
                v = "n"+node+"\n n"+node+"[label=\" Do While  : \"]\nn"+node+"-> "+self.exp.ast()
                for x in self.cuerpo:
                    try:
                        v+="\nn"+node+"->"+x.ast()
                    except:
                        pass
                return v
            
            except Exception as e:
                print("ERROR-AST6: "+str(e))
                return "error"

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
        if(a.tipo == TIPO_TEMP.ERROR):
            ts.addError("Error Switch: "+a.cadena,self.linea)
            return ""
        
        cadena = ""
        ts.addEntorno()
        for c in self.cuerpo:
            try:
                b = c.ejecutar(ts,ex)
                cadena+=b.cadena
            except:
                pass
        v="\n"+ tempC + ":\n"+cadena+a.cadena+"\n if ("+a.temporal+") goto "+tempC +";\ngoto "+tempF+"; "+"\n "+tempF+":\n"       
        ts.popEntorno()
        return valorTemporal(TIPO_TEMP.INSTRUCCION,v,"","","","")
        
    def ast(self):
        node = getHash(self)
        return ""

#----------------------------------------------------- For     ------------------------------------------------------------
class Forr():
    def __init__(self,asig,cond,exp,cuerpo,linea):
        self.asig = asig 
        self.cond = cond
        self.exp = exp 
        self.cuerpo = cuerpo
        self.linea = linea
    
    def ejecutar(self,ts,ex):
        # TD ARREGLO
        #.-.-.-.-.-
        tempT = ts.generarEtiqueta()
        tempF = ts.generarEtiqueta()
        tempC = ts.generarEtiqueta()
        ts.addEntorno()
        pre   = self.asig.ejecutar(ts,ex)
        if(pre.tipo == TIPO_TEMP.ERROR):
            ts.addError("Error For: "+pre.cadena,self.linea)
            return ""
        condi = self.cond.ejecutar(ts,ex)
        if(condi.tipo == TIPO_TEMP.ERROR):
            ts.addError("Error For: "+condi.cadena,self.linea)
            return ""
        a     = self.exp.ejecutar(ts,ex)
        
        if(a.tipo == TIPO_TEMP.ERROR):
            ts.addError("Error For: "+a.cadena,self.linea)
            return ""
        cadena = ""
        ts.addEntorno()
        for c in self.cuerpo:
            try:
                b = c.ejecutar(ts,ex)
                cadena+=b.cadena
            except Exception as e:
                print("ERROR FOR : "+e)
        v="\n"+str(pre.cadena)+"\n"+ str(tempC) + ":\n"+ str(condi.cadena)+"\n if ("+str(condi.temporal)+") goto "+str(tempT) +";\ngoto "+str(tempF)+";\n "+str(tempT) +":"+ cadena+str(a.cadena)+"\n goto "+str(tempC)+";\n"+str(tempF)+":\n"       
        ts.popEntorno()
        ts.popEntorno()
        return valorTemporal(TIPO_TEMP.INSTRUCCION,v,"","","","")
        
        
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" FOR  : \"]\nn"+node+"-> "+self.asig.ast()+"\nn"+node+"->"+self.cond.ast()+"\nn"+node+"->"+self.exp.ast()+"\nn"+node+"->nb"+node+"\nnb"+node+"[label=\"Body\"]\n"
            for x in self.cuerpo:
                try:
                    v+="\nnb"+node+"->"+x.ast()
                except:
                    pass
            return v
        
        except Exception as e:
            print("ERROR-AST7: "+str(e))
            return "error"


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
                    if(v.tipo == TIPO_TEMP.ERROR):
                        ts.addError("Error PrintF: "+v.cadena,self.linea)
                        return ""
                    cadena+=v.cadena
                    print(cadena)
                    self.exp = re.sub(r"[\%][a-zA-Z]","",self.exp,1)
                    prints  += "\nprint("+v.temporal+");"
                except Exception as e:
                    print("ERROR: " + e)           
        else:
            print("No hay params")

        v2="\n"+cadena+"\n print ("+self.exp+");"+prints       
        return valorTemporal(TIPO_TEMP.INSTRUCCION,v2,"","","","")
        
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Printf  :"+self.exp.replace("\"","")+" \"]"
            if(self.cuerpo!=None):
                for x in self.cuerpo:
                    try:
                        v+="\nn"+node+"->"+x.ast()
                    except:
                        pass
            return v
        
        except Exception as e:
            print("ERROR-AST8: "+str(e))
            return "error\n"


#----------------------------------------------------- ReadF     ------------------------------------------------------------
class Readf():
    def __init__(self,linea):
        self.linea = linea
    
    def ejecutar(self,ts,ex):
        # TD ARREGLO
        #.-.-.-.-.-
        cadena = ""
        prints=""
        return valorTemporal(TIPO_TEMP.VALOR,"","read()",TIPO.READ,"","")
        
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Readf  : \"]\n"
            return v
        
        except Exception as e:
            print("ERROR-AST9: "+str(e))
            return "error\n"


#----------------------------------------------------- Etoiqueta     ------------------------------------------------------------
class Etiqueta():
    def __init__(self,linea):
        self.linea = linea
    
    def ejecutar(self,ts,ex):
        # TD ARREGLO
        #.-.-.-.-.-
        cadena = ""
        prints=""
        return valorTemporal(TIPO_TEMP.INSTRUCCION,"\n"+self.linea + ":","",TIPO.ENTERO,"","")
        
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Etiqueta  : "+ str(self.linea)+"\"]\n"
            return v
        
        except Exception as e:
            print("ERROR-AST10: "+str(e))
            return "error\n"


#----------------------------------------------------- Salto     ------------------------------------------------------------
class Salto():
    def __init__(self,linea):
        self.linea = linea
    
    def ejecutar(self,ts,ex):
        # TD ARREGLO
        #.-.-.-.-.-
        cadena = ""
        prints=""
        return valorTemporal(TIPO_TEMP.INSTRUCCION, "\ngoto "+self.linea +";","",TIPO.ENTERO,"","")
        
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Go To  : "+ str(self.linea)+"\"]"
            return v
        
        except Exception as e:
            print("ERROR-AST11: "+str(e))
            return "error\n"


#----------------------------------------------------- CALL     ------------------------------------------------------------
class Call():
    def __init__(self,name, params,linea):
        self.name = name 
        self.params = params
        self.linea = linea
    
    def ejecutar(self,ts,ex):
        met = None
        x = 0
        cadena = ""
        tag = ts.generarEtiqueta()

        if (self.name) in ts.metodos:
            met = ts.metodos[self.name]
        else:
            return #error no existe el metodo
        if (self.params != None ): 
            for i in range(len(self.params)):
                temp = ts.generarParam()
                v = self.params[x].ejecutar(ts,ex)
                if(v.tipo == TIPO_TEMP.ERROR):
                    ts.addError("Error Llamado: "+v.cadena,self.linea)
                    return ""
                cadena += v.cadena
                cadena += "\n"+temp+" = "+v.temporal+";"
                ts.addVariable(met.params[x],v.value,temp,str(self.linea))
                x = x+1
            
        cadena += "\n"+tag+":"
        ex = ts.generarEtiqueta() 
        ts.addEntorno()
        for a in met.body:
            try:
                b = a.ejecutar(ts,Extra(ex,None,None))
                cadena+=b.cadena
            except Exception as e:
                print("ERROR: "+str(e) + "   en "+ self.linea  + "  --- " +str(a))  
        cadena += "\n"+ex+":"
        prints = ""
        ts.popEntorno()
        return valorTemporal(TIPO_TEMP.INSTRUCCION, cadena,"","","","")
        
    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Llamado  : "+ str(self.name)+"\"]"
            return v
        
        except Exception as e:
            print("ERROR-AST12: "+str(e))
            return "error\n"

#----------------------------------------------------- ASIGNACION     ------------------------------------------------------------
class Incremento():

    def __init__(self,name,arr,linea):
        self.name = name 
        self.arr = arr 
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
        cad = "" 
        acs = ""
        index = list()  
        if(self.arr != None):
            for x in self.arr:
                if(isinstance(x, ValorAcceso)):
                    acs += "['"+x.valor+"']"
                else:
                    z = x.ejecutar(ts,ex)
                    cad += z.cadena
                    acs += "["+z.temporal+"]" 
        cad += "\n"+temp.temp+acs+" = "+temp.temp+acs+"+ 1 ;"
        ts.addVariable(self.name,temp.tipo,temp.temp, str(self.linea))
        return valorTemporal(TIPO_TEMP.INSTRUCCION,cad,"","","","")

    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Incremento (++)  : "+ str(self.name)+"\"]\n"
            return v
        
        except Exception as e:
            print("ERROR-AST13: "+str(e))
            return "error\n"


#----------------------------------------------------- DECREMENTO     ------------------------------------------------------------
class Decremento():

    def __init__(self,name,arr,linea):
        self.name = name 
        self.arr = arr 
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
        cad = "" 
        acs = ""
        index = list()  
        if(self.arr != None):
            for x in self.arr:
                if(isinstance(x, ValorAcceso)):
                    acs += "['"+x.valor+"']"
                else:
                    z = x.ejecutar(ts,ex)
                    cad += z.cadena
                    acs += "["+z.temporal+"]" 
        cad += "\n"+temp.temp+acs+" = "+temp.temp+acs+"- 1 ;"
        ts.addVariable(self.name,temp.tipo,temp.temp, str(self.linea))
        return valorTemporal(TIPO_TEMP.INSTRUCCION,cad,"","","","")

    def ast(self):
        try:
            node = str(getHash(self))
            v = "n"+node+"\n n"+node+"[label=\" Decremento (++)  : "+ str(self.name)+"\"]\n"
            return v
        
        except Exception as e:
            print("ERROR-AST14: "+str(e))
            return "error\n"