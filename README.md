# Projeto RAD: API de Checkout Paulo iPhones

Este repositório contém o desenvolvimento de uma **API CRUD completa** para processamento de vendas e cálculos financeiros da loja **Paulo iPhones**. O projeto foi construído utilizando **Python + Flask + SQLAlchemy + SQLite**, seguindo os princípios de Desenvolvimento Rápido de Aplicações (RAD).

## Funcionalidades Implementadas

### Operações de Negócio Real
| Operação | Cálculo | Exemplo Real |
|----------|---------|-------------|
| `venda_casada` | `a + b` | iPhone + Capa (4500 + 200) |
| `troca_usado` | `a - b` | Novo - Usado (4500 - 200) |
| `atacado` | `a * b` | Estoque (2000 * 10) |
| `parcelamento` | `a / b` | 12x (3600 / 12) |

### **Endpoints CRUD Completos**
```
POST    /checkout          → Criar venda + calcular
GET     /vendas            → Listar todas
GET     /vendas/:id        → Ver uma
PUT     /vendas/:id        → Atualizar
DELETE  /vendas/:id        → Excluir
```

## Instalação e Execução

### 1. Clonar e Ativar Ambiente Virtual
```bash
git clone https://github.com/pauloveloso/checkout-api.git
cd checkout-api
python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
# .venv\Scripts\activate    # Windows
2. Instalar Dependências:

### 2. Instalar Dependências
```bash
pip install flask flask-sqlalchemy
```

### 3. Rodar API
```bash
python checkout_api.py
```
```
Banco criado: checkout_api.db
* Running on http://127.0.0.1:5001
Testes Completos (curl)
**Terminal 1:** python checkout_api.py (deixe rodando)

**Terminal 2:**
```bash
# 1. CRIAR venda casada
curl -X POST http://127.0.0.1:5001/checkout -H "Content-Type: application/json" -d '{"a":4500,"b":200,"operacao":"venda_casada"}'

# 2. Listar vendas
curl http://127.0.0.1:5001/vendas

# 3. Ver ID 1
curl http://127.0.0.1:5001/vendas/1

# 4. ATUALIZAR ID 1
curl -X PUT http://127.0.0.1:5001/vendas/1 -H "Content-Type: application/json" -d '{"produto":"iPhone 16 Pro Max","val_tot":5200}'

# 5. Ver atualizado
curl http://127.0.0.1:5001/vendas/1

# 6. EXCLUIR
curl -X DELETE http://127.0.0.1:5001/vendas/1
```

## Estrutura do Banco (SQLite)
```
Tabela: venda
├── id (PK, auto)
├── produto (string)
├── val_tot (float)
├── quant (int)
└── data (datetime)
```

## **Respostas ao Desafio Acadêmico**

### O que foi feito profissional
- **CRUD completo** com banco SQLite persistente
- **Validação robusta** de entrada + tratamento de erros
- **HTTP Status Codes** corretos (201, 200, 400, 404, 500)
- **Persistência** com SQLAlchemy + histórico com timestamp
- **Operações semânticas** mapeadas para negócio real
- **GitHub profissional** com README técnico

### **Melhorias futuras**
- Interface **Streamlit** para vendedores
- **Autenticação JWT** para segurança
- **Deploy Heroku/Railway** com PostgreSQL
- **Testes unitários** com pytest
- **Docker** para portabilidade

## Alunos
**Paulo Henrique Veloso da Silva** - 202502195495
**Josef Lucas Sousa Campos** - 202502967969
***

