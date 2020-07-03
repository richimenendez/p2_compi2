import webbrowser
import os

head = ''' <html>
<head>

<style>
.et {background-color: powderblue;}
</style>
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>'''

def reporteErrores(eL,eS,eSem):
    html = '''
	<h1>Reporte de Errores: </h1>
	<h3> Ricardo Menéndez - 201602916 </h3>
    <h4> Errores Lexicos </h4>
<table width="800" border="1" align="center">
    '''
    for x in eL:
        try:
            html+= '<tr><td> '+x+'</td></tr>'
        except Exception as e:
            print("Error generando linea de reporte gramatical  "+ str(e))
    html+='''</table>
    <h4> Errores Sintacticos </h4>
<table width="800" border="1" align="center">'''
    for x in eS:
        try:
            html+= '<tr><td> '+x+'</td></tr>'
        except Exception as e:
            print("Error generando linea de reporte gramatical  "+ str(e))
    html+='''</table>
    <h4> Errores Semanticos </h4>
<table width="800" border="1" align="center">'''
    for x in eSem:
        try:
            html+= '<tr><td> '+x.valor +"    en linea: "+ str(x.linea)+'</td></tr>'
        except Exception as e:
            print("Error generando linea de reporte gramatical  "+ str(e))
    html+="</body></html>"
    try:
        contenido = head + html
        with open('reporte_ErroresC.html','w') as rep:
            rep.write(contenido)
    except Exception as e:
        print("No se pudo generar el reporte: " + str(e))

def reporteAST(root):
    dot = "digraph {\nroot[label=\"root\"]\n error[label=\"Error\"]\n"
    for x in root:
        
        dot += '\nroot ->'+ x.ast()
    dot += "\n}"
    try:
        contenido = dot
        with open('ASTC.dot','w') as rep:
            rep.write(contenido)
        os.system('dot "ASTC.dot" -o "ASTC.pdf" -Tpdf')
    except:
        print("No se pudo")

def reporteGDA(root):
    dot = "digraph {\nroot[label=\"root\"]\n error[label=\"Error\"]\n"
    for x in root:
        
        dot += '\nroot ->'+ x.gda("")
    dot += "\n}"
    try:
        contenido = dot
        with open('GDA.dot','w') as rep:
            rep.write(contenido)
        os.system('dot "GDA.dot" -o "GDA.pdf" -Tpdf')
    except:
        print("No se pudo")

def gramaticalASC(lista):
    html = '''
	<h1>Reporte Gramatical: Gramatica Ascendente</h1>
	<h3> Ricardo Menéndez - 201602916 </h3>
<table width="1000" border="1" align="center">
    '''
    for x in lista:
        try:
            html+= x.grammar()
        except Exception as e:
            print("Error generando linea de reporte gramatical  "+ str(e))
    html+="</body></html>"
    try:
        contenido = head + html
        with open('reporte_GAscC.html','w') as rep:
            rep.write(contenido)
    except Exception as e:
        print("No se pudo generar el reporte: " + str(e))


def gramaticalDES():
    pass

def reporteTS(vars,metods):
    html = '''
	<h1>Reporte Tabla de Simbolos: </h1>
	<h3> Ricardo Menéndez - 201602916 </h3>
	<br/><br/>
    <h3> Variables:</h3>
    <table width="800" border="1" align="center">
    <tr class="et"><th> Variable </th> <th> Linea </th> <th> Tipo </th><th> Temporal </th></tr> 
    '''
    for y in vars:
        try:
            html += '''
        <tr><td>'''+y.nombre+"</td><td>"+str(y.linea)+ '''</td><td>'''+y.tipo.name+"</td><td>"+str(y.temp)+ "</td></tr>"
        except Exception as e:
            print(e)
    html+="</table>"
    html+='''
    <h3> Metodos </h3>
    <table width="800" border="1" align="center">
    <tr class="et"><th> Metodo </th> </tr> 
    '''
    for x in metods:
        html += '''
        <tr><td>'''+x+"</td></tr>"
    html+="</table></body></html>"
    try:
        contenido = head + html
        with open('reporte_TSC.html','w') as rep:
            rep.write(contenido)
    except Exception as e:
        print("No se pudo generar el reporte: " + str(e))


def reporteOptimizacion(eL):
    html = '''
	<h1>Reporte de Optimizacion: </h1>
	<h3> Ricardo Menéndez - 201602916 </h3>
    <h4> Reglas APlicadas </h4>
<table width="800" border="1" align="center">
    '''
    for x in eL:
        try:
            html+= '<tr><td> '+x+'</td></tr>'
        except Exception as e:
            print("Error generando linea de reporte gramatical  "+ str(e))
    html+='''</table>'''
   
    html+="</body></html>"
    try:
        contenido = head + html
        with open('reporte_Opt.html','w') as rep:
            rep.write(contenido)
    except Exception as e:
        print("No se pudo generar el reporte: " + str(e))