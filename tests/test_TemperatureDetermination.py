from src.TemperatureDetermination import TemperatureDetermination
import pytest

def test_init_temperature():
    td = TemperatureDetermination(20.0,1)
    assert td.input_temperature == 20.0

def test_init_temperature_NG_sub():
    #範囲外の温度感覚が入力された場合デフォルト値の25.0になる
    td2 = TemperatureDetermination(-100.0,1)
    assert td2.input_temperature == 25.0

def test_init_temperature_NG_upper():
    td2 = TemperatureDetermination(100.0,1)
    assert td2.input_temperature == 25.0

def test_init_sense():
    td3 = TemperatureDetermination(25.0,1)
    td3.decision_base()
    assert td3.input_temperature_sense == "1"

def test_init_sense_NG():
    #範囲外の温度感覚が入力された場合デフォルト値の３になる
    td4 = TemperatureDetermination(25.0,10)
    td4.decision_base()
    assert td4.input_temperature_sense == "3"

def test_decision_base():
    td5 = TemperatureDetermination(20.0,1)
    td5.decision_base()
    assert td5.decision_base() == 15.0

