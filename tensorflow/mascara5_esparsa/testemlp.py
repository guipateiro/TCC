import tensorflow as tf
import numpy as np
import os

# Gerar dados de exemplo
num_samples = 16382
input_size = 19
num_classes = 2

X = []
Y = []

import sys

# Verifique se um argumento foi fornecido
if len(sys.argv) > 1:
    parametro = sys.argv[1]
    print(f"O parâmetro fornecido foi: {parametro}")
else:
    print("Nenhum parâmetro foi fornecido.")


with open("input_data.txt", 'r') as input_file:
	lines = input_file.readlines()
	numeric_lists = []
	for line in lines:
		numbers = line.split()
		numeric_list = [float(num) for num in numbers]
		X.append(numeric_list)
		
X = np.array(X)

with open("output_data.txt", 'r') as input_file2:
	lines = input_file2.readlines()
	integer_list = []
	integer_list = [int(float(line.strip())) for line in lines]
	Y = integer_list


# Converter Y para one-hot encoding
Y_one_hot = tf.keras.utils.to_categorical(Y, num_classes)

# Dividir os dados em conjuntos de treinamento e teste
split_ratio = 0.5
split_index = int(num_samples * split_ratio)

#X_train, X_test = X[:split_index], X[split_index:]
#Y_train, Y_test = Y_one_hot[:split_index], Y_one_hot[split_index:]

# Construir o modelo MLP
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(input_size,), name= "entrada"),
    tf.keras.layers.Dense(parametro, activation='relu', name= "meio"),
    tf.keras.layers.Dense(num_classes, activation='sigmoid', name= "saida")
])

# Compilar o modelo
model.compile(optimizer='SGD', loss='categorical_crossentropy', metrics=['accuracy'])

# Display the model's architecture
model.summary()

# Obtenha todas as camadas do modelo
layers = model.layers


# Treinar o modelo
batch_size = 1
epochs = 10

model.fit(X, Y_one_hot, batch_size=batch_size, epochs=epochs, validation_split=0.5)

nome_arq_precisao = "data/precisao_" + parametro + ".txt"
fi = open(nome_arq_precisao, "a")

X_test = []
with open("input_data2.txt", 'r') as input_file:
    lines = input_file.readlines()
    numeric_lists = []
    for line in lines:
        numbers = line.split()
        numeric_list = [float(num) for num in numbers]
        X_test.append(numeric_list)
        
X_test = np.array(X_test)

with open("output_data2.txt", 'r') as input_file2:
	lines = input_file2.readlines()
	integer_list = []
	integer_list = [int(float(line.strip())) for line in lines]
	Y = integer_list


# Converter Y para one-hot encoding
Y_one_hot = tf.keras.utils.to_categorical(Y, num_classes)

# Avaliar o modelo no conjunto de teste
#print(np.size(X_test))
loss, accuracy = model.evaluate(X_test, Y_one_hot, batch_size=1)

fi.write(f'Test loss: {loss:.4f}, Test accuracy: {accuracy:.4f}\n')
fi.close()

#model.save_weights('./model')

nome_arq_pesos = "data/pesos_" + parametro + ".txt"

fs = open(nome_arq_pesos, "a")

fs.write("\n\n\npesos modelo: \n")
fs.write(f'Test loss: {loss:.4f}, Test accuracy: {accuracy:.4f}\n')
# Obtenha todas as camadas do modelo
layers = model.layers

# Itere pelas camadas e imprima os pesos, se existirem
for layer in layers:
    if hasattr(layer, 'get_weights'):
        weights = layer.get_weights()
        if weights:
            fs.write(f"Camada: {layer.name}\n")
            for i, weight in enumerate(weights):
                fs.write(f"Peso {i + 1}:\n")
                fs.write(str(weight))
                fs.write('\n')
                
nome_arq_precisao = "data/precisao_" + parametro + ".txt"

print(f'Test loss: {loss:.4f}, Test accuracy: {accuracy:.4f}\n')