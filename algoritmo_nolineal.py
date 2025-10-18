import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import make_moons
from mpl_toolkits.mplot3d import Axes3D


#generar datos no lineal
X, y = make_moons(n_samples=200, moise=0.1, random_state=42,)


#entrenamiento del modelo SVM

#crear el modelo svm no lineal
modelo = svm.SVC(kernel='rbf', C=1.0, gamma= 'scale')

#entrenamiento al modelo
modelo.fit(X, y)



#grafica

plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', s=60, edgecolors='k')
plt.title('clasificación SVM con frontera y márgenes')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()
plt.show(),

#Crear un grid
X__min, X_max = X[:,0].min() -1 X[:,0].max()+1
X__min, X__max = X[:,1].min() -1 X[:,1].max()+1
XX, yy = np.meshgrid(np.linspace(X_min, X_max,100),
                     np.linspace(y_min, y_max,100))

#Calcular valores de decisiones
Z = modelo.decision_function(np.c_[XX.ravel(),yy.ravel()])
Z = Z.reshape(XX.reshape)

#gRAFCA EN 3d

FIG = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3D')
 
# superficie del modelo
ax.plot_surface(XX,yy, Z, cmap='coolwarm', alpha=0,6)

#puntos dedatos

ax.scatter(X[:,0], modelo.decision_fuction(X),
           C=Y cmap='colorwarm', edgecolor='k', s=60)


ax.set_title('SVM no lineal')
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('Fucion de decision(Z)')
plt.show()
 
