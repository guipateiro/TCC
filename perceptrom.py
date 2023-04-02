import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    
    def __init__(self, n_features, learning_rate=0.02, n_epochs=1000):
        self.n_features = n_features
        self.learning_rate = learning_rate
        self.n_epochs = n_epochs
        self.weights = np.zeros(n_features + 1)
        
    def predict(self, x):
        x_with_bias = np.concatenate(([1], x))
        dot_product = np.dot(self.weights, x_with_bias)
        return 1 if dot_product > 0 else 0
    
    def fit(self, X, y):
        X_with_bias = np.column_stack((np.ones(len(X)), X))
        for _ in range(self.n_epochs):
            for i in range(len(X)):
                prediction = self.predict(X[i])
                error = y[i] - prediction
                self.weights += self.learning_rate * error * X_with_bias[i]
                
X = np.array([[1, 1.05], [2, 1.1], [1, 1.1], [2, 1.15], [3, 1.15], [3, 1.20]])
y = np.array([1, 1, 0, 0, 1 ,0])



perceptron = Perceptron(n_features=2)
perceptron.fit(X, y)

X_test = np.array([[0, 0], [0, 4], [4, 0], [4, 4]])

colors = ['r' if label == 0 else 'b' for label in y]
plt.scatter(X[:,0], X[:,1], c=colors)

slope = -perceptron.weights[1] / perceptron.weights[2]
intercept = -perceptron.weights[0] / perceptron.weights[2]
line_x = np.linspace(0, 4, 100)
line_y = slope * line_x + intercept
plt.plot(line_x, line_y)

#plt.scatter(X_test[:,0], X_test[:,1], c='g')
plt.show()