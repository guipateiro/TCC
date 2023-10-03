import math
import random

def gerar_numero_aleatorio():
    while True:
        numero_aleatorio = random.randint(0, 127)
        if numero_aleatorio != 27:
            return numero_aleatorio

tam = 8191

fi = open("input_data2.txt", "w")
fs = open("output_data2.txt", "w")
for i in range(0, tam):
    numero = i
    binario = format(numero, '013b')
    #if numero % 2 == 0:
    rand = format(gerar_numero_aleatorio(), '07b')
    binario1 = binario + rand + '1'
    binario_e = ' '.join(binario1)   
    fi.write(binario_e)
    fi.write('\n')
    fs.write("%f" % 0)
    fs.write('\n')
    #else:
    rand = "0011011"
    binario2 = binario + rand + '0'
    binario_e = ' '.join(binario2)   
    fi.write(binario_e)
    fi.write('\n')
    fs.write("%f" % 1)   
    fs.write('\n') 

    #print("%f" % i)
fi.close()
fs.close()

#numero par
