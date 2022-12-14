# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fluPPuVWtnulDaEMw2V_2cyppJRl102X
"""

#  Imported basic Liberaries used for any algorithm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import dataset
dataset = pd.read_csv('language_detection.csv')
train_data = dataset.iloc[:,:-1]
y_train = dataset.iloc[:,-1]

# Import re liberary for removing extra elements from the strings or to tokenize the string
import re
#  nitk liberary for Reduce words to their stems and to 
# remove some common words like the,in,is etc from the string which are of no use
import nltk
nltk.download('stopwords')
# Stopword remove unnecessary words like the,is,not etc
from nltk.corpus import stopwords
# PorterStemmer reduces word to their stems
from nltk.stem.porter import PorterStemmer

# Corpus is a list containing all filtered strings
corpus = []
for i in range(0, 22000):
    review = dataset['Text'][i]
    review = review.lower() # Convert uppercase letter in small case letters
    review = review.split() # spilts each word and make array
    ps = PorterStemmer() 
    review = [ps.stem(word) for word in review] # passes each word from ps.stem() to reduce words to there stems
    review = ' '.join(review) # join words to recombine string
    corpus.append(review) # append filtered string in corpus

#  Import CountVectorizer from sklearn liberary used to convert strings into BOWs array
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 3000)
X = cv.fit_transform(corpus).toarray()

y_y = dataset.iloc[:,-1].values
#  LabelEncoding used to convert column into vectors without increasing the number of column
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y_y)
print(y)

#  dictionary to save each language where key value of languages is equal to there LabelEncoding vectored value
dic_result = {}
for i in range(len(y)):
    dic_result[y[i]] = y_y[i]

print(dic_result)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

Uses Knn neighbourer algorithm
# from sklearn.neighbors import KNeighborsClassifier
# classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
# classifier.fit(X_train, y_train)
# 84 % accuracy
Uses Logistic regression algorithm
# from sklearn.linear_model import LogisticRegression
# classifier = LogisticRegression(random_state = 0)
# classifier.fit(X_train, y_train)
# 93.33 % accuracy

Uses SVM algorithm
# from sklearn.svm import SVC
# classifier = SVC(kernel = 'linear', random_state = 0)
# classifier.fit(X_train, y_train)
# 93.22

# Uses decision tree algorithm
# from sklearn.tree import DecisionTreeClassifier
# classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
# classifier.fit(X_train, y_train)
# 91.05 %

Uses random forest algorithm
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)
# 92.79

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
accuracy_score(y_test, y_pred)

# Test string
# text_ = "?? ???? ?????????? ?????? ?????????????????????? ?????????????????? ?????????????????????? ?????????????? ?????? ???????????????????????????? ???????????????????? ??????????, ?????????? ?????????????????? ??????, ???????? ???????? ???????? ?????? ????????

# print(text_)
# text_ = re.sub(r'[!@#$(),"%^*?:;~`0-9]', ' ', text_)
# text_ = re.sub(r'[[]]', ' ', text_)
# text_ = text_.lower()
# text_ = text_.split()
# text_ = [ps.stem(word) for word in text_]
# text_ = ' '.join(text_)
# print(text_)

# text = [text_]
# X_test = cv.transform(text)

# y_pred = classifier.predict(X_test.toarray())
# print(y_pred)
# print(dic_result[y_pred[0]])

