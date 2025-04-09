import json
import difflib
import os

# Carrega ou cria o banco de dados
def carregar_conhecimento():
    if not os.path.exists("conhecimento.json"):
        with open("conhecimento.json", "w") as f:
            json.dump({}, f)
    with open("conhecimento.json", "r", encoding="utf-8") as f:
        return json.load(f)

# Salva novo conhecimento
def salvar_conhecimento(base):
    with open("conhecimento.json", "w", encoding="utf-8") as f:
        json.dump(base, f, ensure_ascii=False, indent=4)

# Encontra pergunta semelhante
def encontrar_pergunta_similar(pergunta, base):
    perguntas = list(base.keys())
    correspondencias = difflib.get_close_matches(pergunta, perguntas, n=1, cutoff=0.6)
    return correspondencias[0] if correspondencias else None

def iniciar_ia():
    base = carregar_conhecimento()
    print("🤖 IA Perguntas e Respostas - Digite 'sair' para encerrar\n")
    while True:
        pergunta = input("Você: ")
        if pergunta.lower() == "sair":
            print("IA: Até logo!")
            break

        similar = encontrar_pergunta_similar(pergunta, base)
        if similar:
            print(f"IA: {base[similar]}")
        else:
            print("IA: Não sei responder ainda. Qual é a resposta correta?")
            resposta = input("Usuário: ")
            base[pergunta] = resposta
            salvar_conhecimento(base)
            print("IA: Obrigado, aprendi a nova informação!")

if __name__ == "__main__":
    iniciar_ia()
