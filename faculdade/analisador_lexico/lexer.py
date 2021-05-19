import sys
import logging

from ts import TS
from tag import Tag
from token_pasc import Token
# from token_pasc import tokens
from typing import Iterator, Optional, Callable, Generator, TextIO

class Lexer():
   '''
   Classe que representa o Lexer (AFD):
   
   [1] Voce devera se preocupar quando incremetar as linhas e colunas,
   assim como, quando decrementar ou reinicia-las. Lembre-se, ambas 
   comecam em 1.
   [2] Toda vez que voce encontrar um lexema completo, voce deve retornar
   um objeto Token(Tag, "lexema", linha, coluna). Cuidado com as
   palavras reservadas, que ja sao cadastradas na TS. Essa consulta
   voce devera fazer somente quando encontrar um Identificador.
   [3] Se o caractere lido nao casar com nenhum caractere esperado,
   apresentar a mensagem de erro na linha e coluna correspondente.
   Obs.: lembre-se de usar o metodo retornaPonteiro() quando necessario. 
         lembre-se de usar o metodo sinalizaErroLexico() para mostrar
         a ocorrencia de um erro lexico.
   '''
   def __init__(self, input_file):
      try:
         self._input_file: TextIO = open(input_file, 'rb')
         self._leitor: Generator = self._le_arquivo()
         self._lexema: str = ''
         self._simbolo: str = ''
         self._sep: tuple = (' ', '\t', '\n', '\r')
         self._estado: int = 1
         self._qtd_erros: int = 0
         self.list_tokens: list = []
         self.lookahead = 0
         self._line_atual = 1
         self._column_atual = 0
         self._line_lexer = 1
         self._column_lexer = 0
         self.ts = TS()
      except IOError:
         print('Erro de abertura do arquivo. Encerrando.')
         sys.exit(0)

   def _closeFile(self):
      try:
         self._input_file.close()
      except IOError:
         print('Erro ao fechar arquivo. Encerrando.')
         sys.exit(0)

   def sinalizaErroLexico(self, message: str = 'Caractere invalido') -> str:
      self._qtd_erros += 1
      if self._qtd_erros > 0:
         logging.critical('Limite máximo de erros lexicos suportados foi atingido.')
         raise SyntaxError
      return f"[Erro Lexico]: {message} [ { self._simbolo} ] na linha { str(self._line_atual)} e coluna {str(self._column_atual)}"

   def retornaPonteiro(self):
      self._input_file.seek(self._input_file.tell()-1)


   def printTS(self):
      self.ts.printTS()

   def printTokens(self):
      for token in self.list_tokens:
         try:
            print(token.toString())
         except:
            print('[Erro Lexico]:', token)

   def _limpa_lexema(self):
      self._lexema = ''
      self._estado = 1

   def _atualiza_linha_lexer(self):
      self._line_lexer = self._line_atual
      self._column_lexer = self._column_atual

   def _le_arquivo(self) -> Generator:
      while True:
         try:
            self._simbolo: str = self._input_file.read(1).decode('ascii')
            
            # Sinaliza coluna e linha
            self._column_atual += 1
            if self._simbolo == '\n':
               self._line_atual += 1
               self._column_atual = 0
            print(self._simbolo)
            yield self._simbolo.lower()
         
         except UnicodeDecodeError as e:
            print(f'[Decode Error] Não foi possivel ler o caractere na posição linha {self._line_atual}, coluna {self._column_atual}')
            raise

   def analisa(self):
      
      while True:
         self._simbolo:str = next(self._leitor)
         
         #EOF
         if self._simbolo == '':
         
            self.list_tokens.append(Token(Tag.EOF, Tag.EOF.value, self._line_atual, self._column_atual))
            self._closeFile()
            break
         if self._estado == 1:
            
            list_simbolos: list = [ smb.value for smb in self.ts.get_SMB()]
            if self._simbolo in list_simbolos:
               self.list_tokens.append(Token(Tag(self._simbolo), Tag(self._simbolo).value, self._line_atual, self._column_atual))
               continue

            self._atualiza_linha_lexer()
            if self._simbolo in self._sep:
               self._estado = 1
               continue
            
            if self._simbolo == '=':
               self._estado = 2
               continue

            if self._simbolo == '!':
               self._estado = 4
               continue
            
            if self._simbolo == '<':
               self._estado = 6
               continue
            
            if self._simbolo == '>':
               self._estado = 9
               continue

            if self._simbolo.isdigit():
               self._lexema += self._simbolo
               self._estado = 12
               continue
            
            if self._simbolo.isalpha():
               self._lexema += self._simbolo
               self._estado = 14
               continue
            
            if self._simbolo == ':':
               self._estado = 16
               continue
            
            if self._simbolo == '"':
               self._estado = 17
               continue
            
            self.list_tokens.append(self.sinalizaErroLexico())
            self._limpa_lexema()
            continue

         if self._estado == 2:
            self._limpa_lexema()
            if self._simbolo == '=':
               self.list_tokens.append(Token(Tag.OP_EQ, Tag.OP_EQ.value, self._line_lexer, self._column_lexer))
               continue
               
            self.list_tokens.append()
            continue

         if self._estado == 4:
            self._limpa_lexema()
            if self._simbolo == '=':
               self.list_tokens.append(Token(Tag.OP_NE, Tag.OP_NE.value, self._line_lexer, self._column_lexer))
               continue

            self.list_tokens.append(self.sinalizaErroLexico())
            continue
         
         if self._estado == 16:
            self._limpa_lexema()
            if self._simbolo == '=':
               self.list_tokens.append(Token(Tag.OP_ATRIB, Tag.OP_ATRIB.value, self._line_lexer, self._column_lexer))
               continue

            self.list_tokens.append(self.sinalizaErroLexico())
            continue
         
         if self._estado == 17:
            if self._simbolo == '"':
               self._limpa_lexema()
               self.list_tokens.append(Token(Tag.KW_CHAR, self._lexema, self._line_lexer, self._column_lexer))
               continue
            self._lexema += self._simbolo
            
            if self._simbolo == '\n':
               self.list_tokens.append(self.sinalizaErroLexico("Era esperado uma aspas dupla na linha"))
            continue

         if self._estado == 6:
            self._limpa_lexema()
            if self._simbolo == '=':
               self.list_tokens.append(Token(Tag.OP_LE, Tag.OP_LE.value, self._line_lexer, self._column_lexer))
               continue

            self.retornaPonteiro()
            self.list_tokens.append(Token(Tag.OP_LT, Tag.OP_LT.value, self._line_lexer, self._column_lexer))
            continue

         if self._estado == 9:
            self._limpa_lexema()
            if self._simbolo == '=':
               self.list_tokens.append(Token(Tag.OP_GE, Tag.OP_GE.value, self._line_lexer, self._column_lexer))
               continue

            self.retornaPonteiro()
            self.list_tokens.append(Token(Tag.OP_GT, Tag.OP_GT.value, self._line_lexer, self._column_lexer))
            continue
         
         if self._estado == 12:
            if self._simbolo.isdigit():
               self._lexema += self._simbolo           
               continue
            
            self.retornaPonteiro()
            self.list_tokens.append(Token(Tag.NUM, self._lexema, self._line_lexer, self._column_lexer))
            self._limpa_lexema()
         if self._estado == 14:
            if self._simbolo.isalnum():
               self._lexema += self._simbolo
               continue
         
            if not self.ts.getToken(self._lexema):
               token = Token(Tag.ID, self._lexema, self._line_lexer, self._column_lexer)
               self.list_tokens.append(token)
               self.ts.addToken(self._lexema, token)

            self._limpa_lexema()
            self.retornaPonteiro()
      # fim while    

      