import time
import sys
import db
from temperature import Temperature

def AAA():
    try:
        tActual = 25
        InsideTemp = 25
        OutsideTemp = 25
        #tmp = Temperature.objects.all()
        tActual = Temperature.objects(temperatureCategory=0).order_by("-time").first()
        InsideTemp = Temperature.objects(temperatureCategory=1).order_by("-time").first()
        OutsideTemp = Temperature.objects(temperatureCategory=2).order_by("-time").first()
        temp_list = [tActual,InsideTemp,OutsideTemp]
        return temp_list
    except Exception as error:
        print(error, file=sys.stderr)