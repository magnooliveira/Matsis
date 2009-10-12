#Autor : Magno Lima Oliveira

'''
>>> equacao = SistemaDuasIncognitas(4,-3,-3,2) 
>>> equacao.acharDuasRetasCoincidentes()
[8, -6, -6]
>>> equacao = SistemaDuasIncognitas(1,1,1,2) 
>>> equacao.acharDuasRetasParalelas()
[2, 2, 1]
>>> equacao = SistemaDuasIncognitas(1,2,3,2) 
>>> equacao.acharDuasRetasConcorrentes()
[3, 4, 6]

'''

import random
from random import randrange

class SistemaDuasIncognitas(object):

	def __init__(self,coeficiente_a,coeficiente_b,coeficiente_c, k=random.randrange(2,6)):
		self.equacao_Da_Reta_Do_Usuario = [coeficiente_a,coeficiente_b,coeficiente_c]
		self.k=k

	def acharDuasRetasCoincidentes(self):
		equacao_Gerada_Pelo_Sistema=map(lambda x:x*self.k,self.equacao_Da_Reta_Do_Usuario)
		return equacao_Gerada_Pelo_Sistema
		
	def acharDuasRetasParalelas(self):
		equacao_Gerada_Pelo_Sistema=map(lambda x:x*self.k,self.equacao_Da_Reta_Do_Usuario)
		equacao_Gerada_Pelo_Sistema[len(self.equacao_Da_Reta_Do_Usuario)-1]-=1
		return equacao_Gerada_Pelo_Sistema
		
	def acharDuasRetasConcorrentes(self): 
		equacao_Gerada_Pelo_Sistema=map(lambda x:x*self.k,self.equacao_Da_Reta_Do_Usuario)
		equacao_Gerada_Pelo_Sistema[0]+=1
		return equacao_Gerada_Pelo_Sistema


	
if __name__=='__main__':
	import doctest,Sistema_De_Duas_Incognitas
	doctest.testmod()
