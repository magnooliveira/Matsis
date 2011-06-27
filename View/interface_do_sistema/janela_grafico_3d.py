# coding: utf-8
#!/usr/bin/python
#Autor: Magno Lima Oliveira
from sys import path
import os.path

caminho_do_model =  os.path.expanduser( "~/Matsis/Model/sistema_model")
caminho_do_controller =  os.path.expanduser("~/Matsis/Controller")

path.append(caminho_do_model)
path.append(caminho_do_controller)

from Sistema_De_Tres_Incognitas import *

from Gera_Grafico_3D import *
from ClasseControle import *

#import matplotlib
#import matplotlib.pyplot as plt

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

class Janela_Grafico_3D(object):
	"""
	Testando minha primeira janela para gráficos 3d
	em glade.
	"""
	def __init__(self):
		"""
		Metodo Construtor da classe

		"""
		self.validar = Controle()
		self.arquivoglade = os.path.expanduser("~/Matsis/View/interface_do_sistema/Janela_Grafico_3D.glade")
		self.xml = gtk.glade.XML(self.arquivoglade)
		self.mainWindow = self.xml.get_widget('window1')
		self.mainWindow.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#00FF00"))
		self.xml.signal_autoconnect(self)
		self.mainWindow.show_all()

		gtk.main()

	def passaParaReal(self):
		try:
			self.a1=float(self.xml.get_widget("edta1").get_text())
			self.b1=float(self.xml.get_widget('edtb1').get_text())
			self.c1=float(self.xml.get_widget('edtc1').get_text())
			self.d1=float(self.xml.get_widget('edtd1').get_text())

			self.a2=float(self.xml.get_widget("edta2").get_text())
			self.b2=float(self.xml.get_widget('edtb2').get_text())
			self.c2=float(self.xml.get_widget('edtc2').get_text())
			self.d2=float(self.xml.get_widget('edtd2').get_text())

			self.a3=float(self.xml.get_widget("edta3").get_text())
			self.b3=float(self.xml.get_widget('edtb3').get_text())
			self.c3=float(self.xml.get_widget('edtc3').get_text())
			self.d3=float(self.xml.get_widget('edtd3').get_text())


			return True
		except ValueError:
			self.validar.alerta("Digite apenas números !")
			return self.xml.get_widget('edta1').grab_focus()
			return False

	def validar_edits(self):
		texto = "Digite o coeficiente de %s!"

		if self.xml.get_widget('edta1').get_text()=="":
			self.validar.alerta(texto%"a1")
			self.xml.get_widget('edta1').grab_focus()

		elif self.xml.get_widget('edtb1').get_text()=="":
			self.validar.alerta(texto%"b1")
			self.xml.get_widget('edtb1').grab_focus()

		elif self.xml.get_widget('edtc1').get_text()=="":
			self.validar.alerta(texto%"c1")
			self.xml.get_widget('edtc1').grab_focus()

		elif self.xml.get_widget('edtd1').get_text()=="":
			self.validar.alerta(texto%"d1")
			self.xml.get_widget('edtd1').grab_focus()

		elif self.xml.get_widget('edta2').get_text()=="":
			self.validar.alerta(texto%"a2")
			self.xml.get_widget('edta2').grab_focus()

		elif self.xml.get_widget('edtb2').get_text()=="":
			self.validar.alerta(texto%"b2")
			self.xml.get_widget('edtb2').grab_focus()

		elif self.xml.get_widget('edtc2').get_text()=="":
			self.validar.alerta(texto%"c2")
			self.xml.get_widget('edtc2').grab_focus()

		elif self.xml.get_widget('edtd2').get_text()=="":
			self.validar.alerta(texto%"d2")
			self.xml.get_widget('edtd2').grab_focus()

		elif self.xml.get_widget('edta3').get_text()=="":
			self.validar.alerta(texto%"a3")
			self.xml.get_widget('edta3').grab_focus()

		elif self.xml.get_widget('edtb3').get_text()=="":
			self.validar.alerta(texto%"b3")
			self.xml.get_widget('edtb3').grab_focus()

		elif self.xml.get_widget('edtc3').get_text()=="":
			self.validar.alerta(texto%"c3")
			self.xml.get_widget('edtc3').grab_focus()

		elif self.xml.get_widget('edtd3').get_text()=="":
			self.validar.alerta(texto%"d3")
			self.xml.get_widget('edtd3').grab_focus()

		else:

			return True


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

	def on_btnGerarGrafico_clicked(self, *args):
		if (self.validar_edits() == True):
			if (self.passaParaReal() == True):
				grafico = Gera_Grafico_3D(self.a1, self.b1, self.c1, self.d1, self.a2,\
																								self.b2,\
																								self.c2,\
																								self.d2,\
																								self.a3,\
																								self.b3,\
																								self.c3,\
																								self.d3)

				grafico.gerar_grafico_3d()
		else:
			pass
		gtk.main()

	def on_window1_destroy(self,*args):
		gtk.main_quit()

if __name__=="__main__":
	w = Janela_Grafico_3D()

