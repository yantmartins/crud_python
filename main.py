from Entity.Produto import Produto
from Entity.Cliente import Cliente

def gerenciar_produto():
    prod1 = Produto()

    while True:
        print("\n --- Gerenciamento dos Produtos ---")    
        print("1. Cadastrar Produtos")    
        print("2. Listar Produtos")    
        print("3. Atualizar Produtos")    
        print("4. Deletar Produtos")    
        print("5. Voltar")
        opcao = int(input("Escolha uma opção: "))

        match opcao:
            case 1:    
                prod1.nome = input("Digite o nome do produto: ")
                prod1.marca = input("Digite a marca do produto:")
                prod1.modelo = input("Digite o modelo do produto:")
                prod1.descricao = input("Digite a descrição do produto:")
                prod1.preco = input("Digite o preço do produto:")
                prod1.tipo = input("Digite o tipo do produto:")
                prod1.tamanho = input("Digite o tamanho do produto:")
                prod1.peso = input("Digite o peso do produto: ")

                if prod1.cadastra():
                    print("Produto cadastrado com sucesso!")

            case 2:    
                produtos = prod1.seleciona()
                for produto in produtos:
                    print(f" ID: {produto[0]} Nome: {produto[1]} Marca: {produto[2]}")

            case 3:    
                id_prod = int(input("Digite o ID do produto que deseja atualizar: "))
                produto_selecionado = prod1.seleciona_por_id(id_prod)

                produto_selecionado[1] = input("DIGITE O NOVO NOME: ")
                produto_selecionado[2] = input("DIGITE A NOVA MARCA: ")
                produto_selecionado[3] = input("DIGITE O NOVO MODELO: ")
                produto_selecionado[4] = input("DIGITE A NOVA DESCRIÇÃO: ")
                produto_selecionado[5] = input("DIGITE O NOVO PREÇO: ")
                produto_selecionado[6] = input("DIGITE O NOVO TIPO: ")
                produto_selecionado[7] = input("DIGITE O NOVO TAMANHO: ")
                produto_selecionado[8] = input("DIGITE O NOVO PESO: ")
                
                if prod1.atualiza(produto_selecionado):
                    print("Produto atualizado com sucesso")

            case 4:
                id_prod = int(input("Digite o ID do produto para deletar: "))
                if prod1.delete(id_prod):
                    print("Produto deletado")

            case 5:
                break
def gerenciar_cliente():                
    cli1 = Cliente()

    while True:
        print("\n --- Gerenciamento dos Clientes ---")    
        print("1. Cadastrar Clientes")    
        print("2. Listar Clientes")    
        print("3. Atualizar Clientes")    
        print("4. Deletar Clientes")    
        print("5. Voltar")
        opcao = int(input("Escolha uma opção: "))

        match opcao:
            case 1:
                cli1.nome = input("Digite seu nome: ")
                cli1.cpf = input("Digite seu CPF: ")
                cli1.email = input("Digite seu email: ")
                cli1.fone = input("Digite seu telefone: ")
                cli1.endereco = input("Digite seu endereço: ")
                cli1.cidade = input("Digite sua cidade: ")

                if cli1.cadastrar():
                    print("Cliente cadastrado com sucesso")

            case 2:
                clientes = cli1.selecionar()
                for cliente in clientes:
                    print(f" ID: {cliente[0]} Nome: {cliente[1]} CPF: {cliente[2]}")

            case 3:
                id_cli = int(input("Digite o ID do cliente que deseja atualizar:"))
                cliente_selecionado = cli1.selecionar_por_id(id_cli)

                cliente_selecionado[1] = input("DIGITE O NOVO NOME: ")
                cliente_selecionado[2] = input("DIGITE O NOVO CPF: ")
                cliente_selecionado[3] = input("DIGITE O NOVO EMAIL: ")
                cliente_selecionado[4] = input("DIGITE O NOVO TELEFONE: ")
                cliente_selecionado[5] = input("DIGITE O NOVO ENDEREÇO: ")
                cliente_selecionado[6] = input("DIGITE A NOVA CIDADE: ")

                if cli1.atualizar(cliente_selecionado):
                    print("Cliente atualizado com sucesso")

            case 4:
                id_cli = int(input("Digite o ID do cliente para deletar: "))
                if cli1.deletar(id_cli):
                    print("Cliente deletado")

            case 5:
                break
    
def menu():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Gerenciar Produtos")
        print("2. Gerenciar Clientes")
        print("3. Sair")
        opcao = int(input("Escolha uma opção: "))

        match opcao:
            case 1:
                gerenciar_produto()
            case 2:
                gerenciar_cliente()
            case 3:
                print("Saindo")
                break        


if __name__ == "__main__":
    menu()

  


