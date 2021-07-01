import sys
import logging
from tag import Tag
from tb_preditiva import TB

class Parser():

	def __init__(self, lexer):
		self.lexer = lexer
		self.gen_token = lexer.le_lexer() # Leitura inicial obrigatoria do primeiro simbolo
		self.token = next(self.gen_token)
		self.pilha: list = [Tag.EOF, 'prog'] #Pilha inciada com simbolo incial e EOF
		self.TB: dict = TB
		self._qtd_erros_sintatico: int = 0
		
		if self.token is None: # erro no Lexer
			sys.exit(0)


	def sinalizaErroSemantico(self, message):

		print("[Erro Semantico] na linha " + str(self.token.getLinha()) + " e coluna " + str(self.token.getColuna()) + ": ")
		print(message, "\n")


	def sinalizaErroSintatico(self, message):
		print("[Erro Sintatico] na linha " + str(self.token.getLinha()) + " e coluna " + str(self.token.getColuna()) + ": ")
		print(message, "\n")

		self._qtd_erros_sintatico += 1
		if self._qtd_erros_sintatico > 0:
			logging.critical('Limite máximo de erros sintaticos suportados foi atingido.')
			raise RuntimeError	


	def advance(self):
		print("[DEBUG] token: ", self.token.toString())
		self.token = next(self.gen_token)
		print(self.token.toString())
		if self.token is None: # erro no Lexer
			sys.exit(0)
	

	def skip(self, message):
		self.sinalizaErroSintatico(message)
		self.advance()


	def isToken(self, simbolo):
		# print('ISTOKEN', simbolo, '\n\n')
		if isinstance(simbolo, str):
			return False
		
		return True


	def desempilha(self):
		self.pilha.pop(-1)


	def empilha(self, list_simbolo):
		self.desempilha()
		list_simbolo.reverse()
		self.pilha.extend(list_simbolo)

	def le_pilha(self):
		while self.pilha:
			simbolo = self.pilha[-1]
			# print('\npilha',self.pilha)
			# print('TOKEN', self.token.tag , '\n\n')

			if self.isToken(simbolo):
				if simbolo == self.token.tag:
					self.desempilha()
					self.advance()
					continue
				# print('ISTOKEN ERROR')
				self.sinalizaErroSintatico('message')			
			else:
				# print('TOKEN', self.token.tag )
				# print(f'\nTB\nToken: {self.token.tag}\nSimbolo: {simbolo}\n', TB[simbolo, self.token.tag])
				if TB.get((simbolo, self.token.tag), 'N\A') != 'N\A':
					self.empilha(TB[simbolo, self.token.tag])
					continue
				
				self.sinalizaErroSintatico('message')			

    
