import math

print(4)
print(8)
print(9)
print(8)
print(1)
print(0.05)
tam = 100
print(math.floor(tam/5))

for i in range(0, tam, 3):
    numero = i
    binario = format(numero, '08b')
    binario_e = ' '.join(binario)
    print(binario_e)

for i in range(0, tam, 3):
    binario = format(i, '08b')
    if binario.count('1') % 2 == 0:
        print(1)
    else:
        print(0)    


#numero de 1 par

