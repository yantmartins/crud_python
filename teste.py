from DB.Database import Database

if __name__ == "__main__":
    db = Database()

    while True:
        print("\n1 - Cadastrar Clientes")
        print("2 - Cadastrar Produtos")
        print("3 - Listar Clientes")
        print("4 - Listar Produtos")
        print("5 - Buscar cliente por ID")
        print("6 - Buscar produto por ID")
        print("7 - Atualizar Clientes")
        print("8 - Atualizar Produtos")
        print("9 - Deletar Clientes")
        print("10 - Deletar Produtos")
        print("11 - Encerrar Conexão")

        opcao = input("\nEscolha uma opção: ")

        match opcao:
            case '1':
                nome = input("Digite o nome: ")
                cpf = input("Digite o CPF: ")
                email = input("Digite o e-mail: ")
                telefone = input("Digite o telefone: ")
                endereco = input("Digite o endereço: ")
                cidade = input("Digite a cidade: ")
                db.insert_client(nome, cpf, email, telefone, endereco, cidade)
                
            case '2':
                nome = input("Digite o nome do produto: ")
                marca = input("Digite a marca: ")
                modelo = input("Digite o modelo: ")
                descricao = input("Digite a descrição: ")
                preco = float(input("Digite o preço: "))
                tipo = input("Digite o tipo: ")
                tamanho = input("Digite o tamanho: ")
                peso = input("Digite o peso: ")
                db.insert_product(nome, marca, modelo, descricao, preco, tipo, tamanho, peso)
            case '3':
                db.select_client()
            case '4':
                db.select_product()
            case '5':
                id = int(input("Digite o ID do cliente: "))
                db.select_client_by_id(id)        
            case '6':
                id = int(input("Digite o ID do produto: "))
                db.select_product_by_id(id)
            case '7':
                id = int(input("Digite o ID do cliente pata atualizar: "))
                db.update_client(id)
            case '8':
                id = int(input("Digite o ID do produto para atualizar: "))
                db.update_product(id)
            case '9':    
                id = int(input("Digite o ID do cliente para deletar: "))
                db.delete_client(id)
            case '10':
                id = int(input("Digite o ID do produto: "))
                db.delete_product(id)                            
            case '11':
                db.close_connection()
                break






