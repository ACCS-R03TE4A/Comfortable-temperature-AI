import time
import sys
import db
from temperature import Temperature

def AAA():
    try:
        #tmp = Temperature.objects.all()
        tActual = Temperature.objects(temperatureCategory=0).order_by("-time").first()
        #InsideTemp = Temperature.objects(temperatureCategory=1).order_by("-time").first()
        #OutsideTemp = Temperature.objects(temperatureCategory=2).order_by("-time").first()
        return tActual
    except Exception as error:
        print(error, file=sys.stderr)