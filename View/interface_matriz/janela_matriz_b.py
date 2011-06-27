# coding:UTF-8
#!/usr/bin/env python

from sys import *
import os
import numpy

from random import randint

caminho_do_model = os.path.expanduser( "~/Matsis/Model/matriz_model")
caminho_do_controller =  os.path.expanduser("~/Matsis/Controller")

path.append(caminho_do_model)
path.append(caminho_do_controller)

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

class Janela_Matriz_B(object):

	def __init__(self, tipo_operacao, matriz_A, linha, coluna = 0):
		self.tipo_operacao = tipo_operacao
		self.linha = linha
		self.coluna = coluna
		self.matriz_A = matriz_A

		self.controle = Controle()

		# verifica se he ordem quadrada
		if self.coluna == 0:
			self.coluna = self.linha

		if self.tipo_operacao == 5:
			self.arquivoglade = os.path.expanduser("~/Matsis/View/interface_matriz/janela_matriz_soma_B.glade")

		if self.tipo_operacao == 6:
			self.arquivoglade = os.path.expanduser("~/Matsis/View/interface_matriz/janela_matriz_sub_B.glade")

		if self.tipo_operacao == 7:
			self.arquivoglade = os.path.expanduser("~/Matsis/View/interface_matriz/janela_matriz_mult_B.glade")


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
		self.mainWindow.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#4169E1"))
		self.mainWindow.show_all()

		self.xml.signal_autoconnect(self)

		gtk.main()

	def on_btn_limpar_clicked(self, *args):
		for posicao in range(0, self.produto):
			self.lista[posicao].set_text("")
		self.matriz = []

	def on_btn_preencher_clicked(self, *args):
		for posicao in range(0, self.produto):
			self.lista[posicao].set_text(str(randint(1,30)))

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

	def on_btn_matriz_somar_clicked(self, *args):
		self.matriz = []
		if self.validar_edits():
			self.passa_para_real_as_linhas()
			mat_B = Matriz (self.matriz[:self.linha])
			soma = mat_B.somar(self.matriz_A)
			texto = str(soma)
			self.controle.resultado(texto)

	def on_btn_matriz_subtrair_clicked(self, *args):
		self.matriz = []
		if self.validar_edits():
			self.passa_para_real_as_linhas()
			mat_B = Matriz (self.matriz[:self.linha])
			soma = mat_B.subtrair(self.matriz_A)
			texto = str(soma)
			self.controle.resultado(texto)

	def on_btn_matriz_multiplicar_clicked(self, *args):
		self.matriz = []
		if self.validar_edits():
			self.passa_para_real_as_linhas()
			mat_B = Matriz (self.matriz[:self.linha])
			soma = mat_B.multiplicar(self.matriz_A)
			texto = str(soma)
			self.controle.resultado(texto)

	def on_window_destroy(self,*args):
		gtk.main_quit()

if __name__=="__main__":
	j = Janela_Matriz_B([(1,2),(3,2)], 2, 2)

