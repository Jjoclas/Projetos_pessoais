import sys
import logging
from token_pasc import Token
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
		

	def sinalizaErroSemantico(self, message):

		print("[Erro Semantico] na linha " + str(self.token.getLinha()) + " e coluna " + str(self.token.getColuna()) + ": ")
		print(message, "\n")


	def sinalizaErroSintatico(self, message):
		print("[Erro Sintatico] na linha " + str(self.token.getLinha()) + " e coluna " + str(self.token.getColuna()) + ": ")
		print(message, "\n")

		self._qtd_erros_sintatico += 1
		if self._qtd_erros_sintatico > 0:
			logging.critical('Limite máximo de erros sintaticos suportados foi atingido.')
			sys.exit(0)
		self.advance()

	def msg_simbolos_esperados(self, simbolo):
		tpl_smb: list = [ keys[1] for keys in self.TB.keys() if simbolo in keys ]
		return f'Esperado: {tpl_smb}, recebido: '

	def advance(self):
		if not isinstance(self.token, str): # erro no Lexer
			print("[DEBUG] token: ", self.token.toString())
		
		try:
			self.token = next(self.gen_token)
		except StopIteration:
			pass

		if isinstance(self.token, str): # erro no Lexer
			self.advance()
	

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
		print(list_simbolo)
		self.desempilha()
		list_simbolo = list(list_simbolo)
		list_simbolo.reverse()
		print(list_simbolo)
		print('print\n\n')
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
				self.sinalizaErroSintatico(f'Esperado: {simbolo}, recebido: {self.token.lexema}')			
			else:
				print('TOKEN', self.token.tag )
				print(f'\nTB\nToken: {self.token.tag}\nSimbolo: {simbolo}\n', TB.get((simbolo, self.token.tag), 'N\A'))
				if TB.get((simbolo, self.token.tag), 'N\A') != 'N\A':
					self.empilha(TB[simbolo, self.token.tag])
					continue
				
				self.sinalizaErroSintatico(self.msg_simbolos_esperados(simbolo) + self.token.lexema)			

    
