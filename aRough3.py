import pandas as pd

data = pd.read_csv("Dataset.csv")
print("DATA::")
print(data)
print()

data["Gender"].replace("Male", 1, inplace=True)
data["Gender"].replace("Female", 0, inplace=True)

head = data.head()
print("HEAD::")
print(head)
print()

X = data.drop("Purchased", axis=1)
y = data["Purchased"]
print("LEN X AND Y::")
print(len(X), len(y))

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
model = GaussianNB()

print("MODEL.FIT RESULT:")
print(model.fit(X_train, y_train))
print("MODEL.SCORE RESULT:")
print(model.score(X_test, y_test))
print()

y_preds = model.predict(X_test)
print("PREDICTION RESULT")
print(y_preds)
