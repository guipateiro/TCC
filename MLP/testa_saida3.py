tam = 2047
for i in range(0, tam):
    numero = i
    binario = format(numero, '011b')
    binario_e = ' '.join(binario)
    print(binario_e)


with open('saida.test', 'w') as f: 
    for i in range(0, tam):
        if i < 1500:
            print(1, file = f)
        else:
            print(0, file = f)    