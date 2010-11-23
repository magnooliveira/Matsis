# -*- coding:UTF-8 -*-
			#########################################################
			# Autor  : Magno Lima Oliveira							#
			# E-mail : magnolimaoliveira@gmail.com					#
			# Projeto: MatSis										#
			# Objetivo : a partir de uma equacao da reta dada é		# 
			#			 possivel calcular uma outra equação, 		#
            #            aleatoriamente, de acordo com o tipo de 	#
            #            sistema definido   						#
			#########################################################


"""
>>> equacao= SistemaTresIncognitas(1,2,2,3,2,2)
>>> equacao.acharTresPlanosCoincidentes()
([2, 4, 4, 6], [2, 4, 4, 6])
>>> equacao.acharDoisPlanosCoincidentesUmParalelo()
([2, 4, 4, 6], [2, 4, 4, 7])
>>> equacao.acharDoisPlanosCoincidentesUmIntersecta()
([2, 4, 4, 6], [3, 5, 5, 6])
>>> equacao.acharTresPlanosParalelos()
([2, 4, 4, 7], [2, 4, 4, 7])
>>> equacao.acharTresPlanosComUmaRetaComum()
([3, 6, 7, 6], [8, 16, 18, 18])
>>> equacao.acharTresPlanosIntersectamDoisADois()
([3, 6, 7, 6], [8, 16, 18, 20])
"""


import random
from random import randrange

class SistemaTresIncognitas(object):
		
	def __init__(self,coeficiente_a,coeficiente_b,coeficiente_c,coeficiente_d,k=random.randrange(2,5),p=random.randrange(6,9)):
		self.primeira_Equacao_Do_Usuario = [coeficiente_a,coeficiente_b,coeficiente_c,coeficiente_d]
		self.k=k
		self.p=p
	
	def acharTresPlanosCoincidentes(self):
		segunda_Equacao=map(lambda x:x*self.k,self.primeira_Equacao_Do_Usuario)
		terceira_Equacao=map(lambda y:y*self.p,self.primeira_Equacao_Do_Usuario)
		return segunda_Equacao,terceira_Equacao
		
	def acharDoisPlanosCoincidentesUmParalelo(self):
		segunda_Equacao=map(lambda x:x*self.k,self.primeira_Equacao_Do_Usuario)
		terceira_Equacao=map(lambda y:y*self.p,self.primeira_Equacao_Do_Usuario)
		terceira_Equacao[len(terceira_Equacao)-1]+=1
		return segunda_Equacao,terceira_Equacao
		
	def acharDoisPlanosCoincidentesUmIntersecta(self):
		segunda_Equacao=map(lambda x:x*self.k,self.primeira_Equacao_Do_Usuario)
		terceira_Equacao=map(lambda y:y*self.p,self.primeira_Equacao_Do_Usuario)
		for i in range(len(terceira_Equacao)-1):
			terceira_Equacao[i]+=1
		return segunda_Equacao,terceira_Equacao
		
	def acharTresPlanosParalelos(self):
		segunda_Equacao=map(lambda x:x*self.k,self.primeira_Equacao_Do_Usuario)
		terceira_Equacao=map(lambda y:y*self.p,self.primeira_Equacao_Do_Usuario)
		segunda_Equacao[len(segunda_Equacao)-1]+=1
		terceira_Equacao[len(terceira_Equacao)-1]+=1
		return segunda_Equacao,terceira_Equacao
		
	def acharDoisPlanosParalelosUmIntersecta(self):
		segunda_Equacao=map(lambda x:x*self.k,self.primeira_Equacao_Do_Usuario)
		terceira_Equacao=map(lambda y:y*self.p,self.primeira_Equacao_Do_Usuario)
		segunda_Equacao[len(segunda_Equacao)-1]+=1
		for i in range(len(terceira_Equacao)-1):
			terceira_Equacao[i]+=1
		return segunda_Equacao,terceira_Equacao
		
	def acharTresPlanosComUmaRetaComum(self):
		segunda_Equacao=map(lambda x:x*self.k,self.primeira_Equacao_Do_Usuario)
		for i in range(len(segunda_Equacao)-1):
			segunda_Equacao[i]+=i+1
		terceira_Equacao=map(lambda x,y:x+y,(map(lambda x:x*self.p,self.primeira_Equacao_Do_Usuario)),(map(lambda y:y*self.k,segunda_Equacao)))
		return segunda_Equacao,terceira_Equacao
		
	def acharTresPlanosIntersectamDoisADois(self):
		segunda_Equacao=map(lambda x:x*self.k,self.primeira_Equacao_Do_Usuario)
		for i in range(len(segunda_Equacao)-1):
			segunda_Equacao[i]+=i+1
		terceira_Equacao=map(lambda x,y:x+y,(map(lambda x:x*self.p,self.primeira_Equacao_Do_Usuario)),(map(lambda y:y*self.k,segunda_Equacao)))
		terceira_Equacao[len(terceira_Equacao)-1]+=2
		return segunda_Equacao,terceira_Equacao
	
	# Achar uma solucao para tres planos e um  ponto comum
	def acharTresPlanosUmPontoComum(self):
		pass
		
if __name__=='__main__':
	import doctest,Sistema_De_Tres_Incognitas
	doctest.testmod()
