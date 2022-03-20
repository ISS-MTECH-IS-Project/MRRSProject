#pip install py2neo

from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
from py2neo.ogm import Repository
from py2neo import Graph,Path,Subgraph
from py2neo import NodeMatcher,RelationshipMatcher
# from Py2NeoGraphObject import (Symptom, Disease, AKA, Medication)
from neomodel import db, StructuredNode, config, match, relationship
from NeomodelGraphObject import (Symptom, Disease, AKA, Medication, CaseInc, SuspectedSymptomRel)
import uuid


# noinspection PyMethodMayBeStatic
class DataAccessLayer():

    def __init__(self, neo4jURL =None,dbName=None,username=None, password=None):
        # Neo4j Settings 
        self.Neo4jDBURL = neo4jURL or "neo4j://localhost:7687"
        self.DefaultDB = dbName or "neo4j"
        self.DBUserName = username or "ENTER YOUR NEO4J USERNAME"
        self.DBPassword = password or "ENTER YOUR NEO4J PASSWORD HERE"
        self.Graph = None
        self.Session = None

        config.DATABASE_URL = "bolt://"+self.DBUserName+":"+self.DBPassword+"@localhost:7687"
        # self.Py2NeoGraph = Graph(self.Neo4jDBURL, auth=(self.DBUserName, self.DBPassword))
        # self.Py2NeoRepo = Repository("bolt://neo4j@localhost:7687", password=self.DBPassword)

    #   region DB Connection & Config related

    # Always connect to the correct DB first before us
    @property
    def CreateDBConnection(self):
        # Initialize the graph DB 
        self.Graph = GraphDatabase.driver(
             self.Neo4jDBURL,
             auth=(self.DBUserName, self.DBPassword)
         )
        self.Session = self.Graph.session(database=self.DefaultDB)

        return self

    @property
    def ClearCurrentDB(self):
        """Delete all the nodes and relationships"""
        query = (
                "MATCH (all_nodes)"
                "OPTIONAL MATCH (all_nodes)-[all_rels]->()"
                "DELETE all_nodes, all_rels"
            )
        with self.Session as session:
            result = session.run(query)

    def ChangeDB(self, dbName):
        """Change underlying DataAccessLayer DB"""
        self.DefaultDB = dbName
        self.Session = self.Graph.session(database=self.DefaultDB)
        return self

    #   endregion

    #   region Single Node Operations

    def __GetOneNodeOfANYTypeUsingName(self,nodename:str):
        query= "MATCH (n) where n.name =$name return n"
        param_dictionary = {'name':nodename}
        results, meta = db.cypher_query(query, param_dictionary,resolve_objects=True)
        if results:
            node = results[0][0]
            nodeLabel, = node.labels
            if nodeLabel == 'Disease':
                return self.GetOneDiseaseNode(node.id)
            elif nodeLabel == 'Symptom':
                return self.GetOneSymptomNode(node.id)
            elif nodeLabel == 'AKA':
                return self.GetOneAKANode(node.id)
            elif nodeLabel == 'Medication':
                return self.GetOneMedicationNode(node.id)
            elif nodeLabel == 'Case':
                return self.CreateOrGetCaseNode(node.id)
            else:
                return node
        return None

    def __GetOneNodeOfSpecificTypeUsingName(self, nodename:str, nodeLabel:str):
        query = "MATCH (n:nodelabel) where n.name=$name return n"
        query = query.replace("nodelabel",nodeLabel)
        param_dictionary = {'name': nodename}
        results, meta = db.cypher_query(query, param_dictionary, resolve_objects=True)
        if results:
            node = results[0][0]
            return node
        return None

    def GetOneDiseaseNode(self,name:str = None, ID:int = None) -> Disease:
        """
        Get one disease node using name
        If ID is not null, ID will be used
        """
        if ID is None:
            return Disease.nodes.first_or_none(name=name)
        else:
            diseases = Disease.nodes.all()
            for d in diseases:
                if d.id == ID:
                    return d

    def GetOneSymptomNode(self,name:str = None, ID:int = None) -> Symptom:
        """
        Get one symptom node using name
        If ID is not null, ID will be used
        """
        if ID is None:
            return Symptom.nodes.first_or_none(name=name)
        else:
            symptoms = Symptom.nodes.all()
            for s in symptoms:
                if s.id == ID:
                    return s
            return None

    def CreateOrGetSymptomNode(self, symptomName:str = None, onlyGet:bool=False) -> Symptom:
        checkforsymptom = Symptom.nodes.first_or_none(name=symptomName)
        if checkforsymptom is None and not onlyGet:
            symptom_instance = Symptom(name=symptomName)
            symptom_instance.save()
            return symptom_instance
        else:
            return checkforsymptom

    def GetAllSymptomFromDiseaseOrCaseByNameOrID(self, nodename:str = None, ID:int = None) -> [Symptom]:
        TryDiseaseNode = self.GetOneDiseaseNode(nodename, ID)
        TryCaseNode = self.CreateOrGetCaseNode(nodename, ID, True)

        if TryDiseaseNode:
            # return TryDiseaseNode.symptoms.all()
            # Hackish -> by changing the hackish line in match.py in neomodel cypher
            # in view that we are not likely to write crazy shell script, using cypher instead.
            query = """
            MATCH (d:Disease) WHERE d.name=$name with d 
            OPTIONAL MATCH ((d)-[r1:`hasSymptom`]->(symptoms:Symptom)) 
            RETURN symptoms
            """
            param_dictionary = {'name': TryDiseaseNode.name}
            results, meta = db.cypher_query(query, param_dictionary, resolve_objects=True)
            return results
        if TryCaseNode:
            # return TryCaseNode.suspected_symptoms.all() - see above
            query = """
            MATCH (c:CaseInc) WHERE c.name=$name with c 
            OPTIONAL MATCH ((c)-[r1:`suspectedSymptom`]->(symptoms:Symptom)) 
            RETURN symptoms
            """
            param_dictionary = {'name': TryCaseNode.name}
            results, meta = db.cypher_query(query, param_dictionary, resolve_objects=True)
            return results
        return None

    def GetAllDiseaseFromSymptomOrCaseByNameOrID(self, nodename:str = None, ID:int = None) -> [Symptom]:
        TrySymptomNode = self.GetOneSymptomNode(nodename, ID)
        TryCaseNode = self.CreateOrGetCaseNode(nodename, ID, True)

        if TrySymptomNode:
            # return TrySymptomNode.diseases.all() - see above
            query = """
            MATCH (s:Symptom) WHERE s.name=$name with s 
            OPTIONAL MATCH ((s)-[r1:`isDetectedIn`]->(diseases:Disease)) 
            RETURN diseases
            """
            param_dictionary = {'name': TrySymptomNode.name}
            results, meta = db.cypher_query(query, param_dictionary, resolve_objects=True)
            return results
        if TryCaseNode:
            # return TryCaseNode.suspected_diseases.all() - see above
            query = """
            MATCH (c:CaseInc) WHERE c.name=$name with c 
            OPTIONAL MATCH ((c)-[r1:`suspectedDisease`]->(diseases:Disease)) 
            RETURN diseases
            """
            param_dictionary = {'name': TryCaseNode.name}
            results, meta = db.cypher_query(query, param_dictionary, resolve_objects=True)
            return results
        return None

    def GetOneAKANode(self,name:str = None, ID:int = None) -> AKA:
        """
        Get one AKA node using name
        If ID is not null, ID will be used
        """
        if ID is None:
            return AKA.nodes.first_or_none(name=name)
        else:
            AKAs = AKA.nodes.all()
            for a in AKAs:
                if a.id == ID:
                    return a
            return None

    def GetOneMedicationNode(self, name:str = None, ID:int = None) -> Medication:
        """
        Get one medication node using name
        If ID is not null, ID will be used
        """
        if ID is None:
            return Medication.nodes.first_or_none(name=name)
        else:
            medications = Medication.nodes.all()
            for m in medications:
                if m.id == ID:
                    return m
            return None

    def __CreateOrGetCaseNode(self, casename:str = None, onlyGet:bool = False):
        checkforcase = CaseInc.nodes.first_or_none(name=casename)
        if checkforcase is None and not onlyGet:
            case_instance = CaseInc(name=casename)
            case_instance.save()
            return case_instance
        else:
            return checkforcase

    def __CreateAnonymousCaseNode(self):
        case_instance = CaseInc(name="Case-" + str(uuid.uuid4())[:8])
        case_instance.save()
        return case_instance

    def CreateOrGetCaseNode(self, casename:str = None, ID:int = None, onlyGet:bool = False) -> CaseInc:
        """
        ID will take precedent if present.
        Will attempt to use ID(precedent) or name to search for node
        If node is not found in DB, an anonymous (meaning random assign name) Case node will be created
        """
        if ID is None:
            if casename:
                return self.__CreateOrGetCaseNode(casename, onlyGet)
            else:
                if not onlyGet:
                    return self.__CreateAnonymousCaseNode()
                else:
                    return None
        else:
            cases = CaseInc.nodes.all()
            for c in cases:
                if c.id == ID:
                    return c
            # ID not found eh?
            if casename:
                self.__CreateOrGetCaseNode(casename, onlyGet)
            else:
                if not onlyGet:
                    return self.__CreateAnonymousCaseNode()
                else:
                    return None

    def SaveCaseNode(self,case_instance:CaseInc) -> CaseInc:
        """
        Save Case node to DB
        In future, this should be the over-arch
        """
        case_instance.save()
        return case_instance

    def DeleteCaseNode(self,casename:str = None,case_instance:CaseInc = None):
        """
        Delete a Case node
        If Case is pass it, it will be used and name will be ignored
        """
        if case_instance is None:
            if not casename:
                caseToDelete = CaseInc.nodes.get_or_none(name=casename)
                if caseToDelete is not None:
                    caseToDelete.delete()
        else:
            case_instance.delete()

    def UpdateDiseaseToCase(self,case_instance:CaseInc, suspectedDisease:Disease, confidence:float=0) -> CaseInc:
        rel = case_instance.suspected_diseases.relationship(suspectedDisease)
        if rel:
            rel.confidence = confidence
            rel.save()
        else:
            rel = case_instance.suspected_diseases.connect(suspectedDisease, {'confidence':confidence})
            case_instance.save()
        return case_instance

    def UpdateSymptomToCase(self,case_instance:CaseInc, suspectedSymptom:Symptom, suspectedLevel:float=1.0) -> CaseInc:
        rel = case_instance.suspected_symptoms.relationship(suspectedSymptom)
        if rel:
            rel.suspectedLevel = suspectedLevel
            rel.save()
        else:
            case_instance.suspected_symptoms.connect(suspectedSymptom, {'suspectedLevel':suspectedLevel})
            case_instance.save()
        return case_instance

    def PushAllSymptomOfAnotherDiseaseToCase(self,case_instance:CaseInc, saidDisease:Disease) -> CaseInc:
        if saidDisease:
            for symptom in saidDisease.symptoms:
                case_instance.suspected_symptoms.connect(symptom)
        case_instance.save()
        return case_instance

    def RemoveAllMatchingDiseaseFromCase(self,case_instance:CaseInc, removeDisease:[Disease]) -> CaseInc:
        if removeDisease:
            for disease in removeDisease:
                case_instance.suspected_diseases.disconnect(disease)
        case_instance.save()
        return case_instance

    def RemoveAllMatchingSymptomFromCase(self,case_instance:CaseInc, removeSymptom:[Symptom]) -> CaseInc:
        if removeSymptom:
            for symptom in removeSymptom:
                case_instance.suspected_symptoms.disconnect(symptom)
        case_instance.save()
        return case_instance

    #   endregion

    #   region Multiple Node Operations

    def GetAllNodeListOfType(self,nodeLabel:str):
        """
        Get ALL rows from current Table \n
        Valid NodeLabels \n
        Symptom , Disease, AKA, Medication\n
        returns a dictionary of Nodes in flat list
        """

        if nodeLabel == 'Disease':
            return Disease.nodes.all()
        elif nodeLabel == 'Symptom':
            return Symptom.nodes.all()
        elif nodeLabel == 'AKA':
            return AKA.nodes.all()
        elif nodeLabel == 'Medication':
            return Medication.nodes.all()
        elif nodeLabel == 'Case':
            return CaseInc.nodes.all()
        else:
            return None

    def DeleteAllNodeListOfType(self, nodeLabel:str):
        """
        Get ALL rows from current Table \n
        Valid NodeLabels \n
        Symptom , Disease, AKA, Medication\n
        returns a dictionary of Nodes in flat list
        """
        templateQuery = "MATCH (n:MYTEMPLATEWORD) optional match (n)-[r]->() delete n,r"
        if nodeLabel == 'Disease':
            templateQuery = templateQuery.replace("MYTEMPLATEWORD","Disease")
        elif nodeLabel == 'Symptom':
            templateQuery = templateQuery.replace("MYTEMPLATEWORD","Symptom")
        elif nodeLabel == 'AKA':
            templateQuery = templateQuery.replace("MYTEMPLATEWORD","AKA")
        elif nodeLabel == 'Medication':
            templateQuery = templateQuery.replace("MYTEMPLATEWORD","Medication")
        elif nodeLabel == 'Case':
            templateQuery = templateQuery.replace("MYTEMPLATEWORD","CaseInc")
        else:
            return None

        with self.Session as session:
            result = session.run(templateQuery)

    #   endregion