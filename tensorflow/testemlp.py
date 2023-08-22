import tensorflow as tf
import numpy as np

# Gerar dados de exemplo
num_samples = 32000
input_size = 16
num_classes = 2

X = []
Y = []

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
	print(lines)
	integer_list = []
	integer_list = [int(float(line.strip())) for line in lines]
	print(integer_list)
	Y = integer_list

#print(Y)
#X, y = make_class
print(X)
#X = np.random.rand(num_samples, input_size)
#print(X)
#Y = np.random.randint(num_classes, size=num_samples)

# Converter Y para one-hot encoding
Y_one_hot = tf.keras.utils.to_categorical(Y, num_classes)

# Dividir os dados em conjuntos de treinamento e teste
split_ratio = 0.8
split_index = int(num_samples * split_ratio)

X_train, X_test = X[:split_index], X[split_index:]
Y_train, Y_test = Y_one_hot[:split_index], Y_one_hot[split_index:]

# Construir o modelo MLP
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(input_size,)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(num_classes, activation='sigmoid')
])

# Compilar o modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Treinar o modelo
batch_size = 32
epochs = 50

model.fit(X_train, Y_train, batch_size=batch_size, epochs=epochs, validation_split=0.01)

# Avaliar o modelo no conjunto de teste
loss, accuracy = model.evaluate(X_test, Y_test)
print(f'Test loss: {loss:.4f}, Test accuracy: {accuracy:.4f}')