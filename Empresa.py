class Funcionario:
    def __init__(self, nome, salario, cargo):
        #   Inicializada os atributos comuns a todos os funcionarios
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def calcular_pagamento(self):
        #   Retornar o salario do funcionario (sem bonus ou horas extras)
        return self.salario

#   A classe gerente herda de Funcionario
class Gerente(Funcionario):
    def __init__(self, nome, salario, cargo, bonus):
        #   Chama o metodo __init__ da calsse pai (Funcionario) usando super()
        super().__init__(nome, salario, cargo)
        #   Adiciona um atributo especifico para gerentes: bonus
        self.bonus = bonus

    def calcular_pagamento(self):
        #   Retorna o salario do funcionario (sem bonus ou horas extras)
        return self.salario + self.bonus
    
#   A classe desenvolvedor tambem herda de funcionario
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, cargo, horas_extras = 0, valor_hora_extra = 0):
        #   Chama o metodo __init__ da classe pai (Funcionario) usando super()
        super().__init__(nome, salario, cargo)
        #   Adiciona atributos especificos para desenvolvedores: horas extras e valor por hora extra
        self.horas_extras = horas_extras
        self.valor_horas_extra = valor_hora_extra

    def calcular_pagamento(self):
        #   Calcula o pagamento incluindo as horas extras do desenvolvedor
        return self.salario + (self.horas_extras * self.valor_horas_extra)
    
#   Classe que gerencia ps funcionarios e pagamentos
class SistemaEmpresa:
    #   Inicializa uma lista de funcionarios
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self,funcionario):
        #   Adiciona um funcionario a lista
        self.funcionarios.append(funcionario)

    def processar_pagamentos(self):
        #   Processa os pagamentos de todos os funcionarios cadastrados
        for funcionario in self.funcionarios:
            print(f"Pagamento de {funcionario.nome}: R$ {funcionario.calcular_pagamento():.2f}")

#   Criando instancias de funcionarios
carlos = Gerente("Carlos", 8000, "Gerente de Projetos", 2000)
ana = Desenvolvedor("Ana", 5000, "Desenvolvedora", horas_extras=10, valor_hora_extra=50)

#   Criando o sistema e adicionando funcionarios
sistema = SistemaEmpresa()
sistema.adicionar_funcionario(carlos)
sistema.adicionar_funcionario(ana)

#   Processando os pagamentos
sistema.processar_pagamentos()