from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

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

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(14), nullable=False)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    quant_estoque = db.Column(db.Integer, nullable=False)

@app.route('/checkout', methods=['POST'])
def calcular_venda():
    dados = request.get_json()
    
    if not dados or 'a' not in dados or 'b' not in dados or 'operacao' not in dados:
        return jsonify({"erro": "Dados da venda (a, b, operacao) nao informados corretamente"}), 400

    a = float(dados.get('a'))
    b = float(dados.get('b'))
    operacao = dados.get('operacao')

    if operacao == 'soma':
        resultado = a + b
    elif operacao == 'subtracao':
        resultado = a - b
    elif operacao == 'multiplicacao':
        resultado = a * b
    elif operacao == 'divisao':
        if b == 0:
            return jsonify({"erro": "O numero de parcelas nao pode ser zero"}), 400
        resultado = a / b
    else:
        return jsonify({"erro": "Operacao de venda invalida"}), 400

    nova_venda = Venda(produto="iPhone+acessorio", val_tot=resultado, quant=int(b) if operacao == 'multiplicacao' else 1)
    db.session.add(nova_venda)
    db.session.commit()

    return jsonify({
        "loja": "Paulo iPhones",
        "a": a,
        "b": b,
        "operacao": operacao,
        "resultado": round(resultado, 2)
    }), 200

@app.route('/vendas', methods=['GET'])
def listar_vendas():
    vendas = Venda.query.all()
    return jsonify([{"id":v.id, "produto":v.produto, "total":v.val_tot, "quant":v.quant} for v in vendas])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print(f" Banco criado: {db_path}")
    app.run(debug=True, port=5001)
