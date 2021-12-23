import time
import sys
import db
from temperature import Temperature

def get_temp():
    try:
        #DBから最も新しい各温度を取得
        tActual = Temperature.objects(temperatureCategory=0).order_by("-time").first()
        InsideTemp = Temperature.objects(temperatureCategory=1).order_by("-time").first()
        OutsideTemp = Temperature.objects(temperatureCategory=2).order_by("-time").first()
        #各の温度をリストにして返す
        temp_list = [tActual,InsideTemp,OutsideTemp]
        return temp_list
    except Exception as error:
        print(error, file=sys.stderr)