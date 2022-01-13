import json
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression as LR
from sklearn.model_selection import train_test_split
from Comfortable_temperature_AI.db.create_predict_temp import get_temp
from Comfortable_temperature_AI.db.create_csv import TensorGenerater
import math

from logging import getLogger, config
logger = getLogger(__name__)
with open("log_config.json", "r") as f:
    config.dictConfig(json.load(f))

class ComfortTemperaturePredictionAI:
    '''
    入力温度感覚、温度感覚カテゴリはAI実装後は削除する。
    デフォルトの値は現在は仮の値とする。
    ACCS-SERVERより外部気温が入力される。
    '''

    SENS_CATEGORY = {"0":-2.0, "1":-1.0, "2":0.0, "3":1.0, "4":2.0} #温度感覚カテゴリ

    def __init__(self):
        #モデルのファイルを読み込む
        try:
            self.model = pickle.load(open('model.sav', 'rb'))
        except FileNotFoundError:
            self.create_model()

    def getTargetTemperature(self, input_temperature_sense):
        d_temperature = None
        latest_temp = get_temp()
        print(latest_temp)
        try:
            if((latest_temp["tActual"].Temperature < -20) | (latest_temp["tActual"].Temperature > 60)): #最低温度は要件定義に従う
                raise ValueError()
            d_temperature = self.SENS_CATEGORY[input_temperature_sense]
        except ValueError:
            #範囲外の温度が入力された場合デフォルト値の25.0になる
            latest_temp["tActual"] = 25
            logger.info("Temperature is out of range.")
        except KeyError:
            d_temperature = 0
            logger.info("No such temperature sense.")
        input_temperature_sense = str(input_temperature_sense)
        predicated = self.predict(latest_temp)
        if(abs(predicated - latest_temp["tActual"].Temperature) >= 3):
            output = predicated
        else:
            output = latest_temp["tActual"].Temperature + d_temperature
        return output
    
    def predict(self, temps):
        result = self.model.predict(pd.DataFrame([[ temps["tActual"].Temperature, temps["InsideTemp"].Temperature,temps["OutsideTemp"].Temperature]]))
        logger.info(result)
        return result
    
    def create_model(self):
        #データの読み込みは未定
        try:
            data = pd.read_csv('Learn.csv')
        except FileNotFoundError:
            tg = TensorGenerater()
            data = tg.generate()
        print(data)
        model = LR(fit_intercept = True, normalize = False, copy_X = True, n_jobs = 1)
        X, Y = data.loc[:,['tActual','tInside','tOutside']].values , data['tSuitable'].values
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=20)
        model.fit(X_train, Y_train)
        #モデルをファイルに書き出す
        filename = 'model.sav'
        pickle.dump(model, open(filename, 'wb'))
        logger.info("saved model")
        self.model = model