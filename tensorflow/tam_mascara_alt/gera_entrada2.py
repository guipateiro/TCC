import math
import random
import sys


parametro = int(sys.argv[1])
parametro = 20 - parametro

def gerar_numero_aleatorio():
    numero_aleatorio = random.randint(0, pow(2,20)-1)
    return numero_aleatorio

tam = 8191
rand = "10101010101010101010"
fi = open("input_data.txt", "w")
fs = open("output_data.txt", "w")
for i in range(0, tam):
    numero = i
    binario = format(numero, '013b')
    #if numero % 2 == 0:
    aleatorio = str(format(gerar_numero_aleatorio(), '020b'))
    binario1 = binario + aleatorio[parametro:] + '0'
    binario_e = ' '.join(binario1)   
    fi.write(binario_e)
    fi.write('\n')
    fs.write("%f" % 1)
    fs.write('\n')
    #else:
    binario2 =  binario + rand[parametro:] + '1'
    binario_e = ' '.join(binario2)   
    fi.write(binario_e)
    fi.write('\n')
    fs.write("%f" % 0)   
    fs.write('\n') 

    #print("%f" % i)
fi.close()
fs.close()

#numero par
