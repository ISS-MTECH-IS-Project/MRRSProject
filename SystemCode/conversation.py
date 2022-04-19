from models import *
from topicmodel import *
from kbdecision import *
from DataAccessLayer import DataAccessLayer

# Hyper Parameters to confirm a disease
confidenceScoreHP = 0.7


class CaseService(metaclass=SingletonMeta):
    caseCache = {}

    def createCase(self):
        dbcon = DataAccessLayer().CreateDBConnection
        case = dbcon.CreateOrGetCaseNode()
        return case

    def getCaseMessages(self, caseName):
        return self.caseCache.get(caseName)

    def saveCaseMessages(self, caseName, messages):
        self.caseCache[caseName] = messages

    def updateCaseRating(self, caseName, diseaseName, rating):
        dbcon = DataAccessLayer().CreateDBConnection
        case = dbcon.CreateOrGetCaseNode(caseName)
        currentDiseases = dbcon.GetAllDiseaseFromSymptomOrCaseByNameOrID(
            caseName)
        for d in currentDiseases:
            if d[0].name == diseaseName:
                dbcon.RateDiseaseToCase(case, d[0], rating)


class Conversation(metaclass=SingletonMeta):
    # Hyper Parameters
    iterationLimitHP: int = 4

    # Attributes
    tm = TopicModel()
    kb = KbDecisionMaker()

    # Function for Guided (Novice)
    def manageConversation(self, caseID: str = None, symptomResponses: dict = {}, userInput: str = None) -> dict:
        # Set all variables to none
        case = nextAction = None
        symptoms = []
        diseases = []
        confirmedDiseases = []

        dbcon = DataAccessLayer().CreateDBConnection

        # Create a new or retrieve a Case Id
        if caseID:
            case = dbcon.CreateOrGetCaseNode(casename=caseID)
        else:
            case = dbcon.CreateOrGetCaseNode()
        if case.iteration:
            case.iteration += 1
        else:
            case.iteration = 1
        iteration = case.iteration
        dbcon.SaveCaseNode(case)

        if userInput:
            symptomsTM = self.tm.getSymptoms(dbcon, userInput, verbose=True)
            for symptomTM in symptomsTM:
                userInputSuspectedSymptom = dbcon.GetOneSymptomNode(symptomTM)
                symptoms.append(userInputSuspectedSymptom)
        else:
            for symptom in symptomResponses:
                # userInputSuspectedSymptom = self.tm.getSymptoms(dbcon, symptom, verbose = True)
                userInputSuspectedSymptom = dbcon.GetOneSymptomNode(symptom)
                nextAction = self.kb.getNext(
                    case, userInputSuspectedSymptom, symptomResponses[symptom], 0, True)

            # Retrieve the diseases and symptoms
            if nextAction != None:
                diseases = nextAction.get("diseases")
                # print(diseases)
                symptoms = nextAction.get("symptoms")

                # Validate if there is a suspected disease that matches the confidence score
                if len(diseases) > 0:
                    for disease in diseases:
                        confidence = disease[1]
                        print(disease[0].name, "  ", confidence)
                        if confidence >= confidenceScoreHP:
                            confirmedDiseases.append(disease[0])
                    if len(confirmedDiseases) == 0 and iteration >= self.iterationLimitHP:
                        confirmedDiseases.append(diseases[0][0])

        return {"case": case, "symptoms": symptoms, "diseases": diseases, "confirmedDiseases": confirmedDiseases}

    # Function for Unguided (Expert)
    def manageUnguidedConversation(self, caseID: str, userInput: str, symptomResponses: dict) -> dict:
        # Set all variables to none
        case = diseases = confirmedDisease = symptoms = nextAction = None

        dbcon = DataAccessLayer().CreateDBConnection
        # Create a new or retrieve a Case Id
        if caseID:
            case = dbcon.CreateOrGetCaseNode(casename=caseID)
        else:
            case = dbcon.CreateOrGetCaseNode()

        if userInput:
            symptomsTM = self.tm.getSymptoms(dbcon, userInput, verbose=True)
            for symptom in symptomsTM:
                userInputSuspectedSymptom = dbcon.GetOneSymptomNode(symptom)
                symptoms.append(userInputSuspectedSymptom)
        else:
            for symptom in symptoms:
                # userInputSuspectedSymptom = self.tm.getSymptoms(dbcon, symptom, verbose = True)
                userInputSuspectedSymptom = dbcon.GetOneSymptomNode(symptom)
                nextAction = self.kb.getNext(
                    case, userInputSuspectedSymptom, symptomResponses[symptom], 0, True)

            # Retrieve the diseases and symptoms
            diseases = nextAction.get("diseases")
            symptoms = nextAction.get("symptoms")

            confirmedDisease = None

            # Validate if there is a suspected disease that matches the confidence score
            if len(diseases) > 0:
                for disease in diseases:
                    confidence = disease[1]
                    if confidence >= confidenceScoreHP:
                        confirmedDisease = disease

        return {"case": case, "symptoms": symptoms, "diseases": diseases, "confirmedDisease": confirmedDisease}
        # confirmedDisease = None
        # for d in diseases:
        #     confidence = diseases[d]
        #     if confidence > confidenceScore:
        #         confirmedDisease = d

        # questionToAsk = nextSymptom.question

        # return {"case": case, "question":questionToAsk, "confirmed":confirmedDisease}

        # ToDo: Multiple Diseases

        # tm.getSymptom(userInput)
        # res = self.kb.getNext(case, sym)
        #  d = res.diseases[0]
        #  d1 = res.diseases[1]
        #     if d.confidency>0.9:
        #         return ConfirmDiseaseMessage(d)
        # return getMessage(res.symtom)
