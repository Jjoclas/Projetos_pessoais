from tag import Tag
from lexer import Lexer

if __name__ == "__main__":
   lexer = Lexer('prog1.txt')
   lexer.printTS()
   # lexer.analisa()
   # print("\n=>Lista de tokens:")
   # token = lexer.proxToken()
   # while(token is not None and token.getNome() != Tag.EOF):
   #    print(token.toString())
   #    token = lexer.proxToken()

   # print("\n=>Tabela de simbolos:")
   # lexer.printTS()
   # lexer.closeFile()
    
   # print('\n=> Fim da compilacao')
