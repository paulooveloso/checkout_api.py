from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/checkout', methods=['POST'])
def calcular_venda():
    """
    Sistema de Checkout - Paulo iPhones
    Processa vendas, descontos e parcelamentos.
    """
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados da venda nao informados"}), 400

    # 'a' representa o valor principal (iPhone)
    # 'b' representa o modificador (Acessorio, Desconto ou Parcelas)
    a = dados.get('a')
    b = dados.get('b')
    operacao = dados.get('operacao')

    # Validação profissional: garante que os valores sejam números
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return jsonify({"erro": "Os valores 'a' e 'b' precisam ser numericos"}), 400
    
    resultado = 0
    
    if operacao == 'soma':
        # Venda Casada: iPhone + Acessório
        resultado = a + b
    elif operacao == 'subtracao':
        # Trade-in: Valor do Novo - Avaliação do Usado
        resultado = a - b
    elif operacao == 'multiplicacao':
        # Atacado: Preço Unitário * Quantidade
        resultado = a * b
    elif operacao == 'divisao':
        # Parcelamento: Total / Vezes no Cartão
        if b == 0:
            return jsonify({"erro": "O numero de parcelas nao pode ser zero"}), 400
        resultado = a / b
    else:
        return jsonify({"erro": "Operacao de venda invalida"}), 400

    # Retorno estruturado 
    return jsonify({
        "loja": "Paulo iPhones",
        "a": a,
        "b": b,
        "operacao": operacao,
        "resultado": round(resultado, 2)
    }), 200

if __name__ == '__main__':
    app.run(debug=True)