from xmlrpc.client import boolean
from models import *
# from topicmodel import *
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
    questionLimitHP:int = 5

    tm:TopicModel = TopicModel()
    kb:KbDecisionMaker = KbDecisionMaker()

    def __init__(self):
        self.question = question
        # option is a dict {label:str, value:str,image:bool}
        self.options = options
        self.isConclusion = isConclusion

    greeting:str = "how are you doing today?"
    count:int = 0
    def getGreeting(self) -> str:
        self.count += 1
        return self.greeting + str(self.count)

    def getMessage(self, question:str, answer:str) -> FishMessage:
        symptoms = self.tm.getSymptoms(dbcon, answer, verbose=False) # Note this is dictionary
        pass


    def handleConversation(self, caseID:str, userInput:str, isConfirmed:boolean, isGuided:boolean, isATest:boolean) -> dict: 
        confidenceScore:float = Conversation.confidenceScoreHP
        # questionLimit:int = Conversation.questionLimitHP

        # Create a new or retrieve a Case Id
        case = None
        dbcon = DataAccessLayer().CreateDBConnection
        if caseID:
            case = dbcon.CreateOrGetCaseNode(name = caseID)
        else:
            case = dbcon.CreateOrGetCaseNode()

        # Verify if this is a guided (Novice) or unguided (Expert)
        if isGuided:
            # Guided (Novice)
            userInputSymptom = dbcon.GetOneSymptomNode(userInput)
            nextAction = self.kb.getNext(case, userInputSymptom, isConfirmed, 0, isGuided)
        else:
            # Unguided (Expert)
            userInputSuspectedSymptom = self.tm.getSymptoms(dbcon, userInput, verbose=False)
            for (sym, level) in userInputSuspectedSymptom.items():
                symNode = dbcon.GetOneSymptomNode(sym)
                nextAction = self.kb.getNext(case, symNode, False, level, False)

        # 
        nextSymptom = nextAction.symptom
        diseases = nextAction.diseases
        confirmedDisease = None
        for d in diseases:
            confidence = diseases[d]
            if confidence > confidenceScore:
                confirmedDisease = d
        
        questionToAsk = nextSymptom.question

        return {"case": case, "question":questionToAsk, "confirmed":confirmedDisease}

        # ToDo: Multiple Diseases

        # tm.getSymptom(userInput)
        # res = self.kb.getNext(case, sym)
        #  d = res.diseases[0]
        #  d1 = res.diseases[1]
        #     if d.confidency>0.9:
        #         return ConfirmDiseaseMessage(d)
        # return getMessage(res.symtom)
        
