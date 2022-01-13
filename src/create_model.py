import pandas as pd
from sklearn.linear_model import LinearRegression as LR
from sklearn.model_selection import train_test_split
import pickle
import json

from logging import getLogger, config
logger = getLogger(__name__)
with open("../log_config.json", "r") as f:
    config.dictConfig(json.load(f))


def create_model():
    #データの読み込みは未定
    data = pd.read_csv('../input/temp2.csv')
    model = LR(fit_intercept = True, normalize = False, copy_X = True, n_jobs = 1)
    X, Y = data.loc[:,['tActual','tInside','tOutside']].values , data['tSuitable'].values
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=20)
    model.fit(X_train, Y_train)
    #モデルをファイルに書き出す
    filename = 'model.sav'
    pickle.dump(model, open(filename, 'wb'))
    logger.info("saved model")