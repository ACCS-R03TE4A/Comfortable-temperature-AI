import csv
import  db
from temperature import Temperature
from datetime import datetime, timedelta, date
import numpy as np
import pandas as pd

import connect
import Document
import StringField
from mongoengine import *
from flaskr.databases.collection_models.temperature import Temperature

#日付の決定
today = date.today()
range_end = datetime(year=today.year, month=today.month, day=today.day)
range_start = range_end - timedelta(days=7)
seq = Temperature.objects(time__gt=range_start).all()

#リストとデータフレームの初期化
df = None
tActual_list = []
InsideTemp_list = []
OutsideTemp_list = []
tSuitable_list = []

#振り分け
def sorting(temp_data):
    if temp_data.temperatureCategory == 0:
        tActual_list.append(temp_data)
    elif temp_data.temperatureCategory == 1:
        InsideTemp_list.append(temp_data)
    elif temp_data.temperatureCategory == 2:
        OutsideTemp_list.append(temp_data)
    elif temp_data.temperatureCategory == 3:
        tSuitable_list.append(temp_data)
    

for d in seq:
    sorting(d)


# １時間ごとに平均値を計算する。
def average(data_list):
    global range_start
    ave_data_list = []

    while range_start <= range_end:
        t_data_list = []

        for d in data_list:
            if d.time.hour == range_start.hour:
                t_data_list.append(d.temperature)
        
        #空白があればその一時間はNaN
        try:
            ave_data_list.append(sum(t_data_list)/len(t_data_list))
        except ZeroDivisionError:
            ave_data_list.append(np.NaN)

        #次の一時間    
        range_start += timedelta(hours=1)

    return ave_data_list
    


df = pd.DataFrame(
    data={'近辺温度': average(tActual_list), 
    '室温': average(InsideTemp_list),
    '外気温': average(OutsideTemp_list),
    '快適温度' : average(tSuitable_list)}
)


df.to_csv("Learn.csv")
