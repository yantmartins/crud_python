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
                db.insert_client()
            case '2':
                db.insert_product()
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
                print("Conexão encerrada")
                break






