# coding:UTF-8
#!/usr/bin/env python

#Autor: Magno Lima Oliveira

from sys import *
import os.path

caminho_do_model = os.path.expanduser( "~/Matsis/Model/matriz_model")

path.append(caminho_do_model)

from matriz import *
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

class Janela_Numero(object):

	def __init__(self, mat_A):
		"""
		Metodo Construtor da classe
		"""

		self.arquivoglade = os.path.expanduser( "~/Matsis/View/interface_matriz/janela_numero.glade")
		self.xml = gtk.glade.XML(self.arquivoglade)
		self.edt1 = self.xml.get_widget("edt_numero")
		self.numero = 0

		self.mat_A = mat_A

		self.controle = Controle()
		self.fix = self.xml.get_widget('fixed1')

		self.mainWindow = self.xml.get_widget('window')
		self.mainWindow.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#5F9EA0"))
		self.mainWindow.show_all()
		self.xml.signal_autoconnect(self)

		gtk.main()

	def on_window_destroy(self,*args):
		gtk.main_quit()

	def passaParaRealNumero(self):
		try:
			self.numero = float(self.edt1.get_text())
			return self.numero
		except:
			pass

	def validar_edt(self):

		if self.xml.get_widget('edt_numero').get_text()=="":
			self.controle.alerta("Digite Número !")
			self.xml.get_widget('edt_numero').grab_focus()

		else:
			self.passaParaRealNumero()
			return True

	def on_btn_multiplicar_clicked(self, *args):
		self.numero = 0
		if self.validar_edt():
			produto = self.mat_A.multiplicar_um_numero_por_uma_matriz(self.numero)
			texto = str(produto)
			self.controle.resultado(texto)


if __name__=="__main__":
	j = Janela_Numero()

