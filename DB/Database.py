import mysql.connector

class Database():
    def __init__(self,banco = 'sistema_crud'):
        self.banco = banco

    def connect(self):
        self.conn = mysql.connector.connect(host='10.28.1.115',database=self.banco,user='devweb',password='suporte@22')

        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("CONECTADO COM SUCESSO",db_info)
        else:
            print("ERROR")
    
    def insert_client(self):
        self.connect()
        try:
            args = ("Maira Aparecida","55555555555","tmaira95@gmail.com","67982045054","Rua Delegado Julio Cesar da Fonte Nogueira, 223", "Campo Grande")

            self.cursor.execute("INSERT INTO pessoa(nome,cpf,email,fone,endereco,cidade) VALUES (%s,%s,%s,%s,%s,%s)",args)
            self.conn.commit()
            print("CLIENTE CADASTRADO")

        except Exception as error:
            print(error)

    def insert_product(self):
        self.connect()
        try:
            args = ("UHD-AI","LG","OS","Televisão de última geração","58000.00","Smart TV","800","2000")

            self.cursor.execute("INSERT INTO produto(nome,marca,modelo,descricao,preco,tipo,tamanho,peso) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",args)
            self.conn.commit()
            print("Produto Cadastrado")
        except Exception as error:
            print(error)    

    def select_client(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM pessoa")
            clientes = self.cursor.fetchall()
            
            for cli in clientes:
                print(cli)

        except Exception as error:
            print(error)

    def select_product(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * from produto")
            produtos = self.cursor.fetchall()

            for prods in produtos:
                print (prods)
        except Exception as error:
            print(error)        

    def select_client_by_id(self,id):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM pessoa WHERE id = {id}")
            cliente = self.cursor.fetchone()
            print(cliente)
            return cliente
        
        except Exception as error:
            print(error)         

    def select_product_by_id(self,id):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * from produto WHERE id = {id}")
            prodts = self.cursor.fetchone()
            print(prodts)
            return prodts
        
        except Exception as error:
            print(error)


    def update_client(self,id):
        self.connect()
        try:
            cli = list(self.select_client_by_id(id))
            cli[1] = input("DIGITE O NOVO NOME: ")
            cli[2] = input("DIGITE O NOVO CPF: ")
            cli[3] = input("DIGITE O NOVO EMAIL: ")
            cli[4] = input("DIGITE O NOVO TELEFONE: ")
            cli[5] = input("DIGITE O NOVO ENDEREÇO: ")
            cli[6] = input("DIGITE A NOVA CIDADE: ")

            self.cursor.execute(f"UPDATE pessoa SET nome = '{cli[1]}', cpf = '{cli[2]}', email = '{cli[3]}', fone = '{cli[4]}', endereco = '{cli[5]}', cidade = '{cli[6]}' WHERE id = {cli[0]}")
            self.conn.commit()
            print("CLIENTE ATUALIZADO COM SUCESSO")
            self.select_client_by_id(cli[0])
        except Exception as error:
            print(error)    
    
    def update_product(self,id):
        self.connect()
        try:
            pro = list(self.select_product_by_id(id))
            pro[1] = input("DIGITE O NOVO NOME: ")
            pro[2] = input("DIGITE A NOVA MARCA: ")
            pro[3] = input("DIGITE O NOVO MODELO: ")
            pro[4] = input("DIGITE A NOVA DESCRIÇÃO: ")
            pro[5] = input("DIGITE O NOVO PREÇO: ")
            pro[6] = input("DIGITE O NOVO TIPO: ")
            pro[7] = input("DIGITE O NOVO TAMANHO: ")
            pro[8] = input("DIGITE O NOVO PESO: ")

            self.cursor.execute(f"UPDATE produto SET nome = '{pro[1]}', marca = '{pro[2]}', modelo = '{pro[3]}', descricao = '{pro[4]}', preco = '{pro[5]}', tipo = '{pro[6]}', tamanho = '{pro[7]}', peso = '{pro[8]}' WHERE id = {pro[0]}")
            self.conn.commit()
            print("PRODUTO ATUALIZADO COM SUCESSO")
            self.select_product_by_id(pro[0])
        except Exception as error:
            print(error)    
    
    def delete_client(self,id):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM pessoa WHERE id = {id}")
            self.conn.commit()
            print("CLIENTE DELETADO")
            self.select_client()

        except Exception as error:
            print(error)

    def delete_product(self,id):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM produto WHERE id = {id}")
            self.conn.commit()
            print("PRODUTO DELETADO")
            self.select_product()

        except Exception as error:
            print(error)    

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("CONEXÃO ENCERRADA")        


if __name__ == "__main__":
    db = Database()
    #db.connect()
    #db.insert_client()
    #db.insert_product()
    #db.select_client()
    #db.select_product()
    #db.select_client_by_id(1)
    #db.select_product_by_id(2)
    #db.delete_client(6)
    db.delete_product(5)
    #db.update_client(2)
    #db.update_product(2)
    db.close_connection()                            


