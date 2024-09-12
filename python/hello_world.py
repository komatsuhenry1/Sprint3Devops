import mysql.connector

# Conexão com o banco de dados
connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port="3306", database='AiCommerceTables'
)
print("DB conectado!")

cursor = connection.cursor()

# Função para inserir cliente se não existir
def insert_cliente_if_not_exists(cliente):
    check_cliente_query = '''
    SELECT COUNT(*) FROM cliente WHERE id_clie = %s
    '''
    cursor.execute(check_cliente_query, (cliente[0],))
    exists = cursor.fetchone()[0] > 0
    if not exists:
        insert_cliente_query = '''
        INSERT INTO cliente(id_clie, nm_clie, email_clie, endereco_clie, senha_clie)
        VALUES (%s, %s, %s, %s, %s)
        '''
        cursor.execute(insert_cliente_query, cliente)
        print(f"Cliente {cliente[1]} inserido com sucesso!")
    else:
        print(f"Cliente com id {cliente[0]} já existe.")

# Inserção de dados na tabela cliente
cliente_values = [
    (6, 'Lucas Martins', 'lucas.martins@example.com', 'Rua Nova, 789', 'senha987'),
    (7, 'Fernanda Alves', 'fernanda.alves@example.com', 'Avenida Velha, 456', 'senha654')
]
for values in cliente_values:
    insert_cliente_if_not_exists(values)

# Inserção de dados na tabela pedido
insert_pedido_query = '''
INSERT INTO pedido(id_pedido, dt_pedido, status_pedido, preco_total, id_clie)
VALUES (%s, %s, %s, %s, %s)
'''
pedido_values = [
    (6, '2024-06-01', 'Em andamento', 320.00, 6), 
    (7, '2024-07-15', 'Concluído', 150.00, 7)    
]
for values in pedido_values:
    cursor.execute(insert_pedido_query, values)
print("Dados inseridos na tabela pedido com sucesso!")

# Commit para salvar as inserções
connection.commit()

# Atualização de um registro na tabela cliente
update_cliente_query = '''
UPDATE cliente SET email_clie = %s WHERE id_clie = %s
'''
cursor.execute(update_cliente_query, ('lucas.updated@example.com', 6))
print("Registro atualizado na tabela cliente com sucesso!")

# Atualização de um registro na tabela pedido
update_pedido_query = '''
UPDATE pedido SET status_pedido = %s WHERE id_pedido = %s
'''
cursor.execute(update_pedido_query, ('Concluído', 6))
print("Registro atualizado na tabela pedido com sucesso!")

# Deletando todos os registros na tabela pedido relacionados ao cliente
delete_pedido_query = '''
DELETE FROM pedido WHERE id_clie = %s
'''
cursor.execute(delete_pedido_query, (7,))  # Deletar pedidos do cliente com id_clie = 7
print("Registros deletados da tabela pedido com sucesso!")

# Deletando um registro na tabela cliente
delete_cliente_query = '''
DELETE FROM cliente WHERE id_clie = %s
'''
cursor.execute(delete_cliente_query, (7,))
print("Registro deletado da tabela cliente com sucesso!")

# Commit para salvar as atualizações e deleções
connection.commit()

# Leitura final para verificar as atualizações
cursor.execute('SELECT * FROM cliente')
clientes = cursor.fetchall()
print("Clientes após update/delete:", clientes)

cursor.execute('SELECT * FROM pedido')
pedidos = cursor.fetchall()
print("Pedidos após update/delete:", pedidos)

# Leitura de dados das tabelas cliente e pedido
cursor.execute('SELECT * FROM cliente')
clientes = cursor.fetchall()
print("Clientes:", clientes)

cursor.execute('SELECT * FROM pedido')
pedidos = cursor.fetchall()
print("Pedidos:", pedidos)

# Fechando a conexão
connection.close()
