# coding: utf-8
#!/usr/bin/python
#Autor: Magno Lima Oliveira

from sys import path

caminho_do_model =  "/home/patricia/Matsis/Model"
caminho_do_controller =  "/home/patricia/Matsis/Controller"

path.append(caminho_do_model)
path.append(caminho_do_controller)

import pdb
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
		self.validar = Controle()
		self.arquivoglade = "Janela_Esc3.glade"
		self.xml = gtk.glade.XML(self.arquivoglade)
		self.mainWindow = self.xml.get_widget('window1')
		self.btnGerarSistema = self.xml.get_widget('btnEscalonarSistema')
		self.btnLimpar = self.xml.get_widget('btnLimpar')
		self.mainWindow.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#B22222"))
		self.xml.signal_autoconnect(self)
		self.mainWindow.show_all()

		gtk.main()

	def passa_para_real_primeira_linha(self):

		a1=float(self.xml.get_widget("edta1").get_text())
		b1=float(self.xml.get_widget('edtb1').get_text())
		c1=float(self.xml.get_widget('edtc1').get_text())
		d1=float(self.xml.get_widget('edtd1').get_text())
		primeira_linha = (a1, b1, c1, d1)
#		print primeira_linha
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

	def on_btnEscalonarSistema_clicked(self, *args):
		texto = "Digite o coeficiente do %s!"
		self.ativaGrafico=False

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
			sistema = Escalonamento(self.passa_para_real_primeira_linha(), \
														self.passa_para_real_segunda_linha(),\
														self.passa_para_real_terceira_linha())

			sistema.executarTodasAsEtapa()
			self.mostrarResultado(sistema)
			self.ativaGrafico=True

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
		self.ativaGrafico=False

	def on_window1_destroy(self,*args):
		gtk.main_quit()

if __name__=="__main__":
	w = Janela_Esc3()

