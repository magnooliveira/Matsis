# coding: utf-8
#!/usr/bin/python
#Autor: Magno Lima Oliveira


from sys import path
import os.path

caminho_do_model = os.path.expanduser("~/Matsis/Model/sistema_model")
caminho_do_controller = os.path.expanduser("~/Matsis/Controller")

path.append(caminho_do_model)
path.append(caminho_do_controller)

from Sistema_De_Duas_Incognitas import *

from Gera_Grafico_2D import *
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

class Janela1(object):
	"""
	Minha primeira janela
	em glade.
	"""
	def __init__(self):
		"""
		Metodo Construtor da classe
		"""
		self.validar = Controle()
		self.arquivoglade =os.path.expanduser( "~/Matsis/View/interface_do_sistema/janela.glade")
		self.xml = gtk.glade.XML(self.arquivoglade)



		self.xml.signal_autoconnect(self)

		self.mainWindow = self.xml.get_widget('window1')
		self.mainWindow.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#B22222"))
		self.mainWindow.show_all()

		self.a1 = None
		self.b1 = None
		self.c1 = None

		self.btnGerarSistema = self.xml.get_widget('btnGerarSistema')
		self.btnLimpar = self.xml.get_widget('btnLimpar')
		self.btnGerarGrafico = self.xml.get_widget('btnLimpar')

		# Comboxbox
		self.cbxSistema = self.xml.get_widget('combobox1')

		# Preparar a Caixa Comboxbox para selecao

		# Componente ListStore para armazenar as retas
		store = gtk.ListStore(str)
		store.append(["         -Selecione-"])
		store.append(["Duas Retas Coincidentes"])
		store.append(["Duas Retas Paralelas"])
		store.append(["Duas Retas Concorrentes"])
		# Celula texto para nossa Caixa de Selecao
		celula = gtk.CellRendererText()
		# Associa o ListStore a Caixa de Selecao
		self.cbxSistema.set_model(store)
		# Associa a celula a caixa de selecao
		self.cbxSistema.pack_start(celula, True)
		self.cbxSistema.add_attribute(celula, 'text', 0)

		# Coloca o foco no -Selecionar-
		self.cbxSistema.set_active(0)

		self.combo = self.cbxSistema.get_active_text()

		gtk.main()

	def passaParaReal(self):
		try:
			self.a1=float(self.xml.get_widget("edta1").get_text())
			self.b1=float(self.xml.get_widget('edtb1').get_text())
			self.c1=float(self.xml.get_widget('edtc1').get_text())
			return True
		except ValueError:
			self.validar.alerta("Digite apenas números !")
			return self.xml.get_widget('edta1').grab_focus()
			return False

	def criar_equacao(self):
		equacao = SistemaDuasIncognitas(self.a1,self.b1,self.c1)
		return equacao

	def mostrarResultado(self,resposta):
		self.xml.get_widget('edta2').set_text(str(self.resposta[0]))
		self.xml.get_widget('edtb2').set_text(str(self.resposta[1]))
		self.xml.get_widget('edtc2').set_text(str(self.resposta[2]))

	def validar_edits(self):
		self.combo = self.cbxSistema.get_active_text()
		texto = "Digite o coeficiente de %s!"
		if self.xml.get_widget('edta1').get_text()=="":
			self.validar.alerta(texto%"a")
			self.xml.get_widget('edta1').grab_focus()

		elif self.xml.get_widget('edtb1').get_text()=="":
			self.validar.alerta(texto%"b")
			self.xml.get_widget('edtb1').grab_focus()

		elif self.xml.get_widget('edtc1').get_text()=="":
			self.validar.alerta(texto%"c")
			self.xml.get_widget('edtc1').grab_focus()

		elif self.combo == "         -Selecione-":
			texto = "Selecione uma opção de sistema!"
			self.validar.alerta("Selecione uma opção de sistema!")

		else:
			return True

	def on_btnGerarSistema_clicked(self, *args):
		self.ativaGrafico=False
		if self.validar_edits():
			if (self.passaParaReal()):

				if self.combo == "Duas Retas Coincidentes":
					self.resposta = self.criar_equacao().acharDuasRetasCoincidentes()
					self.mostrarResultado(self.resposta)
					self.ativaGrafico=True

				elif self.combo == "Duas Retas Paralelas":
					self.resposta = self.criar_equacao().acharDuasRetasParalelas()
					self.mostrarResultado(self.resposta)
					self.ativaGrafico=True

				elif self.combo == "Duas Retas Concorrentes":
					self.resposta = self.criar_equacao().acharDuasRetasConcorrentes()
					self.mostrarResultado(self.resposta)
					self.ativaGrafico=True

	def on_btnLimpar_clicked(self, *args):
		self.xml.get_widget('edta1').set_text("")
		self.xml.get_widget('edtb1').set_text("")
		self.xml.get_widget('edtc1').set_text("")
		self.xml.get_widget('edta2').set_text("")
		self.xml.get_widget('edtb2').set_text("")
		self.xml.get_widget('edtc2').set_text("")
		self.xml.get_widget('edta1').grab_focus()
		self.ativaGrafico=False

	def on_btnGerarGrafico_clicked(self, *args):
		if (self.ativaGrafico == True):
			grafico = Grafico(self.a1,self.b1,self.c1,self.resposta[0],self.resposta[1],self.resposta[2])
			grafico.gerarGrafico2D()
			del grafico
		else:
			self.validar.alerta("Gere um Sistema!")
		gtk.main()

	def on_window1_destroy(self,*args):
		gtk.main_quit()

if __name__=="__main__":
	w = Janela1()

