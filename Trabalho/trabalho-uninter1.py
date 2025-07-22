print('Bem vindo a loja do Gustavo Hortega!')

#Entradas com atribuições do valor de pedido e quantidade de parcelas.
valorDoPedido = float(input('Entre com o valor do pedido: '))
quantidadeParcelas = int(input('Entre com a quantidade de parcelas: '))

juros = None

if quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    juros = 0.04 #Juros de 4% - Parcelas 4x a 5x.
elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    juros = 0.08 #Juros de 8% - Parcelas 6x a 8x.
elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
    juros = 0.16 #Juros de 16% - Parcelas 9x a 12x.
elif quantidadeParcelas >= 13:
    juros = 0.32 #Juros de 32% - Parcelas Acima de 13x.
else:
    juros = 0 #Caso nenhuma das opções acima seja true, o programa reconhece que não há juros por parcelas.

valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas # Calculo do valor das parcelas

valorTotalParcelado = valorDaParcela * quantidadeParcelas #Calculo do valor total

print(f'O valor das parcelas é de:R$ {valorDaParcela:.2f}')
print(f'O valor total parcelado é de:R$ {valorTotalParcelado:.2f}')