from xmlrpc.client import boolean
from models import *
from topicmodel import *
from kbdecision import *

class FishMessage:
    question=""
    # option is a dict {label:str, value:str,image:bool}
    options=[]
    isConclusion=False

class Conversation(metaclass=SingletonMeta):

    tm:TopicModel = TopicModel()
    kb:KbDecisionMaker = KbDecisionMaker()

    greeting:str = "how are you doing today?"
    count:int = 0
    def getGreeting(self) -> str:
        self.count += 1
        return self.greeting+str(self.count)

    def getMessage(self, question:str, answer:str) -> FishMessage:
        symptoms = self.tm.getSymptoms(question, answer)
        pass


    def handleConversation(self, caseId:str, userInput:str, isConfirmed:boolean, isGuided:boolean) -> dict: 
        case = None
        dbcon = DataAccessLayer().CreateDBConnection
        if caseId:
            case = dbcon.CreateOrGetCaseNode(name=caseId)
        else:
            case = dbcon.CreateOrGetCaseNode()
        if isGuided:
            inputSymptom = dbcon.GetOneSymptomNode(userInput)
            nextAction = self.kb.getNext(case, inputSymptom, isConfirmed, 0, isGuided)
        else:
            supsepectedSym = self.tm.getSymptoms(userInput)
            for (sym, level) in supsepectedSym:
                nextAction = self.kb.getNext(case, sym, False, level, False)

        nextSymptom = nextAction.symptom
        diseases = nextAction.diseases
        confirmeDisease = None
        for d in diseases:
            confidence = diseases[d]
            if confidence>0.8:
                confirmeDisease = d
        
        questionToAsk = nextSymptom.question

        return {"case": case, "question":questionToAsk, "confirmed":confirmeDisease}

        # tm.getSymptom(userInput)
        # res = self.kb.getNext(case, sym)
        #  d = res.diseases[0]
        #  d1 = res.diseases[1]
        #     if d.confidency>0.9:
        #         return ConfirmDiseaseMessage(d)
        # return getMessage(res.symtom)
        
