import ply.lex as lex

# Definir las palabras clave
reserved = {
    'entonces': 'ENTONCES',
    'si': 'SI',
    'si_no': 'SI_NO',
    'fin_si': 'FIN_SI'
}

# Lista de tokens
tokens = [
    'ID'
] + list(reserved.values())

# Expresiones regulares para tokens
t_ID = r'[a-zA-Z][a-zA-Z0-9]*'

# Ignorar caracteres en blanco
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print("carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Funciones para manejar palabras clave
def t_Si(t):
    r'si'
    return t

def t_Entonces(t):
    r'entonces'
    return t

def t_Si_No(t):
    r'si_no'
    return t

def t_Fin_Si(t):
    r'fin_si'
    return t

# Construir el lexer
lexer = lex.lex()

# Ejemplo de uso
lexer.input('si algo entonces si_no algo más fin_si')

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)