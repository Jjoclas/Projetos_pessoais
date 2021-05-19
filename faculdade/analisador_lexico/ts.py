from tag import Tag
from token_pasc import Token

class TS:
   '''
   Classe para a tabela de simbolos representada por um dicionario: {'chave' : 'valor'}
   '''
   def __init__(self):
      
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
   
   def get_KW(self) -> tuple:
      list_token: list = []
      
      for kw in Tag:
         if kw.name.startswith('KW_'):
            list_token.append(kw)
      
      return tuple(list_token)

   def get_SMB(self) -> tuple:
      list_token: list = []
      
      for smb in Tag:
         if smb.name.startswith('SMB_'):
            list_token.append(smb)
      
      return tuple(list_token)

   def get_OP(self) -> tuple:
      list_token: list = []
      
      for op in Tag:
         if op.name.startswith('OP_'):
            list_token.append(op)
      
      return tuple(list_token)

   def _add_kw(self):
      for kw in self.get_KW():
         self.ts[kw.value] = Token(kw, kw.value, 0, 0)