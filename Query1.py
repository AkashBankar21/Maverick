import os
import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen

def req(url, filename):
    req = Request(url,headers ={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mydata = webpage.decode("utf8")
    f=open(filename,'w',encoding="utf-8")
    f.write(mydata)
    f.close

url = 'https://www.worldometers.info/coronavirus/'
req(url, 'homepage.html')

tokens = (
    'OPENTABLE', 'CONTENT', 'OPENBR', 'OPENNOBR', 'CLOSENOBR', 'OPENHEAD', 'CLOSEHEAD',
    'OPENHEADER', 'CLOSEHEADER', 'OPENROW', 'CLOSEROW', 'OPENBODY',
    'OPENDATA', 'CLOSEDATA', 'ENDSKIPS', 'OPENHREF', 'CLOSEHREF', 'CLOSEBODY', 'CLOSETABLE')

t_ignore = '\t'

def t_OPENTABLE(t):
     r'<table.id="main_table_countries_today".[^>]+>'
     return t

def t_OPENHEAD(t):
     r'<thead[^>]*>'
     return t

def t_CLOSEHEAD(t):
     r'<\/thead[^>]*>'
     return t

def t_OPENHEADER(t):
     r'<th[^>]*>'
     return t

def t_OPENROW(t):
     r'<tr[^>]*>'
     return t

def t_CLOSEHEADER(t):
     r'<\/th[^>]*>'
     return t

def t_OPENBR(t):
     r'[\/]*<br>'
     return t

def t_OPENNOBR(t):
     r'<nobr>'
     return t

def t_CLOSENOBR(t):
     r'<\/nobr>'
     return t

def t_CLOSEROW(t):
     r'<\/tr>'
     return t

def t_OPENBODY(t):
    r'<tbody>'
    return t

def t_OPENDATA(t):
     r'<td[^>]*>'
     return t

def t_CLOSEDATA(t):
     r'<\/td>'
     return t

def t_ENDSKIPS(t):
     r'<![^>]*>'
     return t

def t_OPENHREF(t):
     r'<a[^>]*>'
     return t

def t_CLOSEHREF(t):
     r'<\/a>'
     return t

def t_CLOSEBODY(t):
    r'<\/tbody>'
    return t

def t_CLOSETABLE(t):
    r'<\/table>'
    return t

def t_CONTENT(t):
     r'[a-zA-Z0-9_#-,.]+'
     return t

def t_error(t):
    t.lexer.skip(1)


def p_start(p):
    '''
    start : OPENTABLE handleheader handlebody CLOSETABLE
    '''
    pass

def p_handleheader(p):
     '''
     handleheader : OPENHEAD OPENROW handleheaderdata CLOSEROW CLOSEHEAD
     '''
     pass

def p_handleheaderdata(p):
     '''
     handleheaderdata : OPENHEADER content CLOSEHEADER handleheaderdata
                      | empty
     '''
     pass

def p_handlebody(p):
     '''
     handlebody : OPENBODY handlerow CLOSEBODY
     '''
     pass

def p_handlerow(p):
     '''
     handlerow : OPENROW handledata endskip CLOSEROW handlerow
               | empty
     '''
     pass

def p_handledata(p):
     '''
     handledata : OPENDATA content CLOSEDATA handledata
                | OPENDATA OPENHREF content CLOSEHREF CLOSEDATA handledata
                | OPENDATA OPENNOBR content CLOSENOBR CLOSEDATA handledata
                | empty
     '''
     if len(p) == 5 and p[2] is not None:
          print(p[2])
     if len(p) == 7 and p[3] is not None:
          print(p[3])

def p_endskip(p):
     '''
     endskip : ENDSKIPS handledata endskip
             | empty
     '''
     pass

def p_content(p):
    '''
    content : CONTENT content
            | CONTENT OPENBR content
            | CONTENT OPENBR OPENNOBR content CLOSENOBR content
            | empty
    '''
    p[0] = p[1]

def p_empty(p):
    '''
    empty :
    '''
    pass

def p_error(p):
    pass

def getdata():
    file_obj= open('table.html','r',encoding="utf-8")
    data=file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    for tok in lexer:
        pass
    parser = yacc.yacc()
    parser.parse(data)
    file_obj.close()

getdata()