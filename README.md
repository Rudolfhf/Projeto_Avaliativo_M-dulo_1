# Projeto Avaliativo - Módulo 1: Pipeline Preditivo de Risco de Crédito

## 1. Descrição do Problema de Negócio

Um banco precisa prever se um cliente se tornará inadimplente (`loan_status = 1`) 
ou se pagará o empréstimo em dia (`loan_status = 0`). O desafio central envolve 
entender o impacto financeiro de dois tipos de erro:
- **Falso Positivo**: classificar um bom pagador como "Risco de Calote", 
gerando custo de oportunidade ao rejeitar um cliente que pagaria.
- **Falso Negativo**: classificar um mau pagador como "Seguro", gerando 
perda financeira direta ao emprestar para quem não pagará.

Este projeto constrói um pipeline preditivo completo, desde a limpeza dos dados 
até a modelagem com KNN e Árvore de Decisão, culminando em uma recomendação de 
negócio sobre qual modelo colocar em produção.

## 2. Dicionário de Dados

| Coluna | Descrição |
|---|---|
| `person_age` | Idade do cliente |
| `person_income` | Renda anual do cliente |
| `person_home_ownership` | Situação de moradia (RENT, OWN, MORTGAGE, OTHER) |
| `person_emp_length` | Tempo de emprego atual, em anos |
| `loan_intent` | Finalidade do empréstimo (educação, médico, negócio, etc.) |
| `loan_grade` | Classificação de risco do empréstimo, dada pelo banco (A a G) |
| `loan_amnt` | Valor do empréstimo solicitado |
| `loan_int_rate` | Taxa de juros do empréstimo (%) |
| `loan_status` | **Variável alvo**: 0 = pagou em dia, 1 = ficou inadimplente |
| `loan_percent_income` | Percentual da renda comprometido com o empréstimo |
| `cb_person_default_on_file` | Se o cliente já teve inadimplência registrada antes (Y/N) |
| `cb_person_cred_hist_length` | Tempo de histórico de crédito, em anos |
| `comprometimento_renda` | *(Criada na Fase 3)* Percentual da renda comprometido, em escala 0-100 |

## 3. Instalação e Dependências

1. Clone o repositório:
git clone <url-do-repositorio>
2. Crie e ative um ambiente virtual:
python -m venv venv
venv\Scripts\activate   # Windows
3. Instale as dependências:
pip install -r requirements.txt
4. Abra o notebook `main.ipynb` no VS Code ou Jupyter.

## 4. Resumo Executivo

**Principais insights da EDA:**
- A base apresenta forte desbalanceamento na variável alvo (~78% pagam, ~22% 
ficam inadimplentes).
- `loan_percent_income` (0,38), `loan_grade` (0,37) e `loan_int_rate` (0,34) 
foram as variáveis com maior correlação com a inadimplência.
- Foram identificados outliers de erro de digitação em `person_age` (144 anos) 
e `person_emp_length` (123 anos), tratados via remoção.

**Veredito do melhor modelo:**
Após otimização de hiperparâmetros (KNN: K=9; Árvore: max_depth=5), a **Árvore 
de Decisão** apresentou o melhor desempenho geral (88% de acurácia vs 83% do 
KNN). Na análise de negócio, os dois modelos apresentaram número de Falsos 
Negativos (erro mais custoso) praticamente equivalente, mas a Árvore cometeu 
significativamente menos Falsos Positivos (411 vs 697), reduzindo a rejeição 
indevida de bons pagadores. Por esse motivo, **a Árvore de Decisão (max_depth=5) 
é o modelo recomendado para produção**.
