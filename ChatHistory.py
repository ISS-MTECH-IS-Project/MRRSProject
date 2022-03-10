# Scenario - Chatbot needs to ask question, user will also ask question
# ChatHistory class - this will interface with the front end and load up with UI with Bot question
class ChatHistory:
     def __init__(self): 
        self.MessageHistory = [] # [string of user input & bot message - printing this creates a chat like content between user and bot]
        self.UserInputHistoryTokens = [] # for every user input, we bring this token array (this will be the basis of symptom matching)
        self.Stage = 0 # where 0 is the first user input receive stage, and we can define a numeric break point if there are too many stages (too many probes)
        
        # add array of tokens UserInputHistoryTokens
        def AddUserInputHistoryTokens(self,Tokens): 
            for token in Tokens:
                if token not in self.UserInputHistoryTokens:
                    self.UserInputHistoryTokens.append(token)