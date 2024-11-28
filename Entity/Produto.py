from DB.Database import Database

class Produto:
    def __init__(self) -> None:
        self.nome = None
        self.marca = None
        self.modelo = None
        self.descricao = None
        self.preco = None
        self.tipo = None
        self.tamanho = None
        self.peso = None
        self.banco = Database()

    def cadastra(self):
        tupla = (self.nome, self.marca, self.modelo, self.descricao, self.preco, self.tipo, self.tamanho, self.peso)
        res = self.banco.insert_product(tupla)
        if res == True:
            print("Produto cadastrado com sucesso")

    def seleciona(self):
        dados = self.banco.select_product()
        return dados

    def seleciona_por_id(self,id):
        dado = self.banco.select_product_by_id(id)
        return list(dado)

    def atualiza(self,lista):
        res = self.banco.update_product(lista)
        return res

    def delete(self,id):
        res = self.banco.delete_product(id)
        return res    
