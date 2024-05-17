from flask import Flask, jsonify, request, make_response, redirect
import asyncpg
import asyncio
app = Flask(__name__)

async def get_db_connection():
    return await asyncpg.connect(
        database="postgres",
        user="postgres",
        password="postgres",
        host="db",
        port=5432
    )

async def test_db_connection():
    conn = await get_db_connection()
    if conn:
        print("Conectado ao banco de dados com sucesso!")
    await conn.close()

@app.route('/novo', methods=['POST'])
async def banco_insert():
    data = request.json
    nome = data.get('nome')
    email = data.get('email')
    desc = data.get('descricao')

    try:
        conn = await get_db_connection()
        resposta = await conn.execute('INSERT INTO pedido (nome, email, descricao) VALUES ($1, $2, $3)', nome, email, desc)
        if resposta == 'INSERT 0 1':
            id = await conn.fetchval('SELECT id FROM pedido WHERE nome = $1', nome)
            return jsonify({'id': id})
        else:
            return make_response('Erro ao inserir', 400)
    finally:
        await conn.close()

@app.route('/pedidos', methods=['GET'])
async def banco_delete():
    try:
        conn = await get_db_connection()
        resposta = await conn.fetch('SELECT * FROM pedido')
        resposta = [{'id': i[0], 'nome': i[1], 'email': i[2], 'descricao': i[3]} for i in resposta]
        return jsonify(resposta)
    finally:
        await conn.close()

@app.route('/pedidos/<int:id>', methods=['GET', 'DELETE', 'POST'])
async def banco_select(id):
    if request.method == 'POST':
        data = request.json
        desc = data.get('descricao')
        try:
            conn = await get_db_connection()
            resposta = await conn.execute('UPDATE pedido SET descricao = $1 WHERE id = $2', desc, id)
            if resposta == 'UPDATE 1':
                return make_response('Pedido atualizado com sucesso', 200)
            else:
                return make_response('Erro ao atualizar', 400)
        finally:
            await conn.close()
    if request.method == 'DELETE':
        try:
            conn = await get_db_connection()
            resposta = await conn.execute('DELETE FROM pedido WHERE id = $1', id)
            if resposta == 'DELETE 1':
                return make_response('Pedido deletado com sucesso', 200)
            else:
                return make_response('Erro ao deletar', 400)
        finally:
            await conn.close()
    try:
        conn = await get_db_connection()
        resposta = await conn.fetch('SELECT * FROM pedido WHERE id = $1', id)
        resposta = [{'id': i[0], 'nome': i[1], 'email': i[2], 'descricao': i[3]} for i in resposta]
        return jsonify(resposta)
    finally:
        await conn.close()



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_db_connection())
    app.run(host="0.0.0.0", port=5000, debug=True)