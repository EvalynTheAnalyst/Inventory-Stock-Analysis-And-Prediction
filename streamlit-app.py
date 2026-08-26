import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Stockout Predictor", page_icon="📦", layout="wide")

st.markdown(
    """
    <style>
    .main { background-color: #0e1117; }
    h1 { color: #4CAF50; }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📦 Stockout Risk Predictor")
st.write("Upload your inventory data and get instant stockout risk predictions.")

API_URL = "https://stockout-api.onrender.com/predict-batch"

RISK_LABELS = {0: "Safe", 1: "Caution", 2: "Critical"}
RISK_COLORS = {0: "#ccffcc", 1: "#fff3cd", 2: "#ffcccc"}

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    if st.button("Run Prediction", type="primary"):
        with st.spinner("Running predictions..."):
            response = requests.post(API_URL, files={"file": uploaded_file})

        if response.status_code == 200:
            data = response.json()

            if "error" in data:
                st.error(data["error"])
            else:
                results = pd.DataFrame(data)
                results["prediction"] = results["prediction"].astype(int)
                results["risk_label"] = results["prediction"].map(RISK_LABELS)

                st.success("Prediction complete!")

                total = len(results)
                safe = (results["prediction"] == 0).sum()
                caution = (results["prediction"] == 1).sum()
                critical = (results["prediction"] == 2).sum()

                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Total Items", total)
                col2.metric("✅ Safe", safe)
                col3.metric("⚠️ Caution", caution)
                col4.metric("🚨 Critical", critical)

                def highlight_risk(row):
                    color = RISK_COLORS[row["prediction"]]
                    return [f"background-color: {color}"] * len(row)

                st.dataframe(
                    results.style.apply(highlight_risk, axis=1),
                    use_container_width=True
                )
        else:
            st.error(f"Something went wrong: {response.status_code}")
