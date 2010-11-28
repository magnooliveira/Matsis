# coding:UTF-8
#!/usr/bin/env python

#Autor: Magno Lima Oliveira

from sys import *
import os.path

caminho_da_matriz = os.path.expanduser("~/Matsis/View/interface_matriz")
caminho_do_controller =  os.path.expanduser("~/Matsis/Controller")

path.append(caminho_da_matriz)
path.append(caminho_do_controller)

from janela_matriz import *
from janela_matriz_b import *
from ClasseControle import *
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

class Janela_Ordem(object):

	def __init__(self, tipo_operacao, coluna_anterior = 0, mat_A = None):
		"""
		Metodo Construtor da classe
		"""
		self.tipo_operacao = tipo_operacao
		if (self.tipo_operacao > 0)  and (self.tipo_operacao < 4):
			self.arquivoglade = os.path.expanduser( "~/Matsis/View/interface_ordem/janela_ordem_quadrada.glade")
			self.xml = gtk.glade.XML(self.arquivoglade)
			self.edt1 = self.xml.get_widget("edt_ordem1")

		elif self.tipo_operacao > 3:
			self.arquivoglade = os.path.expanduser( "~/Matsis/View/interface_ordem/janela_ordem_variada.glade")
			self.xml = gtk.glade.XML(self.arquivoglade)
			self.edt1 = self.xml.get_widget("edt_ordem1")
			self.edt2 = self.xml.get_widget("edt_ordem2")

		self.controle = Controle()
		self.fix = self.xml.get_widget('fixed1')
		self.btn_ok = self.xml.get_widget('btn_ok')

		self.coluna_anterior = coluna_anterior
		self.mat_A  = mat_A

		self.mainWindow_ordem = self.xml.get_widget('window_ordem')
		self.mainWindow_ordem.show_all()
		self.ordem1 = 0
		self.ordem2 = 0
		self.xml.signal_autoconnect(self)

		gtk.main()

	def on_window_ordem_destroy(self,*args):
		gtk.main_quit()

	def passaParaInteiroOrdem1(self):
		try:
			self.ordem1 = int(float(self.edt1.get_text()))
			return self.ordem1
		except:
			pass

	def passaParaInteiroOrdem2(self):
		try:
			self.ordem2 = int(float(self.edt2.get_text()))
			return self.ordem2
		except:
			pass

	def validar_edt(self):
		if (self.tipo_operacao > 0)  and (self.tipo_operacao < 4):

			if self.xml.get_widget('edt_ordem1').get_text()=="":
				self.controle.alerta("Digite a ordem !")
				self.xml.get_widget('edt_ordem1').grab_focus()

			else:

				if (self.passaParaInteiroOrdem1() > 10) or (self.passaParaInteiroOrdem1() < 1):
					self.controle.alerta("Valor máximo é 10 e o valor mínimo 1")
					self.xml.get_widget('edt_ordem1').grab_focus()

				else:
					return True

		elif self.tipo_operacao > 3:

			if self.xml.get_widget('edt_ordem1').get_text()=="":
				self.controle.alerta("Digite o número de Linhas !")
				self.xml.get_widget('edt_ordem1').grab_focus()

			elif self.xml.get_widget('edt_ordem2').get_text()=="":
				self.controle.alerta("Digite o número de Colunas !")
				self.xml.get_widget('edt_ordem2').grab_focus()

			elif (self.passaParaInteiroOrdem1() > 10) or (self.passaParaInteiroOrdem1() < 1):
					self.controle.alerta("Valor máximo de Linha é 10 e o mínimo 1")
					self.xml.get_widget('edt_ordem1').grab_focus()

			elif (self.passaParaInteiroOrdem2() > 10) or (self.passaParaInteiroOrdem2() < 1):
					self.controle.alerta("Valor máximo de Coluna é 10 e o mínimo 1")
					self.xml.get_widget('edt_ordem2').grab_focus()

			else:
				return True

	def on_btn_ok_clicked(self, *args):
		if self.validar_edt():
			if self.coluna_anterior == 0:
				self.mainWindow_ordem.hide()
				matriz = Janela_Matriz(self.tipo_operacao, self.ordem1, self.ordem2)
				self.mainWindow_ordem.destroy()
			else:
				if self.coluna_anterior != self.ordem1:
					self.controle.alerta("O número de colunas da matriz A é diferente do número de linhas da Matriz B !")
					self.xml.get_widget('edt_ordem1').grab_focus()
				else:
					self.mainWindow_ordem.hide()
					matriz = Janela_Matriz_B(self.tipo_operacao,self.mat_A, self.ordem1, self.coluna_anterior)
					self.mainWindow_ordem.destroy()


if __name__=="__main__":
	j = Janela_Ordem(7, 1,[[2]])

