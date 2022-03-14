## import library
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

class DataAccessLayer():
    def __init__(self, neo4jURL =None,dbName=None,username=None, password=None):
        # Neo4j Settings 
        self.Neo4jDBURL = neo4jURL or "neo4j://localhost:7687"
        self.DefaultDB = dbName or "neo4j"
        self.DBUserName = username or "ENTER YOUR NEO4J USERNAME"
        self.DBPassword = password or "ENTER YOUR NEO4J PASSWORD HERE"
        self.Graph = None
        self.Session = None


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
    
    def GetAllFromTable(self,nodeLabel):
        """
        Get ALL rows from current Table \n
        Valid NodeLabels \n
        Symptom , Disease, AKA, Medication\n
        returns a disctionary of Nodes
        """
        query = (
                "MATCH (n:" + nodeLabel +")"
                "RETURN n"
            )
        with self.Session as session:
            results = session.run(query)
            Nodes = {}
            for result in results:
                Nodes[result['n']['name']]=result['n']
            return Nodes
    
    