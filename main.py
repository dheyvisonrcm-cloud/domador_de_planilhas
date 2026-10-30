import glob
import os
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


def domar_qualquer_planilha():
    # Encontra todos os arquivos .xlsx na pasta (ignorando os já limpos)
    arquivos = [
        f
        for f in glob.glob("*.xlsx")
        if not f.endswith("_limpa.xlsx") and not f.startswith("~$")
    ]

    if not arquivos:
        print("⚠️ Nenhuma planilha Excel encontrada para processar.")
        return

    for caminho_entrada in arquivos:
        print(f"\n🔄 Processando: {caminho_entrada}...")

        # Nomes de saída dinâmicos
        nome_base = os.path.splitext(caminho_entrada)[0]
        caminho_excel_saida = f"{nome_base}_limpa.xlsx"
        caminho_pdf_saida = f"relatorio_{nome_base}.pdf"

        # 1. Leitura
        df = pd.read_excel(caminho_entrada)

        # 2. Limpeza Geral
        df_limpo = df.drop_duplicates()
        df_limpo.columns = [str(col).strip() for col in df_limpo.columns]

        # Limpar espaços de texto
        colunas_texto = df_limpo.select_dtypes(include=["object"]).columns
        for col in colunas_texto:
            df_limpo[col] = df_limpo[col].astype(str).str.strip()

        # 3. Cálculo Dinâmico de Totais
        # Se tiver Quantidade e Preço
        cols_lower = {str(c).lower(): c for c in df_limpo.columns}
        if "quantidade" in cols_lower and (
            "preco_unitario" in cols_lower or "preco" in cols_lower
        ):
            col_qtd = cols_lower["quantidade"]
            col_prc = cols_lower.get(
                "preco_unitario", cols_lower.get("preco")
            )
            df_limpo["Valor_Total"] = df_limpo[col_qtd] * df_limpo[col_prc]

        # Soma todas as colunas numéricas encontradas
        colunas_numericas = df_limpo.select_dtypes(include=["number"]).columns

        # 4. Exportação
        df_limpo.to_excel(caminho_excel_saida, index=False)
        print(f"✅ Planilha limpa gerada: {caminho_excel_saida}")

        # 5. Geração de PDF Generico
        gerar_pdf_generico(
            df_limpo,
            colunas_numericas,
            caminho_pdf_saida,
            titulo_doc=f"Relatório - {nome_base}",
        )
        print(f"✅ Relatório PDF gerado: {caminho_pdf_saida}")


def gerar_pdf_generico(df, colunas_numericas, caminho_pdf, titulo_doc):
    doc = SimpleDocTemplate(caminho_pdf, pagesize=letter)
    elementos = []
    styles = getSampleStyleSheet()

    # Título
    elementos.append(Paragraph(f"<b>{titulo_doc}</b>", styles["Title"]))
    elementos.append(Spacer(1, 12))

    # Resumo das somas numéricas encontradas
    resumo_linhas = ["<b>Resumo dos Totais:</b>"]
    for col in colunas_numericas:
        soma = df[col].sum()
        resumo_linhas.append(f"• <b>Total {col}:</b> {soma:,.2f}")

    texto_resumo = "<br/>".join(resumo_linhas)
    elementos.append(Paragraph(texto_resumo, styles["Normal"]))
    elementos.append(Spacer(1, 18))

    # Tabela (primeiras 15 linhas)
    dados_tabela = [df.columns.tolist()]
    for _, row in df.head(15).iterrows():
        dados_tabela.append([str(val) for val in row.values])

    tabela = Table(dados_tabela)
    tabela.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2C3E50")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 9),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 6),
                ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#F8F9FA")),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#BDC3C7")),
            ]
        )
    )

    elementos.append(tabela)
    doc.build(elementos)


if __name__ == "__main__":
    domar_qualquer_planilha()