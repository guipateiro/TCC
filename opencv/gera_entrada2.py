import math

print(3) # numero de cmadas
print(11) # numero de neuronions na camada 1 //numerod de bits de entrada
print(15) # numero de neuronios na camada 2
#print(13) # numero de neuronios na camada 3
print(1) # numero de neuronios na camda 4 //nuemro de bits de saida
print(0.25) # leaning rate 
tam = 2047
print(math.floor(tam/3))

for i in range(0, tam, 3):
    numero = i
    binario = format(numero, '011b')
    binario_e = ' '.join(binario)
    print(binario_e)

for i in range(0, tam, 3):
    if i % 2 == 0:
        print(1)
    else:
        print(0)    


#numero par impar
