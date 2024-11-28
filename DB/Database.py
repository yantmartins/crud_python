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
    
    def insert_client(self,param:tuple):
        self.connect()
        try:
            self.cursor.execute(""" 
                                INSERT INTO pessoa 
                                (nome,cpf,email,fone,endereco,cidade) 
                                VALUES (%s,%s,%s,%s,%s,%s)
                                """,param)
            self.conn.commit()
            return True
        
        except Exception as error:
            print(error)

        finally:
            self.close_connection()    

    def insert_product(self,param:tuple):
        self.connect()
        try:
            self.cursor.execute("INSERT INTO produto(nome,marca,modelo,descricao,preco,tipo,tamanho,peso) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",param)
            self.conn.commit()
            return True
        
        except Exception as error:
            print(error)

        finally:
            self.close_connection()         

    def select_client(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM pessoa")
            clientes = self.cursor.fetchall()
            
            return clientes

        except Exception as error:
            print(error)
        
        finally:
            self.close_connection()       

    def select_product(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * from produto")
            produtos = self.cursor.fetchall()

            return produtos

        except Exception as error:
            print(error)
        
        finally:
            self.close_connection()               

    def select_client_by_id(self,id):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM pessoa WHERE id = {id}")
            cliente = self.cursor.fetchone()
            return cliente
        
        except Exception as error:
            print(error)
        finally:
            self.close_connection()                

    def select_product_by_id(self,id):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * from produto WHERE id = {id}")
            prodts = self.cursor.fetchone()
            return prodts
        
        except Exception as error:
            print(error)
        finally:
            self.close_connection()       


    def update_client(self,lista):
        self.connect()
        try:
            self.cursor.execute(f"""UPDATE pessoa 
                                SET nome = '{lista[1]}',
                                cpf = '{lista[2]}',
                                email = '{lista[3]}', 
                                fone = '{lista[4]}', 
                                endereco = '{lista[5]}', 
                                cidade = '{lista[6]}' 
                                WHERE id = {lista[0]}
                                """)
            self.conn.commit()
            return True
            
        except Exception as error:
            print(error)
        finally:
            self.close_connection()           
    
    def update_product(self,lista):
        self.connect()
        try:
            self.cursor.execute(f"""UPDATE produto
                                SET nome = '{lista[1]}',
                                marca = '{lista[2]}',
                                modelo = '{lista[3]}',
                                descricao = '{lista[4]}',
                                preco = '{lista[5]}',
                                tipo = '{lista[6]}',
                                tamanho = '{lista[7]}',
                                peso = '{lista[8]}' 
                                WHERE id = {lista[0]}
                                """)
            self.conn.commit()
            return True
            
        except Exception as error:
            print(error)
        finally:
            self.close_connection()           
    
    def delete_client(self,id):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM pessoa WHERE id = {id}")
            self.conn.commit()
            return True
        
        except Exception as error:
            print(error)
        finally:
            self.close_connection()       

    def delete_product(self,id):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM produto WHERE id = {id}")
            self.conn.commit()
            return True

        except Exception as error:
            print(error)
        finally:
            self.close_connection()           

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
    #db.delete_product(5)
    #db.update_client(2)
    #db.update_product(2)
    #db.close_connection()                            


