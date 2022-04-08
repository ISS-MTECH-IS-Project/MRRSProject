from xmlrpc.client import boolean
from models import *
from topicmodel import *
from kbdecision import *

class FishMessage():

    def __init__(self, question, options, isConclusion):
        self.question = question
        # option is a dict {label:str, value:str,image:bool}
        self.options = options
        self.isConclusion = isConclusion

    def getQuestion(self):
        return self.question

    def getOptions(self):
        return self.options

    def getIsConclusion(self):
        return self.isConclusion

class Conversation(metaclass=SingletonMeta):
    # Hyper Parameters
    confidenceScoreHP:float = 0.8
    iterationLimitHP:int = 5

    # Attributes
    tm = TopicModel()
    kb = KbDecisionMaker()
    dbcon = DataAccessLayer().CreateDBConnection

    # def __init__(self):
        # self.question = question
        # option is a dict {label:str, value:str,image:bool}
        # self.options = options
        # self.isConclusion = isConclusion

    # greeting:str = "how are you doing today?"
    # count:int = 0
    # def getGreeting(self) -> str:
    #     self.count += 1
    #     return self.greeting + str(self.count)

    # def getMessage(self, question:str, answer:str) -> FishMessage:
    #     symptoms = self.tm.getSymptoms(question, answer)
    #     pass

    # Function for Guided (Novice)
    def manageConversation(self, caseID:str=None, symptomResponses:dict={}, userInput:str=None, iteration:int=0) -> dict:
        # Set all variables to none 
        case = confirmedDisease = nextAction = None
        symptoms = []
        diseases = []

        iteration += 1

        # Create a new or retrieve a Case Id
        if caseID:
            case = self.dbcon.CreateOrGetCaseNode(casename = caseID)
        else:
            case = self.dbcon.CreateOrGetCaseNode()

        if userInput:
            symptomsTM = self.tm.getSymptoms(self.dbcon, userInput, verbose = True)
            for symptomTM in symptomsTM:
                userInputSuspectedSymptom = self.dbcon.GetOneSymptomNode(symptomTM)
                symptoms.append(userInputSuspectedSymptom)
        else:
            for symptom in symptomResponses:
                # userInputSuspectedSymptom = self.tm.getSymptoms(self.dbcon, symptom, verbose = True)
                userInputSuspectedSymptom = self.dbcon.GetOneSymptomNode(symptom)
                nextAction = self.kb.getNext(case, userInputSuspectedSymptom, symptomResponses[symptom], 0, True)

            # Retrieve the diseases and symptoms
            if nextAction != None:
                diseases = nextAction.get("diseases")
                # print(diseases)
                symptoms = nextAction.get("symptoms")

                # Validate if there is a suspected disease that matches the confidence score
                if len(diseases) > 0:
                    for disease in diseases:
                        confidence = disease[1]
                        if confidence >= self.confidenceScoreHP:
                            confirmedDisease = disease

        return {"case": case, "iteration": iteration, "symptoms":symptoms, "diseases":diseases, "confirmedDisease":confirmedDisease} 

    # Function for Unguided (Expert)
    def manageUnguidedConversation(self, caseID:str, userInput:str, symptomResponses:{}) -> dict: 
        # Set all variables to none 
        case = diseases = confirmedDisease = symptoms = nextAction = None

        # Create a new or retrieve a Case Id
        if caseID:
            case = self.dbcon.CreateOrGetCaseNode(casename = caseID)
        else:
            case = self.dbcon.CreateOrGetCaseNode()

        if userInput:
            symptomsTM = self.tm.getSymptoms(self.dbcon, userInput, verbose = True)
            for symptom in symptomsTM:
                userInputSuspectedSymptom = self.dbcon.GetOneSymptomNode(symptom)
                symptoms.append(userInputSuspectedSymptom)
        else:
            for symptom in symptoms:
                # userInputSuspectedSymptom = self.tm.getSymptoms(self.dbcon, symptom, verbose = True)
                userInputSuspectedSymptom = self.dbcon.GetOneSymptomNode(symptom)
                nextAction = self.kb.getNext(case, userInputSuspectedSymptom, symptomResponses[symptom], 0, True)

            # Retrieve the diseases and symptoms
            diseases = nextAction.get("diseases")
            symptoms = nextAction.get("symptoms")

            confirmedDisease = None

            # Validate if there is a suspected disease that matches the confidence score
            if len(diseases) > 0:
                for disease in diseases:
                    confidence = disease[1]
                    if confidence >= self.confidenceScoreHP:
                        confirmedDisease = disease

        return {"case": case, "symptoms":symptoms, "diseases":diseases, "confirmedDisease":confirmedDisease} 
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


        