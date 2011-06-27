# coding:UTF-8
#!/usr/bin/env python
			#########################################################
			# Autor  : Magno Lima Oliveira							#
			# E-mail : magnolimaoliveira@gmail.com					#
			# Projeto: MatSis										#
			# Objetivo : a partir de uma equacao da reta dada é		#
			#			 possivel calcular uma outra equação, 		#
            #            aleatoriamente, de acordo com o tipo de 	#
            #            sistema definido   						#
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

class JanelaSobre(object):

	def __init__(self):
		"""
		Metodo Construtor da classe
		"""
		self.arquivoglade = "/home/patricia/Matsis/View/interface_principal/sobre.glade"
		self.xml = gtk.glade.XML(self.arquivoglade)


		self.fix = self.xml.get_widget('fixed2')
		self.botao = self.xml.get_widget('btn_sair')



		img = gtk.Image()
		img.set_from_file("/home/patricia/Matsis/View/interface_principal/sobre.jpg")
		self.fix.add(img)
		self.mainWindow1 = self.xml.get_widget('window2')
		self.mainWindow1.show_all()

		self.xml.signal_autoconnect(self)

		gtk.main()


	def on_window2_destroy(self,*args):
		gtk.main_quit()

if __name__=="__main__":
    p = JanelaSobre()

