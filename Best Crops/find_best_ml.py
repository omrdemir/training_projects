# All required libraries are imported here for you.
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load the dataset
ekin = pd.read_csv("soil_measures.csv")

# Write your code here





# print(ekin.isna().sum())      # eksik veri kontorlu
# print(ekin["crop"].unique())     # ekinlerin tipleri


X = ekin.drop(columns="crop") # N P K ph
#print(X)

y = ekin["crop"] # tahmin edilecek ekin
#print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=30)

feature_perf = {} # her bir ozelligin puanini tutacak

for feature in ["N", "P", "K", "ph"]:
    
    model = LogisticRegression(multi_class="multinomial") # model olusturma

    model.fit(X_train[[feature]], y_train) # dongudeki ozellikle modeli egitme

    preds = model.predict(X_test[[feature]]) # tahminler

    f1 = metrics.f1_score(y_test, preds, average="weighted") # tahminleri karsilasitirp her birinin f1 skoru cikarma

    feature_perf[feature] = f1

    print(f"{feature}, f1 score: {f1}\n")

    
best_predictive_feature = {'K': feature_perf["K"]}
print(best_predictive_feature)

    