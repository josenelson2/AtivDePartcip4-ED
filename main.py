from linkedQueue import Queue

def menu():
    print("\n==== Menu Queue Ativ 4 ====")
    print("1. Adicionar (enqueue)")
    print("2. Remover (dequeue)")
    print("3. Mostrar elementos da fila")
    print("4. Mostrar tamanho da fila")
    print("5. Procurar nome na fila")
    print("0. Sair")

fila = Queue()

while True:
    menu()
    op = int(input("Escolha uma opção: "))

    while op < 0 or op > 5:
        op = int(input("Opção inválida! Digite novamente: ")) 
     
    if op == 1:
        name = input("Digite o nome que deseja adicionar: ")
        fila.enqueue(name)
        print(f"Pronto. O elemento '{name}' foi adicionado!")

    elif op == 2:
        name = fila.dequeue()
        if name == None:
            print("Fila vazia!")
        else:
            print(f"Pronto. O elemento '{name}' foi removido!")

    elif op == 3:
        nomes = fila.showNames()
        if nomes:
            print("Nomes das pessoas na fila")
            print(" -> ".join(nomes))
        else:
            print("Nao ha pessoas na fila.")

    elif op == 4:
        quant = fila.showSize()
        print(f"A quantidade de pessoas na fila eh {quant}.")

    elif op == 5:
        name = input("Qual nome deseja encontrar: ")
        resul = fila.find(name)
        if resul == None:
            print("Nome não encontrado!")
        else:
            print("Nome encontrado!")
            
    else:
        break


