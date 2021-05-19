from tag import Tag
from lexer import Lexer

if __name__ == "__main__":
   #Lê arquivo
   lexer = Lexer('prog1.txt')
   #Realiza analise léxica
   lexer.analisa()
   
   print("\n=>Lista de tokens:")
   lexer.printTokens()

   print("\n=>Tabela de simbolos:")
   lexer.printTS()
   
   print('\n=> Fim da compilacao')
