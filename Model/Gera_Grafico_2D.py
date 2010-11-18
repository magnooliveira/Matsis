import matplotlib
matplotlib.use('GTK')
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import numpy as np

class Grafico(object):
	def __init__(self,*arg):
		self.arg = arg
	
	def gerarGrafico2D(self):
		listax1,listay1,listax2,listay2,listax,listay=[],[],[],[],[],[]
			
		for x in range(-10,11):
			listay1.append(((-self.arg[0]*x) + self.arg[2])/self.arg[1])
			listax1.append(x)
			listay2.append(((-self.arg[3]*x) + self.arg[5])/self.arg[4])
			listax2.append(x)
			listay.append(x)
			listax.append(0)
			
		yticks=np.arange(-10,11,1)
		xticks=np.arange(-10,11,1)
		plt.title("MatSis")
		plt.yticks(yticks)
		plt.xticks(xticks)
		plt.plot(listax1,listay1,lw=2)
		plt.plot(listax2,listay2,lw=2)
		plt.plot(listax,listay,'0',lw=4)
		plt.plot(listay,listax,'0',lw=4)

		plt.ylabel('coordenadas de y')
		plt.xlabel('coordenadas de x')
		plt.grid(True)
		plt.show()

	def gerarGrafico3D(self):
		listax1,listay1,listax2,listay2,listax,listay=[],[],[],[],[],[]
			
		for x in range(-10,11):
			listay1.append(((-self.arg[0]*x) + self.arg[2])/self.arg[1])
			listax1.append(x)
			listay2.append(((-self.arg[3]*x) + self.arg[5])/self.arg[4])
			listax2.append(x)
			listay.append(x)
			listax.append(0)
			
		yticks=np.arange(-10,11,1)
		xticks=np.arange(-10,11,1)
		plt.title("MatSis")
		plt.yticks(yticks)
		plt.xticks(xticks)
		plt.plot(listax1,listay1,lw=2)
		plt.plot(listax2,listay2,lw=2)
		plt.plot(listax,listay,'0',lw=4)
		plt.plot(listay,listax,'0',lw=4)

		plt.ylabel('coordenadas de y')
		plt.xlabel('coordenadas de x')
		plt.grid(True)
		plt.show()
