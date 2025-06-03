from abc import ABC, abstractmethod

# Classe blue print
class Personagem(ABC):
    def __init__(self, vida, stamina, mana):
        self.vida = vida
        self.stamina = stamina
        self.mana = mana

    @abstractmethod
    def habilidade(self):
        pass

# Classes funcional
class Melee(Personagem):
    def __init__(self):
        super().__init__(vida=100, stamina=70, mana=10)

    def habilidade(self):
        print("Melee usa GOLPE DE ESPADA!")

class Ranger(Personagem):
    def __init__(self):
        super().__init__(vida=70, stamina=100, mana=40)

    def habilidade(self):
        print("Range dispara FLECHA EXPLOSIVA!")

class Wizard(Personagem):
    def __init__(self):
        super().__init__(vida=50, stamina=30, mana=120)

    def habilidade(self):
        print("Wizard conjura BOLA DE FOGO!")

# Fábrica blue print5
class FábricaDePersonagem(ABC):
    @abstractmethod
    def criar_personagem(self):
        pass

# Fábricas concretas
class FábricaMelee(FábricaDePersonagem):
    def criar_personagem(self):
        return Melee()

class FábricaRanger(FábricaDePersonagem):
    def criar_personagem(self):
        return Ranger()

class FábricaWizard(FábricaDePersonagem):
    def criar_personagem(self):
        return Wizard()

# Função que usa o Factory
def jogar(fábrica):
    personagem = fábrica.criar_personagem()
    print(f"Vida: {personagem.vida}, Stamina: {personagem.stamina}, Mana: {personagem.mana}")
    personagem.habilidade()

# Testando
print("=== Jogando com Melee ===")
jogar(FábricaMelee())

print("\n=== Jogando com Range ===")
jogar(FábricaRanger())

print("\n=== Jogando com Wizard ===")
jogar(FábricaWizard())