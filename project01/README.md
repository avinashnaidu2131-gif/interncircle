# Project 01: Exploratory Data Analysis (EDA) on Titanic

Cleans the Titanic passenger data with pandas and answers three questions written up front: did women survive more than men, did ticket class matter, and was age related to survival?

## Files
- `project01_titanic_eda.ipynb`: the notebook (questions, cleaning with reasons, groupings, answers, summary).
- `project01_titanic_eda.html`: the same notebook exported to HTML.

## Run
```bash
pip install pandas seaborn jupyter
jupyter notebook project01_titanic_eda.ipynb     # or open it in VS Code and click Run All
```
The dataset downloads on first run (`sns.load_dataset("titanic")`), so you need internet.

## Findings
- Women survived at about 74% versus about 19% for men.
- Survival fell from about 63% in first class to about 24% in third class.
- Children (12 and under) had the best survival rate by age, about 58%.

These are associations, not proof of cause.
