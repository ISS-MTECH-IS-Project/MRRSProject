#pip install py2neo

from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
from py2neo.ogm import Repository
from py2neo import Graph,Path,Subgraph
from py2neo import NodeMatcher,RelationshipMatcher
# from Py2NeoGraphObject import (Symptom, Disease, AKA, Medication)
from neomodel import config
from NeomodelGraphObject import (Symptom, Disease, AKA, Medication, Case)


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

    def ChangeDB(self, dbName):
        """Change underlying DataAccessLayer DB"""
        self.DefaultDB = dbName
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

    def GetOneDiseaseNode(self,name)->Disease:
        """
        Get one disease node using name
        """
        return Disease.nodes.get(name=name)

    def GetOneSymptomNode(self,name)->Symptom:
        """
        Get one symptom node using name
        """
        return Symptom.nodes.get(name=name)

    def GetOneAKANode(self,name)->AKA:
        """
        Get one AKA node using name
        """
        return AKA.nodes.get(name=name)

    def GetOneMedicationNode(self,name)->Medication:
        """
        Get one medication node using name
        """
        return Medication.nodes.get(name=name)

    def GetOneCaseNode(self,name)->Case:
        """
        Get one case node using name
        """
        return Case.nodes.get(name=name)

    def SaveCaseNode(self,case_instance:Case)->Case:
        """
        Save case to DB
        """
        case_instance.save()

    def GetAllNodeListOfType(self,nodeLabel):
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
        else:
            return None
    