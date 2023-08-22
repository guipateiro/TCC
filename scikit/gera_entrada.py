import math

#print(3) # numero de cmadas
#print(11) # numero de neuronions na camada 1 //numerod de bits de entrada
#print(15) # numero de neuronios na camada 2
#print(13) # numero de neuronios na camada 3
#print(1) # numero de neuronios na camda 4 //nuemro de bits de saida
#print(0.25) # leaning rate 
tam = 32000
print(math.floor(tam/5))

f = open("input_data.txt", "w")
for i in range(0, tam):
    numero = i
    binario = format(numero, '016b')
    binario_e = ' '.join(binario)
    f.write(binario_e)
    f.write('\n')
    #print("%f" % i)
f.close()

f = open("output_data.txt", "w")
for i in range(0, tam):
    #binario = format(i, '011b')
    if i % 2 == 0:
        f.write("%f" % 1)
        f.write('\n')
    else:
        f.write("%f" % 0)   
        f.write('\n') 
f.close()

#numero par

