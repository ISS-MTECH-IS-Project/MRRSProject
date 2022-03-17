from models import *
from dbservice import *
class KbDecisionMaker(metaclass=SingletonMeta):
    __db:DBservice = None


    def __init__(self) -> None:
        self.__db = DBservice()


    def getNext(self, case:Case, symptom:Symptom) -> dict :
        """
        return a dict
        {"symptom": next Symtom if any
        "diseases": [{"disease": disease, "confidence":0.8}]
        list of dictionary of diseases and confidence level sorted by confidence level
        """
        self.__db.confirmSymptomToCase(case,symptom)
        currentDiseases = self.__db.getDiseasesFromCase(case)
        suspectDiseases = self.__db.getDiseases(symptom)
        for d in suspectDiseases:
            if currentDiseases[d]:
                disease = currentDiseases[d]
                # logic here

        pass




