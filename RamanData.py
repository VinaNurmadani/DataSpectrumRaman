# -*- coding: utf-8 -*-
"""Untitled34.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RSxGM7lAZl3M_DZJ0pWAvkEdR0D6ViGN
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Step 1: Read and preprocess data
def read_data(file_prefix, start_num, end_num):
    data = []
    for i in range(start_num, end_num + 1):
        if i not in [20, 27, 28, 29, 30, 33, 40]:  # Skip missing files
            file_path = f'{file_prefix}{i}.txt'
            file_data = pd.read_csv(file_path, delimiter='\t', header=None, names=['wavelength', 'intensity'])
            data.append(file_data)
    return data

plb_data = read_data('PLB', 1, 43)
m_data = read_data('M', 11, 49)
l_data = read_data('L', 11, 49)
lbs_data = read_data('LBS', 1, 164)
lb_data = read_data('LB', 11, 49)

target_names = ['L', 'LB', 'LBS', 'M','PLB']
labels_names = [0,1,2,3,4]

# Step 2: Feature Extraction
def extract_features(data_list):
    features = []
    for data in data_list:
        # Example: Calculating mean intensity
        mean_intensity = np.mean(data['intensity'])
        features.append([mean_intensity])
    return features

plb_features = extract_features(plb_data)
m_features = extract_features(m_data)
l_features = extract_features(l_data)
lbs_features = extract_features(lbs_data)
lb_features = extract_features(lb_data)

# Combine features
data_features = plb_features + m_features + l_features + lbs_features + lb_features

# Combine labels
labels = np.array(['PLB'] * len(plb_features) + ['M'] * len(m_features) + ['L'] * len(l_features) + ['LBS'] * len(lbs_features) + ['LB'] * len(lb_features))

# Step 3: Modeling
X_train, X_test, y_train, y_test = train_test_split(data_features, labels, test_size=0.2, random_state=42)

#Random Forest

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred_RF = model.predict(X_test)
accuracy_RF = accuracy_score(y_test, y_pred_RF)
classification_rep_RF = classification_report(y_test, y_pred_RF)
conf_matrix_RF = confusion_matrix(y_test, y_pred_RF)

print("Accuracy:", accuracy_RF)
print("Classification Report:\n", classification_rep_RF)
print("Confusion Matrix:\n", conf_matrix_RF)

disp = ConfusionMatrixDisplay(conf_matrix_RF, display_labels=target_names)
disp.plot(cmap=plt.cm.Blues, xticks_rotation=45)
plt.tight_layout()
plt.show()

#KNN

classifier_KNN = KNeighborsClassifier(n_neighbors=2,p=2,algorithm='auto',weights='uniform')
model_KNN = classifier_KNN.fit(X_train,y_train)
y_pred_KNN=model_KNN.predict(X_test)

accuracy_KNN = accuracy_score(y_test, y_pred_KNN)
classification_rep_KNN = classification_report(y_test, y_pred_KNN)
conf_matrix_KNN = confusion_matrix(y_test, y_pred_KNN)

print("Accuracy:", accuracy_KNN)
print("Classification Report:\n", classification_rep_KNN)
print("Confusion Matrix:\n", conf_matrix_KNN)

disp = ConfusionMatrixDisplay(conf_matrix_KNN, display_labels=target_names)
disp.plot(cmap=plt.cm.Blues, xticks_rotation=45)
plt.tight_layout()
plt.show()

#Decision Tree

classifier_DT = DecisionTreeClassifier(max_depth = 3)
model_DT = classifier_DT.fit(X_train, y_train)
y_pred_DT = model_DT.predict(X_test)

accuracy_DT = accuracy_score(y_test, y_pred_DT)
classification_rep_DT = classification_report(y_test, y_pred_DT)
conf_matrix_DT = confusion_matrix(y_test, y_pred_DT)

print("Accuracy:", accuracy_DT)
print("Classification Report:\n", classification_rep_DT)
print("Confusion Matrix:\n", conf_matrix_DT)

disp = ConfusionMatrixDisplay(conf_matrix_DT, display_labels=target_names)
disp.plot(cmap=plt.cm.Blues, xticks_rotation=45)
plt.tight_layout()
plt.show()