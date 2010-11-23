# coding:UTF-8
#!/usr/bin/env python

#Autor: Magno Lima Oliveira

from Sobre import *
from janela2d import *
from janela3d import *
from janela_esc3 import *
from janela_esc4 import *

from sys import *

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
		self.arquivoglade = "Menu.glade"
		self.xml = gtk.glade.XML(self.arquivoglade)

		self.menu = self.xml.get_widget('menubar1')

		self.fix = self.xml.get_widget('fixed1')

		img = gtk.Image()
		img.set_from_file("matematica.jpg")
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

if __name__=="__main__":
    j = JanelaSobre()
    w = JanelaPrincipal()

