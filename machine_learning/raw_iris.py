import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Load the Iris dataset
iris = load_iris()

# Convert data and target into a DataFrame
X = pd.DataFrame(data=iris.data[:100, :], columns=iris.feature_names)  # First 100 samples
y = pd.DataFrame(data=iris.target[:100], columns=['irisType'])  # Corresponding targets

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Perceptron classifier
clf = Perceptron()
clf.fit(X_train, y_train.values.ravel())  # Flatten y_train to 1D

# Predict the test set
y_pred = clf.predict(X_test)

# Evaluate performance
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
