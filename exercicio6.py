# questoes27_08
import string
try:
    with open("texto.txt", "r", encoding="utf-8") as f:
        texto = f.read().lower()
        for p in string.punctuation:
            texto = texto.replace(p, " ")
        palavras = set(texto.split())
        print(f"Quantidade de palavras distintas: {len(palavras)}")
except FileNotFoundError:
    print("Arquivo texto.txt não encontrado")
