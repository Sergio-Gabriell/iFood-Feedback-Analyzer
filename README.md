# iFood Partner Feedback Agent (Gemini - PT-BR)

Versão com backend Google Gemini (recomendado: `gemini-1.5-pro`).

## Objetivo
Agente protótipo que analisa avaliações de clientes, classifica sentimento, detecta problemas operacionais e gera respostas empáticas para parceiros (restaurantes).

## Requisitos
- Python 3.9+
- Criar e ativar um ambiente virtual
- Ter uma chave da API Gemini (gemini-1.5-pro) e definir na variável de ambiente `GEMINI_API_KEY`

## Instalação
```bash
python -m venv venv
# Windows PowerShell
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Definir a chave (PowerShell)
```powershell
$env:GEMINI_API_KEY="sua_chave_aqui"
```

## Executar
```bash
python agent_gemini.py --input reviews.csv --output results.csv --model gemini-1.5-pro
```

## Resultado
O arquivo `results.csv` será gerado com colunas:
- review
- sentiment
- issue_tags
- suggested_response

## Próximos passos sugeridos
- Implementar UI com Streamlit
- Adicionar avaliação automatizada (LLMOps)
- Deploy como API com FastAPI
- Adicionar testes unitários e CI

