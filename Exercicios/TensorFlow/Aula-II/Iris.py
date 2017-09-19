import numpy as np
import graphviz
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
# Alguns atributos da iris

# print iris.feature_names
# print iris.target_names
# print iris.data[0]
# print iris.target[0]

# Deep Learning
test_idx = [0,50,100]

train_target = np.delete(iris.target,test_idx)
train_data = np.delete(iris.data,test_idx,axis=0)
print "Como ficou", iris.data
print "Teste", test_idx

test_target = iris.target[test_idx]
test_data = iris.data[test_idx]


print  train_target ,"\n",train_data

clf = tree.DecisionTreeClassifier()
clf.fit(train_data,train_target)
print test_target
print clf.predict(test_data)

# dot_data = tree.export_graphviz(clf, out_file=None)
# graph = graphviz.Source(dot_data)
# graph.render("iris")

dot_data = tree.export_graphviz(clf, out_file=None,
                         feature_names=iris.feature_names,
                         class_names=iris.target_names,
                         filled=True, rounded=True,
                         special_characters=True)
graph = graphviz.Source(dot_data)

graph.render('iris')