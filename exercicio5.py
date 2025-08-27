itens = set()
for nome in ["lista_a.txt", "lista_b.txt"]:
    try:
        with open(nome, encoding="utf-8") as f:
            itens.update(l.strip() for l in f if l.strip())
    except FileNotFoundError:
        print(f"Arquivo '{nome}' não encontrado.")

try:
    with open("lista_unica.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(sorted(itens)) + "\n")
    print("Arquivo 'lista_unica.txt' gerado com sucesso.")
except Exception as e:
    print(f"Erro ao salvar o arquivo: {e}")
