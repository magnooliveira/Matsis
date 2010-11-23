from escalonamento import Escalonamento

class EscalonamentoQuatroLinhas(Escalonamento):

	def __init__(self,primeira_linha="", segunda_linha="", terceira_linha="", quarta_linha=""):
		self.primeira_linha = list(primeira_linha)
		self.segunda_linha = list(segunda_linha)
		self.terceira_linha = list(terceira_linha)
		self.quarta_linha = list(quarta_linha)

	def trocar_terceiro_pelo_quarto(self):
		self.terceira_linha, self.quarta_linha = self.quarta_linha, self.terceira_linha
		return self.terceira_linha

	def fazer_o_primeiro_elemento_da_quarta_linha_ficar_zero(self):
		if self.quarta_linha[0] != 0:
			self.quarta_linha = self.somar_linha_por_outra_linha(self.primeira_linha, self.quarta_linha)
		return self.quarta_linha

	def fazer_o_segundo_elemento_da_quarta_linha_ficar_zero(self):
		if self.quarta_linha[1] != 0:
			self.quarta_linha = self.somar_linha_por_outra_linha(self.segunda_linha, self.quarta_linha, posicao = 1)
		return self.quarta_linha

	def trocar_da_terceira_com_a_quarta_linha_para_obter_tres_zeros_na_ultima_linha(self):
		if self.terceira_linha[2] == 0:
			self.trocar_terceiro_pelo_quarto()
		return self.terceira_linha

	def fazer_o_terceiro_elemento_da_quarta_linha_ficar_zero_quando_o_terceiro_elemento_da_terceira_for_igual(self):
		if self.terceira_linha[2] == self.quarta_linha[2]:
			terceira_linha_adaptada = self.multiplica_linha_pelo_modificador(self.terceira_linha, -1)
			self.quarta_linha = map(lambda x,y:x+y, terceira_linha_adaptada, self.quarta_linha)
		return self.quarta_linha

	def fazer_o_terceiro_elemento_da_terceira_linha_ficar_um(self):
		if self.terceira_linha[2] != 0:
			numero_modificador = 1./self.terceira_linha[2]
			self.terceira_linha = self.multiplica_linha_pelo_modificador(self.terceira_linha, numero_modificador)
		return self.terceira_linha

	def fazer_o_terceiro_elemento_da_quarta_linha_ficar_zero(self):
		if self.quarta_linha[2] != 0:
			self.quarta_linha = self.somar_linha_por_outra_linha(self.terceira_linha, self.quarta_linha, posicao = 2)
		return self.quarta_linha

	def fazer_o_quarto_elemento_da_quarta_linha_ficar_um(self):
		if self.quarta_linha[3] != 0:
			numero_modificador = 1./self.quarta_linha[3]
			self.quarta_linha = self.multiplica_linha_pelo_modificador(self.quarta_linha, numero_modificador)
		return self.quarta_linha

	def fazer_o_quarto_elemento_da_terceira_linha_ficar_zero(self):
		if self.terceira_linha[3] != 0:
			self.terceira_linha = self.somar_linha_por_outra_linha(self.quarta_linha, self.terceira_linha, posicao = 3)
		return self.terceira_linha

	def fazer_o_quarto_elemento_da_segunda_linha_ficar_zero(self):
		if self.segunda_linha[3] != 0:
			self.segunda_linha = self.somar_linha_por_outra_linha(self.quarta_linha, self.segunda_linha, posicao = 3)
		return self.segunda_linha

	def fazer_o_quarto_elemento_da_primeira_linha_ficar_zero(self):
		if self.primeira_linha[3] != 0:
			self.primeira_linha = self.somar_linha_por_outra_linha(self.quarta_linha, self.primeira_linha, posicao = 3)
		return self.primeira_linha

	def executarTodasAsEtapa(self):
		self.fazer_o_primeiro_elemento_da_primeira_linha_ficar_um()
		self.fazer_o_primeiro_elemento_da_segunda_linha_ficar_zero()
		self.fazer_o_primeiro_elemento_da_terceira_linha_ficar_zero()
		self.fazer_o_primeiro_elemento_da_quarta_linha_ficar_zero()#
		self.trocar_da_segunda_com_a_terceira_linha_para_obter_dois_zeros_na_ultima_linha()
		self.fazer_o_segundo_elemento_da_terceira_linha_ficar_zero_quando_o_segundo_elemento_da_segunda_for_igual()
		self.fazer_o_segundo_elemento_da_segunda_linha_ficar_um()
		self.fazer_o_segundo_elemento_da_terceira_linha_ficar_zero()
		self.fazer_o_segundo_elemento_da_quarta_linha_ficar_zero()#
		self.trocar_da_terceira_com_a_quarta_linha_para_obter_tres_zeros_na_ultima_linha()#
		self.fazer_o_terceiro_elemento_da_quarta_linha_ficar_zero_quando_o_terceiro_elemento_da_terceira_for_igual()#
		self.fazer_o_terceiro_elemento_da_terceira_linha_ficar_um()
		self.fazer_o_terceiro_elemento_da_quarta_linha_ficar_zero()#
		self.fazer_o_quarto_elemento_da_quarta_linha_ficar_um()#
		self.fazer_o_quarto_elemento_da_terceira_linha_ficar_zero()#
		self.fazer_o_quarto_elemento_da_segunda_linha_ficar_zero()#
		self.fazer_o_quarto_elemento_da_primeira_linha_ficar_zero()#
		self.fazer_o_terceiro_elemento_da_segunda_linha_ficar_zero()
		self.fazer_o_segundo_elemento_da_primeira_linha_ficar_zero()
		self.fazer_o_terceiro_elemento_da_primeira_linha_ficar_zero()

	def __repr__(self):
		return ("x = %.3f, y = %.3f, z = %0.3f, w = %0.3f")%(self.primeira_linha[4], self.segunda_linha[4],\
				self.terceira_linha[4], self.quarta_linha[4])

