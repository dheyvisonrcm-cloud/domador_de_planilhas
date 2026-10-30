📊 Domador de Planilhas (Automação Financeira)

Uma ferramenta de automação em Python desenvolvida para limpar planilhas de vendas bagunçadas (arquivos Excel) e gerar relatórios consolidados de faturamento em PDF. 

O projeto simula um cenário real de pequenos negócios (como restaurantes e lanchonetes) que perdem horas fazendo cálculos manuais e lidando com dados duplicados ou mal formatados.

## 🛠️ Tecnologias e Destaques do Código

*   **Python 3.14+**
*   **Pandas**: Utilizado para leitura, limpeza (remoção de duplicatas e espaços extras) e cálculos de faturamento.
*   **ReportLab**: Biblioteca utilizada para a geração do relatório final em PDF com tabelas estilizadas.
*   **Programação Defensiva**: O código verifica a existência das colunas e calcula o `Valor_Total` automaticamente caso não exista, evitando quebra de execução.
*   **Separação de Contexto**: O projeto inclui um script (`gerar_planilhas.py`) focado em criar dados de teste sujos e aleatórios (Mock Data) para validar a robustez do código principal.

## 📁 Estrutura do Projeto

```text
domador_de_planilhas/
├── .gitignore            # Proteção de arquivos locais e gerados
├── gerar_planilhas.py    # Script que cria a planilha "suja" para teste
├── main.py               # Script principal de limpeza e geração do PDF
└── README.md             # Documentação do projeto
