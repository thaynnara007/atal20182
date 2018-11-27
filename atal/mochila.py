def mochila(pesoMax, pesos, valores, qntdItens):

    dp = [[0 for j in xrange(pesoMax + 1)] for i in xrange(qntdIntens + 1)]

    for item in xrange(1,qntdIntens + 1):
        for capacidade in xrange(1,pesoMax + 1):

            if pesos[item] > capacidade: dp[item][capacidade] = dp[item - 1][capacidade]
            else: dp[item][capacidade] = max(dp[item - 1][capacidade], dp[item - 1][capacidade - pesos[item]] + valores[item])
    
    return dp[-1][-1]


pesoMax = int(raw_input("peso max:"))
qntdIntens = int(raw_input("quantidade de itens:"))
pesos = [0] * (qntdIntens + 1)
valores = [0] * (qntdIntens + 1)
dp = [[0 for j in xrange(pesoMax + 1)] for i in xrange(qntdIntens + 1)]
print 'itens:'
for item in xrange(1, qntdIntens + 1):

    peso, valor = map(int, raw_input().split())
    pesos[item] = peso
    valores[item] = valor

print mochila(pesoMax, pesos, valores, qntdIntens)
