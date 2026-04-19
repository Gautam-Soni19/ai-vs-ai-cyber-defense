import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

# Step 1: Load original dataset
dataset = pd.read_csv("data/dataset.csv")

# Step 2: Load attack logs
logs = pd.read_csv("logs/attack_log.csv")

# Step 3: Create new malicious rows from mutated payloads
new_data = pd.DataFrame({
    "text": logs["mutated"],
    "label": "malicious"
})

# Step 4: Merge old + new data
updated_dataset = pd.concat([dataset, new_data], ignore_index=True)

# Step 5: Remove duplicate rows
updated_dataset = updated_dataset.drop_duplicates()

# Step 6: Save updated dataset back
updated_dataset.to_csv("data/dataset.csv", index=False)

print(f"Updated dataset size: {len(updated_dataset)} rows")

# Step 7: Split into X and y
X = updated_dataset["text"]
y = updated_dataset["label"]

# Step 8: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Step 9: Create pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer(analyzer="char", ngram_range=(2, 5), lowercase=True)),
    ("clf", LinearSVC())
])

# Step 10: Train model
model.fit(X_train, y_train)

# Step 11: Evaluate model
accuracy = model.score(X_test, y_test)
print(f"Retrained Model Accuracy: {accuracy:.2f}")

y_pred = model.predict(X_test)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Step 12: Save updated model
joblib.dump(model, "models/defender_model.joblib")

print("Retrained model saved successfully!")