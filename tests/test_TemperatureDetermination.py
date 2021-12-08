from src.TemperatureDetermination import TemperatureDetermination
import pytest

@pytest.fixture(scope = 'module', autouse=True)
def scope_module():
    print()
    print(f"-----------------{__name__}のテスト-----------------")
    yield
    print(f"--------------------------------------------------------")
    print()

def test_init_temperature():
    #初期化正常パターン
    td = TemperatureDetermination(20.0,1)
    assert td.input_temperature == 20.0

def test_init_temperature_NG_sub():
    #入力温度が５度より低い場合
    td2 = TemperatureDetermination(-100.0,1)
    assert td2.input_temperature == 25.0

def test_init_temperature_NG_upper():
    #入力温度が５0度より高い場合
    td2 = TemperatureDetermination(100.0,1)
    assert td2.input_temperature == 25.0

def test_init_sense():
    #入力温度感覚正常パターン
    td3 = TemperatureDetermination(25.0,1)
    assert td3.input_temperature_sense == "1"

def test_init_sense_NG():
    #入力温度感覚が範囲外
    td4 = TemperatureDetermination(25.0,10)
    assert td4.input_temperature_sense == "3"

def test_decision_base():
    #入力が正常な場合の出力温度
    td5 = TemperatureDetermination(20.0,1)
    td5.decision_base()
    assert td5.decision_base() == 15.0

def test_decision_base_NG():
    #入力が異常な場合の出力温度（デフォルト値）
    td5 = TemperatureDetermination(100.0,10)
    td5.decision_base()
    assert td5.decision_base() == 25.0
