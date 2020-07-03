"""
ANALIZADOR DEL PROYECTO 1
    RICARDO ANTONIO MENÉNDEZ TOBÍAS
    201602916
"""



import ply.yacc as yacc 

from tkinter import *

reservadas = {
    'main': 'main',
    'goto': 'goto',

    'int': 'int',
    'float': 'float',
    'double': 'double',
    'char': 'char',
    'void': 'void',
    'sizeof': 'sizeof',
    
    'printf': 'printf',
    'array': 'array',
    'unset': 'unset',
    'if': 'if',
    'else': 'else',
    'abs': 'abs',
    'xor': 'xor',
    'exit': 'exit',

    'scanf': 'scanf',
    'printf': 'printf',

    'break': 'break',
    'return': 'return', 

    'while': 'while',
    'do': 'do',
    'for': 'for',
    'switch': 'switch',
    'case': 'case',
    'default': 'default',
    

    'struct': 'struct', 

}

tokens = [
    'SUMA',
    'RESTA',
    'MULTI',
    'DIV',
    'PORCENTAJE',  


    'NOT',
    'AND',
    'OR',
    'SXOR',

    'DIGUAL',
    'IGUAL',
    'DESIGUAL',
    'MAYORIGUAL',
    'MENORIGUAL',
    'MAYOR',
    'MENOR',

    'BNOT',
    'BAND',
    'BOR',
    'BXOR',
    'BLEFT',
    'BRIGHT',

    'IZQCOR',
    'DERCOR',
    'COMA',

    'IZQPAR',
    'DERPAR',
    'IZQLLAVE',
    'DERLLAVE',
    'PCOMA',
    'DP',
    'ID',
    'DOUBLE',
    'INTEGER',
    'VAR',
    'STR',

    'FLECHA',
    'INCE',
    'DECRE',
    'ASK',
    'PUNTO' 
] + list(reservadas.values())

t_RESTA = r'-'
t_SUMA = r'\+'
t_MULTI = r'\*'
t_DIV = r'\/'
t_PORCENTAJE = r'\%'
 
t_PUNTO = r'\.'
t_COMA = r'\,' 

t_NOT = r'\!'
t_AND = r'\&\&'
t_OR = r'\|\|'

t_IGUAL = r'\='
t_DIGUAL = r'\=\='
t_DESIGUAL = r'\!\='
t_MAYORIGUAL = r'\>\='
t_MENORIGUAL = r'\<\='
t_MAYOR = r'\>'
t_MENOR = r'\<'

t_BNOT = r'\~'
t_BAND = r'\&'
t_BOR = r'\|'
t_BXOR = r'\^'
t_BLEFT = r'\<\<'
t_BRIGHT = r'\>\>'

t_IZQPAR = r'\('
t_DERPAR = r'\)'

t_IZQCOR = r'\{'
t_DERCOR = r'\}'

t_PCOMA = r'\;'
t_DP = r'\:'
t_IZQLLAVE = r'\['
t_DERLLAVE = r'\]'

t_FLECHA = r'\-\>'
t_INCE = r'\+\+'
t_DECRE = r'\-\-'


t_ASK = r'\?'


def t_DOUBLE(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor no es parseable a decimal %d",t.value)
        t.value = 0
    return t    

def t_STR(t):
    r'((\'.*?\')|(\".*?\"))'
    t.value = t.value
    return t

def t_INTEGER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor no es parseable a integer %d",t.value)
        t.value = 0
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(),'ID') 
    return t

def t_VAR(t):
    r'[\$](([t|v|s|a][\d]+)|sp|ra)'
    return t

def t_COMENTARIO(t):
    r'\/\/.*\n'
    t.lexer.lineno += 1

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Caracter irreconocible! '%s'"% t.value[0])
    #meter a tabla de errores!
    erroresLexicos.append("Error Lexico: "+t.value[0]+"  en linea:  "+ str(int(t.lexer.lineno)))
    t.lexer.skip(1)

#Creador del analizador lexico LEX
import ply.lex as lex 

lexer = lex.lex()

from Arbol.arit import *
from Arbol.valores import *
from Arbol.simbolos import *
from Arbol.ast import *
from Arbol.relacion import *
from Arbol.logico import *


precedence = (
    ('left','COMA'),
    ('right','ASK'),
    ('left','BLEFT','BRIGHT'),
    ('left' ,'BXOR'),
    ('left','OR','BOR'),
    ('left','AND','BAND'),
    ('left','MAYOR','MENOR','DIGUAL','DESIGUAL','MAYORIGUAL','MENORIGUAL'),
    ('left','RESTA','SUMA'),
    ('left','DIV','MULTI','PORCENTAJE'),
    ('right','NOT','BNOT','sizeof')
)

def p_s_tag(t):
    '''s    : lbody'''
    t[0] = t[1]

def p_lbody(t):
    ''' lbody : lbody body
              | body'''
    if(len(t)==2):
        t[0] = []
        t[0].append( t[1])
    else:
        t[0] = t[1]
        t[0].append(t[2])

def p_body(t):
    '''
    body : TYPE ID IZQPAR lpam DERPAR IZQCOR linst DERCOR
    '''
    t[0] = AddMetodo(t[2],t[4],t[7],str(""))

def p_body2(t):
    '''
    body : TYPE main IZQPAR lpam DERPAR IZQCOR linst DERCOR
    '''
    t[0] = Metodo(t[2],None,t[7],str(t.lineno(1)))

def p_body_str(t):
    "body : struct ID IZQCOR linst DERCOR"
    t[0] = t[4]

def p_body_decl(t):
    "body : decla PCOMA"
    t[0] = t[1]

def p_linst(t):
    '''
    linst : linst inst 
          | inst 
    '''
    if(len(t)==2):
        t[0] = []
        t[0].append(t[1])
    else:
        t[0] = t[1]
        t[0].append(t[2])


def p_lpam(t):
    '''
    lpam : lparam 
         | 
    '''
    if(len(t)==1):
        t[0]  = None 
    else:
        t[0] = t[1]

def p_lparam(t):
    '''
    lparam : lparam COMA TYPE ident
         | TYPE ident
    '''
    if(len(t)==3):
        t[0] = list() 
        t[0].append(t[2])
    else:
        t[0] = t[1]
        t[0].append(t[4])




        # -------------------------------------------------------------------------------               INSTRUCCIONES


def p_inst(t):      # INSTRUCCIÓNES
    '''
    inst : asig PCOMA
         | para
         | si
         | mientras
         | cual
         | call
         | dow
         | prin
         | decla PCOMA
         | tag
         | gotot PCOMA
    '''
    t[0] = t[1]

def p_call(t):
    "call : ident IZQPAR plex DERPAR PCOMA "
    t[0] = Call(t[1],t[3],str(t.lineno(1)))


def p_plex(t):
    '''
        plex : lex 
             | 
    '''
    if(len(t)==1):
        t[0] = None 
    else:
        t[0] = t[1]
def p_lex(t):
    '''
        lex : lex COMA exp
            | exp
    '''
    if(len(t)==2):
        t[0] = []
        t[0].append(t[1])
    else:
        t[0] = t[1] 
        t[0].append(t[3])
        
def p_tag(t):
    "tag : ident DP"
    t[0] = Etiqueta(t[1])

def p_goto(t):
    "gotot : goto ident"
    t[0] = Salto(t[2])

def p_asig(t):      # INSTRUCCIÓN ----> ASIGNACIÓN
    '''asig : ident lacs IGUAL exp  
            | ident IGUAL exp  '''
    if(len(t)==5):
        t[0] = Asignacion(t[1],t[2],t[4],str(t.lineno(1)))
    else:
        t[0] = Asignacion(t[1],None,t[3],str(t.lineno(1)))

def p_asig_Incre(t):      # INSTRUCCIÓN ----> INCREMENTO
    '''asig : ident lacs INCE  
            | ident INCE  '''
    if(len(t)==4):
        t[0] = Incremento(t[1],t[2] ,str(t.lineno(1)))
    else:
        t[0] = Incremento(t[1],None ,str(t.lineno(1)))

def p_asig_decre(t):      # INSTRUCCIÓN ----> INCREMENTO
    '''asig : ident lacs DECRE  
            | ident DECRE  '''
    if(len(t)==4):
        t[0] = Decremento(t[1],t[2],str(t.lineno(1)))
    else:
        t[0] = Decremento(t[1],None,str(t.lineno(1)))

def p_declara(t):      # INSTRUCCIÓN ----> ASIGNACIÓN
    '''decla : TYPE ident lacs IGUAL exp  
             |  TYPE ident IGUAL exp  '''
    if(len(t)==7):
        t[0] = Declaracion(t[2],t[3],t[5],str(t.lineno(1)))
    else:
        t[0] = Declaracion(t[2],None,t[4],str(t.lineno(1)))
        
def p_while(t):     # INSTRUCCIÓN ----> WHILE
    "mientras : while IZQPAR exp DERPAR IZQCOR linst DERCOR"
    t[0] = Para(t[3],t[6],str(""))
def p_dow(t):     # INSTRUCCIÓN ----> DO WHILE
    "dow : do IZQCOR linst DERCOR while IZQPAR exp DERPAR PCOMA"
    t[0] = NekoPara(t[7],t[3],str(""))

def p_if(t):     # INSTRUCCIÓN ----> IF
    '''si : if IZQPAR exp DERPAR IZQCOR linst DERCOR lelsi els
          | if IZQPAR exp DERPAR IZQCOR linst DERCOR els'''
    if(len(t)==9):
        t[0] = Si(t[3],t[6],None,t[8],str(t.lineno(1)))
    else:
        t[0] = Si(t[3],t[6],t[8],t[9],str(t.lineno(1)))

def p_lelif(t):
    '''
    lelsi : lelsi elsi
        |  elsi
    '''
    if(len(t)==2):
        t[0] = list()
        t[0].append(t[1])
    else:
        t[0] = t[1] 
        t[0].append(t[2])
 
def p_elif(t):
    "elsi : else if IZQPAR exp DERPAR IZQCOR linst DERCOR"
    t[0] = ElseSi(t[4],t[7],None,None,str(t.lineno(1)))
def p_else(t):
    '''els : else IZQCOR linst DERCOR
        | '''
    if(len(t)==1):
        t[0] = None
    else:
        t[0] = t[3]

def p_for(t):     # INSTRUCCIÓN ----> FOR
    "para : for IZQPAR para1 exp PCOMA para2 DERPAR IZQCOR linst DERCOR"
    t[0] = Forr(t[3],t[4],t[6],t[9],str(t.lineno(1)))

def p_for1(t):
    '''
    para1 : asig PCOMA
          | decla PCOMA
    '''
    t[0] = t[1]


def p_for2(t):
    '''
    para2 : asig
          | decla
          | exp
    '''
    t[0] = t[1]



def p_switch(t):  # INSTRUCCIÓN -----> SWITCH
    "cual : switch IZQPAR exp DERPAR IZQCOR lcase def DERCOR "

def p_lcase(t):
    '''
    lcase : lcase caso
        | caso
    '''

def p_case(t):
    '''
    caso : case ID DP linst break PCOMA
        | case ID DP linst 
    '''

def p_def(t):
    '''def : default DP linst break PCOMA
           |'''


def p_printf(t):     # INSTRUCCIÓN ----> LLAMADO PRINTF
    '''prin : printf IZQPAR STR lexpr DERPAR PCOMA'''
    t[0] = Printf(t[3],t[4],str(t.lineno(1)))

def p_printf2(t):     # INSTRUCCIÓN ----> LLAMADO PRINTF
    '''prin : printf IZQPAR STR DERPAR PCOMA'''
    t[0] = Printf(t[3],None,str(t.lineno(1)))

def p_readf(t):     # INSTRUCCIÓN ----> LLAMADO scanf
    '''exp : scanf IZQPAR DERPAR'''
    t[0] = Readf( str(""))

def p_lexp(t):      # LISTA DE expresiones
    '''
        lexpr : lexpr COMA exp
             | COMA exp
    '''
    if(len(t)==4):
        t[0] = t[1]
        t[0].append(t[3])
    else:
        t[0] = list()
        t[0].append(t[2])

def p_ids(t):   
    '''
    ident   :  ID
    '''
    t[0] = t[1]


def p_accesos(t):
    '''
        lacs : lacs acs
             | acs
    '''
    if(len(t)==2):
        t[0] = list()
        t[0].append(t[1])
    else:
        t[0] = t[1]
        t[0].append(t[2])

def p_array(t):
    '''
        acs : IZQLLAVE exp DERLLAVE
    '''
    t[0] = ValorArray2(t[2])

def p_access(t):
    '''
        acs : PUNTO ID 
    '''
    t[0] = ValorAcceso(t[2])



def p_expresion(t):
    '''
    exp : exp     SUMA    exp
        | exp     RESTA   exp  
        | exp     MULTI   exp
        | exp     DIV     exp
        | exp     PORCENTAJE     exp
        | exp     DIGUAL     exp
        | exp     DESIGUAL     exp
        | exp     MAYOR     exp
        | exp     MENOR     exp
        | exp     MAYORIGUAL     exp
        | exp     MENORIGUAL     exp
        | exp     AND     exp
        | exp     OR     exp
        | exp     BAND     exp
        | exp     BOR     exp
        | exp     BXOR     exp
        | exp     BLEFT    exp
        | exp     BRIGHT     exp
        | RESTA   exp
        | NOT     exp
        | BNOT    exp 
        | sizeof    exp 
        | IZQPAR exp DERPAR
    '''
    if(t[2]=='+'):
        t[0] = Suma(t[1],t[3])
    elif(t[2]=='-'):
        t[0] = Resta(t[1],t[3])
    elif(t[2]=='*'):
        t[0] = Multi(t[1],t[3])
    elif(t[2]=='/'):
        t[0] = Divi(t[1],t[3])
    elif(t[2]=='%'):
        t[0] = Modulo(t[1],t[3])
    elif(t[2]=='>'):
        t[0] = Mayor(t[1],t[3])
    elif(t[2]=='>='):
        t[0] = MayorQue(t[1],t[3])
    elif(t[2]=='<'):
        t[0] = Menor(t[1],t[3])
    elif(t[2]=='<='):
        t[0] = MenorQue(t[1],t[3])
    elif(t[2]=='=='):
        t[0] = Igual(t[1],t[3])
    elif(t[2]=='!='):
        t[0] = Desigual(t[1],t[3])
    elif(t[2]=='&&'):
        t[0] = And(t[1],t[3])
    elif(t[2]=='||'):
        t[0] = Or(t[1],t[3])
    elif(t[2]=='&'):
        t[0] = BAnd(t[1],t[3])
    elif(t[2]=='|'):
        t[0] = BOr(t[1],t[3])
    elif(t[2]=='^'):
        t[0] = Xor(t[1],t[3])
    elif(t[1]=='!'):
        t[0] = Not(t[2],None)
    elif(t[1]=='~'):
        t[0] = BNot(t[2],None)
    elif(t[1]=='('):
        t[0] = t[2]
    elif(t[1]=='-'):
        t[0] = Resta2(t[2],None)
    elif(t[1]=='sizeof'):
        t[0] = Tamano(t[2],None)
    
def p_cast(t):
    '''
    exp : IZQPAR TYPE DERPAR exp
    '''
    t[0] = Casteo(t[2],t[4])

def p_ternario(t):
    '''
    exp : exp ASK exp DP exp
    '''
    t[0] = Casteo(t[2],t[4])

def p_value_dou(t):
    '''
    exp  : DOUBLE
    '''
    t[0] = ValorDoble(t[1])

def p_value_ent(t):
    "exp  : INTEGER"
    t[0] = ValorEntero(t[1])

def p_value_id(t):
    "exp  : ident"
    t[0] = ValorVariable(t[1],None)

def p_value_id2(t):
    "exp  : ident lacs"
    t[0] = ValorVariable(t[1],t[2])

def p_value_str(t):
    "exp  : STR"
    t[0] = ValorString(t[1])

def p_valur_arr(t):
    " exp : IZQCOR lex DERCOR"
    t[0] = ValorArray(t[2])

def p_type(t):
    '''
    TYPE : int
        | float
        | char
        | double
        | void
    '''
    t[0] = t[1]

def p_error(t): 
        #erroresSintacticos.append("Error Sintactico:  Token: "+str(t.value) + "   En Linea : " +str(t.lineno))
    try:
        print("Sintax : El error es: "+t.value+" en la linea "+ t.lineno)
    except:
        print("ERROR CRITICO " + str(t))  

#Creador del Analisis Sintactico
from Arbol.reportes import *
erroresLexicos = []
erroresSintacticos = []
parser = yacc.yacc()
def ejecutar(v):
    lexer = lex.lex()
    global parser
    parser = yacc.yacc()
    global erroresLexicos 
    erroresLexicos = []
    global erroresSintacticos
    erroresSintacticos = []
    ts = TablaSimbolos()
    arbol = parser.parse(v,tracking=True)
    cadena = ""
    for a in arbol:
        c = a.ejecutar(ts,None)
        if isinstance(a,Metodo): 
            cadena+=c.cadena
        if isinstance(a,Declaracion): 
            cadena+=c.cadena
    try:
        reporteErrores([],[],ts.errorSemantico)
    except Exception as e:
        print("Error Generando el Reporte:  "+ str(e))
    try:
        reporteAST(arbol)
    except Exception as e:
        print("Error Generando el Reporte:  "+ str(e))
    try:
        reporteTS(ts.tsReport,ts.metodos)
    except Exception as e:
        print("Error Generando el Reporte:  "+ str(e))


    return cadena
    # tk = tkinter.Tk() # Create the object
    # tk.geometry('1280x200')
    # text = tkinter.Text(tk,height=200, width=1280)
    # text.pack()


    # tk.mainloop()
    # tk.destroy()
