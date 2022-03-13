from models import *

class DBservice(metaclass=SingletonMeta):

    # define your connections here
    __neo4jURL__=""
    __neo4jPass__=""
    __graph__ = None

    def __init__(self) -> None:
        # setup the neo4j connections here
        pass

    def saveSymptom (self, symptom:Symptom) -> Symptom:
        # put the save symtom to neo4j logic here
        return Symptom()

    def getSymptom (self, name:str) -> Symptom:
        # put the search symtom by name in neo4j logic here
        return Symptom()
    
    def getCondition (self, name:str) -> Condition:
        # 
        return Condition()

    def getConditions (self, symptom:Symptom) -> list[Condition]:
        # put the logic to find all conditions for a given symptom in neo4j here
        return []

    def getSymptoms (self, condition:Condition) -> list[Symptom]:
        # put the logic to find all symptoms for a given condition in neo4j here
        return []

    def getCase(self, id:int) -> Case:
        # get case by id
        return Case()

    def saveCase(self, case:Case) -> Case:
        return Case()

    


