			#########################################################
			# Autor  : Magno Lima Oliveira							#
			# E-mail : magnolimaoliveira@gmail.com					#
			# Projeto: MatSis										#
			# Objetivo : criar uma classe chamada de Matriz			#
			#			 que calcule suas propriedades.		 		#
			#########################################################

"""
>>> A = Matriz([(2,2),(2,3)])
>>> A.calcular_Traco()
matrix([[5]])
>>> A.calcular_Inversa()
matrix([[ 1.5, -1. ],
        [-1. ,  1. ]])
>>> A.descobrir_Ordem_da_Matriz()
(2, 2)
>>> A.calcular_Transposta()
matrix([[2, 2],
        [2, 3]])

>>> A.calcular_determinante()
2.0
>>> B = Matriz([(1,1),(1,1)])
>>> A.matriz + B.matriz
matrix([[3, 3],
        [3, 4]])

>>> A.calcular_Transposta()*B.matriz
matrix([[4, 4],
        [5, 5]])
>>> 3*A.calcular_Inversa()
matrix([[ 4.5, -3. ],
        [-3. ,  3. ]])

>>> matriz_A = Matriz([(3,1,5),(2,0,-2),(-1,4,-3)])
>>> matriz_A.calcular_Inversa()
matrix([[ 0.11111111,  0.31944444, -0.02777778],
        [ 0.11111111, -0.05555556,  0.22222222],
        [ 0.11111111, -0.18055556, -0.02777778]])

>>> matriz_B = Matriz([(3,2),(6,4)])
>>> matriz_B.calcular_Inversa()
'Matriz Singular !'

>>> matriz_B = Matriz([(3,2),(6,4)])
>>> matriz_A = Matriz([(3,2),(6,4)])

"""

from numpy.linalg import det
import numpy

class  Matriz (object):

	def __init__(self,*matriz):
		self.matriz = numpy.matrix(matriz[0])

	def calcular_Traco(self):
		return self.matriz.trace()

	def calcular_Inversa(self):
		try:
			return self.matriz.I # I = Inverso
		except numpy.linalg.linalg.LinAlgError:
			return " Matriz Singular ! "

	def descobrir_Ordem_da_Matriz(self):
		return self.matriz.shape

	def calcular_Transposta(self):
		return self.matriz.T

	def calcular_determinante(self):
		return det(self.matriz)

	def somar(self, matriz_A):
		soma = self.matriz + matriz_A.matriz
		return soma

	def subtrair(self, matriz_A):
		sub = matriz_A.matriz - self.matriz
		return sub

	def multiplicar(self, matriz_A):
		mult = matriz_A.matriz * self.matriz
		return mult

	def multiplicar_um_numero_por_uma_matriz(self, numero):
		mult_num = numero * self.matriz
		return mult_num


if __name__ == "__main__":
	import doctest,matriz
	doctest.testmod()

