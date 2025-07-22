print("Bem vindo a Empresa do Gustavo Hortega")

# Lista de funcionários
lista_funcionarios = []

# ID inicial baseado no RU
id_global = 5220700

def cadastrar_funcionario(id_func): #Cadastra os funcionários
    print('-------------- MENU CADASTRAR FUNCIONÁRIO ------------')  
    print(f'Id do funcionário: {id_func}')
    nome = input("Por favor entre com o nome do Funcionário: ")
    setor = input("Por favor entre com o setor do Funcionário: ")
    salario = float(input("Por favor entre com o salário do Funcionário: "))
    funcionario = { #Dicionário do cadastrado
        "id": id_func,
        "nome": nome,
        "setor": setor,
        "salario": salario
    }
    lista_funcionarios.append(funcionario.copy()) #Insere o funcionário na lista

def consultar_funcionarios():#Faz a consulta dos funcionários na lista.
    while True:
        print("------------------------------------------")
        print("-------- MENU CONSULTAR FUNCIONÁRIO -------")
        print("Escolha a opção desejada:")
        print("1 - Consultar Todos os Funcionários")
        print("2 - Consultar Funcionário por id")
        print("3 - Consultar Funcionário(s) por setor")
        print("4 - Retornar")
        opcao = input(">>")
        
        if opcao == "1":
            for funcionario in lista_funcionarios: #Faz a consulta para cada funcionário existente na lista
                print("--------------------")
                print(f"id: {funcionario['id']}")
                print(f"nome: {funcionario['nome']}")
                print(f"setor: {funcionario['setor']}")
                print(f"salário: {funcionario['salario']}")
        elif opcao == "2":
            id_consulta = int(input("Digite o id do funcionário: ")) #faz a consulta por ID
            encontrado = False
            for funcionario in lista_funcionarios:
                if funcionario['id'] == id_consulta:
                    print("--------------------")
                    print(f"id: {funcionario['id']}")
                    print(f"nome: {funcionario['nome']}")
                    print(f"setor: {funcionario['setor']}")
                    print(f"salário: {funcionario['salario']}")
                    encontrado = True
                    break
            if not encontrado: #Verifica se o funcionário foi encontrado negando a condição acima.
                print("Funcionário não encontrado.")
        elif opcao == "3":
            setor_consulta = input("Digite o setor do(s) funcionário(s): ")
            encontrados = [f for f in lista_funcionarios if f['setor'].lower() == setor_consulta.lower()]
            if encontrados:
                for funcionario in encontrados:
                    print("--------------------")
                    print(f"id: {funcionario['id']}")
                    print(f"nome: {funcionario['nome']}")
                    print(f"setor: {funcionario['setor']}")
                    print(f"salário: {funcionario['salario']}")
            else:
                print("Nenhum funcionário encontrado nesse setor.")
        elif opcao == "4":
            return
        else:
            print("Opção inválida")

def remover_funcionario():#Remove o funcionário da lista pelo ID
    while True:
        try:
            id_remover = int(input("Digite o id do funcionario a ser removido: "))
            for funcionario in lista_funcionarios:
                if funcionario['id'] == id_remover:
                    lista_funcionarios.remove(funcionario)
                    print("Funcionário removido com sucesso!")
                    return
            print("Id inválido")
        except ValueError:
            print("Entrada inválida, digite um número.")

while True: #Menu Principal
    print("------------------------------------------")
    print("-------------- MENU PRINCIPAL ------------")
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Funcionários")
    print("2 - Consultar Funcionário(s)")
    print("3 - Remover Funcionário")
    print("4 - Sair")
    opcao = input(">>")

    if opcao == "1":
        cadastrar_funcionario(id_global)
        id_global += 1
    elif opcao == "2":
        consultar_funcionarios()
    elif opcao == "3":
        remover_funcionario()
    elif opcao == "4":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida")
