import sys

from tag import Tag


class Parser():

    def __init__(self, lexer):
       self.lexer = lexer
       self.gen_token = lexer.le_lexer() # Leitura inicial obrigatoria do primeiro simbolo
       self.token = next(self.gen_token)
       if self.token is None: # erro no Lexer
            sys.exit(0)

    def sinalizaErroSemantico(self, message):
       print("[Erro Semantico] na linha " + str(self.token.getLinha()) + " e coluna " + str(self.token.getColuna()) + ": ")
       print(message, "\n")

    def sinalizaErroSintatico(self, message):
       print("[Erro Sintatico] na linha " + str(self.token.getLinha()) + " e coluna " + str(self.token.getColuna()) + ": ")
       print(message, "\n")

    def advance(self):
       print("[DEBUG] token: ", self.token.toString())
       self.token = next(self.gen_token)
       print(self.token.toString())
       if self.token is None: # erro no Lexer
            sys.exit(0)
    
    def skip(self, message):
       self.sinalizaErroSintatico(message)
       self.advance()

    
