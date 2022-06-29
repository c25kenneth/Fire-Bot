import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.utils import shuffle

df = pd.read_csv("forestfires.csv")
df = df.drop(["month", "day", "FFMC", "DMC", "DC", "ISI"], 1)

print(df)

X = np.array(df.drop(["area"], 1))
y = np.array(df["area"])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

model = linear_model.LinearRegression()

model.fit(X_train, y_train)
acc = model.score(X_test, y_test)

pickle_in = open('app/model.pickle', 'rb')
linear = pickle.load(pickle_in)

pred = linear.predict([ [7, 5, 8.2, 51, 6.7, 0.0] ])
print(pred)