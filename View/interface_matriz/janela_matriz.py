# coding:UTF-8
#!/usr/bin/env python

from sys import *
import os

caminho_do_model = os.path.expanduser( "~/Matsis/Model/matriz_model")
caminho_do_controller =  os.path.expanduser("~/Matsis/Controller")
caminho_da_view_ordem =  os.path.expanduser ("~/Matsis/View/interface_ordem")

path.append(caminho_do_model)
path.append(caminho_do_controller)
path.append(caminho_da_view_ordem)

from ordem import *
from janela_numero import *
from janela_matriz_b import *
from ClasseControle import *
from matriz import *

try:
	import pygtk
	pygtk.require("2.0")
except:
	pass
try:
	import gtk
	import gtk.glade
except:
	sys.exit(1)

class Janela_Matriz(object):

	def __init__(self, tipo_operacao, linha , coluna = 0):
		self.linha = linha
		self.coluna = coluna
		self.tipo_operacao = tipo_operacao

		self.controle = Controle()

		# verifica se he ordem quadrada
		if self.coluna == 0:
			self.coluna = self.linha

		if self.tipo_operacao == 1:
			self.arquivoglade = os.path.expanduser("~/Matsis/View/interface_matriz/janela_matriz_traco.glade")

		if self.tipo_operacao == 2:
			self.arquivoglade = os.path.expanduser("~/Matsis/View/interface_matriz/janela_matriz_determinante.glade")

		if self.tipo_operacao == 3:
			self.arquivoglade = os.path.expanduser("~/Matsis/View/interface_matriz/janela_matriz_inversa.glade")

		if self.tipo_operacao == 4:
			self.arquivoglade = os.path.expanduser("~/Matsis/View/interface_matriz/janela_matriz_transposta.glade")

		if self.tipo_operacao == 5:
			self.arquivoglade = os.path.expanduser("~/Matsis/View/interface_matriz/janela_matriz_soma_A.glade")

		if self.tipo_operacao == 6:
			self.arquivoglade = os.path.expanduser("~/Matsis/View/interface_matriz/janela_matriz_sub_A.glade")

		if self.tipo_operacao == 7:
			self.arquivoglade = os.path.expanduser("~/Matsis/View/interface_matriz/janela_matriz_mult_A.glade")

		if self.tipo_operacao == 8:
			self.arquivoglade = os.path.expanduser("~/Matsis/View/interface_matriz/janela_matriz_mult_num_A.glade")

		self.xml = gtk.glade.XML(self.arquivoglade)

		self.produto = self.linha*self.coluna
		self.matriz = []

		self.fix = self.xml.get_widget('fixed')
		px = 0
		py = 0
		self.lista = []
		for i in range(1, self.linha+1):
			py = py +40
			px = 0
			for j in range(1, self.coluna+1):
				px = px + 70
				self.aij = gtk.Entry()
				self.aij.set_size_request(60,25)
				self.aij.set_uposition(px,py)
				self.fix.add(self.aij)
				self.lista.append(self.aij)

		self.mainWindow = self.xml.get_widget('window')
		self.mainWindow.show_all()

		self.xml.signal_autoconnect(self)

		gtk.main()

	def on_btn_limpar_clicked(self, *args):
		for posicao in range(0, self.produto):
			self.lista[posicao].set_text("")
		self.matriz = []

	def validar_edits(self)	:
		condicao = False
		for posicao in range(0, self.produto):
			condicao = True
			if self.lista[posicao].get_text() == "":
				self.controle.alerta("Campo a completar !")
				self.lista[posicao].grab_focus()
				condicao = False
				break;
		return condicao

	def passa_para_real_as_linhas(self):
		linha = []
		for posicao in range(0, self.produto):
				ai=float(self.lista[posicao].get_text())
				linha.append(ai)
				if ((posicao+1) % self.coluna == 0):
					linha = tuple(linha)
					self.matriz.append(linha)
					linha = []

		return self.matriz

	def on_btn_traco_clicked(self, *args):
		self.matriz = []
		if self.validar_edits():
			self.passa_para_real_as_linhas()
			mat = Matriz (self.matriz[:self.linha])
			traco = mat.calcular_Traco()
			self.controle.alerta("O traço é %.3f !"%traco)

	def on_btn_determinante_clicked(self, *args):
		self.matriz = []
		if self.validar_edits():
			self.passa_para_real_as_linhas()
			mat = Matriz (self.matriz[:self.linha])
			det = mat.calcular_determinante()
			self.controle.alerta("O Determinante é %.3f !"%det)

	def on_btn_inversa_clicked(self, *args):
		self.matriz = []
		if self.validar_edits():
			self.passa_para_real_as_linhas()
			mat = Matriz (self.matriz[:self.linha])
			inverso = mat.calcular_Inversa()
			texto = str(inverso)
			self.controle.alerta(texto)

	def on_btn_transposta_clicked(self, *args):
		self.matriz = []
		if self.validar_edits():
			self.passa_para_real_as_linhas()
			mat = Matriz (self.matriz[:self.linha])
			trans = mat.calcular_Transposta()
			texto = str(trans)
			self.controle.alerta(texto)

	def on_btn_matriz_a_clicked(self, *args):
		self.matriz = []
		if self.validar_edits():
			self.passa_para_real_as_linhas()
			mat_A = Matriz (self.matriz[:self.linha])
			mat_B = Janela_Matriz_B(self.tipo_operacao, mat_A, self.linha, self.coluna)

	def on_btn_matriz_a_sub_clicked(self, *args):
		self.matriz = []
		if self.validar_edits():
			self.passa_para_real_as_linhas()
			mat_A = Matriz (self.matriz[:self.linha])
			mat_B = Janela_Matriz_B(self.tipo_operacao ,mat_A, self.linha, self.coluna)

	def on_btn_matriz_a_mult_clicked(self, *args):
		self.matriz = []
		if self.validar_edits():
			self.passa_para_real_as_linhas()
			mat_A = Matriz (self.matriz[:self.linha])
			janela_ordem = Janela_Ordem(self.tipo_operacao, self.coluna, mat_A)

	def on_btn_matriz_a_mult_num_clicked(self, *args):
		self.matriz = []
		if self.validar_edits():
			self.passa_para_real_as_linhas()
			mat_A = Matriz (self.matriz[:self.linha])
			janela_numero = Janela_Numero(mat_A)

	def on_window_destroy(self,*args):
		gtk.main_quit()

if __name__=="__main__":
	j = Janela_Matriz(1,2,2)

