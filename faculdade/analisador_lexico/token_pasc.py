from tag import Tag
class Token:
   '''
   Classe que representa um token
   '''
   def __init__(self, tag, lexema, linha, coluna, tipo=Tag.TIPO_VOID):
      self.nome = tag.name
      self.tag = tag
      self.lexema = lexema
      self.linha = linha
      self.coluna = coluna
      self.tipo = tipo

      if tag in (Tag.CHAR, Tag.KW_CHAR):
         self.tipo = Tag.TIPO_CHAR
      
      if tag in (Tag.NUM, Tag.KW_NUM):
         self.tipo = Tag.TIPO_NUM

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
      str_token: str = f"< {str(self.nome)}, {repr(self.lexema)}, Tipo: {str(self.tipo)}" 
      str_token += ">" if self.linha == 0 else f" Linha:{self.linha}, Coluna:{self.coluna}>"
      return str_token
