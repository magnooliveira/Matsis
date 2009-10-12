#Autor : Magno Lima Oliveira

'''
>>> equacao = SistemaDuasIncognitas((4,-3,-3),2) 
>>> equacao.acharDuasRetasCoincidentes()
[8,-6,-6]
>>> equacao = SistemaDuasIncognitas((1,1,1),2) 
>>> equacao.acharDuasRetasParalelas()
[2,2,1]
>>> equacao = SistemaDuasIncognitas((1,2,3),2) 
>>> equacao.acharDuasRetasCoincidentes()
[3,4,6]

'''

import random
from random import randrange

class SistemaDuasIncognitas(object):

	def __init__(self,*L1, k=random.randrange(2,6)):
		self.L1=list(L1)
		self.k=k

	def acharDuasRetasCoincidentes(self):
		L2=map(lambda x:x*self.k,self.L1)
		return L2
		
	def acharDuasRetasParalelas(self):
		L2=map(lambda x:x*self.k,self.L1)
		L2[len(self.L1)-1]-=1
		return L2
		
	def acharDuasRetasConcorrentes(self): 
		L2=map(lambda x:x*self.k,self.L1)
		L2[0]+=1
		return L2


	
if __name__=='__main__':
	import doctest,ClasseSistemaDuasIncognitas
	doctest.testmod()
