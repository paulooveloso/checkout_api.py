Projeto RAD: API de Checkout Paulo iPhones
Este repositório contém o desenvolvimento de uma API para processamento de vendas e cálculos financeiros da loja Paulo iPhones. O projeto foi construído utilizando Python e o framework Flask, seguindo os princípios de Desenvolvimento Rápido de Aplicações (RAD).



Descrição do Sistema
A aplicação funciona como um motor de cálculos para o checkout da loja. Ela recebe dados via requisição POST no formato JSON, contendo os valores 'a', 'b' e a 'operacao' desejada.


As operações foram mapeadas para situações reais de negócio:

Soma: Cálculo de venda casada (Aparelho + Acessório).

Subtração: Modalidade Trade-in (Valor do novo - Avaliação do usado).

Multiplicação: Cálculo de custo para reposição de estoque (Preço unitário * Quantidade).

Divisão: Simulação de parcelamento para o cliente (Valor total / Parcelas).

Requisitos e Execução
Para rodar o projeto localmente, é necessário ter o Python instalado e seguir os passos abaixo:

Instalação da biblioteca necessária:

pip install flask 


Execução do servidor:
python3 paulo_iphones_api.py

O serviço ficará disponível em http://127.0.0.1:5000/checkout.

Respostas ao Desafio Acadêmico
O que foi feito de forma profissional? 
O código não se limita a uma calculadora simples; ele valida se os dados recebidos são numéricos e utiliza tratamentos de erro para evitar que o servidor pare de funcionar (como proteção contra divisão por zero). Além disso, a API utiliza códigos de status HTTP apropriados, como o 400 (Bad Request) para entradas inválidas, garantindo uma comunicação padronizada com o cliente.


Como o protótipo pode ser melhorado? Uma evolução natural seria a implementação de um banco de dados SQLite para persistir o histórico de vendas realizadas. Também seria viável a criação de uma interface visual utilizando Streamlit para facilitar o uso pelos vendedores da loja, além de adicionar camadas de autenticação para proteger os dados financeiros.