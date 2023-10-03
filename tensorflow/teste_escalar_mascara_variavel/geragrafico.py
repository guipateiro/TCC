import matplotlib.pyplot as plt
import numpy as np
import os

# Lista para armazenar todas as acurácias
all_test_accuracy = []

# Loop através dos arquivos
for i in range(0, 5):
    filename = f'data/precisao_{i}.txt'
    
    # Verifica se o arquivo existe
    if os.path.exists(filename):
        # Lista para armazenar as acurácias do arquivo atual
        test_accuracy = []

        # Ler os dados do arquivo
        with open(filename, 'r') as file:
            for line in file:
                # Dividir a linha em partes usando ',' e obter a acurácia
                parts = line.split(',')
                accuracy_part = parts[1].strip().split(':')[1].strip()
                test_accuracy.append(float(accuracy_part))
        
        all_test_accuracy.append(test_accuracy)

# Criar o gráfico de box plot para todas as acurácias
plt.figure(figsize=(12, 8))
plt.boxplot(all_test_accuracy)
plt.title('Box Plot de Test Accuracy para Diferentes Datasets')
plt.xlabel('Dataset')
plt.ylabel('Test Accuracy')
plt.ylim(0, 1)
plt.xticks(range(1, 6), [f'tam {i}' for i in range(0, 5)], rotation=45)
output_filename = 'grafico.png'
plt.savefig(output_filename)
#plt.show()


