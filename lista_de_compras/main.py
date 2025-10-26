# Lista que armazenará os itens
lista_compras = []

# Função para mostrar o menu
def mostrar_menu():
    print("\n=== MENU LISTA DE COMPRAS ===")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Listar itens")
    print("4. Buscar item")
    print("5. Sair")

# Função para adicionar item
def adicionar_item():
    nome = input("Digite o nome do item: ").strip()
    quantidade = input("Digite a quantidade: ").strip()
    preco = input("Digite o preço unitário: ").strip()

    # Criando um dicionário para o item
    item = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }

    lista_compras.append(item)
    print(f"Item '{nome}' adicionado com sucesso!")

# Função para remover item
def remover_item():
    nome = input("Digite o nome do item que deseja remover: ").strip()
    encontrado = False
    for item in lista_compras:
        if item["nome"].lower() == nome.lower():
            lista_compras.remove(item)
            print(f"Item '{nome}' removido com sucesso!")
            encontrado = True
            break
    if not encontrado:
        print(f"Item '{nome}' não encontrado na lista.")

# Função para listar todos os itens
def listar_itens():
    if not lista_compras:
        print("A lista de compras está vazia.")
    else:
        print("\n=== LISTA DE COMPRAS ===")
        for i, item in enumerate(lista_compras, start=1):
            print(f"{i}. {item['nome']} - Quantidade: {item['quantidade']} - Preço: {item['preco']}")

# Função para buscar item
def buscar_item():
    nome = input("Digite o nome do item para buscar: ").strip()
    encontrados = [item for item in lista_compras if nome.lower() in item["nome"].lower()]

    if encontrados:
        print("\nItens encontrados:")
        for item in encontrados:
            print(f"{item['nome']} - Quantidade: {item['quantidade']} - Preço: {item['preco']}")
    else:
        print("Nenhum item encontrado com esse nome.")

# Loop principal
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        adicionar_item()
    elif opcao == "2":
        remover_item()
    elif opcao == "3":
        listar_itens()
    elif opcao == "4":
        buscar_item()
    elif opcao == "5":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")