#coding: utf-8

import sys

# Esse metodo recebe uma lista com as matriculas dos alunos
# e retorna essa lista em ordem crescente de matriculas
def retorna_matriculas_decrescente(alist):
	for j in xrange(len(alist)):
		for i in xrange(len(alist)-1):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
	return alist

# Esse metodo recebe e valor para ser dado o troco e uma lista com os tipos de moedas possiveis
# e retorna o numero minimo de moedas possiveis em que o troco pode ser dado
#
# Caso o valor não possa ser alcançado pela combinação de moedas o valor -1 é retornado Ex: valor = 11  moedas = {5, 10, 25}
# Assuma que existe uma quantidade infinita de cada tipo de moeda
def retorna_minimo_moedas(valor, tipos_moedas):
	print valor, tipos_moedas
	resultado = retorna_minimo_moedas_FB(tipos_moedas, valor)
	if resultado == sys.maxint:
		return -1
	else:
		return resultado

def retorna_minimo_moedas_FB(tipos_moedas, valor):
	if valor == 0:
		return 0
	
	resultado = sys.maxint
	
	for moeda in tipos_moedas:
		
		if (moeda <= valor):
			resultado = min(resultado, retorna_minimo_moedas_FB(tipos_moedas, valor - moeda) + 1) 
		
	return resultado	 

# Mochila Binaria interativo
  
# Retorna o valor maximo que cabe na mochila com 
# capacidade peso_maximo
def mochila_binaria(peso_maximo, pesos, valores, n): 
  
    dp = [[0 for j in xrange(peso_maximo + 1)] for i in xrange(n + 1)]

    for item in xrange(1, n + 1):
        for capacidade in xrange(1, peso_maximo + 1):

            if pesos[item - 1] > capacidade: dp[item][capacidade] = dp[item - 1][capacidade]
            else: dp[item][capacidade] = max(dp[item - 1][capacidade], dp[item - 1][capacidade - pesos[item - 1]] + valores[item - 1])
    
    return dp[-1][-1]