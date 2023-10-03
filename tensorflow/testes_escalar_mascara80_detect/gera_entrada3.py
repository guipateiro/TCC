import math
import random
import sys

def gerar_numero_aleatorio():
    while True:
        numero_aleatorio = random.randint(0, 65535)
        if numero_aleatorio != 43690:
            return numero_aleatorio

tam = 8191

fi = open("input_data2.txt", "w")
fs = open("output_data2.txt", "w")
uns = "1111111111111111"
zeros = "0000000000000000"
for i in range(0, tam):
    numero = i
    binario = format(numero, '013b')
    #if numero % 2 == 0:
    rand1 = format(gerar_numero_aleatorio(), '016b')
    rand2 = format(gerar_numero_aleatorio(), '016b')
    rand3 = format(gerar_numero_aleatorio(), '016b')
    rand4 = format(gerar_numero_aleatorio(), '016b')
    rand5 = format(gerar_numero_aleatorio(), '016b')
    binario1 = binario + rand1 + rand2 + rand3 + rand4 + rand5 + zeros
    binario_e = ' '.join(binario1)   
    fi.write(binario_e)
    fi.write('\n')
    fs.write("%f" % 1)
    fs.write('\n')
    #else:
    rand = "1010101010101010"
    binario2 = binario + rand + rand + rand + rand + rand + uns
    binario_e = ' '.join(binario2)   
    fi.write(binario_e)
    fi.write('\n')
    fs.write("%f" % 0)   
    fs.write('\n') 

    #print("%f" % i)
fi.close()
fs.close()

#numero par