notas = [9,7,7,10,3,9,6,6,2]

print(f'O número de alunos que tirou nota 7 é: {notas.count(7)}') #ache quantos alunos tiraram nota 7

notas[-1] = 4 #subistitua a ultima nota por 4

print (notas)
print(f'A maior nota é {max(notas)}') #ache a maior nota

notas.sort #ordene todas as notas
print(notas)

print(f'A média é: {sum(notas) / len(notas)}') #mostre a média