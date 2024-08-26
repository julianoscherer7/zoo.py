class Animal:
    def __init__(self, nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao):
        self.nome = nome
        self.idade = idade
        self.barulho = barulho
        self.movimento = movimento
        self.alimentacao = alimentacao
        self.habitat = habitat
        self.vizinhos = vizinhos  
        self.horas_alimentacao = horas_alimentacao

    def fazer_barulho(self):
        return self.barulho

    def movimento(self):
        return self.movimento

    def alimentacao(self):
        return self.alimentacao

    def habitat(self):
        return self.habitat

    def vizinhos(self):
        return ", ".join(self.vizinhos) if self.vizinhos else "Nenhum vizinho registrado"

    def horas_alimentacao(self):
        return self.horas_alimentacao

class Mamifero(Animal):
    pass

class Ave(Animal):
    pass

class Reptil(Animal):
    pass

animais = [
    Mamifero("Leão", 8, "Rugido", "Corre", "Carnívoro", "Selva", ["Elefante", "Tigre"], "12:00"),
    Ave("Águia", 5, "Chilro", "Voa", "Carnívoro", "Montanhas", ["Coruja"], "13:00"),
    Reptil("Cobra", 3, "Sibilar", "Rasteja", "Carnívoro", "Florestas", ["Tartaruga"], "10:00"),
    Mamifero("Elefante", 15, "Bramido", "Anda", "Herbívoro", "Savana", ["Leão"], "15:00"),
    Ave("Coruja", 4, "Pio", "Voa", "Carnívoro", "Florestas", ["Águia"], "23:00"),
    Reptil("Tartaruga", 100, "Silêncio", "Anda devagar", "Herbívoro", "Praias", ["Cobra"], "11:00"),
]


def cadastrar_animal():
    categoria = input("Categoria do animal (Mamífero, Ave, Réptil): ").strip().lower()
    nome = input("Nome do animal: ").strip()
    idade = int(input("Idade do animal: "))
    barulho = input("Som característico do animal: ").strip()
    movimento = input("Movimento do animal: ").strip()
    alimentacao = input("Dieta do animal: ").strip()
    habitat = input("Habitat do animal: ").strip()
    vizinhos = input("Nomes dos vizinhos (máximo 2, separados por vírgula): ").strip().split(",")[:2]
    horas_alimentacao = input("Horário de alimentação: ").strip()

    if categoria == "mamífero":
        animal = Mamifero(nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao)
    elif categoria == "ave":
        animal = Ave(nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao)
    elif categoria == "réptil":
        animal = Reptil(nome, idade, barulho, movimento, alimentacao, habitat, vizinhos, horas_alimentacao)
    else:
        print("Categoria inválida!")
        return

    animais.append(animal)
    print(f"{nome} cadastrado com sucesso!")


def listar_animais():
    if not animais:
        print("Nenhum animal cadastrado.")
    else:
        print("\nAnimais cadastrados:")
        for animal in animais:
            print(f"- {animal.nome}")


def buscar_animal():
    nome = input("Digite o nome do animal: ").strip()
    for animal in animais:
        if animal.nome.lower() == nome.lower():
            print(f"\nNome: {animal.nome}")
            print(f"Idade: {animal.idade}")
            print(f"Som: {animal.fazer_barulho()}")
            print(f"Movimento: {animal.movimento}")
            print(f"Dieta: {animal.alimentacao}")
            print(f"Habitat: {animal.habitat}")
            print(f"Vizinhos: {animal.vizinhos()}")
            print(f"Horário de Alimentação: {animal.horas_alimentacao}")
            return
    print(f"Animal {nome} não encontrado.")


def listar_por_categoria():
    categoria = input("Categoria (Mamífero, Ave, Réptil): ").strip().lower()
    encontrados = []
    for animal in animais:
        if (categoria == "mamífero" and isinstance(animal, Mamifero)) or \
           (categoria == "ave" and isinstance(animal, Ave)) or \
           (categoria == "réptil" and isinstance(animal, Reptil)):
            encontrados.append(animal.nome)
    if encontrados:
        print(f"Animais na categoria {categoria.capitalize()}: {', '.join(encontrados)}")
    else:
        print(f"Nenhum animal encontrado na categoria {categoria.capitalize()}.")


def listar_vizinhos():
    nome = input("Digite o nome do animal: ").strip()
    for animal in animais:
        if animal.nome.lower() == nome.lower():
            print(f"Vizinhos de {animal.nome}: {animal.vizinhos()}")
            return
    print(f"Animal {nome} não encontrado.")

def simular_alimentacao():
    nome = input("Digite o nome do animal: ").strip()
    for animal in animais:
        if animal.nome.lower() == nome.lower():
            print(f"{animal.nome} foi alimentado às {animal.horas_alimentacao}.")
            return
    print(f"Animal {nome} não encontrado.")

def menu():
    while True:
        print("\n----- Menu Zoo OO -----")
        print("1. Listar todos os animais")
        print("2. Buscar animal")
        print("3. Listar animais por categoria")
        print("4. Listar vizinhos de um animal")
        print("5. Simular alimentação")
        print("6. Cadastrar novo animal")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_animais()
        elif opcao == "2":
            buscar_animal()
        elif opcao == "3":
            listar_por_categoria()
        elif opcao == "4":
            listar_vizinhos()
        elif opcao == "5":
            simular_alimentacao()
        elif opcao == "6":
            cadastrar_animal()
        elif opcao == "7":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()

	


