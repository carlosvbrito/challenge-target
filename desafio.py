import random
from datetime import datetime

# ======================================================
# BASES DE DADOS (SIMULADO)
# ======================================================

vendas_json = {
  "vendas": [
    { "vendedor": "João Silva", "valor": 1200.50 },
    { "vendedor": "João Silva", "valor": 950.75 },
    { "vendedor": "João Silva", "valor": 1800.00 },
    { "vendedor": "João Silva", "valor": 1400.30 },
    { "vendedor": "João Silva", "valor": 1100.90 },
    { "vendedor": "João Silva", "valor": 1550.00 },
    { "vendedor": "João Silva", "valor": 1700.80 },
    { "vendedor": "João Silva", "valor": 250.30 },
    { "vendedor": "João Silva", "valor": 480.75 },
    { "vendedor": "João Silva", "valor": 320.40 },

    { "vendedor": "Maria Souza", "valor": 2100.40 },
    { "vendedor": "Maria Souza", "valor": 1350.60 },
    { "vendedor": "Maria Souza", "valor": 950.20 },
    { "vendedor": "Maria Souza", "valor": 1600.75 },
    { "vendedor": "Maria Souza", "valor": 1750.00 },
    { "vendedor": "Maria Souza", "valor": 1450.90 },
    { "vendedor": "Maria Souza", "valor": 400.50 },
    { "vendedor": "Maria Souza", "valor": 180.20 },
    { "vendedor": "Maria Souza", "valor": 90.75 },

    { "vendedor": "Carlos Oliveira", "valor": 800.50 },
    { "vendedor": "Carlos Oliveira", "valor": 1200.00 },
    { "vendedor": "Carlos Oliveira", "valor": 1950.30 },
    { "vendedor": "Carlos Oliveira", "valor": 1750.80 },
    { "vendedor": "Carlos Oliveira", "valor": 1300.60 },
    { "vendedor": "Carlos Oliveira", "valor": 300.40 },
    { "vendedor": "Carlos Oliveira", "valor": 500.00 },
    { "vendedor": "Carlos Oliveira", "valor": 125.75 },

    { "vendedor": "Ana Lima", "valor": 1000.00 },
    { "vendedor": "Ana Lima", "valor": 1100.50 },
    { "vendedor": "Ana Lima", "valor": 1250.75 },
    { "vendedor": "Ana Lima", "valor": 1400.20 },
    { "vendedor": "Ana Lima", "valor": 1550.90 },
    { "vendedor": "Ana Lima", "valor": 1650.00 },
    { "vendedor": "Ana Lima", "valor": 75.30 },
    { "vendedor": "Ana Lima", "valor": 420.90 },
    { "vendedor": "Ana Lima", "valor": 315.40 }
  ]
}

estoque_json = [
  { "codigoProduto": 101, "descricaoProduto": "Caneta Azul", "estoque": 150 },
  { "codigoProduto": 102, "descricaoProduto": "Caderno Universitário", "estoque": 75 },
  { "codigoProduto": 103, "descricaoProduto": "Borracha Branca", "estoque": 200 },
  { "codigoProduto": 104, "descricaoProduto": "Lápis Preto HB", "estoque": 320 },
  { "codigoProduto": 105, "descricaoProduto": "Marcador de Texto Amarelo", "estoque": 90 }
]

movimento_json = [ 
    { "codigoMovimento": 1, "codigoProduto": 100, "tipoMovimento": "Inicial", "quantidade": 0 , "data": "02/12/2025" },
]


# ======================================================
# CALCULAR COMISSÕES
# ======================================================
def calcular_comissoes():
    comissoes = {}

    for venda in vendas_json["vendas"]:
        vendedor = venda["vendedor"]
        valor = venda["valor"]

        if valor < 100:
            comissao = 0
        elif valor < 500:
            comissao = valor * 0.01
        else:
            comissao = valor * 0.05

        comissoes[vendedor] = comissoes.get(vendedor, 0) + comissao

    print("\n===== COMISSÕES =====")
    for vendedor, total in comissoes.items():
        print(f"{vendedor}: R$ {total:.2f}")
    print("=====================\n")
    print("Pressione uma tecla...")
    input()


# ======================================================
# MOVIMENTAÇÃO DE ESTOQUE
# ======================================================
def movimentar_estoque():
    print("\n=== Produtos ===")
    for p in estoque_json:
        print(f"{p['codigoProduto']} - {p['descricaoProduto']} | Estoque: {p['estoque']}")

    codigo = int(input("\nDigite o código do produto:\n"))
    quantidade = int(input("Digite a quantidade (use negativo (-) para saída): "))
   
    tipo = "ENTRADA"
    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    for produto in estoque_json:
        if produto["codigoProduto"] == codigo:
            movimento_id = int(random.randint(1, 1000))
            produto["estoque"] += quantidade
            if (quantidade < 0):
                tipo = "SAÍDA"

            print("\n=== MOVIMENTAÇÃO REGISTRADA ===")
            print("ID:", movimento_id)
            print("Produto:", produto["descricaoProduto"])
            print("Descrição do movimento:", tipo)
            print("Estoque final:", produto["estoque"])
            print("===============================\n")

            inserirMovimento(movimento_id, codigo, tipo, quantidade, data)


            print("Pressione uma tecla...")
            input()
            return

    print("❌ Produto não encontrado!\n")
    print("Pressione uma tecla...")
    input()

def getMovimento():
    codigo = int(input("\nDigite o código do movimento:\n"))
    for mov in movimento_json:
        if mov["codigoMovimento"] == codigo:
            # data = datetime.strptime(mov['data'], "%d/%m/%Y %H:%M:%S")
            print(f"Código Movimento: {mov['codigoMovimento']} - Código Produto: {mov['codigoProduto']} - Tipo: {mov['tipoMovimento']} - Quantidade: {mov['quantidade']} - Data: {mov['data']}")
            print("Pressione uma tecla...")
            input()
            return
    print("❌ Movimento não encontrado!\n")
    print("Pressione uma tecla...")
    input()

def inserirMovimento(codigoMovimento, codigoProduto, tipo, quantidade, data):

    newMovimento = { 
        "codigoMovimento": codigoMovimento, 
        "codigoProduto": codigoProduto,
        "tipoMovimento": tipo, 
        "quantidade": quantidade , 
        "data": data
    }
    movimento_json.append(newMovimento)


# ======================================================
# CALCULAR JUROS DE ATRASO
# ======================================================
def calcular_juros():
    valor = float(input("Digite o valor: R$ "))
    data_venc = input("Digite a data de vencimento (dd/mm/aaaa): ")

    hoje = datetime.now()
    venc = datetime.strptime(data_venc, "%d/%m/%Y")

    if hoje <= venc:
        print("\nSem juros. Ainda não venceu.\n")
        return

    dias = (hoje - venc).days
    juros = valor * 0.025 * dias

    print("\n===== Juros =====")
    print("Dias de atraso:", dias)
    print(f"Juros acumulados: R$ {juros:.2f}")
    print("=================\n")
    print("Pressione uma tecla...")
    input()


# ======================================================
# MENU PRINCIPAL
# ======================================================
def menu():
    while True:
        print("===== MENU PRINCIPAL =====")
        print("1 - Calcular comissão de vendedores")
        print("2 - Movimentar estoque")
        print("3 - Calcular juros por atraso")
        print("4 - Consultar Movimento")
        print("0 - Sair")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            calcular_comissoes()
        elif opc == "2":
            movimentar_estoque()
        elif opc == "3":
            calcular_juros()
        elif opc == "4":
            getMovimento()
        elif opc == "0":
            print("\nSaindo...")
            break
        else:
            print("❌ Opção inválida!\n")


# Iniciar o programa
menu()

