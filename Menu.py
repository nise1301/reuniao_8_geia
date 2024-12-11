from ContaBancaria import ContaBancaria

def criar_conta(lista_contas):
    numero = input("Digite o número da conta: ")
    titular = input("Digite o nome do titular: ")
    conta = ContaBancaria(numero, titular) #aqui que estamos criando o objeto propriamente dito
    lista_contas.append(conta)
    print(f"Conta {numero} criada com sucesso.")

def encontrar_conta(lista_contas, numero):
    for conta in lista_contas:
        if conta.numero == numero:
            return conta
    return None

def menu():
    lista_contas = []
    while True:
        print("\nSistema de Controle de Conta Bancária")
        print("1. Criar nova conta")
        print("2. Realizar depósito")
        print("3. Fazer saque")
        print("4. Consultar saldo")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_conta(lista_contas)
        elif opcao == "2":
            numero = input("Digite o número da conta para depósito: ")
            conta = encontrar_conta(lista_contas, numero)
            if conta:
                valor = float(input("Digite o valor do depósito: "))
                conta.depositar(valor)
            else:
                print("Conta não encontrada.")
        elif opcao == "3":
            numero = input("Digite o número da conta para saque: ")
            conta = encontrar_conta(lista_contas, numero)
            if conta:
                valor = float(input("Digite o valor do saque: "))
                conta.sacar(valor)
            else:
                print("Conta não encontrada.")
        elif opcao == "4":
            numero = input("Digite o número da conta para consulta de saldo: ")
            conta = encontrar_conta(lista_contas, numero)
            if conta:
                conta.consultar_saldo()
            else:
                print("Conta não encontrada.")
        elif opcao == "5":
            print("Operação Encerrada")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
