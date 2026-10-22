"""
Project 05 - Interactive ML Web App (Streamlit)
Run locally:  streamlit run app.py
Needs model.joblib in the same folder (created by the Project 04 notebook).
"""
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

MODEL_PATH = Path(__file__).parent / "model.joblib"   # works locally and on Streamlit Cloud
FEATURES = ["pclass", "sex", "age", "fare"]            # SAME order as in training (Project 04)

st.set_page_config(page_title="Titanic Survival Predictor", page_icon="🚢")


@st.cache_resource
def load_model():
    """Load the model once so it is not reloaded on every click."""
    return joblib.load(MODEL_PATH)


def validate(pclass, sex, age, fare):
    """Return a friendly message if the input is invalid, otherwise None."""
    if pclass not in (1, 2, 3):
        return "Ticket class must be 1, 2 or 3."
    if sex not in ("female", "male"):
        return "Please choose female or male."
    if not 1 <= age <= 80:
        return "Age must be between 1 and 80."
    if not 0 <= fare <= 500:
        return "Fare must be between 0 and 500."
    return None


st.title("🚢 Would this passenger have survived?")
st.write("An educational model (a decision tree) trained on the Titanic passenger list. "
         "Choose a passenger's details and press **Predict**.")

pclass = st.selectbox("Ticket class", [1, 2, 3])
sex = st.radio("Sex", ["female", "male"], horizontal=True)
age = st.slider("Age", 1, 80, 30)
fare = st.slider("Fare paid", 0, 500, 30)

if st.button("Predict"):
    problem = validate(pclass, sex, age, fare)
    if problem:
        st.warning(problem)
        st.stop()

    try:
        model = load_model()
    except FileNotFoundError:
        st.error("The model file is missing. Run the Project 04 notebook to train and save "
                 "`model.joblib`, then put it next to this app.")
        st.stop()
    except Exception:
        st.error("The model file could not be loaded. Retrain it with the same scikit-learn "
                 "version that this app uses.")
        st.stop()

    row = pd.DataFrame([[pclass, 1 if sex == "female" else 0, age, fare]], columns=FEATURES)
    try:
        chance = model.predict_proba(row)[0][1]
    except Exception:
        st.error("Something went wrong while making the prediction. Please try different inputs.")
        st.stop()

    st.metric("Estimated chance of survival", f"{chance:.0%}")
    st.progress(float(chance))
    st.write("The model leans towards **survived**." if chance >= 0.5
             else "The model leans towards **did not survive**.")
    st.caption("A learning exercise. It describes a historical dataset and is not advice.")
