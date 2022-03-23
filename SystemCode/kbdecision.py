from xmlrpc.client import boolean
from models import SingletonMeta
from DataAccessLayer import DataAccessLayer
from NeomodelGraphObject import *
class KbDecisionMaker(metaclass=SingletonMeta):


    def __init__(self) -> None:
        pass


    def getNext(self, case:CaseInc, symptom:Symptom, isConfirmed:boolean, suspectLevel:float, isGuided:boolean) -> dict :
        """
        return a dict
        {"symptom": next Symtom if any
        "diseases": [{"disease": disease, "confidence":0.8}]
        list of dictionary of diseases and confidence level sorted by confidence level
        """
        dbcon = DataAccessLayer().CreateDBConnection
        currentDiseases = dbcon.GetAllDiseaseFromSymptomOrCaseByNameOrID(case.name)
        suspectDiseases = dbcon.GetAllDiseaseFromSymptomOrCaseByNameOrID(symptom.name)
        for d in suspectDiseases:
            if currentDiseases[d]:
                disease = currentDiseases[d]
                # logic here

        pass




