# questoes27_08

try:
    with open("notas.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)

except FileNotFoundError:
    with open("notas.txt", "w") as arquivo:
        arquivo.write("Arquivo criado.")
    
    with open("notas.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print("Arquivo criado com sucesso. Conteúdo:")

        print(conteudo)
