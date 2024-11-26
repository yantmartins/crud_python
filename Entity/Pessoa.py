from DB.Database import Database

class Pessoa:
    def __init__(self) -> None:
        self.nome = None
        self.cpf = None
        self.email = None
        self.fone = None
        self.endereco = None
        self.cidade = None

    def cadastrar(self):
        tupla = (self.nome,self.cpf,self.email,self.fone,self.endereco,self.cidade)
        db = Database()
        db.insert_client(tupla)

    def getPessoa(self):
        db = Database()
        pes = db.select_client()
        return pes       



        