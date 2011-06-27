#import matplotlib
#matplotlib.use( 'Agg' )
#import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import *

class Gera_Grafico_3D(object):

	def __init__(self, *args):
		self.ax1 = Axes3D(figure())

		self.a1 = args[0]
		self.b1 = args[1]
		self.c1 = args[2]
		self.d1 = args[3]

		self.a2 = args[4]
		self.b2 = args[5]
		self.c2 = args[6]
		self.d2 = args[7]

		self.a3 = args[8]
		self.b3 = args[9]
		self.c3 = args[10]
		self.d3 = args[11]


	def calcular_plano(self, a, b, c, d, cor):

		u = arange(-3.14158, 3.14158, 0.05)
		v = arange(-3.14158, 3.14158, 0.05)

		x, y = meshgrid(u, v)
		z = (-a*x -b*y +d)/c

		return self.ax1.plot_surface(x, y, z, rstride = 10, cstride = 10, color = cor)

	def gerar_grafico_3d(self):

		self.calcular_plano(self.a1, self.b1, self.c1, self.d1, "r")
		self.calcular_plano(self.a2, self.b2, self.c2, self.d2, "b")
		self.calcular_plano(self.a3, self.b3, self.c3, self.d3, "g")
		show()

if __name__ == '__main__':
	grafico = Gera_Grafico_3D(1, 2, 2, 3, 1, 1, 1, 1, 3, 6, 6, 0)
	grafico.gerar_grafico_3d()

