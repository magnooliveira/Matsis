# coding:UTF-8
#!/usr/bin/env python

#Autor: Magno Lima Oliveira

import matplotlib
matplotlib.use('GTKAgg')

from sys import *
import os.path

caminho_da_view_ordem =  os.path.expanduser ("~/Matsis/View/interface_ordem")
caminho_da_view_sitema =  os.path.expanduser ("~/Matsis/View/interface_do_sistema")
caminho_do_controller =  os.path.expanduser("~/Matsis/Controller")

path.append(caminho_da_view_ordem)
path.append(caminho_da_view_sitema)
path.append(caminho_do_controller)

from about import *
from janela_ordem import *
from Sobre import *
from janela2d import *
from janela3d import *
from janela_esc3 import *
from janela_esc4 import *
from janela_grafico_3d import *

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

class JanelaPrincipal(object):
	"""
	Minha primeira janela
	em glade.
	"""
	def __init__(self):
		"""
		Metodo Construtor da classe
		"""

		self.arquivoglade = "/home/patricia/Matsis/View/interface_principal/Menu.glade"
		self.xml = gtk.glade.XML(self.arquivoglade)

		self.menu = self.xml.get_widget('menubar1')

		self.fix = self.xml.get_widget('fixed1')
		self.j  = JanelaSobre()
		img = gtk.Image()
		img.set_from_file("/home/patricia/Matsis/View/interface_principal/matematica.jpg")
		self.fix.add(img)
		self.mainWindow1 = self.xml.get_widget('window1')
		self.mainWindow1.show_all()

		self.xml.signal_autoconnect(self)

		gtk.main()


	def on_window1_destroy(self,*args):
		gtk.main_quit()

	def on_esc3_activate(self,*args):
 		janela_esc3 = Janela_Esc3()

	def on_esc4_activate(self,*args):
		janela_esc4 = Janela_Esc4()

	def on_sistema2d_activate(self,*args):
		janela2d = Janela1()

	def on_sistema3d_activate(self,*args):
		janela3d = Janela2()

	def on_grafico3d_activate(self,*args):
		janela_grafico_3d = Janela_Grafico_3D()

	def on_calcular_traco_activate(self,*args):
		traco = 1
		self.ordem_quadrada_traco = Janela_Ordem(traco)

	def on_calcular_determinante_activate(self,*args):
		det = 2
		self.ordem_quadrada_determinate = Janela_Ordem(det)

	def on_calcular_matriz_inversa_activate(self, *args):
		inversa = 3
		self.ordem_quadrada_inversa = Janela_Ordem(inversa)

	def on_achar_transposta_activate(self, *args):
		trans = 4
		self.ordem_variada_transposta = Janela_Ordem(trans)

	def on_somar_duas_matrizes_activate(self, *args):
		soma_A  = 5
		self.ordem_variada_soma = Janela_Ordem(soma_A)

	def on_subtrair_duas_matrizes_activate(self, *args):
		sub_A  = 6
		self.ordem_variada_subtrair = Janela_Ordem(sub_A)

	def on_multiplicar_duas_matrizes_activate(self, *args):
		mult_A  = 7
		self.ordem_variada_multiplicar = Janela_Ordem(mult_A)

	def on_multiplicar_numero_por_matriz_activate(self, *args):
		mult_num_A  = 8
		self.ordem_variada_multiplicar = Janela_Ordem(mult_num_A)

	def on_sobre_activate(self, *args):
		self.about = Janela_About()

if __name__=="__main__":

	w = JanelaPrincipal()

