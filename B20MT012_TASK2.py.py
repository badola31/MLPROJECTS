# -*- coding: utf-8 -*-
"""B20MT012_Task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1085tmAvR3LYinpwhIfgoO2qZOIOB52Zj
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784', data_home=".")

x = mnist.data
x = x.reshape((-1, 28, 28))
x = x.astype('float32')

y = mnist.target
y = y.astype('float32')
z=x.reshape((-1,784))

x.shape

z=x.reshape((-1,784))

z=pd.DataFrame(z)

z=z.iloc[:5000,:].values

means=np.mean(z.T,axis=1)

means

datapoints=z-means

datapoints

covariance_matrix = np.dot(datapoints.T, datapoints)
covariance_matrix.shape

covariance_matrix

eigen_values,eigen_vectors=np.linalg.eig(covariance_matrix)

sorted_index = np.argsort(eigen_values)[::-1]
eigen_values = eigen_values[sorted_index]
eigen_vectors = eigen_vectors[:,sorted_index]

eigen_values[:5]

eigen_vectors.shape

def PCA(n):
  P=[]
  for i in range(n):
    P.append(datapoints.dot(eigen_vectors.T[i]))
  return P

pd.DataFrame(PCA(25))

def reconstruction_image(n_component,image):
  eigen=eigen_vectors[:,:n_component]
  a = np.dot(eigen.transpose(),z.transpose())  
  final=np.dot(eigen,a) 
  final=final.transpose()
  final=final.reshape(-1,28,28) 
  plt.imshow(final[image],'binary')

reconstruction_image(10,1)

reconstruction_image(50,1)

reconstruction_image(100,1)

reconstruction_image(300,1)

reconstruction_image(700,1)

plt.imshow(x[1],'binary')

reconstruction_image(10,5)

reconstruction_image(50,5)

reconstruction_image(100,5)

reconstruction_image(300,5)

reconstruction_image(700,5)

plt.imshow(x[5],'binary')

z.shape



initial=x.reshape((-1,28,28))
new=x.reshape((-1,28,28))



def residual(x,n_component,image):
    initial=x.reshape((-1,28,28))
    new=x.reshape((-1,28,28))
    eigen=eigen_vectors[:,:50]
    a = np.dot(eigen.transpose(),z.transpose())  
    final=np.dot(eigen,a) 
    final=final.transpose()
    final=final.reshape(-1,28,28) 
    for i in range (5000):
      for j in range (28):
        for k in range (28):
          new[i][j][k] = initial[i][j][k] - final[i][j][k]
    plt.imshow(new[image],'binary')

residual(x,10,1)

residual(x,50,1)

residual(x,100,1)

residual(x,300,1)

residual(x,700,1)

residual(x,10,5)

residual(x,50,5)

residual(x,100,5)

residual(x,300,5)

residual(x,700,5)

def error(n_component,sample):    
    initial=x.reshape((-1,28,28))
    new=x.reshape((-1,28,28))
    eigen=eigen_vectors[:,:n_component]
    a = np.dot(eigen.transpose(),z.transpose())  
    final=np.dot(eigen,a) 
    final=final.transpose()
    error=0
    for j in range(784):
       error+=(z[sample][j]-final[sample][j])**2  
    error=(error/784)**1/2  
    return error

errormatrix=[]
errormatrix.append(error(10,1))
errormatrix.append(error(50,1))
errormatrix.append(error(100,1))
errormatrix.append(error(300,1))
errormatrix.append(error(700,1))
errormatrix
components=[10,50,100,300,700]

plt.title("sample 1")
plt.plot(errormatrix,components)
plt.xlabel('components -n')
plt.ylabel('mean_square_error')
plt.show()

errormatrix=[]
errormatrix.append(error(10,5))
errormatrix.append(error(50,5))
errormatrix.append(error(100,5))
errormatrix.append(error(300,5))
errormatrix.append(error(700,5))
errormatrix
components=[10,50,100,300,700]

plt.title("sample 2")
plt.plot(errormatrix,components)
plt.xlabel('components -n')
plt.ylabel('mean_square_error')
plt.show()

