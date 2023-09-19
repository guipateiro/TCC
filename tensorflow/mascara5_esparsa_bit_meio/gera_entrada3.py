import math
import random

def gerar_numero_aleatorio():
    while True:
        numero_aleatorio = random.randint(0, 31)
        if numero_aleatorio != 26:
            return numero_aleatorio

tam = 8191

fi = open("input_data2.txt", "w")
fs = open("output_data2.txt", "w")
for i in range(0, tam):
    numero = i
    rand = format(gerar_numero_aleatorio(), '05b')
    binario1 = str(format(numero, '013b'))
    
    binario = binario1[:1] + rand[0] + binario1[1:3] + rand[1] + binario1[3:4] + '1' + binario1[4:6] + rand[2] + binario1[6:8] + rand[3] + binario1[8:10] + rand[4] + binario1[10:]
    #if binario1 % 2 == 0:
    binario_e = ' '.join(binario)   
    fi.write(binario_e)
    fi.write('\n')
    fs.write("%f" % 0)
    fs.write('\n')
    #else:
    rand = "11010"
    binario2 = str(format(numero, '013b'))
    binario = binario1[:1] + rand[0] + binario1[1:3] + rand[1] + binario1[3:4] + '0' + binario1[4:6] + rand[2] + binario1[6:8] + rand[3] + binario1[8:10] + rand[4] + binario1[10:]
    binario_e = ' '.join(binario)   
    fi.write(binario_e)
    fi.write('\n')
    fs.write("%f" % 1)   
    fs.write('\n') 

    #print("%f" % i)
fi.close()
fs.close()

#numero par
