# Project 05: Streamlit Interactive ML Web App

A small web app around the Titanic decision tree from Project 04. Choose ticket class, sex, age and fare, press **Predict**, and see the estimated chance of survival.

## Files
- `app.py`: the Streamlit app (cached model loading, input validation, friendly error messages, caption).
- `requirements.txt`: packages for deployment.
- `model.joblib`: created by running the Project 04 notebook (it is copied here automatically).

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
Use `streamlit run`, not `python app.py`. The app opens at http://localhost:8501.

## Deploy (free, Streamlit Community Cloud)
1. Run the Project 04 notebook so `project05/model.joblib` exists.
2. Check `model.joblib` and `requirements.txt` are committed in the repo.
3. If the deploy fails with a version warning, pin your versions in `requirements.txt`. Find them with `pip show scikit-learn streamlit pandas joblib`, then write lines like `scikit-learn==1.7.2`, and retrain the model with the same version.
4. At https://share.streamlit.io choose the repo, branch `main`, and main file `project05/app.py`.
5. Open the public link on your phone to test it.

*Educational example only. It describes a historical dataset and is not advice.*
