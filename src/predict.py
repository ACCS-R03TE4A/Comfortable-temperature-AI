import pandas as pd
import pickle
from logging import getLogger, config
import json

logger = getLogger(__name__)
with open("../log_config.json", "r") as f:
    config.dictConfig(json.load(f))

def predict(tActual,tInside,tOutside):
    #モデルのファイルを読み込む
    loaded_model = pickle.load(open('model.sav', 'rb'))
    result = loaded_model.predict(pd.DataFrame([[tActual,tInside,tOutside]]))
    logger.info(result)
    return result