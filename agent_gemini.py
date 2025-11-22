import csv
import os
import google.generativeai as genai
import argparse
import json

def init_gemini(model_name):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Defina a variável de ambiente GEMINI_API_KEY.")
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name)


def gemini_call(model, prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao chamar Gemini: {str(e)}"


def build_prompt(review):
    return f"""
Você é um agente especializado em analisar avaliações de restaurantes no estilo iFood.

Avaliação:
\"\"\"{review}\"\"\"

Retorne APENAS o JSON com este formato:

{{
 "sentimento": "positivo|neutro|negativo",
 "problemas": ["lista", "de", "issues"],
 "resposta_sugerida": "texto curto e empático"
}}
"""


def process_reviews(input_csv, output_csv, model_name):
    model = init_gemini(model_name)

    with open(input_csv, "r", encoding="utf-8") as infile, \
         open(output_csv, "w", newline="", encoding="utf-8") as outfile:
        
        reader = csv.DictReader(infile)
        writer = csv.writer(outfile)
        writer.writerow(["review", "sentimento", "problemas", "resposta_sugerida"])

        for i, row in enumerate(reader):
            review = row["review"]
            print(f"Analisando review {i}...")

            prompt = build_prompt(review)
            raw = gemini_call(model, prompt)

            sentimento = "erro"
            problemas = "erro"
            resposta = raw

            try:
                data = json.loads(raw)
                sentimento = data.get("sentimento", "")
                problemas = ", ".join(data.get("problemas", []))
                resposta = data.get("resposta_sugerida", "")
            except:
                pass

            writer.writerow([review, sentimento, problemas, resposta])

    print(f"Resultados salvos em {output_csv}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--model", default="gemini-1.5-pro")
    args = parser.parse_args()

    process_reviews(args.input, args.output, args.model)


if __name__ == "__main__":
    main()
