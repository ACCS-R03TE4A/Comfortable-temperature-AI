import os
import json
import sys
sys.path.append("/home/ubuntu/ACCS-SERVER")
from Comfortable_temperature_AI.src.TemperatureDetermination import ComfortTemperaturePredictionAI
from logging import getLogger, config, basicConfig, DEBUG
logger = getLogger(__name__)
with open("log_config.json", "r") as f:
    config.dictConfig(json.load(f))
basicConfig(level=DEBUG)

ai = ComfortTemperaturePredictionAI()
ai.create_model()
logger.debug(f"終了:{__name__}")