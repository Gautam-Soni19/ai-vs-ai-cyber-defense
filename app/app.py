import sys
import os
import csv
import subprocess
import pandas as pd
import streamlit as st
import joblib

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from attacker.mutator import mutate, mutate_with_trace, payloads

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(
    page_title="AI vs AI Cyber Defense System",
    page_icon="🛡️",
    layout="wide"
)

# ---------------------------
# Paths
# ---------------------------
MODEL_PATH = "models/defender_model.joblib"
LOG_FILE = "logs/attack_log.csv"

# ---------------------------
# Helper functions
# ---------------------------
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

def ensure_log_file():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["original", "mutated", "prediction", "result"])

def run_simulation():
    model = load_model()
    results = []

    for original in payloads:
        mutated, techniques_applied = mutate_with_trace(original)
        prediction = model.predict([mutated])[0]

        if prediction == "malicious":
            result = "Blocked"
        else:
            result = "Bypassed"

        results.append({
            "original": original,
            "mutated": mutated,
            "prediction": prediction,
            "result": result,
            "techniques": techniques_applied
        })

        with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([original, mutated, prediction, result])

    return results

def predict_custom_payload(user_payload):
    model = load_model()
    prediction = model.predict([user_payload])[0]
    return prediction

def get_logs():
    ensure_log_file()
    try:
        return pd.read_csv(LOG_FILE)
    except Exception:
        return pd.DataFrame(columns=["original", "mutated", "prediction", "result"])

# ---------------------------
# Start app
# ---------------------------
ensure_log_file()

st.title("🛡️ AI vs AI Cyber Defense System")
st.caption("Attacker mutates cyber payloads. Defender AI analyzes and blocks them.")

st.markdown("""
This project simulates a basic **AI vs AI cybersecurity workflow**:

- **Attacker module** creates mutated XSS and SQL Injection payloads
- **Defender model** classifies them as benign or malicious
- **Logs** store attack attempts
- **Retraining** helps the defense improve over time
""")

# ---------------------------
# Top metrics
# ---------------------------
logs_df = get_logs()

total_tested = len(logs_df)
blocked_count = len(logs_df[logs_df["result"] == "Blocked"]) if not logs_df.empty else 0
bypassed_count = len(logs_df[logs_df["result"] == "Bypassed"]) if not logs_df.empty else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total Logged Attacks", total_tested)
col2.metric("Blocked", blocked_count)
col3.metric("Bypassed", bypassed_count)

st.divider()

# ---------------------------
# Run simulation section
# ---------------------------
st.subheader("⚔️ Run Attack Simulation")

if st.button("Run Full Simulation"):
    results = run_simulation()
    st.success("Simulation completed successfully.")

    for i, item in enumerate(results, start=1):
        with st.container():
            st.markdown(f"### Attack #{i}")
            c1, c2 = st.columns(2)

            with c1:
                st.markdown("**Original Payload**")
                st.code(item["original"], language="html")

            with c2:
                st.markdown("**Mutated Payload**")
                st.code(item["mutated"], language="html")

            c3, c4 = st.columns(2)
            with c3:
                st.markdown(f"**Prediction:** `{item['prediction']}`")
            with c4:
                if item["result"] == "Blocked":
                    st.markdown("**Result:** ✅ Blocked")
                else:
                    st.markdown("**Result:** ❌ Bypassed")

            st.markdown("**Mutation Techniques Applied:**")
            st.write(", ".join(item["techniques"]))

            st.divider()

# ---------------------------
# Custom payload tester
# ---------------------------
st.subheader("🧪 Test Your Own Payload")

user_payload = st.text_area(
    "Enter a custom payload or normal input:",
    placeholder="Example: <script>alert(1)</script> or hello world"
)

if st.button("Test Custom Payload"):
    if user_payload.strip():
        prediction = predict_custom_payload(user_payload)

        if prediction == "malicious":
            st.error(f"Prediction: {prediction} → Blocked")
        else:
            st.success(f"Prediction: {prediction} → Allowed / Possible Bypass")
    else:
        st.warning("Please enter a payload first.")

st.divider()

# ---------------------------
# Retrain section
# ---------------------------
st.subheader("🔁 Retrain Defender")

st.write("Use logged mutated attacks to retrain the defender model.")

if st.button("Retrain Model"):
    try:
        result = subprocess.run(
            [sys.executable, "defender/retrain_model.py"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            load_model.clear()
            st.success("Model retrained successfully.")
            st.text(result.stdout)
        else:
            st.error("Retraining failed.")
            st.text(result.stderr)

    except Exception as e:
        st.error(f"Error during retraining: {e}")

st.divider()

# ---------------------------
# Recent logs section
# ---------------------------
st.subheader("📄 Recent Attack Logs")

logs_df = get_logs()

if not logs_df.empty:
    st.dataframe(logs_df.tail(10), use_container_width=True)
else:
    st.info("No attack logs available yet.")

# ---------------------------
# Footer
# ---------------------------
st.divider()
st.markdown("Built as a prototype for AI vs AI cybersecurity simulation.")