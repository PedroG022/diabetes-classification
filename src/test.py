import pickle
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import metrics

dataset = pickle.load(open('objects/dataset.pkl', 'rb'))
model = pickle.load(open('objects/model.pkl', 'rb'))

X = dataset.drop('diabetes', axis=1)
y = dataset.diabetes

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

y_pred = model.predict(X_test)

print(pd.crosstab(y_test, y_pred, rownames=['Real'], colnames=['Predito'], margins=True))
print('\n')
print(metrics.classification_report(y_test, y_pred))
