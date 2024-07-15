import mariadb
import sys

class UsuarioModel:
    def __init__(self, db_name='marcio_db', user='marcio_2182', password='2182', host='localhost', port=3306):
        try:
            self.conn = mariadb.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=db_name
            )
        except mariadb.Error as e:
            print(f"Erro de conexão ao MariaDB: {e}")
            sys.exit(1)
       
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                idade INT
            )
        ''')
        self.conn.commit()

    def inserir_usuario(self, nome, idade):
        cursor = self.conn.cursor()
        try:
            cursor.execute('INSERT INTO usuarios (nome, idade) VALUES (?, ?)', (nome, idade))
            self.conn.commit()
        except mariadb.Error as e:
            print(f"Erro ao inserir usuário: {e}")

#---------------------------------------------------------------------------------------
    #Função para Deletar um usuario
    def apagar_usuario(self, id):
        cursor = self.conn.cursor()
        try:
            cursor.execute(f'''
            DELETE FROM usuarios
            WHERE id = {id}
            ''')
            print(f'deletado: ')
            self.conn.commit()
        except mariadb.Error as e:
            print(f'Erro ao deletar usuario: {e}')

    #função para atualizar os dados do usuario
    def atualizar_dados_usuarios(self, id, nome, idade):
        cursor = self.conn.cursor()
        try:
            cursor.execute(f'''
            UPDATE usuarios 
            SET nome = ?, idade = ? 
            WHERE id = ?
            ''',(nome, idade, id))
            print(f'atualizado')
            self.conn.commit()
        except mariadb.Error as e:
            print(f'Erro ao atualizar dados do usuario: {e}')

#------------------------------------------------------------------------------------------

    def selecionar_usuarios(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM usuarios')
        return cursor.fetchall()

    def fechar_conexao(self):
        self.conn.close()




