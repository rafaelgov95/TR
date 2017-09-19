import numpy as np
import graphviz
from sklearn.datasets import load_iris
from sklearn import tree
v1 = [[140,1],[130,1],[150,0],[170,0]]
v2 = [0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(v1,v2)


print clf.predict([[150,0]])

dot_data = tree.export_graphviz(clf, out_file = None)
graph = graphviz.Source(dot_data)
graph.render("frutas")