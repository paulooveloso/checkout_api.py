from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db_path = os.path.join(os.path.dirname(__file__), 'checkout_api.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db = SQLAlchemy(app)

class Venda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto = db.Column(db.String(100), nullable=False)
    val_tot = db.Column(db.Float, nullable=False)
    quant = db.Column(db.Integer, nullable=False)
    data = db.Column(db.DateTime, default=datetime.now)

@app.route('/checkout', methods=['POST'])
def calcular_venda():
    dados = request.get_json()
    
    if not dados or 'a' not in dados or 'b' not in dados or 'operacao' not in dados:
        return jsonify({"erro": "Dados da venda (a, b, operacao) nao informados corretamente"}), 400

    a = float(dados.get('a'))
    b = float(dados.get('b'))
    operacao = dados.get('operacao')

    if operacao == 'venda_casada':
        resultado = a + b
    elif operacao == 'troca_usado':
        resultado = a - b
    elif operacao == 'atacado':
        resultado = a * b
    elif operacao == 'parcelamento':
        if b == 0:
            return jsonify({"erro": "O numero de parcelas nao pode ser zero"}), 400
        resultado = a / b
    else:
        return jsonify({"erro": "Operacao de venda invalida"}), 400

    nova_venda = Venda(produto=operacao, val_tot=resultado, quant=int(b) if operacao == 'atacado' else 1)
    db.session.add(nova_venda)
    db.session.commit()

    return jsonify({
        "loja": "Paulo iPhones",
        "a": a,
        "b": b,
        "operacao": operacao,
        "resultado": round(resultado, 2)
    }), 201

@app.route('/vendas', methods=['GET'])
def listar_vendas():
    vendas = Venda.query.all()
    return jsonify([{
        "id": v.id,
        "produto": v.produto, 
        "total": v.val_tot,
        "quant": v.quant,
        "data_hora": v.data.strftime('%d/%m/%y %H:%M:%S')
    } for v in vendas]), 200

@app.route('/vendas/<int:id>', methods=['GET'])
def ver_indiv(id):
    venda = Venda.query.get(id)
    if venda:
        return jsonify({
            "id": venda.id,
            "produto": venda.produto,
            "total": venda.val_tot,
            "quant": venda.quant,
            "data_hora": venda.data.strftime('%d/%m/%y %H:%M:%S')
        }), 200
    
    return jsonify({"erro": "Venda não encontrada"}), 404

@app.route('/vendas/<int:id>', methods=['PUT'])
def atualizar_venda(id):
    venda = Venda.query.get(id)
    if not venda:
        return jsonify({"erro": "Venda não encontrada"}), 404
    
    dados = request.get_json()
    
    try:
        if 'produto' in dados:
            venda.produto = dados['produto']
        if 'val_tot' in dados:
            venda.val_tot = float(dados['val_tot'])
        if 'quant' in dados:
            venda.quant = int(dados['quant'])
            
        db.session.commit()
        return jsonify({"mensagem": f"Venda {id} atualizada com sucesso!"}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": "Erro ao atualizar a venda", "detalhes": str(e)}), 500

@app.route('/vendas/<int:id>', methods=['DELETE'])
def excluir_venda(id):
    venda = Venda.query.get(id)
    if not venda:
        return jsonify({"erro": "Venda não encontrada"}), 404
    try:
        db.session.delete(venda)
        db.session.commit()
        return jsonify({"mensagem": f"Venda {id} excluida com sucesso!"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": "Erro ao excluir a venda", "detalhes": str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print(f"Banco criado: {db_path}")
    app.run(debug=True, port=5001)