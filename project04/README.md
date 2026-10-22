# Project 04: First Machine Learning Classifier

Predicts whether a Titanic passenger survived from class, sex, age and fare, using a scikit-learn Decision Tree. Uses a stratified 80/20 train/test split, compares against a baseline, explains the confusion matrix, shows overfitting across tree depths 1 to 12, and states limitations.

## Files
- `project04_ml_classifier.ipynb` / `.html`: the notebook.
- `confusion_matrix.png`, `depth_vs_accuracy.png`, `feature_importance.png`: charts.
- `model.joblib`: created when you run the notebook (also copied to `../project05/` if that folder exists).

## Run
```bash
pip install pandas seaborn matplotlib scikit-learn joblib jupyter
jupyter notebook project04_ml_classifier.ipynb     # run all cells
```
**Run this before Project 05**, because the app loads the model saved here.
