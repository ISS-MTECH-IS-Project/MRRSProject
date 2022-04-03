from NeomodelGraphObject import (Symptom, Disease, AKA, Medication, CaseInc, SuspectedSymptomRel)
import json
from datetime import datetime

# prepping this for object to JSON conversion for frontend

def GetDefaultImagePath(symptomNode:Symptom):
    folderpath = os.getcwd()
    if os.name == 'posix':
        if Symptom.imageurl:
            folderpath += "/Images/"+Symptom.imageurl
    else:
        if Symptom.imageurl:
            folderpath += "\\Images\\"+Symptom.imageurl
    return folderpath

def MapOneDiseaseToFactSheetJSON(diseaseNode:Disease):
    """
    Convert a single disease node object data to flat JSON for frontend display
    Planned for End display
    """

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
        "disease_name":diseaseNode.name,
        "disease_environment": diseaseNode.environment,
        "disease_affectfish": diseaseNode.affectfish,
        "disease_cause":diseaseNode.cause,
        "disease_treatment":diseaseNode.treatment,
        "disease_vetadvised":diseaseNode.vet_advised,
        "disease_alsoknownas":akalist,
        "disease_symptoms":symptomlist,
        "disease_meds":medlist
    }

    return json.dumps(jsonDict,indent=4)

def MapOneSymptomToMessageJSON(symptomNode:Symptom):
    """Convert a single symptom node object data to flat JSON for frontend display"""

    jsonDict = {
        "name":symptomNode.name,
        "confirmed": True,
        "image": GetDefaultImagePath(symptomNode),
        "description":symptomNode.description
    }
    return json.dumps(jsonDict,indent=4)

def MapOneDiseaseToMessageJSON(diseaseNode:Disease):
    """
    Convert a single disease node object data to flat JSON for frontend display
    This is suitable for interim display.
    """

    symptomDescriptions = []
    for sym in diseaseNode.symptoms:
        if sym:
            symptomDescriptions.append(sym.description)

    jsonDict = {
        "name":diseaseNode.name,
        "confirmed": True,
        "description":symptomDescriptions
    }
    return json.dumps(jsonDict,indent=4)

def MapCaseToMessageJSON(caseInc:[CaseInc]):
    """Convert one or multiple symptom node object data to flat JSON for frontend display"""

    symptoms = []
    for sym in caseInc.suspected_symptoms:
        if sym:
            symptoms.append(MapOneSymptomToMessageJSON(sym))

    diseases = []
    for disease in caseInc.suspected_diseases:
        if disease:
            diseases.append(MapOneDiseaseToMessageJSON(disease))

    jsonDict = {
        "isSend":False,
        "isUSer": False,
        "nextOpen": "",
        "symptoms":symptoms,
        "diseases":diseases,
        "time":datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "body":""
    }

    return json.dumps(jsonDict,indent=4)