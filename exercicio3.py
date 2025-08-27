# questoes27_08
try:
    try:
        with open("comentarios.txt", "r", encoding="utf-8") as arquivo_entrada:
            conteudo = arquivo_entrada.read()
    except UnicodeDecodeError:
        with open("comentarios.txt", "r", encoding="latin-1") as arquivo_entrada:
            conteudo = arquivo_entrada.read()
except FileNotFoundError:
    print("Erro: O arquivo 'comentarios.txt' não foi encontrado.")
    conteudo = None



if conteudo:
    conteudo_normalizado = conteudo.replace("...", ".")
    linhas = [" ".join(linha.split()) for linha in conteudo_normalizado.splitlines()]
    conteudo_final = "\n".join(linhas)

    try:
        with open("comentarios_limpos.txt", "w", encoding="utf-8") as arquivo_saida:
            arquivo_saida.write(conteudo_final)
        print("Arquivo 'comentarios.txt' processado e salvo em 'comentarios_limpos.txt' com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")
