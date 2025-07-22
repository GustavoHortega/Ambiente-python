print('----------Bem-vindo a Loja de marmitad do Gustavo Hortega----------\n'\
      '-----------------------------Cardápio------------------------------\n'\
      '-------| Tamanho | Bife Acebolado(BA) | Filé de Frango(FF) |-------\n'\
      '-------|    P    |      R$ 16.00      |      R$ 15.00      |-------\n'\
      '-------|    M    |      R$ 18.00      |      R$ 17.00      |-------\n'\
      '-------|    G    |      R$ 22.00      |      R$ 21.00      |-------\n'\
      '-------------------------------------------------------------------') #Cardápio do restaurante

loop = 0 #Controlador do loop
acum = 0 #Acumulador de valor (Declarada com valor 0)

while loop == 0:
      sabor = input('Entre com o sabor desejado (BA/FF): ')
      if sabor == 'BA' or sabor == 'FF':
            tamanho = input('Entre com o tamanho desejado (P/M/G): ')
            if tamanho not in ['P','M', 'G']:
                  print('Tamanho inválido. Tente Novamente \n')
                  continue
      else:
            print('Sabor inválido, Tente novamente \n')
            continue
      if sabor =='BA':
            sabor = 'Bife Acebolado'
            if tamanho == 'P':
                  acum += 16.00
            elif tamanho == 'M':
                  acum += 18.00
            elif tamanho == 'G':
                  acum += 22.00
      if sabor == 'FF':
            sabor = 'Filé de Frango'
            if tamanho == 'P':
                  acum += 15.00
            elif tamanho == 'M':
                  acum += 17.00
            elif tamanho == 'G':
                  acum += 21.00
      if input('Deseja pedir mais algum coisa? (S/N)') == 'S':
            continue
      else:
            break
print(f'Valor total a ser pago: R$ {acum:.2f}')
      
      