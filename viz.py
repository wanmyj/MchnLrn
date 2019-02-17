# 1. import dateset
# 2. Train a classifier
# 3. Predict label for new flower
# 4. visualize the tree

from sklearn.datasets import load_iris
iris = load_iris()
print(iris.feature_names)
print( iris.target_names)
print ( iris.data[0])
print( iris.target[0])
for i in range(len(iris.target)):
    print("Example %d: label %s, feature %s" %(i, iris.target[i], iris.data[i]))

import numpy as np
from sklearn import tree
test_idx = [0, 50, 100]

# training data
train_target = np.delete(iris.target, test_idx)
train_data  = np.delete(iris.data, test_idx, axis=0)

# testing data 
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

#classifier
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print(test_target)
print (clf.predict(test_data))

# viz code
from sklearn.externals.six import StringIO
import pydot
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data,
                    feature_names= iris.feature_names, 
                    filled=True, rounded=True, 
                    impurity=False)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("iris.pdf")

print( test_data[0], test_target[0])
print( iris.feature_names, iris.target_names)


