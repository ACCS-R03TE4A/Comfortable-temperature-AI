import json
import time
import requests
import db
import sys
from temperature import Temperature


try:
    tmp = Temperature.objects.all()
    print(tmp)
except Exception as error:
    print(error, file=sys.stderr)