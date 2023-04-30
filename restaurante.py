import heapq
import random
import sys

class PriorityQueue:
    def __init__(self, size):
        self.queue = []
        self.index = 0
        self.size = size

    def __len__(self):
        return len(self.queue)

    def push(self, item):
        if len(self.queue) < self.size:
            heapq.heappush(self.queue, (item[0], item[1], self.index, item[2]))
            self.index += 1
        else:
            print("A fila com prioridades está lotada!")

    def pop(self):
        return heapq.heappop(self.queue)

    def peek(self):
        return self.queue[0]

class FastFoodManager:
    def __init__(self):
        self.priority_queue = PriorityQueue(10)
        self.common_queue = []

    def add_group(self):
        if len(self.priority_queue) == self.priority_queue.size:
            print("A fila com prioridades está lotada!")
            return
        num_people = int(input("Digite a quantidade de pessoas no grupo: "))
        prep_time = int(input("Digite o tempo de preparo em minutos: "))
        name = input("Digite o nome da reserva: ")
        self.priority_queue.push((num_people, prep_time, name))
        print("Grupo adicionado com sucesso!")

    def show_next(self):
        if len(self.priority_queue) == 0:
            print("A fila com prioridades está vazia!")
            return
        next_group = self.priority_queue.peek()
        print("O próximo grupo é: ", next_group[3], "com", next_group[0], "pessoas e", next_group[1], "minutos de preparo")

    def prepare_meal(self):
        if len(self.priority_queue) == 0:
            print("A fila com prioridades está vazia!")
            return
        next_group = self.priority_queue.pop()
        wait_time = next_group[1]
        for group in self.common_queue:
            wait_time += group[1]
        self.common_queue.append(next_group)
        print("Preparando refeição para", next_group[3], "com tempo de espera estimado de", wait_time, "minutos")

    def deliver_meal(self):
        if len(self.common_queue) == 0:
            print("Não há nenhuma refeição para entregar!")
            return
        next_group = self.common_queue.pop(0)
        print("A refeição para", next_group[3], "está pronta!")

    def interface(self):
        while True:
            print("\nEscolha uma opção:\n")
            print("1. Definir tamanho da fila com prioridades (escolher esta opção fará com que o usuário deva adicionar os novos grupos manualmente)")
            print("2. Gerar simulação (escolher esta opção irá gerar os grupos aleatóriamente)") 
            print("0. Sair")
            choice = int(input("\n\nDigite a opção escolhida: "))
            if choice == 0:
                print("Saindo...")
                sys.exit()
            elif choice == 1:
                size = int(input("Digite o tamanho da fila: "))
                self.priority_queue = PriorityQueue(size)
                self.common_queue = []
                print("Tamanho da fila com prioridades definido para", size)
                self.fila_criada()
            elif choice == 2:
                self.run_simulation()
            else:
                print("Opção inválida! Tente novamente.")

    def fila_criada(self):
        while True:
            print("\nEscolha uma opção:\n")
            print("1. Adicionar novo grupo na fila com prioridades")
            print("2. Mostrar próximo grupo aguardando")
            print("3. Preparar próxima refeição")
            print("4. Entregar refeição")
            print("0. Sair")
            choice = int(input("\n\nDigite a opção escolhida: "))
            if choice == 0:
                print("Saindo...")
                sys.exit()
            elif choice == 1:
                self.add_group()
            elif choice == 2:
                self.show_next()
            elif choice == 3:
                self.prepare_meal()
            elif choice == 4:
                self.deliver_meal()
            else:
                print("Opção inválida! Tente novamente.")

    def run_simulation(self):
        for i in range(8):
            num_people = random.randint(1, 8)
            prep_time = random.randint(5, 30)
            name = "Grupo " + str(i+1)
            self.priority_queue.push((num_people, prep_time, name))
        print("Simulação iniciada!")
        while True:
            print("\nEscolha uma opção:\n")
            print("1. Adicionar novo grupo na fila com prioridades")
            print("2. Mostrar próximo grupo aguardando")
            print("3. Preparar próxima refeição")
            print("4. Entregar refeição")
            print("0. Sair")
            choice = int(input("\n\nDigite a opção escolhida: "))
            if choice == 0:
                print("Saindo...")
                sys.exit()
            elif choice == 1:
                self.add_group()
            elif choice == 2:
                self.show_next()
            elif choice == 3:
                self.prepare_meal()
            elif choice == 4:
                self.deliver_meal()
            else:
                print("Opção inválida! Tente novamente.")



restaurante = FastFoodManager()
restaurante.interface()