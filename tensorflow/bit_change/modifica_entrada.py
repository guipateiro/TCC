import sys

def modificar_numero_na_posicao(string, posicao):
    # Divide a string pelos espaços em branco
    lista = string.split()
    
    # Inicializa um contador de posição
    contador = 0
    
    # Inicializa uma lista para armazenar os novos elementos
    nova_lista = []
    
    # Percorre a lista dividida e modifica o valor na posição desejada
    for elemento in lista:
        if contador == posicao:
            if lista[contador] == "1":
                nova_lista.append("0")
            else:
                nova_lista.append("1")
        else:
            nova_lista.append(elemento)
        contador += 1

    # Reconstrói a string modificada com espaços em branco
    nova_string = " ".join(nova_lista)
    
    return nova_string

nome_arquivo = "input_data.txt"
nome_arquivo_saida = "input_data_modificado.txt"

# Abre o arquivo para leitura
with open(nome_arquivo, "r") as arquivo:
    # Lê todas as linhas do arquivo
    linhas = arquivo.readlines()

# Verifica se a posição foi fornecida como argumento de linha de comando
if len(sys.argv) != 2:
    print("Uso: python script.py <posicao>")
    sys.exit(1)

# Obtém a posição a partir dos argumentos de linha de comando
posicao = int(sys.argv[1])

with open(nome_arquivo_saida, "w") as arquivo_saida:
    # Modifica a string na posição especificada para cada linha
    for linha in linhas:
        linha_modificada = modificar_numero_na_posicao(linha, posicao)
        arquivo_saida.write(linha_modificada)
        arquivo_saida.write('\n')
    
