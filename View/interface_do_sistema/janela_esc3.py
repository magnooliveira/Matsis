# coding: utf-8
#!/usr/bin/python
#Autor: Magno Lima Oliveira

from sys import path
import os.path

caminho_do_model = os.path.expanduser( "~/Matsis/Model/escalonamento_model")
caminho_do_controller =  os.path.expanduser("~/Matsis/Controller")

path.append(caminho_do_model)
path.append(caminho_do_controller)

from escalonamento import *
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

class Janela_Esc3(object):
	"""
	Janela para escalonamente de 3 por 3
	"""
	def __init__(self):
		"""
		Metodo Construtor da classe

		"""
		self.cont = 0
		self.primeira = None
		self.segunda = None
		self.terceira = None

		self.sistema = Escalonamento()
		self.validar = Controle()
		self.arquivoglade = os.path.expanduser("~/Matsis/View/interface_do_sistema/Janela_Esc3.glade")
		self.xml = gtk.glade.XML(self.arquivoglade)
		self.mainWindow = self.xml.get_widget('window1')
		self.btnGerarSistema = self.xml.get_widget('btnEscalonarSistema')
		self.btnLimpar = self.xml.get_widget('btnLimpar')
		self.mainWindow.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#FF00FF"))
		self.xml.signal_autoconnect(self)
		self.mainWindow.show_all()

		gtk.main()

	def passa_para_real_primeira_linha(self):
		a1=float(self.xml.get_widget("edta1").get_text())
		b1=float(self.xml.get_widget('edtb1').get_text())
		c1=float(self.xml.get_widget('edtc1').get_text())
		d1=float(self.xml.get_widget('edtd1').get_text())
		primeira_linha = (a1, b1, c1, d1)
		return primeira_linha

	def passa_para_real_segunda_linha(self):
		a2=float(self.xml.get_widget("edta2").get_text())
		b2=float(self.xml.get_widget('edtb2').get_text())
		c2=float(self.xml.get_widget('edtc2').get_text())
		d2=float(self.xml.get_widget('edtd2').get_text())
		segunda_linha = (a2, b2, c2, d2)
		return segunda_linha

	def passa_para_real_terceira_linha(self):
		a3=float(self.xml.get_widget("edta3").get_text())
		b3=float(self.xml.get_widget('edtb3').get_text())
		c3=float(self.xml.get_widget('edtc3').get_text())
		d3=float(self.xml.get_widget('edtd3').get_text())
		terceira_linha = (a3, b3, c3, d3)
		return terceira_linha

	def mostrarResultado(self, sistema):
		a1 = "%.3f"%sistema.primeira_linha[0]
		b1 = "%.3f"%sistema.primeira_linha[1]
		c1 = "%.3f"%sistema.primeira_linha[2]
		d1 = "%.3f"%sistema.primeira_linha[3]

		a2 = "%.3f"%sistema.segunda_linha[0]
		b2 = "%.3f"%sistema.segunda_linha[1]
		c2 = "%.3f"%sistema.segunda_linha[2]
		d2 = "%.3f"%sistema.segunda_linha[3]

		a3 = "%.3f"%sistema.terceira_linha[0]
		b3 = "%.3f"%sistema.terceira_linha[1]
		c3 = "%.3f"%sistema.terceira_linha[2]
		d3 = "%.3f"%sistema.terceira_linha[3]



		self.xml.get_widget('edta1').set_text(a1)
		self.xml.get_widget('edtb1').set_text(b1)
		self.xml.get_widget('edtc1').set_text(c1)
		self.xml.get_widget('edtd1').set_text(d1)

		self.xml.get_widget('edta2').set_text(a2)
		self.xml.get_widget('edtb2').set_text(b2)
		self.xml.get_widget('edtc2').set_text(c2)
		self.xml.get_widget('edtd2').set_text(d2)

		self.xml.get_widget('edta3').set_text(a3)
		self.xml.get_widget('edtb3').set_text(b3)
		self.xml.get_widget('edtc3').set_text(c3)
		self.xml.get_widget('edtd3').set_text(d3)

	def validar_edits(self):
		texto = "Digite o coeficiente do %s!"

		if self.xml.get_widget('edta1').get_text()=="":
			self.validar.alerta(texto%"X da primeira equação")
			self.xml.get_widget('edta1').grab_focus()

		elif self.xml.get_widget('edtb1').get_text()=="":
			self.validar.alerta(texto%"Y da primeira equação")
			self.xml.get_widget('edtb1').grab_focus()

		elif self.xml.get_widget('edtc1').get_text()=="":
			self.validar.alerta(texto%"Z da primeira equação")
			self.xml.get_widget('edtc1').grab_focus()

		elif self.xml.get_widget('edtd1').get_text()=="":
			self.validar.alerta("Digite o resultado da primeira equação")
			self.xml.get_widget('edtd1').grab_focus()

		elif self.xml.get_widget('edta2').get_text()=="":
			self.validar.alerta(texto%"X da segunda equação")
			self.xml.get_widget('edta2').grab_focus()

		elif self.xml.get_widget('edtb2').get_text()=="":
			self.validar.alerta(texto%"Y da segunda equação")
			self.xml.get_widget('edtb1').grab_focus()

		elif self.xml.get_widget('edtc2').get_text()=="":
			self.validar.alerta(texto%"Z da segunda equação")
			self.xml.get_widget('edtc2').grab_focus()

		elif self.xml.get_widget('edtd2').get_text()=="":
			self.validar.alerta("Digite o resultado da segunda equação")
			self.xml.get_widget('edtd2').grab_focus()

		elif self.xml.get_widget('edta3').get_text()=="":
			self.validar.alerta(texto%"X da terceira equação")
			self.xml.get_widget('edta3').grab_focus()

		elif self.xml.get_widget('edtb3').get_text()=="":
			self.validar.alerta(texto%"Y da terceira equação")
			self.xml.get_widget('edtb3').grab_focus()

		elif self.xml.get_widget('edtc3').get_text()=="":
			self.validar.alerta(texto%"Z da terceira equação")
			self.xml.get_widget('edtc3').grab_focus()

		elif self.xml.get_widget('edtd3').get_text()=="":
			self.validar.alerta("Digite o resultado da terceira equação")
			self.xml.get_widget('edtd3').grab_focus()

		else:
			return True

	def guarda_primeira(self):
		self.primeira = self.passa_para_real_primeira_linha()
		return self.primeira

	def guarda_segunda(self):
		self.segunda = self.passa_para_real_segunda_linha()
		return self.segunda

	def guarda_terceira(self):
		self.terceira = self.passa_para_real_terceira_linha()
		return self.terceira

	def gerar_sistema_uma_vez(self, primeira_linha, segunda_linha, terceira_linha):
			self.sistema = Escalonamento(primeira_linha, segunda_linha, terceira_linha)

	def on_btnEscalonarSistema_clicked(self, *args):
		if self.validar_edits():
			if self.cont == 0:
				self.sistema = Escalonamento(self.guarda_primeira(), self.guarda_segunda(), self.guarda_terceira())
				self.sistema.executarTodasAsEtapa()

			if (self.cont < 12) and (self.cont > 0):
				self.sistema = Escalonamento(self.primeira, self.segunda, self.terceira)
				self.sistema.executarTodasAsEtapa()

			if self.cont > 11:
				self.validar.alerta("Está Escalonado!")

			self.cont = 12
			self.mostrarResultado(self.sistema)

	def on_btnLimpar_clicked(self, *args):
		self.xml.get_widget("edta1").set_text('')
		self.xml.get_widget('edta1').set_text('')
		self.xml.get_widget('edtb1').set_text('')
		self.xml.get_widget('edtc1').set_text('')
		self.xml.get_widget('edtd1').set_text('')
		self.xml.get_widget('edta2').set_text('')
		self.xml.get_widget('edtb2').set_text('')
		self.xml.get_widget('edtc2').set_text('')
		self.xml.get_widget('edtd2').set_text('')
		self.xml.get_widget('edta3').set_text('')
		self.xml.get_widget('edtb3').set_text('')
		self.xml.get_widget('edtc3').set_text('')
		self.xml.get_widget('edtd3').set_text('')

		self.sistema = Escalonamento()
		self.cont = 0

	def on_btnavancar_clicked(self, *args):
		if self.validar_edits():
			if self.cont == 0:
				self.gerar_sistema_uma_vez(self.guarda_primeira(), self.guarda_segunda(), self.guarda_terceira())
			self.cont =  self.cont + 1

			if self.cont == 1:
				self.sistema.fazer_o_primeiro_elemento_da_primeira_linha_ficar_um()
				self.mostrarResultado(self.sistema)

			elif self.cont == 2:
				self.sistema.fazer_o_primeiro_elemento_da_segunda_linha_ficar_zero()
				self.mostrarResultado(self.sistema)

			elif self.cont == 3:
				self.sistema.fazer_o_primeiro_elemento_da_terceira_linha_ficar_zero()
				self.mostrarResultado(self.sistema)

			elif self.cont == 4:
				self.sistema.trocar_da_segunda_com_a_terceira_linha_para_obter_dois_zeros_na_ultima_linha()
				self.mostrarResultado(self.sistema)

			elif self.cont == 5:
				self.sistema.fazer_o_segundo_elemento_da_terceira_linha_ficar_zero_quando_o_segundo_elemento_da_segunda_for_igual()
				self.mostrarResultado(self.sistema)

			elif self.cont == 6:
				self.sistema.fazer_o_segundo_elemento_da_segunda_linha_ficar_um()
				self.mostrarResultado(self.sistema)

			elif self.cont == 7:
				self.sistema.fazer_o_segundo_elemento_da_terceira_linha_ficar_zero()
				self.mostrarResultado(self.sistema)

			elif self.cont == 8:
				self.sistema.fazer_o_terceiro_elemento_da_terceira_linha_ficar_um()
				self.mostrarResultado(self.sistema)

			elif self.cont == 9:
				self.sistema.fazer_o_terceiro_elemento_da_segunda_linha_ficar_zero()
				self.mostrarResultado(self.sistema)

			elif self.cont == 10:
				self.sistema.somar_o_quarto_elemento_da_terceira_linha_com_o_oposto_do_quarto_elemento_da_segunda_linha()
				self.mostrarResultado(self.sistema)

			elif self.cont == 11:
				self.sistema.fazer_o_segundo_elemento_da_primeira_linha_ficar_zero()
				self.mostrarResultado(self.sistema)

			elif self.cont == 12:
				self.sistema.fazer_o_terceiro_elemento_da_primeira_linha_ficar_zero()
				self.mostrarResultado(self.sistema)

			elif self.cont > 12:
				self.validar.alerta("Está Escalonado!")

	def on_btniniciar_clicked(self,*args):
		if self.validar_edits():
			if self.cont > 0:
				self.cont = 0
				self.sistema.primeira_linha = self.primeira
				self.sistema.segunda_linha = self.segunda
				self.sistema.terceira_linha = self.terceira
				self.mostrarResultado(self.sistema)

	def on_window1_destroy(self,*args):
		gtk.main_quit()

if __name__=="__main__":
	w = Janela_Esc3()

