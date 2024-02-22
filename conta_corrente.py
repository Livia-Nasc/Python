# Crie uma classe para implementar uma Conta Corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: depósito (recebe valor como atributo e soma ao saldo) e saque (recebe valor como atributo e subtrai do saldo).

class conta_bancaria:
    def init(self, saldo, nome, numero_da_conta):
        self.saldo = saldo
        self.nome = nome
        self.numero_da_conta = numero_da_conta
        
    def deposito(self, valor_deposito):
        self.saldo += valor_deposito
        return self.saldo
    
    def saque(self, valor_saque):
        if valor_saque > self.saldo:
            return "O valor excede o limite da conta."
        else:
            self.saldo -= valor_saque
            return ("Olá", self.nome, "O novo saldo da sua conta é", self.saldo, "reais")
    
    def acao(self):
        self.nome = input("Digite seu nome: ")
        self.saldo = float(input("Informe o saldo atual da conta: "))
        self.numero_da_conta = int(input("Digite o número da conta: "))
        acao = input("Você deseja fazer um depósito ou um saque? ")
        if acao == "deposito":
            valor_deposito = float(input("Quanto você deseja depositar? "))
            novo_saldo = self.deposito(valor_deposito)
            print("Olá", self.nome, "O novo saldo da sua conta é", novo_saldo, "reais")
        elif acao == "saque":
            valor_saque = float(input("Quanto você deseja sacar? "))
            novo_saldo = self.saque(valor_saque)
            print(novo_saldo)
banco = conta_bancaria()
banco.acao()
