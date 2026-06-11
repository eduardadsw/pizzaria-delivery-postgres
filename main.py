import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def conectar_banco():
    URL_CONEXAO = os.getenv("DATABASE_URL")

    return psycopg2.connect(URL_CONEXAO)
def listar_cardapio():
    try:
        conexao = conectar_banco()
        cursor= conexao.cursor()
        cursor.execute("SELECT id, sabor, descricao, preco FROM pizzas ORDER BY id")
        pizzas = cursor.fetchall()

        print('\n== CARDÁPIO DE PIZZAS 🍕 ==')

        for pizza in pizzas:
            print(f'[{pizza[0]}] Pizza de {pizza[1]}')
            print(f'Ingredientes: {pizza[2]}')
            print(f'Preço: R$ {pizza[3]:.2f}\n')

        cursor.close()
        conexao.close()

        return pizzas
    except Exception as erro:
        print(f'Opa deu algo errado! Motivo: {erro}')
        return []

def fazer_pedido(pizzas_carregadas):
    try:
        print('== Digite seus dados para o Delivery 📝 ==')
        id_pizza = int(input('ID da Pizza desejada: '))

        ids_validos = [p[0] for p in pizzas_carregadas]
        if id_pizza not in ids_validos:
            print('Opção de pizza inválida ❌')
            return
        nome = str(input('Insira seu nome: ')).strip()
        telefone = str(input('Telefone: ')).strip()
        endereco = str(input('Endereço: ')).strip()
        pagamento = str(input('Forma de pagamento (Cartão/PIX/Dinheiro): ')).strip()
        conexao = conectar_banco()
        cursor = conexao.cursor()

        comando_insert = """
        INSERT INTO pedido(nome_cliente, telefone, endereco, pagamento, id_pizza)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(comando_insert, (nome, telefone, endereco, pagamento, id_pizza))
        conexao.commit()

        print(f'Perfeito, {nome}! O seu pedido foi enviado com sucesso! ✅')

        cursor.close()
        conexao.close()

    except ValueError:
        print('Erro: Por favor insira um número válido para o ID da pizza ❌')
    except Exception as erro:
        print(f'Erro: Por favor insira um número válido para o ID da pizza ❌')

def listar_pedidos_recebidos():
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        comando_select= """
        SELECT ped.id, ped.nome_cliente, ped.telefone, ped.endereco, ped.pagamento, piz.sabor, piz.descricao, ped,data_pedido
        FROM pedido ped
        JOIN pizzas piz ON ped.id_pizza = piz.id
        ORDER BY ped.data_pedido
        """

        cursor.execute(comando_select)
        pedidos = cursor.fetchall()

        print('== PEDIDOS RECEBIDOS NO BANCO ONLINE 🛵==')

        if not pedidos:
            print('Erro inesperado ao salvar pedido: {erro} ❌')

        for p in pedidos:

            print(f"Pedido #{p[0]} - [{p[6]}")
            print(f"👤 Cliente: {p[1]} | 📞 Tel: {p[2]}")
            print(f"🍕 Pizza escolhida: {p[5]}")
            print(f"📍 Endereço: {p[3]}")
            print(f"💳 Pagamento: {p[4]}")
            print("-" * 45)

        cursor.close()
        conexao.close()

    except Exception as erro:
        print(f'❌ Erro ao buscar lista de pedidos: {erro}')


while True:
    print('==============PIZZARIA DELIVERY 🍕✨==============')
    opcao = str(input("""Como podemos te ajudar hoje?
1. Fazer pedido.
2. Ver lista de pedidos.
3. Apenas consultar cardápio
4. Sair
Sua escolha (numero): """)).strip().upper()

    if opcao in '1':
        pizzas_carregadas = listar_cardapio()
        print('2. Iniciando a função de fazer pedido...')
        fazer_pedido(pizzas_carregadas)

    elif opcao in '2':
        print("Iniciando a função de listar pedidos recebidos...")
        listar_pedidos_recebidos()

    elif opcao in '3':
        print('1. Buscando o cardápio no servidor...')
        pizzas_carregadas = listar_cardapio()

    elif opcao in '4':
        print('-' * 10)
        print('Saindo...Volte sempre!')
        print('-' * 10)
        break

    else:
        print('-'*10)
        print('Opção inválida, tente novamente!')
        print('-'*10)









