class Token:
   '''
   Classe que representa um token
   '''
   def __init__(self, nome, lexema, linha, coluna):
      self.nome = nome
      self.lexema = lexema
      self.linha = linha
      self.coluna = coluna

   def getNome(self):
      return self.nome

   def getLexema(self):
      return self.lexema

   def getLinha(self):
      return self.linha

   def setLinha(self, linha):
      self.linha = linha

   def getColuna(self):
      return self.coluna

   def setColuna(self, coluna):
      self.coluna = coluna


   def toString(self):
      str_token: str = f"< {str(self.nome.name)}, {repr(self.lexema)}" 
      str_token += ">" if self.linha == 0 else f" Linha:{self.linha}, Coluna:{self.coluna}>"
      return str_token
