class Escalonamento(object):
	"""
		Esta classe escalona um sistema de 3 linhas e 3 equacoes, ela tera
		uma classe controladora que irar indicar qual linha deve comecar
	"""
	def __init__(self,primeira_linha="", segunda_linha="", terceira_linha=""):
		self.primeira_linha = list(primeira_linha)
		self.segunda_linha = list(segunda_linha)
		self.terceira_linha = list(terceira_linha)

	def multiplica_linha_pelo_modificador(self, linha_a_ser_modificada, numero_modificador):
		linha_modificada = map(lambda x:x*numero_modificador, linha_a_ser_modificada)
		return linha_modificada

	def somar_linha_por_outra_linha(self, linha_a_ser_modificada, linha_a_ser_somada, posicao = 0):
		linha_adaptada = self.multiplica_linha_pelo_modificador(linha_a_ser_modificada, -linha_a_ser_somada[posicao])
		linha_modificada = map(lambda x,y:x+y,linha_adaptada, linha_a_ser_somada)
		return linha_modificada

	def trocar_segundo_pelo_terceiro(self):
		self.segunda_linha, self.terceira_linha = self.terceira_linha, self.segunda_linha
		return self.segunda_linha

	def avaliar_primeiro_elemento_da_segunda_linha(self):
		if self.segunda_linha[0] == 0 and (self.terceira_linha[0] != 0):
			return self.trocar_segundo_pelo_terceiro()

	def fazer_o_primeiro_elemento_da_primeira_linha_ficar_um(self):
		if self.primeira_linha[0] != 0:
			numero_modificador = 1./self.primeira_linha[0]
			self.primeira_linha = self.multiplica_linha_pelo_modificador(self.primeira_linha, numero_modificador)
		return self.primeira_linha

	def fazer_o_primeiro_elemento_da_segunda_linha_ficar_zero(self):
		self.avaliar_primeiro_elemento_da_segunda_linha()
		self.segunda_linha = self.somar_linha_por_outra_linha(self.primeira_linha, self.segunda_linha)
		return self.segunda_linha

	def fazer_o_primeiro_elemento_da_terceira_linha_ficar_zero(self):
		if self.terceira_linha[0] != 0:
			self.terceira_linha = self.somar_linha_por_outra_linha(self.primeira_linha, self.terceira_linha)
		return self.terceira_linha

	def trocar_da_segunda_com_a_terceira_linha_para_obter_dois_zeros_na_ultima_linha(self):
		if self.segunda_linha[1] == 0 and (self.terceira_linha[1] != 0):
			self.trocar_segundo_pelo_terceiro()
		return self.segunda_linha

	def fazer_o_segundo_elemento_da_terceira_linha_ficar_zero_quando_o_segundo_elemento_da_segunda_for_igual(self):
		if (self.segunda_linha[1] == self.terceira_linha[1]) and  (self.terceira_linha[1] != 0):
			segunda_linha_adaptada = self.multiplica_linha_pelo_modificador(self.segunda_linha, -1)
			self.terceira_linha = map(lambda x,y:x+y, segunda_linha_adaptada, self.terceira_linha)
		return self.terceira_linha

	def fazer_o_segundo_elemento_da_segunda_linha_ficar_um(self):
		if self.segunda_linha[1] != 0:
			numero_modificador = 1./self.segunda_linha[1]
			self.segunda_linha = self.multiplica_linha_pelo_modificador(self.segunda_linha, numero_modificador)
		return self.segunda_linha

	def fazer_o_segundo_elemento_da_terceira_linha_ficar_zero(self):
		if self.terceira_linha[1] != 0:
			self.terceira_linha = self.somar_linha_por_outra_linha(self.segunda_linha, self.terceira_linha, posicao = 1)
		return self.terceira_linha

	def fazer_o_terceiro_elemento_da_terceira_linha_ficar_um(self):
		if self.terceira_linha[2] != 0:
			numero_modificador = 1./self.terceira_linha[2]
			self.terceira_linha = self.multiplica_linha_pelo_modificador(self.terceira_linha, numero_modificador)
		return self.terceira_linha

	def fazer_o_terceiro_elemento_da_segunda_linha_ficar_zero(self):
		if self.segunda_linha[2] != 0:
			self.segunda_linha = self.somar_linha_por_outra_linha(self.terceira_linha, self.segunda_linha, posicao = 2)
		return self.segunda_linha

	def somar_o_quarto_elemento_da_terceira_linha_com_o_oposto_do_quarto_elemento_da_segunda_linha(self):
		# [0 0 0 x]  and [0 0 0 y]   seja  diferente de zero
		if (self.terceira_linha[2] == 0) and (self.segunda_linha[2] == 0) and (self.segunda_linha[3] == self.terceira_linha[3]):
			self.terceira_linha[3] = self.terceira_linha[3] - self.segunda_linha[3]
		return self.terceira_linha

	def fazer_o_segundo_elemento_da_primeira_linha_ficar_zero(self):
		if self.segunda_linha[1] == 0:
			linha_adaptada = self.segunda_linha
			linha_a_ser_somada = self.primeira_linha
			self.primeira_linha = map(lambda x,y:x+y,linha_adaptada, linha_a_ser_somada)
			return self.primeira_linha
		if self.primeira_linha[1] != 0:
			self.primeira_linha = self.somar_linha_por_outra_linha(self.segunda_linha, self.primeira_linha, posicao = 1)
		return self.primeira_linha

	def fazer_o_terceiro_elemento_da_primeira_linha_ficar_zero(self):
		if self.terceira_linha[2] == 0:
			linha_adaptada = self.terceira_linha
			linha_a_ser_somada = self.primeira_linha
			self.primeira_linha = map(lambda x,y:x+y,linha_adaptada, linha_a_ser_somada)
			return self.primeira_linha
		if self.primeira_linha[2] != 0:
			self.primeira_linha = self.somar_linha_por_outra_linha(self.terceira_linha, self.primeira_linha, posicao = 2)
		return self.primeira_linha

	def executarTodasAsEtapa(self):
		self.fazer_o_primeiro_elemento_da_primeira_linha_ficar_um()
		self.fazer_o_primeiro_elemento_da_segunda_linha_ficar_zero()
		self.fazer_o_primeiro_elemento_da_terceira_linha_ficar_zero()
		self.trocar_da_segunda_com_a_terceira_linha_para_obter_dois_zeros_na_ultima_linha()
		self.fazer_o_segundo_elemento_da_terceira_linha_ficar_zero_quando_o_segundo_elemento_da_segunda_for_igual()
		self.fazer_o_segundo_elemento_da_segunda_linha_ficar_um()
		self.fazer_o_segundo_elemento_da_terceira_linha_ficar_zero()
		self.fazer_o_terceiro_elemento_da_terceira_linha_ficar_um()
		self.fazer_o_terceiro_elemento_da_segunda_linha_ficar_zero()
		self.somar_o_quarto_elemento_da_terceira_linha_com_o_oposto_do_quarto_elemento_da_segunda_linha()
		self.fazer_o_segundo_elemento_da_primeira_linha_ficar_zero()
		self.fazer_o_terceiro_elemento_da_primeira_linha_ficar_zero()

	def __repr__(self):
		return ("x = %.3f, y = %.3f, z = %0.3f")%(self.primeira_linha[3], self.segunda_linha[3],\
				self.terceira_linha[3])

