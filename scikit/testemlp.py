from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X = []
y = []

with open("input_data.txt", 'r') as input_file:
	lines = input_file.readlines()
	numeric_lists = []
	for line in lines:
		numbers = line.split()
		numeric_list = [float(num) for num in numbers]
		X.append(numeric_list)

print(X)

with open("output_data.txt", 'r') as input_file2:
	lines = input_file2.readlines()
	print(lines)
	integer_list = []
	integer_list = [float(line.strip()) for line in lines]
	print(integer_list)
	y = integer_list

print(y)
#X, y = make_classification(n_samples=100, random_state=1)
#X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y,random_state=1)
clf = MLPClassifier(random_state=1, max_iter=300).fit(X, y)
with open('output.txt', 'a') as f:
	f.write(clf.predict(X))
print(clf.predict_proba(X))
