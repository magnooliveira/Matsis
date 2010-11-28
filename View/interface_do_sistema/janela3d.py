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

from Gera_Grafico_2D import *
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

class Janela2(object):
	"""
	Testando minha primeira janela para gráficos 3d
	em glade.
	"""
	def __init__(self):
		"""
		Metodo Construtor da classe

		"""
		self.validar = Controle()
		self.arquivoglade = os.path.expanduser("~/Matsis/View/interface_do_sistema/Janela3D.glade")
		self.xml = gtk.glade.XML(self.arquivoglade)
		self.mainWindow = self.xml.get_widget('window1')
		self.btnGerarSistema = self.xml.get_widget('btnGerarSistema')
		self.btnLimpar = self.xml.get_widget('btnLimpar')
		self.btnGerarGrafico = self.xml.get_widget('btnLimpar')
		self.btnSair = self.xml.get_widget('btnLimpar')
		self.mainWindow.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#00FF00"))
		self.xml.signal_autoconnect(self)
		self.mainWindow.show_all()

		self.a1 = None
		self.b1 = None
		self.c1 = None
		self.d1 = None

		# Comboxbox
		self.cbxSistema = self.xml.get_widget('combobox1')

		# Preparar a Caixa Comboxbox para selecao

		# Componente ListStore para armazenar as retas
		store = gtk.ListStore(str)
		store.append(["         -Selecione-"])
		store.append(["Tres Planos Coincidentes"])
		store.append(["Dois Planos Coincidentes um Paralelo"])
		store.append(["Dois Planos Coincidentes um Intersecta"])
		store.append(["Tres Planos Paralelos"])
		store.append(["Dois Planos Paralelos um Intersecta"])
		store.append(["Tres Planos Com uma Reta Comum"])
		store.append(["Tres Planos Intersectam Dois a Dois"])
		store.append(["Tres Planos um Ponto Comum"])

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
			self.d1=float(self.xml.get_widget('edtd1').get_text())
			return True
		except ValueError:
			self.validar.alerta("Digite apenas números !")
			return self.xml.get_widget('edta1').grab_focus()
			return False


	def criar_equacao(self):
		equacao = SistemaTresIncognitas(self.a1,self.b1,self.c1,self.d1)
		return equacao

	def mostrarResultado(self,resposta):
		self.xml.get_widget('edta2').set_text(str(self.resposta[0][0]))
		self.xml.get_widget('edtb2').set_text(str(self.resposta[0][1]))
		self.xml.get_widget('edtc2').set_text(str(self.resposta[0][2]))
		self.xml.get_widget('edtd2').set_text(str(self.resposta[0][3]))
		self.xml.get_widget('edta3').set_text(str(self.resposta[1][0]))
		self.xml.get_widget('edtb3').set_text(str(self.resposta[1][1]))
		self.xml.get_widget('edtc3').set_text(str(self.resposta[1][2]))
		self.xml.get_widget('edtd3').set_text(str(self.resposta[1][3]))

	def validar_edits(self):
		texto = "Digite o coeficiente de %s!"
		self.combo = self.cbxSistema.get_active_text()

		if self.xml.get_widget('edta1').get_text()=="":
			self.validar.alerta(texto%"a")
			self.xml.get_widget('edta1').grab_focus()

		elif self.xml.get_widget('edtb1').get_text()=="":
			self.validar.alerta(texto%"b")
			self.xml.get_widget('edtb1').grab_focus()

		elif self.xml.get_widget('edtc1').get_text()=="":
			self.validar.alerta(texto%"c")
			self.xml.get_widget('edtc1').grab_focus()

		elif self.xml.get_widget('edtd1').get_text()=="":
			self.validar.alerta(texto%"d")
			self.xml.get_widget('edtd1').grab_focus()

		elif self.combo == "         -Selecione-":
			self.validar.alerta("Selecione uma opção de sistema!")

		else:
			return True

	def on_btnGerarSistema_clicked(self, *args):
		self.ativaGrafico=False

		if self.validar_edits():
			if (self.passaParaReal()):
				if self.combo == "Tres Planos Coincidentes":
					self.resposta = self.criar_equacao().acharTresPlanosCoincidentes()
					self.mostrarResultado(self.resposta)
					self.ativaGrafico=True

				elif self.combo == "Dois Planos Coincidentes um Paralelo":
					self.resposta = self.criar_equacao().acharDoisPlanosCoincidentesUmParalelo()
					self.mostrarResultado(self.resposta)
					self.ativaGrafico=True

				elif self.combo == "Dois Planos Coincidentes um Intersecta":
					self.resposta = self.criar_equacao().acharDoisPlanosCoincidentesUmIntersecta()
					self.mostrarResultado(self.resposta)
					self.ativaGrafico=True

				elif self.combo == "Tres Planos Paralelos":
					self.resposta = self.criar_equacao().acharTresPlanosParalelos()
					self.mostrarResultado(self.resposta)
					self.ativaGrafico=True

				elif self.combo == "Dois Planos Paralelos um Intersecta":
					self.resposta = self.criar_equacao().acharDoisPlanosParalelosUmIntersecta()
					self.mostrarResultado(self.resposta)
					self.ativaGrafico=True

				elif self.combo == "Tres Planos Com uma Reta Comum":
					self.resposta = self.criar_equacao().acharTresPlanosComUmaRetaComum()
					self.mostrarResultado(self.resposta)
					self.ativaGrafico=True

				elif self.combo == "Tres Planos Intersectam Dois a Dois":
					self.resposta = self.criar_equacao().acharTresPlanosIntersectamDoisADois()
					self.mostrarResultado(self.resposta)
					self.ativaGrafico=True

				elif self.combo == "Tres Planos um Ponto Comum":
					self.resposta = self.criar_equacao().acharTresPlanosUmPontoComum()
					self.mostrarResultado(self.resposta)
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

	def on_btnGerarGrafico_clicked(self, *args):
		if (self.ativaGrafico == True):
			grafico = Grafico(self.a1,self.b1,self.c1,self.resposta[0],self.resposta[1],self.resposta[2])
			grafico.gerarGrafico3D()
		else:
			self.validar.alerta("Gere o Sistema!")
		gtk.main()

	def on_window1_destroy(self,*args):
		gtk.main_quit()

if __name__=="__main__":
	w = Janela2()

