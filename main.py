from Entity.Produto import Produto

prod1 = Produto()

prod1.nome = input("Digite o nome do produto: ")
prod1.marca = input("Digite a marca do produto:")
prod1.modelo = input("Digite o modelo do produto:")
prod1.descricao = input("Digite a descrição do produto:")
prod1.preco = input("Digite o preço do produto:")
prod1.tipo = input("Digite o tipo do produto:")
prod1.tamanho = input("Digite o tamanho do produto:")
prod1.peso = input("Digite o peso do produto: ")

result = prod1.cadastra()
if result == True:
    print("Produto cadastrado com sucesso!")

data_from_bank = prod1.seleciona()

for produto in data_from_bank:
    print(f" ID: {produto[0]} Nome: {produto[1]} Marca: {produto[2]}")

print("Deseja atualizar os dados de um produto?")
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

update = prod1.atualiza(produto_selecionado)
if update == True:
    print("Produto atualizado com sucesso")
    prod_atualizado = prod1.seleciona_por_id(produto_selecionado[0])
    print(prod_atualizado)
else:
    print("Erro ao atualizar")    

from Entity.Cliente import Cliente
cli1 = Cliente()

dados_do_banco = cli1.selecionar()

for cliente in dados_do_banco:
    print(f" ID: {cliente[0]} Nome: {cliente[1]} CPF: {cliente[2]}")


print("Deseja atualizar os dados de um cliente?")
id_cli = int(input("Digite o ID do cliente que deseja atualizar:"))

cliente_selecionado = cli1.selecionar_por_id(id_cli)

cliente_selecionado[1] = input("DIGITE O NOVO NOME: ")
cliente_selecionado[2] = input("DIGITE O NOVO CPF: ")
cliente_selecionado[3] = input("DIGITE O NOVO EMAIL: ")
cliente_selecionado[4] = input("DIGITE O NOVO TELEFONE: ")
cliente_selecionado[5] = input("DIGITE O NOVO ENDEREÇO: ")
cliente_selecionado[6] = input("DIGITE A NOVA CIDADE: ")

atualizacao = cli1.atualizar(cliente_selecionado)
if atualizacao == True:
    print("Cliente atualizado com sucesso")
    cli_atualizado = cli1.selecionar_por_id(cliente_selecionado[0])
    print(cli_atualizado)
else:
    print("Erro ao atualizar")    






print("Deseja deletar um cliente? ")
id_cli = int(input("Digite o ID do cliente que deseja deletar: "))

cli_deletado = cli1.deletar(id_cli)
if cli_deletado == True:
    print("Cliente deletado com sucesso")
    dados_do_banco = cli1.selecionar()

    for cliente in dados_do_banco:
        print(f" ID: {cliente[0]} Nome: {cliente[1]} CPF: {cliente[2]}")




cli1.nome = input("Digite seu nome: ")
cli1.cpf = input("Digite seu CPF: ")
cli1.email = input("Digite seu email: ")
cli1.fone = input("Digite seu telefone: ")
cli1.endereco = input("Digite seu endereço: ")
cli1.cidade = input("Digite sua cidade: ")

result = cli1.cadastrar()
if result == True:
    print("Cliente cadastrado com sucesso!")    


