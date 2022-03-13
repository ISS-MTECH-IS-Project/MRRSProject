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
    
    def getDisease (self, name:str) -> Disease:
        # 
        return Disease()

    def getDiseases (self, symptom:Symptom) -> dict:
        # put the logic to find all diseases for a given symptom in neo4j here
        return []

    def getSymptoms (self, disease:Disease) -> dict:
        # put the logic to find all symptoms for a given disease in neo4j here
        return []

    def getCase(self, id:int) -> Case:
        # get case by id
        return Case()

    def saveCase(self, case:Case) -> Case:
        return Case()

    def getDiseasesFromCase(self, case:Case) -> dict:
        pass

    def updateDiseasesToCase(self, case:Case, disease:Disease):
        pass

    def confirmSymptomToCase(self, case:Case, symptom:Symptom):
        pass


