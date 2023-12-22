# Imports
import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder

print('> Importing data...')

# Dataset importing
dataset = pd.read_csv('dataset/diabetes_prediction_dataset.csv')


# Utilities
def column_names(dataframe):
    return [key for key in dataframe.columns]


# ==============
# Pre processing
# ==============

print('> Processing data...')

# Gender normalization
gender_encoder = LabelEncoder()
gender_label = gender_encoder.fit_transform(dataset['gender'])

dataset['gender'] = gender_label
dataset.gender.value_counts()

# Smoking history normalization
smoking_encoder = LabelEncoder()
smoking_label = smoking_encoder.fit_transform(dataset['smoking_history'])

dataset['smoking_history'] = smoking_label
dataset.smoking_history.value_counts()

# Normalization
for column in column_names(dataset):
    X = np.array(dataset[column]).reshape(-1, 1)

    scaler = MinMaxScaler()
    scaler.fit(X)

    dataset[column] = scaler.transform(X).reshape(1, -1)[0]

# ==============
# Dataset saving
# ==============

print('> Saving dataset...')

pickle.dump(dataset, open('objects/dataset.pkl', 'wb'))

# ==============
# Training
# ==============

print('> Starting training...')

X = dataset.drop('diabetes', axis=1)
y = dataset.diabetes

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# ==============
# Saving model
# ==============

print('> Saving model...')

pickle.dump(model, open('objects/model.pkl', 'wb'))

print('> Model saved.')
