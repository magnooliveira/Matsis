# -*- coding:UTF-8 -*-			
			#########################################################
			# Autor  : Magno Lima Oliveira				#
			# E-mail : magnolimaoliveira@gmail.com		        #
			# Projeto: MatSis				        #				
			# Objetivo : a partir de uma equacao da reta dada é	# 
			#	     possivel calcular uma outra equação, 	#
                        #            aleatoriamente, de acordo com o tipo de 	#
                        #            sistema definido   			#
			#########################################################

'''
>>> equacao = SistemaDuasIncognitas(4,-3,-3,2) 
>>> equacao.acharDuasRetasCoincidentes()
[8, -6, -6]
>>> equacao.acharDuasRetasParalelas()
[8, -6, -7]
>>> equacao.acharDuasRetasConcorrentes()
[9, -6, -6]

'''

import random
from random import randrange

class SistemaDuasIncognitas(object):

	def __init__(self,coeficiente_a,coeficiente_b,coeficiente_c,k=random.randrange(2,6)):
		self.equacao_Do_Usuario=[coeficiente_a,coeficiente_b,coeficiente_c]
		self.k=k

	def acharDuasRetasCoincidentes(self):
		equacao_Do_Sistema=map(lambda x:x*self.k,self.equacao_Do_Usuario)
		return equacao_Do_Sistema
		
	def acharDuasRetasParalelas(self):
		equacao_Do_Sistema=map(lambda x:x*self.k,self.equacao_Do_Usuario)
		equacao_Do_Sistema[len(self.equacao_Do_Usuario)-1]-=1
		return equacao_Do_Sistema
		
	def acharDuasRetasConcorrentes(self): 
		equacao_Do_Sistema=map(lambda x:x*self.k,self.equacao_Do_Usuario)
		equacao_Do_Sistema[0]+=1
		return equacao_Do_Sistema


	
if __name__=='__main__':
	import doctest,Sistema_De_Duas_Incognitas
	doctest.testmod()
