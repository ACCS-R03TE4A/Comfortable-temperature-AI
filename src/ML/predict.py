import pandas as pd
import pickle

def predict(tActual,tInside,tOutside):
    #モデルのファイルを読み込む
    loaded_model = pickle.load(open('model.sav', 'rb'))
    result = loaded_model.predict(pd.DataFrame([[tActual,tInside,tOutside]]))
    print(result)
    return result