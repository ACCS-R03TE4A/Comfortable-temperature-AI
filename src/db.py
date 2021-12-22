from mongoengine import connect, Document, StringField
from config import DATABASE_CONNECTINO_STRING

connect(host=DATABASE_CONNECTINO_STRING)#pip install