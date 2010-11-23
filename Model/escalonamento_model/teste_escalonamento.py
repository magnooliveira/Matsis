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
"""

if __name__ == "__main__":
	import doctest, teste_escalonamento
	from escalonamento import Escalonamento
	doctest.testmod()

