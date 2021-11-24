class TemperatureDetermination:
    '''
    入力温度感覚、温度感覚カテゴリはAI実装後は削除する。
    デフォルトの値は現在は仮の値とする。
    ACCS-SERVERより外部気温が入力される。
    '''
    input_temperature = 25.0  #入力温度
    input_temperature_sense = "3"   #入力温度感覚（1~5の値）
    d_temperature = 0.0 #SENS_CATEGORY[input_temperature_sense]
    SENS_CATEGORY = {"1":-5.0, "2":-3.0, "3":0.0, "4":2.0, "5":5.0} #温度感覚カテゴリ

    def __init__(self,input_temperature,input_temperature_sense):
        try:
            if((input_temperature < 5) | (input_temperature > 50)): #最低温度は要件定義に従う
                raise ValueError()
            self.input_temperature = float(input_temperature)
            self.input_temperature_sense = str(input_temperature_sense)
            self.d_temperature = self.SENS_CATEGORY[self.input_temperature_sense]
        except ValueError:
            #範囲外の温度が入力された場合デフォルト値の25.0になる
            self.input_temperature = 25.0
            print("Temperature is out of range.")
        except KeyError:
            self.input_temperature_sense = "3"
            print("No such temperature sense.")

               
    def decision_base(self):
        output = self.input_temperature + self.d_temperature
        return output

