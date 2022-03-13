from models import *
from dbservice import *
class KbDecisionMaker(metaclass=SingletonMeta):
    __db = None


    def __init__(self) -> None:
        __db = DBservice()


    def getNext(self, case:Case, symptom:Symptom) -> dict :
        """
        return a dict
        {"symptom": next Symtom if any
        "diseases": [{"disease": disease, "confidence":0.8}]
        list of dictionary of diseases and confidence level sorted by confidence level
        """
        pass




