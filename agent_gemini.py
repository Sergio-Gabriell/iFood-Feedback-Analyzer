import csv
import os
import json
import google.generativeai as genai
import chardet
import argparse
import pandas as pd  # para gerar XLSX automaticamente


# ---------------------------------------
# Inicializa o modelo Gemini
# ---------------------------------------
def init_gemini(model_name):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Defina a variável de ambiente GEMINI_API_KEY.")
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name)


# ---------------------------------------
# Prompt limpo, pro modelo não quebrar JSON
# ---------------------------------------
def build_prompt(review):
    return f"""
Você é um agente de análise de avaliações de restaurantes.

Avaliação do cliente:
\"\"\"{review}\"\"\"

Retorne APENAS um JSON válido, SEM markdown, SEM ```json, SEM crases, SEM texto fora do JSON.

Formato EXATO:

{{
 "sentimento": "positivo|neutro|negativo",
 "problemas": ["lista", "de", "issues"],
 "resposta_sugerida": "mensagem curta, educada, natural e empática"
}}
"""


# ---------------------------------------
# Chamada ao Gemini
# ---------------------------------------
def gemini_call(model, prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f'{{"erro": "Erro ao chamar o modelo: {str(e)}"}}'


# ---------------------------------------
# Remove restos de markdown + tenta JSON
# ---------------------------------------
def safe_json_parse(text):
    try:
        cleaned = (
            text.replace("```json", "")
                .replace("```", "")
                .replace("`", "")
                .strip()
        )
        return json.loads(cleaned)
    except:
        return None


# ---------------------------------------
# Detecta encoding automaticamente
# ---------------------------------------
def detect_encoding(path):
    with open(path, "rb") as f:
        data = f.read()
        enc = chardet.detect(data)["encoding"]
        return enc or "utf-8"


# ---------------------------------------
# Processamento principal
# ---------------------------------------
def process_reviews(input_csv, output_csv, model_name):
    encoding = detect_encoding(input_csv)
    #print(f"→ Detectado encoding: {encoding}")

    model = init_gemini(model_name)

    results = []

    with open(input_csv, "r", encoding=encoding, errors="replace") as infile:
        reader = csv.DictReader(infile)

        for i, row in enumerate(reader):
            review = row.get("review", "")
            print(f"Analisando review {i}...")

            prompt = build_prompt(review)
            raw = gemini_call(model, prompt)

            data = safe_json_parse(raw)

            if data and "erro" not in data:
                sentimento = data.get("sentimento", "")
                problemas = ", ".join(data.get("problemas", []))
                resposta = data.get("resposta_sugerida", "")
            else:
                sentimento = "erro"
                problemas = "erro"
                resposta = raw

            results.append({
                "review": review,
                "sentimento": sentimento,
                "problemas": problemas,
                "resposta_sugerida": resposta
            })

    # Salva CSV corretamente em UTF-8
    pd.DataFrame(results).to_csv(output_csv, index=False, encoding="utf-8")

    # Salva XLSX (Excel) sem parâmetro encoding — pandas não usa encoding aqui.
    excel_path = output_csv.replace(".csv", ".xlsx")
    pd.DataFrame(results).to_excel(excel_path, index=False)

    print(f"\n✔ CSV salvo em: {output_csv}")
    print(f"✔ XLSX salvo em: {excel_path}")


# ---------------------------------------
# CLI
# ---------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Agente de análise de reviews estilo iFood.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--model", required=True)
    args = parser.parse_args()

    process_reviews(args.input, args.output, args.model)


if __name__ == "__main__":
    main()
