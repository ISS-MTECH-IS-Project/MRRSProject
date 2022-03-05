# Scenario - using Topic modelling we would have pre-trained some topics
# These topics can be 
# 1) medical conditions
# 2) broad category of a family of medical conditions etc
# 3) symptoms (note we need to exercise care here to segregate conditions vs symptoms)

class Topic:
    def __init__(self, name, tokens, test=False): 
        self.Name = name
        self.Tokens = tokens #[]
        if self.test:
            print(self.Name)
            print(self.Tokens)

class SymptomTopic(Topic):
    def __init__(self, name, tokens, conditions, test=False): 
        super().__init__(self, name, tokens, test=False)
        self.Conditions = conditions #an array of condition name strings

class ConditionTopic(Topic):
    def __init__(self, name, tokens, symptoms, factsheet, test=False): 
        super().__init__(self, name, tokens, test=False)
        self.Symptoms = symptoms #an array of symptom name strings
        self.MedicalFactSheet = factsheet # imagine this like a "page of medical facts for the user to read on the details of this condition"

class CategoryTopic(Topic):
    def __init__(self, name, tokens, symptoms, conditions, test=False): 
        super().__init__(self, name, tokens, test=False)
        self.Symptoms = symptoms #an array of symptom name strings
        self.Conditions = conditions #an array of condition name strings


# Scenario - BotUI Needs to ask question
# Question class -  this will store
# 1) Original question
# 2) UserInputs - these are inputs by user (be it probes / followup) 
# 3) eg { orig : ['token of original question']}
#       { d-treeID : ['above + tokens added after probe'] }
#       { d-treeID2 : ['above + tokens added after probe'] }

class Question:
     def __init__(self, question, test=False): 
        self.question = question
        if self.test:
            print(self.question)

class UserQuestion(Question):
    def __init__(self, question, test): 
        super().__init__(self, question, test)        
        self.UserInput = {}

    def setStageToken(self, DtreeID, tokens):
        if DtreeID not in self.UserInput.keys():
            self.UserInput[DtreeID] = tokens
        else:
            # this question is asked before (should not happen)
            pass
    
# Scenario - User answered question, we need to match
# Matching class -  this will person the calling of backend logic for tokenizing and matching
# 1) Should take in the UserQuestion object (so that at anytime have full context access)
# 2) Should link to all backend logic processing
# 3) Should return either
#   a) Probe object - which the bot UI can use to determine what questions to ask based on missing tokens for nearest match
#   b) Decision Object - which bot UI can use to give a firm answer to user

class MatchingAlgorithm:
    def __init__(self, UserQuestion):
        self.UserQuestion = UserQuestion

    # 1st we text process the question
    def Tokenizer(self,question):
        # TBA
        # return [tokens]
        pass
    
    # then we try to find pre-trained topics (conditions)
    def GetNNearestTopicsUsingTokens(n, tokens):
        # TBA
        # return topics in the form of
        # [
        #   topicObj1 : [tokens]
        #   ..
        #   topicObjN : [tokens]
        # ]
        # results are rank 0 - being closest match to n - least match
        pass

    # next we determine if we need more input or we are already in a very tight scope (meaning all the n topics are very SIMILIAR) 
    def SimiliarityOfNTopics (ntopics):
        # We can use some sort of regression or "feature clustering" here  
        # we should get a float here and it will help us decide if we want to PROBE
        pass

    # some simple Yes No here base on above
    def isProbe():
        pass

    # assume we are probing
    def builtProbeObject():
        # If we imagine the probe object being an investigative role, it is actually prepared with some questions that are built to
        # IMPROVE MATCHING
        # ELIMINATE OPTIONS 
        # eg.   User token [slime]
        #       Condition 1 [spot slime scale]
        #       Condition 2 [white slime eyes]
        #       Condition 3 [green white slime]
        # Probe obj will be built with the following question tokens [spot, scale, white, eyes, green] <= note the last white is removed because it is repeated token
        pass

    # assume we are not probing because the n topics are very similiar, so we do FOLLOWUP (a kind of probe, but we single out differences of the tokens between the topics so that we can zoom in)
    # eg.   User token [slime]
    #       Condition 1 [spot slime scale]
    #       Condition 2 [white slime eyes]
    #       Condition 3 [green white slime]
    # eliminate all common tokens => we are left with [spot, scale, eyes, green] <= questions will be based on this 
    def builtFollowUpObject():
        pass



