from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def menu():
    print(""" 
    Escolha uma opção:
    1-Depositar
    2-Sacar  
    3-Extrato
    4-Transferência
    5-Criar Usuário
    6-Criar Conta            
    7-Sair 
    ===> """)
    try:
        return int(input())
    except ValueError:
        print("Opção inválida! Por favor, insira um número de 1 a 7.")
        return 0


def principal():
    clientes = []
    contas = []

    while True:
        opcao = menu()
        if opcao == 1:
            print("Depósito:")
            try:
                numero_conta = int(input("Número da conta: "))
                valorD = float(input("Qual valor deseja depositar? "))
                conta = next((c for c in contas if c.numero == numero_conta), None)
                if conta:
                    transacao = Deposito(valorD)
                    conta.cliente.realizar_transacao(conta, transacao)
                else:
                    print("Conta não encontrada.")
            except ValueError:
                print("Valor inválido! Por favor, insira um número.")
        elif opcao == 2:
            print("Saque:") 
            try:
                numero_conta = int(input("Número da conta: "))
                valorS = float(input("Qual valor deseja sacar? "))
                conta = next((c for c in contas if c.numero == numero_conta), None)
                if conta:
                    transacao = Saque(valorS)
                    conta.cliente.realizar_transacao(conta, transacao)
                else:
                    print("Conta não encontrada.")
            except ValueError:
                print("Valor inválido! Por favor, insira um número.")
        elif opcao == 3:
            numero_conta = int(input("Número da conta: "))
            conta = next((c for c in contas if c.numero == numero_conta), None)
            if conta:
                print("Extrato:")
                for transacao in conta.historico.transacoes:
                    print(f"{transacao['data']} - {transacao['tipo']}: R${transacao['valor']:.2f}")
                print(f"Saldo: R${conta.saldo:.2f}")
            else:
                print("Conta não encontrada.")
        elif opcao == 4:
            print("Transferência:") 
            try:
                numero_conta_origem = int(input("Número da conta de origem: "))
                numero_conta_destino = int(input("Número da conta de destino: "))
                valorT = float(input("Qual valor deseja transferir? "))
                conta_origem = next((c for c in contas if c.numero == numero_conta_origem), None)
                conta_destino = next((c for c in contas if c.numero == numero_conta_destino), None)
                if conta_origem and conta_destino:
                    transacao_saque = Saque(valorT)
                    if conta_origem.cliente.realizar_transacao(conta_origem, transacao_saque):
                        transacao_deposito = Deposito(valorT)
                        conta_destino.cliente.realizar_transacao(conta_destino, transacao_deposito)
                        print("Transferência realizada com sucesso!")
                else:
                    print("Conta de origem ou destino não encontrada.")
            except ValueError:
                print("Valor inválido! Por favor, insira um número.")
        elif opcao == 5:
            criar_usuario(clientes)
        elif opcao == 6:
            numero_conta = len(contas) + 1
            conta = criar_conta(numero_conta, clientes)
            if conta:
                contas.append(conta)
        elif opcao == 7:
            print("Obrigado por usar nosso serviço")
            break
        else:
            if opcao != 0:
                print("Opção inválida!")

def criar_usuario(clientes):
    try:
        cpf = int(input("Informe seu CPF (SOMENTE NÚMEROS): "))
        usuario = filtrar_usuario(cpf, clientes)
        if usuario:
            print("Já existe um usuário com este CPF!")
            return
        nome = input("Digite seu nome completo: ")
        data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")    
        endereco = input("Informe seu endereço (Rua, Bairro, Cidade/Estado): ")
        cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)
        clientes.append(cliente)
        print("Usuário criado com sucesso!")
    except
