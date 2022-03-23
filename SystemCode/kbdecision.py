from xmlrpc.client import boolean
from models import SingletonMeta
from DataAccessLayer import DataAccessLayer
from NeomodelGraphObject import *
class KbDecisionMaker(metaclass=SingletonMeta):

    def getNext(self, case:CaseInc, symptom:Symptom, isConfirmed:boolean, suspectLevel:float, isGuided:boolean) :
        """
        return a dict
        {"symptom": next Symtom if any
        "diseases": [{"disease": disease, "confidence":0.8}]
        list of dictionary of diseases and confidence level sorted by confidence level
        """
        dbcon = DataAccessLayer(username='neo4j',password='ai-user').CreateDBConnection
        currentDiseases = dbcon.GetAllDiseaseFromSymptomOrCaseByNameOrID(case.name)
        suspectDiseases = dbcon.GetAllDiseaseFromSymptomOrCaseByNameOrID(symptom.name)
        currentDMap = { currentDiseases[i][0].id : currentDiseases[i][0] for i in range(len(currentDiseases))} if currentDiseases[0][0] else {}
        for dl in suspectDiseases:
            d = dl[0]
            weight = d.symptoms.relationship(symptom).weight
            if isGuided:
                if isConfirmed:
                    suspectLevel = weight
                else:
                    suspectLevel = d.symptoms.relationship(symptom).penalty
            diff = suspectLevel
            newConfidence = suspectLevel/len(d.symptoms)
            if d.id in currentDMap:
                rel = case.suspected_symptoms.relationship(symptom)
                if rel:
                    diff = suspectLevel - rel.suspectedLevel
                rel = case.suspected_diseases.relationship(d)
                newConfidence = rel.confidence + (diff*weight)/len(d.symptoms)
            case = dbcon.UpdateDiseaseToCase(case, d, newConfidence)
        case = dbcon.UpdateSymptomToCase(case, symptom, suspectLevel)

        




