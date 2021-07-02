from tag import Tag
from lexer import Lexer
from _parser import Parser

if __name__ == "__main__":
   #Lê arquivo
   lexer = Lexer('test.txt')
   parser = Parser(lexer)
   parser.le_pilha()

   # lexer.analisa_sintax()
   print("\n=>Lista de tokens:")
   lexer.printTokens()

   print("\n=>Tabela de simbolos:")
   lexer.printTS()
   
   print('\n=> Fim da compilacao')
