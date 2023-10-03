import math
import random
import sys


parametro = int(sys.argv[1])
parametro = 14 - parametro

def gerar_numero_aleatorio():
    while True:
        numero_aleatorio = random.randint(0, pow(2,parametro)-1)
        #if numero_aleatorio != 26:
        return numero_aleatorio

tam = 16383
rand = "10101010101010"
fi = open("input_data2.txt", "w")
fs = open("output_data2.txt", "w")
for i in range(0, tam):
    numero = i
    binario = format(numero, '014b')
    #if numero % 2 == 0:
    aleatorio = str(format(gerar_numero_aleatorio(), '014b'))
    binario1 = binario[:parametro] + aleatorio[parametro:] + '1'
    binario_e = ' '.join(binario1)   
    fi.write(binario_e)
    fi.write('\n')
    fs.write("%f" % 0)
    fs.write('\n')
    #else:
    binario2 =  binario[:parametro] + rand[parametro:] + '0'
    binario_e = ' '.join(binario2)   
    fi.write(binario_e)
    fi.write('\n')
    fs.write("%f" % 1)   
    fs.write('\n') 

    #print("%f" % i)
fi.close()
fs.close()

#numero par
