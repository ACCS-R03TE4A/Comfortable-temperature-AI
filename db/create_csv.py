import csv
import logging
# import  Comfortable_temperature_AI.db.db
from Comfortable_temperature_AI.db.temperature import Temperature
from datetime import datetime, timedelta, date
import numpy as np
import pandas as pd
import json
import mongoengine
from logging import getLogger, config, basicConfig, DEBUG
logger = getLogger(__name__)
with open("log_config.json", "r") as f:
    config.dictConfig(json.load(f))
basicConfig(level=DEBUG)

class TensorGenerater:

    def __init__(self):
        #日付の決定
        self.today = date.today()
        self.range_end = datetime(year=self.today.year, month=self.today.month, day=self.today.day)
        self.range_start = self.range_end - timedelta(days=7)
        try:
            self.seq = Temperature.objects(time__gt=self.range_start).all()
        except mongoengine.connection.ConnectionFailure:
            try:
                Comfortable_temperature_AI.db.db
            except NameError:
                import Comfortable_temperature_AI.db.db

        #リストとデータフレームの初期化
        self.df = None
        self.tActual_list = []
        self.InsideTemp_list = []
        self.OutsideTemp_list = []
        self.tSuitable_list = []
    #振り分け
    def sorting(self, temp_data):
        if temp_data.temperatureCategory == 0:
            self.tActual_list.append(temp_data)
        elif temp_data.temperatureCategory == 1:
            self.InsideTemp_list.append(temp_data)
        elif temp_data.temperatureCategory == 2:
            self.OutsideTemp_list.append(temp_data)
        elif temp_data.temperatureCategory == 3:
            self.tSuitable_list.append(temp_data)

    # １時間ごとに平均値を計算する。
    def average(self, data_list):
        range_start_ = self.range_start
        ave_data_list = []

        while range_start_ <= self.range_end:
            t_data_list = []

            for d in data_list:
                if d.time.hour == range_start_.hour:
                    t_data_list.append(d.Temperature)
            
            #空白があればその一時間はNaN
            try:
                ave_data_list.append(sum(t_data_list)/len(t_data_list))
            except ZeroDivisionError:
                ave_data_list.append(np.NaN)

            #次の一時間    
            range_start_ += timedelta(hours=1)

        return ave_data_list
    
    def generate(self):
        logger.debug(f"学習に使用する温度データ行数:{len(self.seq)}")
        for d in self.seq:
            self.sorting(d)
        df = pd.DataFrame(
        data={'tActual': self.average(self.tActual_list), 
        'tInside': self.average(self.InsideTemp_list),
        'tOutside': self.average(self.OutsideTemp_list),
        'tSuitable' : self.average(self.tSuitable_list)}
        )
        df.to_csv("Learn.csv")
        return df