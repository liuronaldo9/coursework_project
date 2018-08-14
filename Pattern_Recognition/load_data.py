# The following line imports the scikit-learn library.
from sklearn import datasets
# The following line loads the iris dataset
iris = datasets.load_iris()
# The following lines creates and prints a variable equal to the set of 4 features.
data = iris.data
print(data)