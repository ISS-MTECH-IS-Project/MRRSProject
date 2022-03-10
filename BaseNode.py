# Mimicking the neo4j graph
# We first create a base node
# A Node can have MANY edges (relationship) to other nodes
# Nodes will have 
# 1) ID - Neo4j assigned
# 2) Name - The name of the node in neo4j
# 3) Edge - the "name of the relationship" is transcribe to different type of nodes so a Condition node will have Symptoms in neo4j and this is represented by the edge connections
# 4) Tokens - these are Topic modelling tokens for the purpose of quick relational search and various logic matching
class BaseNode:
    def __init__(self, ID, name, test=False): 
        self.ID = ID # by neo4j
        self.Name = name
        self.Edge = [] # [ALL Type of Nodes]
        self.Tokens = [] # [Tokens are the result of Topic modelling training]
        if test:
            print(self.ID)
            print(self.Name)
            print(self.Tokens)
            print(self.Edge)

        def AddEdges(self, Node):
            if Node not in self.Edge:
                self.Edge.append(Node)

# Symptom node has 
# 1) a weightage value - good for assigning weightage as we fine tune the model for symptom matching
# 2) Critical Question - text chunk for asking the "right question" - this is proposed for transformer output at this point of time
# 3) List of conditions - this is for quick search purpose when a user input matches the symptom tokens and we want to pick out more conditions for probe 
class SymptomNode(BaseNode):
    def __init__(self, ID, name): 
        super.__init__(self, ID, name)
        self.Condition = [] #[Holds all the Condition Nodes]
        self.Weightage = 1
        self.CriticalQuestion = None

        def AddConditionNode(self, ConditionNode):
            if ConditionNode not in self.Condition:
                self.Condition.append(ConditionNode)
                if ConditionNode not in self.Edge:
                    self.Edge.append(ConditionNode)

# Condition node has 
# 1) AKA (also known as) List - At this moment this is only used for display, 
#   but we could come up with a type of chatbot result that once the user gives a close to 100% match of the condition name, 
#   we straight away return the result
# 2) List of Symptom - this is for quick search purpose at the followup stage (we already narrow down the conditions and now want to follow up with very specific symptoms)
# 3) MinSymptomMatch - some conditions only have 3 - 4 symptoms, 
#   in this case we might want to match all, while some conditions have 10 symptoms, 
#   and by match around 80%, we can have good gauge and might want to be greedy.
# 4) Causes - the chunk of text that describe the causes
# 5) Treatment - the chunk of text that describe the treatment
class ConditionNode(BaseNode):
    def __init__(self, ID, name): 
        super.__init__(self, ID, name)
        self.Symptom = [] #[Holds all the Condition Nodes]
        self.AKA = [] #[Holds all the Also Known As Nodes]
        self.MinSymptomMatch = 1 # (we set this because each condition/disease can have different num of symptoms, this can be the high level decider for probing)
        self.Causes = None
        self.Treatment = None

        def AddSymptomNode(self, SymptomNode):
            if SymptomNode not in self.Symptom:
                self.Symptom.append(SymptomNode)
                if SymptomNode not in self.Edge:
                    self.Edge.append(SymptomNode)

        def AddAKANode(self, AKANode):
            if AKANode not in self.AKA:
                self.AKA.append(AKANode)
                if AKANode not in self.Edge:
                    self.Edge.append(AKANode)
        
        # useful for topic modelling training when pushing in tokens
        def GetAllSymptomsTextChunk(self):
            return "_".join(symptom.Name for symptom in self.Symptom)


# These are by right just "pointing" to the common condition name
# Therefore the condition in this node should be the common ConditionNode
class AKANode(BaseNode):
    def __init__(self, ID, name, Condition): 
        super.__init__(self, ID, name)
        self.isCaseVariant = False # Refer to CaseNode
        self.Condition = Condition # This node should by right just give us the referenced condition

# 1 cause to 1 condition matching at the moment
class CausesNode(BaseNode):
    def __init__(self, ID, name, Condition): 
        super.__init__(self, ID, name)
        self.Condition = Condition
        self.CausesTextChunk= None  # (for now we only want to concentrate on the symptoms, and not root finding causes)


# 1 treatment to 1 condition matching at the moment
class TreaatmentNode(BaseNode):
    def __init__(self, ID, name, Condition): 
        super.__init__(self, ID, name)
        self.Condition = Condition
        self.TreatmentTextChunk= None  # (for now we only want to concentrate on the symptoms, and not suggesting best treatment)


# Assume we start off by using the CBR model
# We first create a "Case object", which we will use it for matching and reasoning
# since our end result is that we want to match this "case" with one or more (depends) of our ConditionNode
# and since a perfect match will mean ConditionNode meets the most symptoms in our "case"
# It can be a variant of the AKANode with added properties like:
# 1) isCaseVariant - prop that determine if we display this to other users
# 2) ChatHistory - the base evidence
# 3) CollectedSymptom - once a symptom matched with ChatHistory, we will append to this
# 3) Dictionary of SuspectedConditions (key) - ConditionNode that has the closest match
#    MatchedConfidence (value) - temporary cal can be CollectSymptoms.length / SuspectedConditionNode.Symptoms.length
class CaseNode(AKANode):
    def __init__(self, ID, name, ChatHistory): 
        super.__init__(self, ID, name, Condition=None)  # The condition is the final "verdict"
        self.isCaseVariant = True
        self.ChatHistory = ChatHistory
        self.CollectedSymptom = []
        self.SuspectedCondition = {}
