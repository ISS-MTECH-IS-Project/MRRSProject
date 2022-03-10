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
        # We can have some RBS here to process the above such that we prioritize SYMPTOMS 
        # => therefore token like this [spot, scale, white, eyes, green] will be sorted to
        # [spot, white, green, scale, eyes] <= [SYMPTOM, SYMPTOM_descriptor, SYMPTOM_descriptor, BODYPART, BODYPART]
        pass

    # assume we are not probing because the n topics are very similiar, so we do FOLLOWUP (a kind of probe, but we single out differences of the tokens between the topics so that we can zoom in)
    # eg.   User token [slime]
    #       Condition 1 [spot slime scale]
    #       Condition 2 [white slime eyes]
    #       Condition 3 [green white slime]
    # eliminate all common tokens => we are left with [spot, scale, eyes, green] <= questions will be based on this 
    # Apply RBS, we get sorted like [spot, green, scale, eyes] <= [SYMPTOM, SYMPTOM_descriptor, BODYPART, BODYPART]
    def builtFollowUpObject():
        pass



# Scenario - using Topic matching, we decide to go ahead with PROBE
# The probe object sent to the UI will have the following purpose
# 1) Send back the original UserQuestion (this design is useful for single user session atm)
# 2) When at Topic Matching stage, generate the list of tokens for question asking, and insert into this object (which will act as the iteration list for probing)
# 3) Symptom matching to improve results OR getting more tokens (user inputs) - the focus is really not to be abductive

class ProbeObject:
    def __init__(self, name, userQuestionObj, test=False): 
        self.Name = name # for session implementation if there's time
        self.UserQuestion = userQuestionObj
        self.CollectedSymptoms =[]
        self.ProbeQuestions = []
    
    def CollectSymptoms (self, symptom):
        # Symptoms from user chat to insert here
        self.CollectedSymptoms.append(symptom)

    def BakeQuestions (self, pre_sorted_question_array):
        self.ProbeQuestions.append(pre_sorted_question_array)


# Scenario - using Topic matching, we decide to go ahead with FOLLOWUP
# The Followup object is a variant of the ProbeObject, but the design difference at this moment is to 
# 1) Recognise this as a stage differential - meaning by right at this stage we no longer do probing - highly abductive and high inference
#    (let's say if user exahust all follow up question with no matching - we will just return the HIGHEST MATCH condition / [conditions] - be it this might be low confidence)
# 2) To facilitate the above, suspected conditions are also bake into this object

class FollowUpObject (ProbeObject):
    def __init__(self, name, userQuestionObj, suspected_conditions, test=False): 
        super().__init__(self, name, userQuestionObj, test=False)
        self.isProbe = False
        self.Conditions = suspected_conditions
    
    def SuspectConditions (self, pre_sorted_condition_array):
        self.ProbeQuestions.append(pre_sorted_condition_array)


