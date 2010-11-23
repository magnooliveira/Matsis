"""
>>> primeira_linha = (1, 2, 3, 4, 23)
>>> segunda_linha = (5, 1, 2, 1, 14)
>>> terceira_linha = (2, 1, 2, 2, 14)
>>> quarta_linha = (3, 4, 2, 1, 18)
>>> escalona = EscalonamentoQuatroLinhas(primeira_linha, segunda_linha, terceira_linha, quarta_linha)
>>> escalona.executarTodasAsEtapa()
>>> escalona
x = 1.000, y = 2.000, z = 2.000, w = 3.000

>>> primeira_linha = (1, 0, 0, 0, 1)
>>> segunda_linha = (0, 1, 0, 0, 2)
>>> terceira_linha = (0, 0, 1, 0, 3)
>>> quarta_linha = (0, 0, 0, 1, 4)
>>> escalona2 = EscalonamentoQuatroLinhas(primeira_linha, segunda_linha, terceira_linha, quarta_linha)
>>> escalona2.executarTodasAsEtapa()
>>> escalona2
x = 1.000, y = 2.000, z = 3.000, w = 4.000
"""

if __name__ == "__main__":
	import doctest, escalonamento_quatro_linhas
	from escalonamento_quatro_linhas import EscalonamentoQuatroLinhas
	doctest.testmod()
