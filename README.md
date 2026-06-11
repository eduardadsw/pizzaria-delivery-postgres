Sistema Delivery - Pizzaria 🍕 (PostgreSQL em Nuvem)

Este é um sistema de Delivery de Pizzaria desenvolvido em Python focado em demonstrar a integração de aplicações locais com bancos de dados relacionais hospedados na nuvem.

Tecnologias Utilizadas
- **Python** (Lógica do sistema e menu interativo)
- **PostgreSQL** (Banco de dados relacional para persistência de dados)
- **Neon.tech** (Hospedagem serverless do banco de dados na nuvem)
- **Psycopg2** (Driver de conexão oficial do PostgreSQL para Python)
- **Python-dotenv** (Gerenciamento seguro de variáveis de ambiente)

Conceitos Aplicados
- **Chaves Estrangeiras (Foreign Keys):** Relacionamento estável entre a tabela de `pedido` e a tabela de `pizzas`.
- **SQL JOIN:** Cruzamento eficiente de tabelas para gerar relatórios detalhados para a administração da pizzaria.
- **Segurança da Informação:** Uso de placeholders `%s` contra ataques de *SQL Injection* e isolamento de credenciais por arquivo `.env`.

Configuração e Execução
1. Clone o repositório.
2. Instale as dependências necessárias:
   pip install psycopg2-binary python-dotenv