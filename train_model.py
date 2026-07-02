import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("placement_dataset.csv")

# Separate Features and Target
X = df.drop(columns=["Student_ID", "Placement"])
y = df["Placement"]

# Label Encoders
label_encoders = {}

categorical_columns = ["Gender", "Department"]

for col in categorical_columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

target_encoder = LabelEncoder()
y = target_encoder.fit_transform(y)
label_encoders["Placement"] = target_encoder

# Scale Data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

# Train KNN
model = KNeighborsClassifier(
    n_neighbors=5,
    metric="minkowski"
)

model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)
accuracy = accuracy_score(y_test, pred)

print(f"Model Accuracy: {accuracy*100:.2f}%")

# Save Files
joblib.dump(model, "knn_model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(label_encoders, "label_encoders.pkl")

print("knn_model.pkl saved")
print("scaler.pkl saved")
print("label_encoders.pkl saved")