print('Bem vindo a Fábrica de Camisetas do Gustavo Hortega')

modelos = { 'MCS': 1.80, 'MLS': 2.10, 'MCE': 2.90, 'MLE': 3.20}

def escolha_modelo(): # Faz a escolha do modelo e retona o valor do modelo
    print('Entre com o modelo desejado\n'\
          'MCS - Maga Curta Simples\n'\
          'MLS - Maga Longa Simples\n'\
          'MCE - Maga Curta Com Estampa\n'\
          'MLE - Maga Longa Com Estampa')
    valor = input('>>')
    if valor in modelos:
        return float(modelos[valor]) #Retorna o valor no dicionário
    else:
        print('Escolha invalida, entre com o modelo novamente.\n')
        return escolha_modelo()
    
def num_camiseta():# Define o numero de camisetas selecionado pelo usuário
    try: #Verifica se o input é um inteiro
        num = int(input('\nEntre com o numero de camisetas: '))
    except:
       print('Opção invalida\n')
       return num_camiseta()
    if num <= 20000:#Verifica se o numero é menor ou igual a 20000(Limite de camisetas)
            return num
    else:
        print('Não aceitamos tantas camisetas de uma vez.\nPor favor entre com o número de camisetas novamente.\n')
        return num_camiseta()
    
def frete(): #Faz a escolha do frete
    print('Escolha o tipo de frete:\n'\
          '1 - Frete por transportadora - R$ 100.00\n'\
          '2 - Frete por Sedex - R$ 200.00\n'\
          '0 - Retirar pedido na fábrica - R$ 0.00')
    vfrete = int(input('>>'))
    if vfrete == 1: #Este bloco retorna o valor confore o frete escolhido.
        return 100.00
    elif vfrete == 2:
        return 200.00
    elif vfrete == 0:
        return 0.00
    else:
        print('Opção invalida\n')
        return frete() #Chama função em um caso de resposta invalida.

#extraindo os valores para trabalhar no main do códico.
vMod = escolha_modelo()
quantidade = num_camiseta()
vFrete = frete()

#define o desconto pela quantidade de itens
desconto = 0

if quantidade >= 20 and quantidade < 200:
    desconto = 0.05
elif quantidade >= 200 and quantidade < 2000:
    desconto = 0.07
elif quantidade >=2000 and quantidade <=20000:
    desconto = 0.12

#Calculo total e total com desconto
total = (vMod * quantidade)
vDesconto = total * desconto
total = (total - vDesconto) + vFrete

print (f'Total: R$ {total:.2f} (Modelo: {vMod:.2f} * Quantidade(com desconto): {(vMod * quantidade) - vDesconto:.2f} + frete: R$ {vFrete:.2f})')