import random
import pandas as pd


def criar_planilha_grande_teste():
    # Lista base de produtos de restaurante/lanchonete
    produtos_base = [
        "Pizza Calabresa",
        "Pizza Quatro Queijos",
        "Pizza Portuguesa",
        "Pizza Frango com Catupiry",
        "Hambúrguer Artesanal",
        "X-Salada",
        "X-Bacon",
        "X-Tudo",
        "Refrigerante Lata",
        "Refrigerante 2L",
        "Suco Natural Laranja",
        "Suco Natural Maracujá",
        "Água Mineral",
        "Cerveja Long Neck",
        "Porção de Batata Frita",
        "Porção de Mandioca",
        "Porção de Calabresa",
        "Pudim de Leite",
        "Brownie com Sorvete",
        "Petit Gâteau",
    ]

    # Tabela de preços aproximados por produto
    precos_base = {
        "Pizza Calabresa": 45.0,
        "Pizza Quatro Queijos": 52.0,
        "Pizza Portuguesa": 48.0,
        "Pizza Frango com Catupiry": 50.0,
        "Hambúrguer Artesanal": 35.0,
        "X-Salada": 22.0,
        "X-Bacon": 26.0,
        "X-Tudo": 30.0,
        "Refrigerante Lata": 6.0,
        "Refrigerante 2L": 12.0,
        "Suco Natural Laranja": 10.0,
        "Suco Natural Maracujá": 10.0,
        "Água Mineral": 4.0,
        "Cerveja Long Neck": 9.0,
        "Porção de Batata Frita": 28.0,
        "Porção de Mandioca": 25.0,
        "Porção de Calabresa": 32.0,
        "Pudim de Leite": 12.0,
        "Brownie com Sorvete": 18.0,
        "Petit Gâteau": 22.0,
    }

    random.seed(42)  # Mantém a mesma geração aleatória para testes reproduzíveis

    produtos = []
    quantidades = []
    precos = []

    # Gera 40 linhas aleatórias
    for _ in range(40):
        prod = random.choice(produtos_base)
        qtd = random.randint(1, 10)
        prc = precos_base[prod]

        # Simula sujeira de texto (espaços antes ou depois do nome)
        if random.random() > 0.5:
            prod_sujo = f"  {prod} "
        else:
            prod_sujo = prod

        produtos.append(prod_sujo)
        quantidades.append(qtd)
        precos.append(prc)

    # Adiciona 10 duplicatas exatas para somar 50 linhas com "bagunça"
    for i in range(10):
        idx = random.randint(0, len(produtos) - 1)
        produtos.append(produtos[idx])
        quantidades.append(quantidades[idx])
        precos.append(precos[idx])

    dados_baguncados = {
        "Produto": produtos,
        "Quantidade": quantidades,
        "Preco_Unitario": precos,
    }

    df = pd.DataFrame(dados_baguncados)
    nome_arquivo = "vendas_baguncadas.xlsx"
    df.to_excel(nome_arquivo, index=False)

    print(f"✅ Planilha de teste com {len(df)} linhas gerada em: {nome_arquivo}")


if __name__ == "__main__":
    criar_planilha_grande_teste()