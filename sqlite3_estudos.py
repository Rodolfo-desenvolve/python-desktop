# biblioteca
import sqlite3

# criar um banco de dados
conexao = sqlite3.connect('banco_dados')

# Apontar para o banco
cursor = conexao.cursor()

# criando uma tabela
# cursor.execute(
#     'CREATE TABLE minha_tabela (data text, nome text, idade int)'
# )

# Fazer um commit
conexao.commit()

# inserindo valores
cursor.execute('INSERT INTO minha_tabela VALUES ("01/01/2021", "Rodolfo", "20")')

cursor.execute('INSERT INTO minha_tabela VALUES ("13/07/2002", "Gustavo", "30")')

# import números aleatorios
from random import randint

# loop
for loop in range(10):
    # gerando um número aleatorio
    numero = randint(18, 35)

    # inserir informações na minha tabela
    cursor.execute(f'INSERT INTO minha_tabela VALUES ("03/05/2005", "Lucaco", {numero})')

# consulta tabela - todas as colunas
# consulta = cursor.execute('SELECT * FROM minha_tabela').fetchall()

# consulta tabela - colunas especificas
# consulta = cursor.execute('SELECT nome, idade FROM minha_tabela').fetchall()

# querry usando o igual '='
# consulta = cursor.execute(
#     '''
#     SELECT * FROM minha_tabela
#     WHERE idade = '30'
#     '''
# ).fetchall()

# querry usando o diferente '<>'
# consulta = cursor.execute(
#     '''
#     SELECT * FROM minha_tabela
#     WHERE nome <> 'Lucaco'
#     '''
# ).fetchall()

# querry usando o diferente 'BETWEEN'
# consulta = cursor.execute(
#     '''
#     SELECT * FROM minha_tabela
#     WHERE idade BETWEEN 15 and 20
#     '''
# ).fetchall()

# querry algo que comece.
# consulta = cursor.execute(
#     '''
#     SELECT * FROM minha_tabela
#     WHERE nome LIKE 'o%'
#     '''
# ).fetchall()

# querry algo que termine
# consulta = cursor.execute(
#     '''
#     SELECT * FROM minha_tabela
#     WHERE nome LIKE '%o'
#     '''
# ).fetchall()

# querry procurando algo com o in
# consulta = cursor.execute(
#     '''
#     SELECT * FROM minha_tabela
#     WHERE nome in ('Rodolfo')
#     '''
# ).fetchall()

# AND
# consulta = cursor.execute(
#     '''
#     SELECT * FROM minha_tabela
#     WHERE idade = 20 AND nome = 'Rodolfo'
#     '''
# ).fetchall()

#  OR
# consulta = cursor.execute(
#     '''
#     SELECT * FROM minha_tabela
#     WHERE idade = 15 OR nome = 'Rodolfo'
#     '''
# ).fetchall()

# NOT
# consulta = cursor.execute(
#     '''
#     SELECT * FROM minha_tabela
#     WHERE nome = 'Rodolfo' AND (idade > 25 OR idade < 35) AND NOT idade = 30
#     '''
# ).fetchall()

# ordenar valores em ordem crescente
# consulta = cursor.execute(
#     '''
#     SELECT * FROM minha_tabela
#     ORDER BY idade
#     '''
# ).fetchall()

# ordenar valores em ordem decrescente
# consulta = cursor.execute(
#     '''
#     SELECT * FROM minha_tabela
#     ORDER BY idade DESC
#     '''
# ).fetchall()

# preenchedo valores nulos
cursor.execute('INSERT INTO minha_tabela VALUES ("ABC", null, "30")')
cursor.execute('INSERT INTO minha_tabela VALUES ("Lucas", null, "20")')


# verificando valores nulos
# consulta = cursor.execute(
#     '''
#     SELECT * FROM minha_tabela
#     WHERE nome IS NULL
#     '''
# ).fetchall()

# verificando valores não nulos
# consulta = cursor.execute(
#     '''
#     SELECT * FROM minha_tabela
#     WHERE nome IS NOT NULL
#     '''
# ).fetchall()

# dando update em valores nulos
# consulta = cursor.execute(
#     '''
#     UPDATE minha_tabela
#     SET nome = 'PREENCHIDO'
#     WHERE nome IS NULL
#     '''
# ).fetchall()

# querry deletar valores
# consulta = cursor.execute(
#     '''
#     DELETE FROM minha_tabela
#     '''
# ).fetchall()

# querry para limitar a quandidade de informações
# consulta = cursor.execute(
#     '''
#     SELECT * FROM minha_tabela
#     LIMIT 6
#     '''
# ).fetchall()

# querry para retorna o menor valor
# consulta = cursor.execute(
#     '''
#     SELECT  MIN (idade) FROM minha_tabela
#     '''
# ).fetchall()

# querry para retornar o maior valor
# consulta = cursor.execute(
#     '''
#     SELECT MAX (idade) FROM minha_tabela
#     '''
# ).fetchall()

# querry SUM = soma AVG = MÉDIA COUNT= contar valores
# consulta = cursor.execute(
#     '''
#     SELECT SUM (idade) FROM minha_tabela
#     '''
# ).fetchall()

# renomea o nome tabela temporariamente
# consulta = cursor.execute(
#     '''
#     SELECT idade as consulta_01 FROM minha_tabela
#     '''
# ).fetchall()


#-----------------------------
# criar tabela tab_vendas
# consulta = cursor.execute(
#     '''
#     CREATE TABLE tab_vendas (id, valor)
#     '''
# )
#
# conexao.commit()
#

# criar tabela tab_cadastro
# consulta = cursor.execute(
#     '''
#     CREATE TABLE tab_cadastro (id, nome)
#     '''
# )
#
# conexao.commit()
#
# cadastrando vendas dos vendedores

# cursor.execute('INSERT INTO tab_vendas VALUES (1, 150)')
# cursor.execute('INSERT INTO tab_vendas VALUES (1, 200)')
# cursor.execute('INSERT INTO tab_vendas VALUES (1, 300)')
#
# cursor.execute('INSERT INTO tab_vendas VALUES (2, 50)')
# cursor.execute('INSERT INTO tab_vendas VALUES (2, 150)')
# cursor.execute('INSERT INTO tab_vendas VALUES (2, 200)')
#

# cadastrando vendedores
# cursor.execute('INSERT INTO tab_cadastro VALUES (1, "Rodolfo silva")')
# cursor.execute('INSERT INTO tab_cadastro VALUES (2, "Lucas villela")')

# cadastrando vendas dos vendedores.
# cursor.execute('INSERT INTO tab_vendas VALUES (3, 999)')

# exibir as tabela em conjuntos com INNER JOIN
# consulta = cursor.execute(
#     '''
#     SELECT * FROM tab_vendas
#     INNER JOIN tab_cadastro
#     ON tab_vendas.id = tab_cadastro.id
#     '''
# ).fetchall()

# Exibir as tabelas em conjunto com LEFT JOIN
# consulta = cursor.execute(
#     '''
#     SELECT * FROM tab_vendas
#     LEFT JOIN tab_cadastro
#     ON tab_vendas.id = tab_cadastro.id
#     '''
# ).fetchall()

# criar tabela tabela_x

# cursor.execute('CREATE TABLE tabela_x (id, nome)')
# conexao.commit()
#

# criar tabela tabela_y
# cursor.execute('CREATE TABLE tabela_y (id, nome)')
# conexao.commit()
#

# cadastrando pessoas tabela_x
# cursor.execute('INSERT INTO tabela_x VALUES (1, "Maria")')
# cursor.execute('INSERT INTO tabela_x VALUES (2, "JOÃO")')
# cursor.execute('INSERT INTO tabela_x VALUES (3, "Rodolfo")')
#
# cadastrando pessoas tabela_y
# cursor.execute('INSERT INTO tabela_y VALUES (1, "Rosana")')
# cursor.execute('INSERT INTO tabela_y VALUES (2, "Rodrigo")')
# cursor.execute('INSERT INTO tabela_y VALUES (3, "Gustavo")')
#
#

# Unidando as tabelas tabela_x e tabela_y
# consulta = cursor.execute(
#     '''
#     SELECT * FROM tabela_x
#     UNION ALL
#     SELECT * FROM tabela_y
#     '''
# ).fetchall()


# consulta = cursor.execute(
#     '''
#     -- usado para comentar no codigo
#     SELECT nome ,MAX (idade) FROM minha_tabela
#     GROUP BY nome
#     '''
# ).fetchall()

consulta = cursor.execute(
    '''
    SELECT * FROM minha_tabela
    '''
).fetchall()
for linha in consulta:
    print(linha)