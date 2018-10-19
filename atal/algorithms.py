#coding: utf-8

import sys
sys.setrecursionlimit(2000)

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

# Caso o valor não possa ser alcançado pela combinação de moedas o valor -1 é retornado Ex: valor = 11  moedas = {5, 10, 25}
# Assuma que existe uma quantidade infinita de cada tipo de moeda

menorQntdMoedas = -1
visitados = set([])
def retorna_minimo_moedas(valor, tipos_moedas):
	
	print valor, tipos_moedas
    
	resultado = retornaMinimoMoedas(valor, 0, 0, tipos_moedas, len(tipos_moedas))
	
	return menorQntdMoedas

def retornaMinimoMoedas(valorAtual, i , qntdMoedas, moedas, sizeMoedas):

   global menorQntdMoedas
   
   tupla = (valorAtual, i, qntdMoedas)

   if tupla not in visitados:

        visitados.add((valorAtual, i, qntdMoedas))

        if i < sizeMoedas:

            if valorAtual == 0:

                if menorQntdMoedas == -1:  menorQntdMoedas = qntdMoedas

                else: menorQntdMoedas = min(menorQntdMoedas, qntdMoedas)
            
            elif moedas[i] <= valorAtual:

                if i < sizeMoedas -1:

                    valorAddProxMoeda = valorAtual - moedas[i + 1]

                    if valorAddProxMoeda >= 0: 
                        retornaMinimoMoedas(valorAddProxMoeda, i + 1, qntdMoedas + 1, moedas, sizeMoedas)

                valorAddMesmaMoeda = valorAtual - moedas[i]

                if valorAddMesmaMoeda >= 0:
                    retornaMinimoMoedas(valorAddMesmaMoeda, i, qntdMoedas + 1, moedas, sizeMoedas)
                
                retornaMinimoMoedas(valorAtual, i + 1, qntdMoedas, moedas, sizeMoedas)
	

