class Restaurante:
    def __init__(self):
        self.cardapio = {}  # dicionário
        self.comanda = {}   # dicionário

    def adicionar_prato(self):
        nome = input("Nome do prato: ")
        preco = float(input("Preço: "))
        tempo = int(input("Tempo de preparo (minutos): "))
        self.cardapio[nome] = (preco, tempo)
        print(f"{nome} foi adicionado ao sistema.")

    def abrir_comanda(self):
        numero = int(input("Insira número da comanda: "))
        if numero in self.comanda:
            print("Comanda já existe.")
            return
        self.comanda[numero] = {
            "pratos": [],
            "total": 0,
            "tempo": 0,
            "status": "Aberta"
        }
        print(f"Comanda {numero} aberta!")  

    def adicionar_pedido(self):
        numero = int(input("Insira o número da comanda: "))
        if numero not in self.comanda:
            print("A comanda não foi encontrada!")
            return

        print("Cardápio disponível:")
        for nome, (preco, tempo) in self.cardapio.items():
            print(f" - {nome}, R${preco:.2f}, Tempo: {tempo} min")

        prato = input("Nome do prato para adicionar: ")
        if prato in self.cardapio:
            preco, tempo = self.cardapio[prato]
            self.comanda[numero]["pratos"].append(prato)
            self.comanda[numero]["total"] += preco
            self.comanda[numero]["tempo"] += tempo
            self.comanda[numero]["status"] = "Sendo preparado"
            print(f"{prato} adicionado à comanda {numero}!")
        else:
            print("Prato não está no cardápio.")

    def verificar_pedido(self):
        numero = int(input("Número da comanda: "))
        if numero not in self.comanda:
            print("Comanda não encontrada.")
            return

        print(f"\nComanda {numero}")
        print(f"Status: {self.comanda[numero]['status']}")
        print(f"Total R$: {self.comanda[numero]['total']:.2f}")
        print(f"Tempo de espera: {self.comanda[numero]['tempo']} minutos")

    def fechar_conta(self):
        numero = int(input("Número da comanda: "))
        if numero not in self.comanda:
            print("Comanda não encontrada.")
            return

        if self.comanda[numero]["status"] == "Aberta":
            print("O pedido ainda está sendo preparado.")
            return

        print(f"\nConta da comanda {numero} fechada")
        print(f"Total a pagar: R${self.comanda[numero]['total']:.2f}")

        print("Escolha forma de pagamento:")
        print("1 - Dinheiro")
        print("2 - Crédito")
        print("3 - Débito")
        print("4 - Pix")

        opcao = input("Digite o número da opção: ")

        if opcao == "1":
            print("Pagamento em dinheiro realizado com sucesso!")
        elif opcao == "2":
            print("Pagamento no crédito realizado com sucesso!")
        elif opcao == "3":
            print("Pagamento no débito realizado com sucesso!")
        elif opcao == "4":
            print("Pagamento no Pix realizado com sucesso!")
        else:
            print("Opção inválida. Tente novamente.")
            return

        del self.comanda[numero]
        print("Comanda finalizada.")


restaurante = Restaurante()

while True:
    print("\n1 - Adicionar ao cardápio")
    print("2 - Abrir comanda")
    print("3 - Adicionar pedido")
    print("4 - Verificar pedido")
    print("5 - Fechar a conta")
    print("6 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        restaurante.adicionar_prato()
    elif opcao == "2":
        restaurante.abrir_comanda()
    elif opcao == "3":
        restaurante.adicionar_pedido()
    elif opcao == "4":
        restaurante.verificar_pedido()
    elif opcao == "5":
        restaurante.fechar_conta()
    elif opcao == "6":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")
