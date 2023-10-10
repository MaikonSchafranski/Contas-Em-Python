class Conta():
    saldo = 0
    conta = 0

    def __init__(self, numero, saldoInicial):
        self.numero = numero
        self.saldoInicial = saldoInicial

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if (self.saldo > 0):
            self.saldo-+valor

        else:
            print('Saldo insuficiente')


if __name__ == '__main__':
    conta = Conta("12345-1", 0)
    print('numero da conta:')
    print(conta.numero)
    print("\nsaldo total:")
    print(conta.saldo)
    print('\ndeposito total:')
    conta.deposito(150)
    print(conta.saldo)
