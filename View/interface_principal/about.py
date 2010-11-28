# coding:UTF-8
#!/usr/bin/env python
			#########################################################
			# Autor  : Magno Lima Oliveira																										  #
			# E-mail : magnolimaoliveira@gmail.com					                                                                  #
			# Projeto: MatSis										                                                                                      #
			# Objetivo : Informar sobre o Soft		                                                                                              #
			#########################################################

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

class Janela_About(object):

	def __init__(self):
		"""
		Metodo Construtor da classe
		"""
		self.arquivoglade = "sobre_novo.glade"
		self.xml = gtk.glade.XML(self.arquivoglade)

		self.fix2 = self.xml.get_widget('fixed2')

		self.mainWindow1 = self.xml.get_widget('window')
		self.mainWindow1.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#B22222"))
		self.mainWindow1.show_all()

		self.xml.signal_autoconnect(self)

		gtk.main()

	def on_window_destroy(self,*args):
		gtk.main_quit()

if __name__=="__main__":
    p = Janela_About()

