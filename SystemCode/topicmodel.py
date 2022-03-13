from models import SingletonMeta

class TopicModel(metaclass=SingletonMeta):

    # get list of symptoms from the question and answer
    def getSymptoms(self, question:str, answer:str) -> list[str]:

        return []