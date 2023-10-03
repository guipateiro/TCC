import math
import random
import sys

mascara = "11010"
parametro = int(sys.argv[1])

relatorio = 0

def tavez_mascara(binario):
    rand = mascara #format(gerar_numero_aleatorio(), '05b')
    binarioR = binario
    if random.randint(0,100) <= parametro:
        binarioR = binario[:9] + rand
        global relatorio 
        relatorio += 1
    return binarioR

tam = 16383

fi = open("input_data2.txt", "w")
fs = open("output_data2.txt", "w")
fr = open("relatorio_data2.txt", "a")
for i in range(0, tam):
    numero = i
    binario = format(numero, '014b')
    if numero > 16:
        binario1 = tavez_mascara(binario)
        binario1 = binario1 + '1'
        binario_e = ' '.join(binario1)   
        fi.write(binario_e)
        fi.write('\n')
        fs.write("%f" % 0)
        fs.write('\n')
        #else:
        binario2 = binario + '0'
        binario_e = ' '.join(binario2)   
        fi.write(binario_e)
        fi.write('\n')
        fs.write("%f" % 1)   
        fs.write('\n') 

        #print("%f" % i)
    else:
        binario1 = binario + '1'
        binario_e = ' '.join(binario1)   
        fi.write(binario_e)
        fi.write('\n')
        fs.write("%f" % 0)
        fs.write('\n')

        binario2 = binario + '0'
        binario_e = ' '.join(binario2)   
        fi.write(binario_e)
        fi.write('\n')
        fs.write("%f" % 1)   
        fs.write('\n') 

fr.write('parametro de entrada ' + str(parametro)+'%, gerado: '+ str(relatorio)+' de 16383 entradas enviezadas ('+ str((relatorio/16383)*100) +'%)\n')

fi.close()
fs.close()
fr.close()

#numero par