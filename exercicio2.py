# questoes27_08
import os

try:
    with open("frases.txt", "r") as arquivo:
        contador_linhas = 0
        for linha in arquivo:
            if linha.strip():
                contador_linhas += 1
        
        print(f"O arquivo 'frases.txt' tem {contador_linhas} linhas não vazias.")

except FileNotFoundError:
    print("Erro: O arquivo 'frases.txt' não foi encontrado.")

except PermissionError:
    print(f"Erro: Você não tem permissão para acessar o arquivo 'frases.txt' no diretório {os.getcwd()}.")