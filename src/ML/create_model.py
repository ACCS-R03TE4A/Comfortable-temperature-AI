import pandas as pd
from sklearn.linear_model import LinearRegression as LR
from sklearn.model_selection import train_test_split
import pickle
def create_model():
    #データの読み込みは未定
    data = pd.read_csv('temp2.csv')
    model = LR(fit_intercept = True, normalize = False, copy_X = True, n_jobs = 1)
    X, Y = data.loc[:,['tActual','tInside','tOutside']].values , data['tSuitable'].values
    X_train, Y_train = train_test_split(X, Y, test_size=0.3, random_state=20)
    model.fit(X_train, Y_train)
    #モデルをファイルに書き出す
    filename = 'model.sav'
    pickle.dump(model, open(filename, 'wb'))
    print("saved model") 