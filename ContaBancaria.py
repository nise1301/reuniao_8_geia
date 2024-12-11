class ContaBancaria:
    def __init__(self, numero, titular): # isso aqui é um construtor em python
        self.numero = numero
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            print("O valor do saque deve ser positivo.")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

"""Na POO em Python, o self substitui o this presente no Java na função de dar contexto aos métodos.
 Ele vai dentro da chamada do método e também na declaração dos atributos para expecificar a classe a qual ele pertence"""