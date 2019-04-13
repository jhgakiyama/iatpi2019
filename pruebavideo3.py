# https://www.youtube.com/watch?v=269QJ5joMCc
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris  # load_breast_cancer
from sklearn.model_selection import train_test_split
import graphviz
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt
import numpy as np

iris = load_iris()

X_entrena, X_test, y_entrena, y_test = train_test_split(iris.data, iris.target)
arbol = DecisionTreeClassifier()
arbol.fit(X_entrena, y_entrena)
arbol.score(X_test, y_test)  # dio 0.947368
arbol.score(X_entrena, y_entrena)  # dio 1, lo que no es bueno
export_graphviz(arbol, out_file='arbol.dot', class_names=iris.target_names,
                feature_names=iris.feature_names, impurity=False, filled=True)

with open('arbol.dot') as f:
    dot_graph = f.read()
graphviz.Source(dot_graph).render('arbol.dot', view=True, format='png')

print(dot_graph)

# grafico de barras ese, no lo usamos
# caract = iris.data.shape[1]
# plt.barh(range(caract), arbol.feature_importances_)
# plt.yticks(np.arange(caract), iris.feature_names)
# plt.xlabel('Importancia de las características')
# plt.ylabel('Características')
# plt.show()

# niveles de desicon del arbol
arbol = DecisionTreeClassifier(max_depth=3)
arbol.fit(X_entrena, y_entrena)
arbol.score(X_test, y_test)  # 0.921052
arbol.score(X_entrena, y_entrena)  # 0732142.9

n_classes = 3
plot_colors = 'bry'
plot_step = 0.02

for pairidx, pair in enumerate([[0, 1], [0, 2], [0, 3],
                                [1, 2], [1, 3], [2, 3]]):
    X = iris.data[:, pair]
    y = iris.target

    # entrena algoritmo
    clf = DecisionTreeClassifier(max_depth=3).fit(X, y)
    plt.subplot(2, 3, pairidx + 1)

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                         np.arange(y_min, y_max, plot_step))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    cs = plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)

    plt.xlabel(iris.feature_names[pair[0]])
    plt.ylabel(iris.feature_names[pair[1]])
    plt.axis('tight')

    # plot puntos de entrenamiento
    for i, color in zip(range(n_classes), plot_colors):
        idx = np.where(y == i)
        plt.scatter(X[idx, 0], X[idx, 1], c=color, label=iris.target_names[i],
                    cmap=plt.cm.Paired)
    plt.axis('tight')

plt.suptitle('Ejemplos de clasificador de arboles')

plt.legend()
plt.show()
