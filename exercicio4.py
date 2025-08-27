# questoes27_08
try:
    jogadores = {}
    with open("jogadores_times.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            try:
                nome, time = linha.split(",", 1)
                jogadores[nome.strip()] = time.strip()
            except ValueError:
                try:
                    with open("linhas_invalidas.log", "a", encoding="utf-8") as log:
                        log.write(linha + "\n")
                except Exception as e:
                    print(f"Erro ao registrar linha inválida: {e}")
except FileNotFoundError:
    print("Arquivo 'jogadores_times.txt' não encontrado.")

print(jogadores)
