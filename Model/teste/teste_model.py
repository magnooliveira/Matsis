"""
>>> primeiraLinha=(1, 2, -1, 7)
>>> segundaLinha=(3, -1, 2, -5)
>>> terceiraLinha=(2, 3, 1, 8)
>>> escalona = Escalonamento(primeiraLinha, segundaLinha, terceiraLinha)
>>> escalona.executarTodasAsEtapa()
>>> escalona
x = 0.000, y = 3.000, z = -1.000
>>> primeiraLinha=(8, 4, 5, -23)
>>> segundaLinha=(4, 8, 1, -7)
>>> terceiraLinha=(-2, -10, 2, 0)
>>> escalona2 = Escalonamento(primeiraLinha, segundaLinha, terceiraLinha)
>>> escalona2.executarTodasAsEtapa()
>>> escalona2
x = -4.000, y = 1.000, z = 1.000
>>> primeiraLinha=(2, 4, 1, 13)
>>> segundaLinha=(0, 5, 3, 19)
>>> terceiraLinha=(0, 0, 1, 3)
>>> escalona3 = Escalonamento(primeiraLinha, segundaLinha, terceiraLinha)
>>> escalona3.executarTodasAsEtapa()
>>> escalona3
x = 1.000, y = 2.000, z = 3.000
>>> primeiraLinha=(1, 3, 5, 0)
>>> segundaLinha=(0, 0, 1, 1)
>>> terceiraLinha=(0, -2, 3, 5)
>>> escalona4 = Escalonamento(primeiraLinha, segundaLinha, terceiraLinha)
>>> escalona4.executarTodasAsEtapa()
>>> escalona4
x = -2.000, y = -1.000, z = 1.000
>>> primeiraLinha=(1, 0, 0, 5)
>>> segundaLinha=(0, 0, 1, 2)
>>> terceiraLinha=(0, 1, 0, 3)
>>> escalona4 = Escalonamento(primeiraLinha, segundaLinha, terceiraLinha)
>>> escalona4.executarTodasAsEtapa()
>>> escalona4
x = 5.000, y = 3.000, z = 2.000
>>> primeiraLinha = (2, 1, 3, 8)
>>> segundaLinha = (4, 2, 2, 4)
>>> terceiraLinha = (2, 5, 3, -12)
>>> escalona5 = Escalonamento(primeiraLinha, segundaLinha, terceiraLinha)
>>> escalona5.executarTodasAsEtapa()
>>> escalona5
x = 2.000, y = -5.000, z = 3.000
>>> primeiraLinha = (2, 3, 4, 27)
>>> segundaLinha = (1, -2, 3, 15)
>>> terceiraLinha = (3, 1, 6, 40)
>>> escalona6 = Escalonamento(primeiraLinha, segundaLinha, terceiraLinha)
>>> escalona6.executarTodasAsEtapa()
>>> escalona6
x = 9.286, y = 0.143, z = 2.000
>>> primeiraLinha = (3, 1, 1, 20)
>>> segundaLinha = (2, -1, -1, -15)
>>> terceiraLinha = (-4, 1, -5, -41)
>>> escalona7 = Escalonamento(primeiraLinha, segundaLinha, terceiraLinha)
>>> escalona7.executarTodasAsEtapa()
>>> escalona7
x = 1.000, y = 8.000, z = 9.000
>>> primeiraLinha = (1.1, 0, 0.1, 10)
>>> segundaLinha = (-0.1, -0.2, 1, -10)
>>> terceiraLinha = (0, 0, 0.2, 10)
>>> escalona7 = Escalonamento(primeiraLinha, segundaLinha, terceiraLinha)
>>> escalona7.executarTodasAsEtapa()
>>> escalona7
x = 4.545, y = 297.727, z = 50.000

>>> primeira_linha = (1, 2, 3, 4, 23)
>>> segunda_linha = (5, 1, 2, 1, 14)
>>> terceira_linha = (2, 1, 2, 2, 14)
>>> quarta_linha = (3, 4, 2, 1, 18)
>>> escalona_quatro = EscalonamentoQuatroLinhas(primeira_linha, segunda_linha, terceira_linha, quarta_linha)
>>> escalona_quatro.executarTodasAsEtapa()
>>> escalona_quatro
x = 1.000, y = 2.000, z = 2.000, w = 3.000

>>> primeira_linha = (1, 0, 0, 0, 1)
>>> segunda_linha = (0, 1, 0, 0, 2)
>>> terceira_linha = (0, 0, 1, 0, 3)
>>> quarta_linha = (0, 0, 0, 1, 4)
>>> escalona_quatro2 = EscalonamentoQuatroLinhas(primeira_linha, segunda_linha, terceira_linha, quarta_linha)
>>> escalona_quatro2.executarTodasAsEtapa()
>>> escalona_quatro2
x = 1.000, y = 2.000, z = 3.000, w = 4.000

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

>>> equacao = SistemaDuasIncognitas(4,-3,-3,2)
>>> equacao.acharDuasRetasCoincidentes()
[8, -6, -6]
>>> equacao.acharDuasRetasParalelas()
[8, -6, -7]
>>> equacao.acharDuasRetasConcorrentes()
[9, -6, -6]

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

if __name__ == "__main__":

	import doctest, teste_model
	from sys import path
	import os.path
	caminho_do_escalonamento_model = os.path.expanduser( "~/Matsis/Model/escalonamento_model")
	caminho_da_matriz_model = os.path.expanduser( "~/Matsis/Model/matriz_model")
	caminho_do_sistema_model =  os.path.expanduser("~/Matsis/Model/sistema_model")
	path.append(caminho_do_escalonamento_model)
	path.append(caminho_da_matriz_model)
	path.append(caminho_do_sistema_model)
	from escalonamento import *
	from escalonamento_quatro_linhas import *
	from matriz import *
	from Sistema_De_Duas_Incognitas import *
	from Sistema_De_Tres_Incognitas import *
	doctest.testmod()

