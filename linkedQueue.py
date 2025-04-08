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
            self.tail = new_node #o final tbm,já que temos apenas um nome
        else:
            self.tail.next = new_node #o último nó passa a apontar para o novo nó
            self.tail = new_node #o novo nó é o último da fila
        self.size += 1 #aumenta a contagem de pessoas na fila
        return "Nome foi enfileirado"
    
    def dequeue(self):
        pass
    
        
