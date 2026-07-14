import pandas as pd
from pathlib import Path
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
)

# ============================================================
# Project Paths
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR / "data" / "HR-Employee-Attrition.csv"

MODELS_DIR = BASE_DIR / "model"
MODELS_DIR.mkdir(exist_ok=True)

# ============================================================
# Load Dataset
# ============================================================

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_csv(DATA_PATH)

# ============================================================
# Dataset Information
# ============================================================

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# ============================================================
# Target Variable
# ============================================================

print("\nTarget Variable Distribution:")
print(df["Attrition"].value_counts())

print("\nTarget Percentage:")
print((df["Attrition"].value_counts(normalize=True) * 100).round(2))

# ============================================================
# Remove Constant Columns
# ============================================================

constant_columns = [
    col for col in df.columns
    if df[col].nunique() == 1
]

print("\nConstant Columns:")
print(constant_columns)

df.drop(columns=constant_columns, inplace=True)

# ============================================================
# Encode Categorical Columns
# ============================================================

label_encoders = {}

categorical_columns = df.select_dtypes(include=["object"]).columns

print("\nEncoding Categorical Columns...")

for column in categorical_columns:

    encoder = LabelEncoder()

    df[column] = encoder.fit_transform(df[column])

    label_encoders[column] = encoder

print("Encoding Completed Successfully!")

joblib.dump(
    label_encoders,
    MODELS_DIR / "label_encoders.pkl"
)

print("Label Encoders Saved!")

# ============================================================
# Save Clean Dataset
# ============================================================

OUTPUT_PATH = BASE_DIR / "data" / "clean_hr_data.csv"

df.to_csv(OUTPUT_PATH, index=False)

print("\nClean Dataset Saved!")

# ============================================================
# Select Features and Target
# ============================================================


selected_features = [

    "Age",

    "Department",

    "Gender",

    "OverTime",

    "JobLevel",

    "MonthlyIncome",

    "JobSatisfaction",

    "EnvironmentSatisfaction",

    "YearsAtCompany",

    "JobRole",

    "WorkLifeBalance",

    "TotalWorkingYears"

]


X = df[selected_features]

y = df["Attrition"]


print("\nSelected Features:")
print(selected_features)


print("\nFeature Shape:", X.shape)

print("Target Shape :", y.shape)

# ============================================================
# Train Test Split
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Samples:", X_train.shape[0])
print("Testing Samples :", X_test.shape[0])

# ============================================================
# Models
# ============================================================

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(
        random_state=42,
        n_estimators=200
    )
}

results = {}

print("\n" + "=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

best_accuracy = 0
best_model = None
best_model_name = ""

for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)

    results[name] = accuracy

    print("\n" + "-" * 50)
    print(name)
    print("-" * 50)

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model
        best_model_name = name

# ============================================================
# Save Best Model
# ============================================================

joblib.dump(
    best_model,
    MODELS_DIR / "attrition_model.pkl"
)
# Save model features

joblib.dump(
    selected_features,
    MODELS_DIR / "features.pkl"
)

print("Features Saved!")
print("\n" + "=" * 60)
print("BEST MODEL")
print("=" * 60)

print("Model :", best_model_name)
print("Accuracy :", round(best_accuracy * 100, 2), "%")

print("\nBest Model Saved Successfully!")

# ============================================================
# Classification Report
# ============================================================

predictions = best_model.predict(X_test)

print("\nClassification Report\n")

print(classification_report(y_test, predictions))

print("\nProject Completed Successfully!")

performance = {

    "model": best_model_name,

    "accuracy": round(best_accuracy*100,2),

    "precision": round(
        precision_score(
            y_test,
            predictions
        )*100,
        2
    ),

    "recall": round(
        recall_score(
            y_test,
            predictions
        )*100,
        2
    ),

    "f1": round(
        f1_score(
            y_test,
            predictions
        )*100,
        2
    )
}


joblib.dump(
    performance,
    MODELS_DIR / "model_results.pkl"
)