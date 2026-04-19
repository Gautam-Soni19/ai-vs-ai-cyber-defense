import joblib
import csv
import os
from attacker.mutator import mutate, payloads

# Load model
model = joblib.load("models/defender_model.joblib")

# Create log file if not exists
log_file = "logs/attack_log.csv"

if not os.path.exists(log_file):
    with open(log_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["original", "mutated", "prediction", "result"])

print("=== AI vs AI Simulation ===\n")

for original in payloads:
    mutated = mutate(original)

    prediction = model.predict([mutated])[0]

    if prediction == "malicious":
        result = "Blocked"
        symbol = "✅"
    else:
        result = "Bypassed"
        symbol = "❌"

    print(f"Original : {original}")
    print(f"Mutated  : {mutated}")
    print(f"Prediction: {prediction}")
    print(f"Result   : {symbol} {result}\n")

    # Save to log
    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([original, mutated, prediction, result])