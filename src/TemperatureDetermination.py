import json

from logging import getLogger, config
logger = getLogger(__name__)
with open("log_config.json", "r") as f:
    config.dictConfig(json.load(f))

class TemperatureDetermination:
    '''
    入力温度感覚、温度感覚カテゴリはAI実装後は削除する。
    デフォルトの値は現在は仮の値とする。
    ACCS-SERVERより外部気温が入力される。
    '''
    input_temperature = 25.0  #入力温度
    input_temperature_sense = "2"   #入力温度感覚（0~4の値）
    d_temperature = 0.0 #SENS_CATEGORY[input_temperature_sense]
    SENS_CATEGORY = {"0":-5.0, "1":-3.0, "2":0.0, "3":3.0, "4":5.0} #温度感覚カテゴリ

    def __init__(self,input_temperature,input_temperature_sense):
        try:
            if((input_temperature < -20) | (input_temperature > 60)): #最低温度は要件定義に従う
                raise ValueError()
            self.input_temperature = float(input_temperature)
            self.input_temperature_sense = str(input_temperature_sense)
            self.d_temperature = self.SENS_CATEGORY[self.input_temperature_sense]
        except ValueError:
            #範囲外の温度が入力された場合デフォルト値の25.0になる
            self.input_temperature = 25.0
            logger.info("Temperature is out of range.")
        except KeyError:
            self.input_temperature_sense = "2"
            logger.info("No such temperature sense.")

               
    def decision_base(self):
        output = self.input_temperature + self.d_temperature
        return output

