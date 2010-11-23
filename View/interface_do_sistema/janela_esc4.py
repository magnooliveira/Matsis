# coding: utf-8
#!/usr/bin/python
#Autor: Magno Lima Oliveira

from sys import path

caminho_do_model =  "/home/patricia/Matsis/Model/escalonamento_model"
caminho_do_controller =  "/home/patricia/Matsis/Controller"

path.append(caminho_do_model)
path.append(caminho_do_controller)

from escalonamento_quatro_linhas import *
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

class Janela_Esc4(object):
	"""
	Janela para escalonamente de 4 por 4
	"""
	def __init__(self):
		"""
		Metodo Construtor da classe

		"""
		self.cont = 0
		self.primeira = None
		self.segunda = None
		self.terceira = None
		self.quarta = None

		self.sistema = EscalonamentoQuatroLinhas()
		self.validar = Controle()
		self.arquivoglade = "/home/patricia/Matsis/View/interface_do_sistema/Janela_Esc4.glade"
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
		e1=float(self.xml.get_widget('edte1').get_text())
		primeira_linha = (a1, b1, c1, d1, e1)
		return primeira_linha

	def passa_para_real_segunda_linha(self):

		a2=float(self.xml.get_widget("edta2").get_text())
		b2=float(self.xml.get_widget('edtb2').get_text())
		c2=float(self.xml.get_widget('edtc2').get_text())
		d2=float(self.xml.get_widget('edtd2').get_text())
		e2=float(self.xml.get_widget('edte2').get_text())
		segunda_linha = (a2, b2, c2, d2, e2)
		return segunda_linha

	def passa_para_real_terceira_linha(self):

		a3=float(self.xml.get_widget("edta3").get_text())
		b3=float(self.xml.get_widget('edtb3').get_text())
		c3=float(self.xml.get_widget('edtc3').get_text())
		d3=float(self.xml.get_widget('edtd3').get_text())
		e3=float(self.xml.get_widget('edte3').get_text())
		terceira_linha = (a3, b3, c3, d3, e3)
		return terceira_linha

	def passa_para_real_quarta_linha(self):

		a4=float(self.xml.get_widget("edta4").get_text())
		b4=float(self.xml.get_widget('edtb4').get_text())
		c4=float(self.xml.get_widget('edtc4').get_text())
		d4=float(self.xml.get_widget('edtd4').get_text())
		e4=float(self.xml.get_widget('edte4').get_text())
		quarta_linha = (a4, b4, c4, d4, e4)
		return quarta_linha


	def mostrarResultado(self, sistema):

		a1 = "%.3f"%(float(sistema.primeira_linha[0]))
		b1 = "%.3f"%(float(sistema.primeira_linha[1]))
		c1 = "%.3f"%(float(sistema.primeira_linha[2]))
		d1 = "%.3f"%(float(sistema.primeira_linha[3]))
		e1 = "%.3f"%(float(sistema.primeira_linha[4]))

		a2 = "%.3f"%(float(sistema.segunda_linha[0]))
		b2 = "%.3f"%(float(sistema.segunda_linha[1]))
		c2 = "%.3f"%(float(sistema.segunda_linha[2]))
		d2 = "%.3f"%(float(sistema.segunda_linha[3]))
		e2 = "%.3f"%(float(sistema.segunda_linha[4]))

		a3 = "%.3f"%(float(sistema.terceira_linha[0]))
		b3 = "%.3f"%(float(sistema.terceira_linha[1]))
		c3 = "%.3f"%(float(sistema.terceira_linha[2]))
		d3 = "%.3f"%(float(sistema.terceira_linha[3]))
		e3 = "%.3f"%(float(sistema.terceira_linha[4]))

		a4 = "%.3f"%(float(sistema.quarta_linha[0]))
		b4 = "%.3f"%(float(sistema.quarta_linha[1]))
		c4 = "%.3f"%(float(sistema.quarta_linha[2]))
		d4 = "%.3f"%(float(sistema.quarta_linha[3]))
		e4 = "%.3f"%(float(sistema.quarta_linha[4]))

		self.xml.get_widget('edta1').set_text(a1)
		self.xml.get_widget('edtb1').set_text(b1)
		self.xml.get_widget('edtc1').set_text(c1)
		self.xml.get_widget('edtd1').set_text(d1)
		self.xml.get_widget('edte1').set_text(e1)

		self.xml.get_widget('edta2').set_text(a2)
		self.xml.get_widget('edtb2').set_text(b2)
		self.xml.get_widget('edtc2').set_text(c2)
		self.xml.get_widget('edtd2').set_text(d2)
		self.xml.get_widget('edte2').set_text(e2)

		self.xml.get_widget('edta3').set_text(a3)
		self.xml.get_widget('edtb3').set_text(b3)
		self.xml.get_widget('edtc3').set_text(c3)
		self.xml.get_widget('edtd3').set_text(d3)
		self.xml.get_widget('edte3').set_text(e3)

		self.xml.get_widget('edta4').set_text(a4)
		self.xml.get_widget('edtb4').set_text(b4)
		self.xml.get_widget('edtc4').set_text(c4)
		self.xml.get_widget('edtd4').set_text(d4)
		self.xml.get_widget('edte4').set_text(e4)

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
			self.validar.alerta(texto%"W da primeira equação")
			self.xml.get_widget('edtd1').grab_focus()

		elif self.xml.get_widget('edte1').get_text()=="":
			self.validar.alerta("Digite o resultado da primeira equação")
			self.xml.get_widget('edte1').grab_focus()

		elif self.xml.get_widget('edta2').get_text()=="":
			self.validar.alerta(texto%"X da segunda equação")
			self.xml.get_widget('edta2').grab_focus()

		elif self.xml.get_widget('edtb2').get_text()=="":
			self.validar.alerta(texto%"Y da segunda equação")
			self.xml.get_widget('edtb2').grab_focus()

		elif self.xml.get_widget('edtc2').get_text()=="":
			self.validar.alerta(texto%"Z da segunda equação")
			self.xml.get_widget('edtc2').grab_focus()

		elif self.xml.get_widget('edtd2').get_text()=="":
			self.validar.alerta(texto%"W da segunda equação")
			self.xml.get_widget('edtd2').grab_focus()

		elif self.xml.get_widget('edte2').get_text()=="":
			self.validar.alerta("Digite o resultado da segunda equação")
			self.xml.get_widget('edte2').grab_focus()

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
			self.validar.alerta(texto%"W da terceira equação")
			self.xml.get_widget('edtd3').grab_focus()

		elif self.xml.get_widget('edte3').get_text()=="":
			self.validar.alerta("Digite o resultado da terceira equação")
			self.xml.get_widget('edte3').grab_focus()

		elif self.xml.get_widget('edta4').get_text()=="":
			self.validar.alerta(texto%"X da quarta equação")
			self.xml.get_widget('edta4').grab_focus()

		elif self.xml.get_widget('edtb4').get_text()=="":
			self.validar.alerta(texto%"Y da quarta equação")
			self.xml.get_widget('edtb4').grab_focus()

		elif self.xml.get_widget('edtc4').get_text()=="":
			self.validar.alerta(texto%"Z da quarta equação")
			self.xml.get_widget('edtc4').grab_focus()

		elif self.xml.get_widget('edtd4').get_text()=="":
			self.validar.alerta(texto%"W da quarta equação")
			self.xml.get_widget('edtd4').grab_focus()

		elif self.xml.get_widget('edte4').get_text()=="":
			self.validar.alerta("Digite o resultado da quarta equação")
			self.xml.get_widget('edte4').grab_focus()

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

	def guarda_quarta(self):
		self.quarta = self.passa_para_real_quarta_linha()
		return self.quarta

	def gerar_sistema_uma_vez(self, primeira_linha, segunda_linha, terceira_linha, quarta_linha):
			self.sistema = EscalonamentoQuatroLinhas(primeira_linha, segunda_linha, terceira_linha, quarta_linha)

	def on_btnEscalonarSistema_clicked(self, *args):
		if self.validar_edits():
			if self.cont == 0:
				self.sistema = EscalonamentoQuatroLinhas(self.guarda_primeira(), self.guarda_segunda(), self.guarda_terceira(), self.guarda_quarta())
				self.sistema.executarTodasAsEtapa()

			if (self.cont < 20) and (self.cont > 0):
				self.sistema = EscalonamentoQuatroLinhas(self.primeira, self.segunda, self.terceira, self.quarta)
				self.sistema.executarTodasAsEtapa()

			if self.cont > 19:
				self.validar.alerta("Está Escalonado!")

			self.cont = 20
			self.mostrarResultado(self.sistema)

	def on_btnLimpar_clicked(self, *args):

		self.xml.get_widget("edta1").set_text('')
		self.xml.get_widget('edta1').set_text('')
		self.xml.get_widget('edtb1').set_text('')
		self.xml.get_widget('edtc1').set_text('')
		self.xml.get_widget('edtd1').set_text('')
		self.xml.get_widget('edte1').set_text('')
		self.xml.get_widget('edta2').set_text('')
		self.xml.get_widget('edtb2').set_text('')
		self.xml.get_widget('edtc2').set_text('')
		self.xml.get_widget('edtd2').set_text('')
		self.xml.get_widget('edte2').set_text('')
		self.xml.get_widget('edta3').set_text('')
		self.xml.get_widget('edtb3').set_text('')
		self.xml.get_widget('edtc3').set_text('')
		self.xml.get_widget('edtd3').set_text('')
		self.xml.get_widget('edte3').set_text('')
		self.xml.get_widget('edta4').set_text('')
		self.xml.get_widget('edtb4').set_text('')
		self.xml.get_widget('edtc4').set_text('')
		self.xml.get_widget('edtd4').set_text('')
		self.xml.get_widget('edte4').set_text('')

		self.sistema = EscalonamentoQuatroLinhas()
		self.cont = 0

	def on_btnavancar_clicked(self, *args):
		if self.validar_edits():
			if self.cont == 0:
				self.gerar_sistema_uma_vez(self.guarda_primeira(), self.guarda_segunda(), self.guarda_terceira(), self.guarda_quarta())
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
				self.sistema.fazer_o_primeiro_elemento_da_quarta_linha_ficar_zero()
				self.mostrarResultado(self.sistema)

			elif self.cont == 5:
				self.sistema.trocar_da_segunda_com_a_terceira_linha_para_obter_dois_zeros_na_ultima_linha()
				self.mostrarResultado(self.sistema)

			elif self.cont == 6:
				self.sistema.fazer_o_segundo_elemento_da_terceira_linha_ficar_zero_quando_o_segundo_elemento_da_segunda_for_igual()
				self.mostrarResultado(self.sistema)

			elif self.cont == 7:
				self.sistema.fazer_o_segundo_elemento_da_segunda_linha_ficar_um()
				self.mostrarResultado(self.sistema)

			elif self.cont == 8:
				self.sistema.fazer_o_segundo_elemento_da_terceira_linha_ficar_zero()
				self.mostrarResultado(self.sistema)

			elif self.cont == 9:
				self.sistema.fazer_o_segundo_elemento_da_quarta_linha_ficar_zero()
				self.mostrarResultado(self.sistema)

			elif self.cont == 10:
				self.sistema.trocar_da_terceira_com_a_quarta_linha_para_obter_tres_zeros_na_ultima_linha()
				self.mostrarResultado(self.sistema)

			elif self.cont == 11:
				self.sistema.fazer_o_terceiro_elemento_da_quarta_linha_ficar_zero_quando_o_terceiro_elemento_da_terceira_for_igual()
				self.mostrarResultado(self.sistema)

			elif self.cont == 12:
				self.sistema.fazer_o_terceiro_elemento_da_terceira_linha_ficar_um()
				self.mostrarResultado(self.sistema)

			elif self.cont == 13:
				self.sistema.fazer_o_terceiro_elemento_da_quarta_linha_ficar_zero()
				self.mostrarResultado(self.sistema)

			elif self.cont == 14:
				self.sistema.fazer_o_quarto_elemento_da_quarta_linha_ficar_um()
				self.mostrarResultado(self.sistema)

			elif self.cont == 15:
				self.sistema.fazer_o_quarto_elemento_da_terceira_linha_ficar_zero()
				self.mostrarResultado(self.sistema)

			elif self.cont == 16:
				self.sistema.fazer_o_quarto_elemento_da_segunda_linha_ficar_zero()
				self.mostrarResultado(self.sistema)

			elif self.cont == 17:
				self.sistema.fazer_o_quarto_elemento_da_primeira_linha_ficar_zero()
				self.mostrarResultado(self.sistema)

			elif self.cont == 18:
				self.sistema.fazer_o_terceiro_elemento_da_segunda_linha_ficar_zero()
				self.mostrarResultado(self.sistema)

			elif self.cont == 19:
				self.sistema.fazer_o_segundo_elemento_da_primeira_linha_ficar_zero()
				self.mostrarResultado(self.sistema)

			elif self.cont == 20:
				self.sistema.fazer_o_terceiro_elemento_da_primeira_linha_ficar_zero()
				self.mostrarResultado(self.sistema)

			elif self.cont > 20:
				self.validar.alerta("Está Escalonado!")

	def on_btniniciar_clicked(self,*args):
		if self.validar_edits():
			if self.cont > 0:
				self.cont = 0
				self.sistema.primeira_linha = self.primeira
				self.sistema.segunda_linha = self.segunda
				self.sistema.terceira_linha = self.terceira
				self.sistema.quarta_linha = self.quarta
				self.mostrarResultado(self.sistema)

	def on_window1_destroy(self,*args):
		gtk.main_quit()

if __name__=="__main__":
	w = Janela_Esc3()

