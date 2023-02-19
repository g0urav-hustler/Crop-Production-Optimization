# Making logistic regression model
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# reading data froam
df = pd.read_csv("data/agricultural_data.csv")


## Feature Scaling

# getting feature to be scalled 
feature_scale = [feature for feature in df.columns if feature != "Crops"]

# fitting and transforming the model
scaler = StandardScaler()
trans_df = scaler.fit_transform(df[feature_scale])

# making scalled dataframe and concating the target variable
model_df = pd.concat([pd.DataFrame(trans_df, columns= feature_scale), df["Crops"]], axis= 1)

# spliting the model
x_train, x_test, y_train, y_test = train_test_split(model_df.drop("Crops", axis = 1), model_df["Crops"],test_size= 0.2, random_state= 0)


## Model fitting
log_regr = LogisticRegression()
log_regr.fit(x_train,y_train)
# predicting crops value
y_predict = log_regr.predict(x_test)


# getting scores of models
print("Accruacy of model =", log_regr.score(x_test, y_test))

print("Classification Report")
# classification report
print(classification_report(y_test,y_predict))
# open a file where model has to save
regr_file = open("models/logistic_regression_model.pkl", "wb")

# dumping model
pickle.dump(log_regr, regr_file)

# closing file
regr_file.close()
