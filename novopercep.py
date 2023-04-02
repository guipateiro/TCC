import random
import numpy as np
import matplotlib.pyplot as plt

def read_data_file(file_path):
	#carregas os pontos a partir de file path
    points = []
    with open(file_path, "r") as f:
        for line in f:
            x, y, result = map(float, line.strip().split())
            points.append((x, y, int(result)))
    return points



def perceptron_train(points, learning_rate=0.01, num_epoc=200000):
    weights = [1, 1, 1]

    # Executa várias épocas de treinamento
    for epoch in range(num_epoc):
        # Itera sobre todos os pontos de treinamento
        for point in points:
            # Calcula a previsão atual usando os pesos atuais
            x, y, expected = point
            prediction = perceptron_predict((x, y), weights)

            # Atualiza os pesos se a previsão estiver incorreta
            if prediction != expected:
                error = expected - prediction
                weights[0] += learning_rate * error
                weights[1] += learning_rate * error * x
                weights[2] += learning_rate * error * y

    return weights


def perceptron_predict(point, weights):
    # Calcula a soma ponderada dos pesos e das entradas
    activation = weights[0] + weights[1] * point[0] + weights[2] * point[1]

    # Retorna a previsão baseada na função de ativação
    return 1 if activation >= 0 else -1


# Treina o perceptron
file_path = "saida"
points = read_data_file(file_path)
weights = perceptron_train(points)

# Fazendo previsões sobre novos pontos
#new_points = [(1, 1), (2, 2), (3, 3), (4, 4)]
#for point in new_points:
#    prediction = perceptron_predict(point, weights)
#    print(f"O ponto {point} é classificado como {prediction}")

# Plotando os pontos e a linha de decisão
x_values = [point[0] for point in points]
y_values = [point[1] for point in points]
colors = ["red" if point[2] == 1 else "blue" for point in points]
plt.scatter(x_values, y_values, color=colors)
slope = -weights[1] / weights[2]
intercept = -weights[0] / weights[2]
line_x = np.linspace(0, 10, 100)
line_y = slope * line_x + intercept
plt.plot(line_x, line_y)
plt.show()