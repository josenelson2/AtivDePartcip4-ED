from node import Node

class Queue:
    def __init__(self): 
        self.head = None #início da fila, não tem ninguém
        self.tail = None #final da fila, não tem ninguém
        self.size = 0    #lista inicia vazia

    def enqueue(self, name): #método usado para adicionar um nome a fila
        new_node = Node(name) #novo nó para guardar o nome
        if self.head is None: #verificar se a lista está vazia
            self.head = new_node #a cabeça da fila passa a ser o nome
            self.tail = new_node #o final tbm, já que temos apenas um nome
        else:
            self.tail.next = new_node #o último nó passa a apontar para o novo nó
            self.tail = new_node #o novo nó é o último da fila
        self.size += 1 #aumenta a contagem de pessoas na fila
        return name
    
    def dequeue(self): #método para excluir um nome da fila
        if self.head is None: #confere se a fila está vazia
            return None
        removed_name = self.head.name #guarda o primeiro nome da fila
        self.head = self.head.next #o primeiro da fila passa a ser o seguinte
        self.size -= 1 #decrementa uma posição da fila
        if self.head is None: #confere se a fila ficou vazia após a remoção
            self.tail = None #o final da fila passa a ser none
        return removed_name
    
    def find(self, name): #método para encontrar nome
        current = self.head #começa a procurar do primeiro nó da fila
        while current: #enquanto o nó for verdade
            if current.name == name:
                return name #retorna nome se for acahado
            current = current.next #nó é substituído pelo próximo
        return None #retorna None se não achar nada
            

    def showNames(self):
        names = []
        current = self.head

        while current is not None:
            names.append(current.name)
            current = current.next
        return names
        

    def showSize(self):
        return self.size



    
        
