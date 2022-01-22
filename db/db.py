from mongoengine import connect, Document, StringField
from Comfortable_temperature_AI.db.config import DATABASE_CONNECTINO_STRING
import json
from logging import getLogger, config, basicConfig, DEBUG
logger = getLogger(__name__)
with open("log_config.json", "r") as f:
    config.dictConfig(json.load(f))
basicConfig(level=DEBUG)

logger.info(f"DB接続文字列:{DATABASE_CONNECTINO_STRING}")

connect(host=DATABASE_CONNECTINO_STRING)#pip install