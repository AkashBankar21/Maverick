from ply import lex

# Define the tokens
tokens = (
    'BEGINNEWS',
    'SKIPTAG',
    'TEXT',
    'ENDNEWS',
    'BEGINRESPONSE',
    'ENDRESPONSE'
)


# Define regular expressions for tokens


def t_BEGINNEWS(t):
    r'<h2><span\s+class="mw-headline"\s+id="Pandemic_chronology">(.+?)</span></h2>'
    return t

def t_ENDNEWS(t):
    r'<h2><span\s+class="mw-headline"\s+id="Summary">(.+?)</span></h2>'
    return t

def t_BEGINRESPONSE(t):
    r'<span\s+class="mw-page-title-main">(.+?)</span>'
    return t

def t_ENDRESPONSE(t):
    r'<h2><span\s+class="mw-headline"\s+id="See_also">(.+?)</span></h2>'
    return t

def t_SKIPTAG(t):
    r'<[^>]+>'
    return t

def t_TEXT(t):
    r'[^<>]+'
    return t

def t_error(t):
    #print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
