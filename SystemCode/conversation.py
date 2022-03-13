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


