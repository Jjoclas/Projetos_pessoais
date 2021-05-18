from tag import Tag
from token import Token

class TS:
   '''
   Classe para a tabela de simbolos representada por um dicionario: {'chave' : 'valor'}
   '''
   def __init__(self):
      '''
      Repare que as palavras reservadas sao todas cadastradas
      a principio com linha e coluna em zero
      '''
      self.ts = {}
      self._add_kw()

   def getToken(self, lexema):
      token = self.ts.get(lexema)
      return token

   def addToken(self, lexema, token):
      self.ts[lexema] = token

   def printTS(self):
      for k, t in (self.ts.items()):
         print(k, ":", t.toString())

   def _add_kw(self):
      for kw in Tag:
         if kw.name.startswith('KW_'):
            self.ts[kw.value] = Token(kw, kw.value, 0, 0)