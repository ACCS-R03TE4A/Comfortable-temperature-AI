class TemperatureDetermination:
    input_temperature = -1.0  #入力温度
    input_temperature_sense = "3"   #入力温度感覚（1~5の値）
    output_temperature = -1.0 #出力温度

    def __init__(self,input_temperature,temperature_sense):
        try:
            if((input_temperature < 5) | (input_temperature > 50)):
                raise ValueError()
            self.input_temperature = float(input_temperature)
            self.temperature_sense = str(temperature_sense)
        except ValueError:
            print("Temperature is out of range.")
            
    
    def decision_base(self):
        SENS_CATEGORY = {"1":-5.0, "2":-3.0, "3":0.0, "4":2.0, "5":5.0}
        try:
            self.output_temperature = self.input_temperature + SENS_CATEGORY[self.input_temperature_sense]
        except KeyError:
            print("No such temperature sense.")