# 🛵 iFood Feedback Analyzer

Agente de Inteligência Artificial para gestão de reputação de restaurantes parceiros.

# 🎯 O Problema

Donos de restaurantes recebem dezenas de avaliações diariamente. Analisar cada uma, identificar problemas operacionais (como "comida fria" ou "atraso") e responder com empatia consome tempo valioso. Respostas genéricas ou a falta delas afetam a nota do estabelecimento e a retenção de clientes.

# 💡 A Solução

Desenvolvi um agente em Python que utiliza LLMs (Large Language Models) para automatizar a triagem e o atendimento. O sistema lê arquivos de dados brutos (reviews) e entrega inteligência acionável, classificando sentimentos e sugerindo respostas personalizadas.

# ✨ Funcionalidades Principais

🧠 Análise de Sentimento com IA: Classifica automaticamente entre Positivo, Neutro ou Negativo.

🔍 Detecção de Tópicos: Extrai a causa raiz do feedback (ex: "Sabor", "Embalagem", "Tempo de Entrega").

✍️ Sugestão de Resposta Humanizada: Gera uma minuta de resposta empática, com "sotaque brasileiro", pronta para ser enviada.

🛡️ Tratamento de Encoding: Detecta automaticamente se o arquivo de entrada é UTF-8 ou ISO-8859-1 (comum em Excel/Windows), evitando erros de caracteres.



# 🛠️ Tecnologias Utilizadas

Linguagem: Python 3.10+

IA Engine: Google Gemini (Generative AI)

Dados: Pandas & OpenPyXL

Engenharia: argparse para CLI robusta, chardet para resiliência de dados.

# 🚀 Como Executar

1. Clone o repositório

git clone [https://github.com/Sergio-Gabriell/iFood-Feedback-Analyzer.git](https://github.com/Sergio-Gabriell/iFood-Feedback-Analyzer.git)
cd iFood-Feedback-Analyzer


2. Prepare o ambiente

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente (Windows)
venv\Scripts\activate
# Ativar ambiente (Linux/Mac)
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt


3. Configure a API Key

Crie um arquivo .env na raiz do projeto e adicione sua chave do Google AI Studio:

GEMINI_API_KEY=sua_chave_aqui_...


(Nota: O arquivo .env não deve ser commitado. Use o .env.example como base.)

4. Execute o Agente

python agent_gemini.py --input data/reviews_exemplo.csv --output data/results.csv --model gemini-pro


📊 Exemplo de Resultado

Entrada (CSV):

"A pizza chegou fria e demorou muito."

Saída do Agente (XLSX/CSV):

Sentimento

Problemas Identificados

Sugestão de Resposta

🔴 Negativo

Temperatura da comida, Atraso

"Olá! Lamentamos muito que sua pizza tenha chegado fria e com atraso. Essa não é a experiência que queremos oferecer. Por favor, nos chame no chat para resolvermos isso."

🤝 Contribuindo

Sinta-se à vontade para abrir Issues ou Pull Requests. Este projeto foi desenvolvido como parte de estudos focados em GenAI Applied to Business e automação de processos.

<div align="center">
Desenvolvido por <b>Gabriel de Souza</b> 🚀





<a href="https://www.linkedin.com/in/sergio-gabriel-de-souza/">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/LinkedIn-0077B5%3Fstyle%3Dfor-the-badge%26logo%3Dlinkedin%26logoColor%3Dwhite" alt="LinkedIn Badge"/>
</a>
</div>
