from mongoengine import connect, Document, StringField, DateTimeField, IntField, FloatField
import pandas as pd

class Temperature(Document):
    time = DateTimeField(required=True)
    temperatureCategory = IntField(required=True)
    Temperature = FloatField(required=True)

    def __str__(self):
        return f"{self.Temperature}"