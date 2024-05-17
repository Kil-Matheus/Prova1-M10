# Prova1-M10

# Como rodar

- docker compose up

- acessar o insomnia e ver as rotas

- testar cada uma, localhost 5000

# Diretórios

Foram criados 2 diretórios:

db = configurações do banco de dados com o dockerfile e o init.sql

app = aplicação em Flask assync, com os requerements e o dockerfile

# Rotas

/novo = Pega um os dados do jsons e faz um insert no banco, o retorno é o id que gerou

/pedidos = Pega todos os registros que tem no banco

/pedidos/id = Em get, retorna os pedidos de um id específico, delete deleta os pedidos do id específico e em post necessita de um json com o id e com a nova descrição para atualizar a descrição de um id específico.