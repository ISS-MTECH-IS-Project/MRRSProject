from NeomodelGraphObject import (Symptom, Disease, AKA, Medication, CaseInc, SuspectedSymptomRel)
from conversation import FishMessage
import json


# prepping this for object to JSON conversion for frontend

def GetDefaultImagePath(self):
    folderpath = os.getcwd()
    if os.name == 'posix':
        folderpath += "/Images/"
    else:
        folderpath += "\\Images\\"
    return folderpath

def MapOneDiseaseToFactSheetJSON(diseaseNode: Disease):
    """Convert a single disease node object data to flat JSON for frontend display"""

    akalist = []
    for aka in diseaseNode.aka:
        if aka:
            akalist.append(aka.name)

    symptomlist = []
    for sym in diseaseNode.symptoms:
        if sym:
            symptomlist.append(sym.description)

    medlist = []
    for med in diseaseNode.medications:
        if med:
            medlist.append(med.description)

    jsonDict = {
        "disease_name": diseaseNode.name,
        "disease_environment": diseaseNode.environment,
        "disease_affectfish": diseaseNode.affectfish,
        "disease_casue": diseaseNode.cause,
        "disease_treatment": diseaseNode.treatment,
        "disease_vetadvised": diseaseNode.vet_advised,
        "disease_alsoknownas": akalist,
        "disease_symptoms": symptomlist,
        "disease_meds": medlist
    }

    return json.dumps(jsonDict, indent=4)


def MapOneDiseaseToFishMsg(diseaseNode: Disease) -> FishMessage:
    """Convert a single disease node object data to FishMessage Object"""

    akalist = []
    for aka in diseaseNode.aka:
        if aka:
            akalist.append(aka.name)

    symptomlist = []
    for sym in diseaseNode.symptoms:
        if sym:
            symptomlist.append(sym.description)

    medlist = []
    for med in diseaseNode.medications:
        if med:
            medlist.append(med.description)

    jsonDict = {
        "disease_name": diseaseNode.name,
        "disease_environment": diseaseNode.environment,
        "disease_affectfish": diseaseNode.affectfish,
        "disease_casue": diseaseNode.cause,
        "disease_treatment": diseaseNode.treatment,
        "disease_vetadvised": diseaseNode.vet_advised,
        "disease_alsoknownas": akalist,
        "disease_symptoms": symptomlist,
        "disease_meds": medlist
    }

    fish_msg = FishMessage()
    fish_msg.question = None
    fish_msg.options = jsonDict
    fish_msg.isConclusion = True

    return fish_msg
