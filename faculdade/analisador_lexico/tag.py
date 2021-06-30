from enum import Enum, auto

class Tag(Enum):
   '''
   Uma representacao em constante de todos os nomes 
   de tokens para a linguagem.
   '''

   # Fim de arquivo
   EOF = 'EOF'

   # Palavras-chave
   KW_PROGRAM =   'program'
   KW_IF =        'if'
   KW_ELSE =      'else'
   KW_WHILE =     'while'
   KW_WRITE =     'write'
   KW_READ =      'read'
   KW_NUM =       'num'
   KW_CHAR =      'char'
   KW_NOT =       'not'
   KW_OR =        'or'
   KW_AND =       'and'
   
   # Operadores 
   OP_LE = '<='
   OP_GE = '>='
   OP_LT = '<'
   OP_GT = '>'
   OP_EQ = '=='
   OP_NE = '!='
   OP_AD = '+'
   OP_MIN = '-'
   OP_MUL = '*'
   OP_DIV = '/'
   OP_ATRIB = '='
   
   # Simbolos
   SMB_OBC = '{'
   SMB_CBC = '}'
   SMB_OPA = '('
   SMB_CPA = ')'
   SMB_COM = ','
   SMB_SEM = ';'

   # Identificador
   ID = auto()

   # Numeros
   NUM = auto()

   # Constantes para tipos
   TIPO_VOID = auto()
   TIPO_BOOL = auto()
   TIPO_NUM =  auto()
   TIPO_CHAR = auto()
   TIPO_ERRO = auto()



