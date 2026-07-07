import os
print("Current directory:", os.getcwd())

# =========================
# 1. IMPORT LIBRARIES
# =========================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# =========================
# 2. LOAD DATASET
# =========================

data = pd.read_csv("Churn_Modelling.csv")

print("First 5 rows:")
print(data.head())

print("\nDataset Info:")
print(data.info())

# =========================
# 3. DATA CLEANING
# =========================

# Drop columns not useful for prediction
data = data.drop(["RowNumber", "CustomerId", "Surname"], axis=1)

print("\nColumns after dropping unnecessary ones:")
print(data.columns)

# =========================
# 4. ENCODING CATEGORICAL DATA
# =========================

# Convert Gender to numeric
le = LabelEncoder()
data["Gender"] = le.fit_transform(data["Gender"])

# One-hot encode Geography
data = pd.get_dummies(data, columns=["Geography"], drop_first=True)

print("\nAfter Encoding:")
print(data.head())

# =========================
# 5. DEFINE FEATURES & TARGET
# =========================

X = data.drop("Exited", axis=1)
y = data["Exited"]

print("\nFeature Shape:", X.shape)
print("Target Shape:", y.shape)

# =========================
# 6. TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# 7. FEATURE SCALING
# =========================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# =========================
# 8. TRAIN MODEL
# =========================

model = RandomForestClassifier(n_estimators=100, random_state=42)

model.fit(X_train, y_train)

print("\nModel Training Completed.")

# =========================
# 9. MAKE PREDICTIONS
# =========================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Probability of churn
churn_prob = model.predict_proba(X_test)[:, 1]

print("\nSample Churn Probabilities:")
print(churn_prob[:10])

# =========================
# 10. CONFUSION MATRIX
# =========================

cm = confusion_matrix(y_test, y_pred)

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# =========================
# 11. FEATURE IMPORTANCE
# =========================

importances = model.feature_importances_
feature_names = X.columns

feature_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importances
}).sort_values(by="Importance", ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(x="Importance", y="Feature", data=feature_df)
plt.title("Feature Importance")
plt.show()

# =========================
# 12. CHURN DISTRIBUTION
# =========================

sns.countplot(x=y)
plt.title("Churn Distribution")
plt.show()

# =========================
# 13. SAVE FINAL REPORT
# =========================

final_report = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred,
    "Churn_Probability": churn_prob
})

final_report.to_csv("Final_Churn_Report.csv", index=False)

print("\nFinal report saved as CSV.")


import pandas as pd

data = pd.read_csv("Churn_Modelling.csv")

print(data.head())


#task
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,11)
width = 0.25

table_2 = [i * 2 for i in x]
table_3 = [i * 3 for i in x]

plt.bar(x - width, table_2, width, label = "table of 2")
plt.bar(x+ width, table_3, width, label = "table of 3")
plt.legend()
plt.gca().invert_xaxis()
plt.show()