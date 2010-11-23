#coding:utf-8

import gtk,gtk.glade

class Controle(object):

	def __init__(self):
		pass

	def alerta(self,texto):
		dialogo= gtk.MessageDialog (None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, texto)
		dialog.set_title("MatSis")
		dialogo.set_markup (texto)
		dialogo.run ()
		return dialogo.destroy ()

