from pathlib import Path
import joblib
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

FEATURES = ["pclass", "sex", "age", "fare"]
df = sns.load_dataset("titanic")[["survived"] + FEATURES].dropna()
df["sex"] = (df["sex"] == "female").astype(int)
X, y = df[FEATURES], df["survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
model = DecisionTreeClassifier(max_depth=4, random_state=42).fit(X_train, y_train)

path = Path(__file__).parent / "model.joblib"   # always saves next to this script
joblib.dump(model, path)
print("Saved to", path, "| test accuracy:", round(model.score(X_test, y_test), 3))