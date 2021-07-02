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
		

	def sinalizaErroSemantico(self, message):

		print("[Erro Semantico] na linha " + str(self.token.getLinha()) + " e coluna " + str(self.token.getColuna()) + ": ")
		print(message, "\n")
		sys.exit(0)


	def sinalizaErroSintatico(self, message):
		print("[Erro Sintatico] na linha " + str(self.token.getLinha()) + " e coluna " + str(self.token.getColuna()) + ": ")
		self.token.tipo = Tag.TIPO_ERRO
		print("[DEBUG] token: ", self.token.toString())
		print(message, "\n")

		self._qtd_erros_sintatico += 1
		if self._qtd_erros_sintatico > 5:
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
		if isinstance(simbolo, str):
			return False
		
		return True


	def desempilha(self):
		self.pilha.pop(-1)


	def empilha(self, tpl_simbolo):
		self.desempilha()
		list_simbolo = list(tpl_simbolo)
		list_simbolo.reverse()
		self.pilha.extend(list_simbolo)

	def le_pilha(self):
		while self.pilha:
			simbolo = self.pilha[-1]

			if self.isToken(simbolo):
				if simbolo == self.token.tag:
					self.desempilha()
					self.advance()
					continue
	
				self.sinalizaErroSintatico(f'Esperado: {simbolo}, recebido: {self.token.lexema}')			
			else:
				if simbolo.startswith('func'):
					getattr(self, simbolo)()
					self.desempilha()
					simbolo = self.pilha[-1]

				if TB.get((simbolo, self.token.tag), 'N\A') != 'N\A':
					self.empilha(TB.get((simbolo, self.token.tag)))
					continue
	
				self.sinalizaErroSintatico(self.msg_simbolos_esperados(simbolo) + self.token.lexema)			

    
	def func_avalia_declaracao(self):
		if self.token.tipo == Tag.TIPO_VOID:
			self.sinalizaErroSemantico(f'Variavel {self.token.lexema} não declarada.')

	def func_avalia_tipo(self):
		token_anterior = self.lexer.list_tokens[-3]
		if self.token.tipo != token_anterior: #Valia tipo do ultimo token com o antepenultimo
			self.sinalizaErroSemantico(f'Variavel {self.token.lexema} não compativel com tipo {token_anterior.tipo}.')
	
	def func_add_tipo(self):
		token_anterior = self.lexer.list_tokens[-3]
		if self.token.tipo == Tag.TIPO_VOID or self.token.tipo == token_anterior.tipo:
			token_anterior.tipo = self.token.tipo

		self.sinalizaErroSemantico(f'Variavel {self.token.lexema} não compativel com tipo {token_anterior.tipo}.')

	def func_add_tipo_decl(self):
		print([ token.tag for token in self.lexer.list_tokens])
		self.lexer.list_tokens[-1].tipo = self.lexer.list_tokens[-2].tipo
		self.token.tipo = self.lexer.list_tokens[-2].tipo