from DB.Database import Database

class Cliente:
    def __init__(self) -> None:
        self.nome = None
        self.cpf = None
        self.email = None
        self.fone = None
        self.endereco = None
        self.cidade = None
        self.banco = Database()

    def cadastrar(self):
        tupla = (self.nome, self.cpf, self.email, self.fone, self.endereco, self.cidade)
        res = self.banco.insert_client(tupla)
        if res == True:
            print("Cliente cadastrado com sucesso!")    

    def selecionar(self):
        dados = self.banco.select_client()
        return dados
    
    def selecionar_por_id(self,id):
        dado = self.banco.select_client_by_id(id)
        return list(dado)
    
    def atualizar(self,lista):
        res = self.banco.update_client(lista)
        return res

    def deletar(self,id):
        res = self.banco.delete_client(id)
        return res