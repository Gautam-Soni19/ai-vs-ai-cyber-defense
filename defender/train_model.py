import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

# Step 1: Load dataset
data = pd.read_csv("data/dataset.csv")

# Step 2: Split into input (X) and labels (y)
X = data["text"]
y = data["label"]

# Step 3: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Step 4: Create pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer(analyzer="char", ngram_range=(2, 5), lowercase=True)),
    ("clf", LinearSVC())
])

# Step 5: Train model
model.fit(X_train, y_train)

# Step 6: Evaluate
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy:.2f}")

y_pred = model.predict(X_test)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Step 7: Save model
joblib.dump(model, "models/defender_model.joblib")

print("Model saved successfully!")