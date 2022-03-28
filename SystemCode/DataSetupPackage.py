## import library
from DataAccessLayer import DataAccessLayer
import os
import pandas as pd

class DataSetUpPackage():
    """
    Assuming you have your CSV and neo4j DB all setup.
    """
    def __init__(self, filePath=None, disease_file=None, symptom_file=None, med_file=None):
        self.DiseaseFilename = disease_file or 'FishDB_Disease.csv'     # pass in if using your own csv dataset
        self.SymptomFilename = symptom_file or 'FishDB_Symptom.csv'     # pass in if using your own csv dataset
        self.MedicationFilename = med_file or 'FishDB_Medication.csv'   # pass in if using your own csv dataset

        # if you directly clone from git hub < this will use ./RawCSV folder
        self.FilePath = filePath or self.GetDefaultCSVPath

        self.SessionInstance = None
        self.Disease_DF = None
        self.Symptom_DF = None
        self.Medication_DF = None
        self.Verbose = False
        self.Disease_DF_RowIndex = 0
        
    @property
    def ReadCSVAndPopulateDB(self, indexCol=None):
        IndexCol = indexCol or 'ID'       
        self.Disease_DF = pd.read_csv(self.FilePath + self.DiseaseFilename,
                                      encoding ="ISO-8859-1", index_col=IndexCol)
        self.Symptom_DF = pd.read_csv(self.FilePath + self.SymptomFilename,
                                      encoding="ISO-8859-1", index_col=IndexCol)
        self.Medication_DF = pd.read_csv(self.FilePath + self.MedicationFilename,
                                         encoding="ISO-8859-1", index_col=IndexCol)
        return self
    
    @property    
    def GetDefaultCSVPath(self):
        folderpath = os.getcwd()
        if os.name == 'posix':
            folderpath += "/RawCSV/"
        else:
            folderpath += "\\RawCSV\\"
        return folderpath

    def CreateDiseaseNode(self, diseaseName=None):
        i = self.Disease_DF_RowIndex
        DiseaseName = diseaseName or self.Disease_DF.iloc[i,0] 
        query = (
            "MERGE (node: "+"Disease"+" {name: $name})"
            "RETURN node"
        )
        with self.SessionInstance as session:
            result = session.run(query, name=DiseaseName)
        if self.Verbose:
            print("create {0} node with name as {1}".format("Disease", DiseaseName))
            
    def SetDiseaseProps(self,diseaseName=None, environment=None,affected_fish=None,
                        cause=None,treatment=None,vetadvice=None):
        i = self.Disease_DF_RowIndex
        DiseaseName = diseaseName or self.Disease_DF.iloc[i,0] 
        Environment = environment or self.Disease_DF.iloc[i,2]
        Affected_fish = affected_fish or self.Disease_DF.iloc[i,3]
        Cause = cause or self.Disease_DF.iloc[i,16]
        Treatment = treatment or self.Disease_DF.iloc[i,17]
        Vet_advised = vetadvice or self.Disease_DF.iloc[i,18]
        query = (
            """
            MATCH (n:Disease {name: $name})
            SET n.environment = $env, n.affectfish = $afish, n.cause = $cause,
            n.treatment = $treatment, n.vet_advised = $vetadvise
            RETURN n
            """
        )

        with self.SessionInstance as session:
            result = session.run(query, name=DiseaseName, 
                                 env=Environment, afish=Affected_fish,
                                 cause=Cause, treatment=Treatment, vetadvise=Vet_advised
                                )
        if self.Verbose:
            print("Set props on {0}-{1}:".format("Disease", DiseaseName))
            print("environment - {0}".format(Environment))
            print("affectfish - {0}".format(Affected_fish))
            print("cause - {0}".format(Cause))
            print("treatment - {0}".format(Treatment))
            print("vet_advised - {0}".format(Vet_advised))
    
    def CreateAKANode(self,diseaseName=None,aka=None):
        i = self.Disease_DF_RowIndex
        DiseaseName = diseaseName or self.Disease_DF.iloc[i,0] 
        AKA = aka or self.Disease_DF.iloc[i,1]
        if pd.isnull(AKA) == False:
            query = (
                """
                MERGE (node: AKA {name: $name})
                RETURN node
                """
            )

            with self.SessionInstance as session:
                result = session.run(query, name=AKA)
            if self.Verbose:
                print("create {0} node with name as {1}".format("AKA", AKA))

            # add AKA relationship
            query = (
                """
                MATCH (n1 {name: $name1})
                MATCH (n2 {name: $name2})
                MERGE (n1) - [r:AKA] -> (n2)
                RETURN n1, n2, r
                """
            )

            with self.SessionInstance as session:
                result = session.run(query, name1=DiseaseName, name2=AKA)
            if self.Verbose:
                print("create {0} -AKA-> {1}".format(DiseaseName, AKA))
                
    def CreateSymptomNode(self,diseaseName=None,symptomColIndexStart=None,symptomColIndexEnd=None):
        i = self.Disease_DF_RowIndex
        DiseaseName = diseaseName or self.Disease_DF.iloc[i,0]
        ColStart = symptomColIndexStart or 4
        ColEnd = symptomColIndexEnd or 15
        disease_df = self.Disease_DF
        for j in range(ColStart, ColEnd):
            # iterate across the associated symptoms  
            if pd.isnull(disease_df.iloc[i,j]) == False:
                # We found a symptom, call the Symptom DataFrame and get the props
                symptomrow = self.Symptom_DF.loc[self.Symptom_DF['SymptomID'] == disease_df.iloc[i,j]]
                symptom_desc = symptomrow['Symptom'].values[0]
                symptom_token = None  # tm.ConvertToTokens(symptom_desc) :-> [string]
                symptom_type = symptomrow['SymptomType'].values[0]
                symptom_cat1 = symptomrow['SymptomCategory1'].values[0]
                symptom_cat2 = symptomrow['SymptomCategory2'].values[0]
                symptom_cat3 = symptomrow['SymptomCategory3'].values[0]
                symptom_question = symptomrow['Question'].values[0]
                symptom_url = symptomrow['ImageURL'].values[0]
                symptom_weight = str(symptomrow['Weight'].values[0])
                symptom_penalty = str(symptomrow['Penalty'].values[0])
                # add symptom node
                query = (
                    """
                    MERGE (n:Symptom {name: $name})
                    SET n.description =$desc, n.type = $stype, n.category1 = $cat1,
                    n.category2 = $cat2, n.category3 = $cat3, n.question = $qn, n.imageurl = $img
                    RETURN n
                    """
                )
                with self.SessionInstance as session:
                    result = session.run(query, name=disease_df.iloc[i,j],
                                         desc=symptom_desc, stype=symptom_type,
                                         cat1=symptom_cat1, cat2=symptom_cat2,
                                         cat3=symptom_cat3, qn=symptom_question, img=symptom_url)
                if self.Verbose:
                    print("create {0} node with name as {1}".format("Symptom", disease_df.iloc[i,j]))

                # add Disease hasSymptom Symptom relationship
                query = (
                    """
                    MATCH (n1 {name: $name1})
                    MATCH (n2 {name: $name2})
                    MERGE (n1) - [r:hasSymptom] -> (n2)
                    SET r.weight =$weight, r.penalty=$penalty                                
                    RETURN n1, n2, r
                    """
                )
                                
                with self.SessionInstance as session:
                    result = session.run(query, name1=DiseaseName, name2=disease_df.iloc[i,j]
                                         , weight=symptom_weight,penalty=symptom_penalty)
                if self.Verbose:
                    print("create {0} -hasSymptom-> {1}".format(DiseaseName, disease_df.iloc[i,j]))
                    
                # add Symptom isDetectedIn Disease relationship
                query = (
                    """
                    MATCH (n1 {name: $name1})
                    MATCH (n2 {name: $name2})
                    MERGE (n1) - [r:isDetectedIn] -> (n2) 
                    SET r.weight =$weight
                    RETURN n1, n2, r
                    """
                )

                with self.SessionInstance as session:
                    result = session.run(query, name1=disease_df.iloc[i,j], name2=DiseaseName, weight=symptom_weight)
                if self.Verbose:
                    print("create {0} -isDetectedIn-> {1}".format(disease_df.iloc[i,j], DiseaseName))
                    
            else:
                break
    
    def CreateMedicationNode (self,diseaseName=None,medColIndexStart=None,medColIndexEnd=None):
        i = self.Disease_DF_RowIndex
        DiseaseName = diseaseName or self.Disease_DF.iloc[i,0]
        ColStart = medColIndexStart or 19
        ColEnd = medColIndexEnd or 26
        disease_df = self.Disease_DF
        for j in range(ColStart, ColEnd):
            # iterate across the associated symptoms  
            if pd.isnull(disease_df.iloc[i,j]) == False:
                # We found meds, call the Med DataFrame and get the props
                medrow = self.Medication_DF.loc[self.Medication_DF['MedicineID'] == disease_df.iloc[i, j]]
                med_desc = medrow['Medicine'].values[0]
                medVOTC= medrow['Vet_Or_OTC'].values[0]
                med_TD = medrow['Treatment_Description'].values[0]
                med_Comfish = medrow['Complicate_Fish'].values[0]
                med_DangerHuman = medrow['IsDangerousHuman'].values[0]
                med_DangerPlant = medrow['IsDangerousPlants'].values[0]
                med_DangerInvert = medrow['IsDangerousInvertebrates'].values[0]
                # add Medication node
                query = (
                    """
                    MERGE (n:Medication {name: $name})
                    SET n.description =$desc, n.vet_or_OTC = $VOTC, n.treatment_desc = $medtd,
                    n.complicate_fish = $comfish, n.danger_human = $dangerhuman, 
                    n.danger_plant = $dangerplant, n.danger_invertebrates = $dangerinvert
                    RETURN n
                    """
                )
                with self.SessionInstance as session:
                    result = session.run(query, name=disease_df.iloc[i,j], desc=med_desc, VOTC=medVOTC,
                                         medtd=med_TD, comfish=med_Comfish, dangerhuman=med_DangerHuman,
                                         dangerplant=med_DangerPlant,dangerinvert=med_DangerInvert)
                if self.Verbose:
                    print("create {0} node with name as {1}".format("Medication", disease_df.iloc[i,j]))

                # add Disease useMedication Medication relationship
                query = (
                    "MATCH (n1 {name: $name1})"
                    "MATCH (n2 {name: $name2})"
                    "MERGE (n1) - [r:"+"useMedication"+"] -> (n2)"   
                    "RETURN n1, n2, r"
                )

                with self.SessionInstance as session:
                    result = session.run(query, name1=DiseaseName, name2=disease_df.iloc[i,j])
                if self.Verbose:
                    print("create {0} -useMedication-> {1}".format(DiseaseName, disease_df.iloc[i,j]))
                
                # add Medication knownTreatment Disease relationship
                query = (
                    "MATCH (n1 {name: $name1})"
                    "MATCH (n2 {name: $name2})"
                    "MERGE (n1) - [r:"+"knownTreatment"+"] -> (n2)"   
                    "RETURN n1, n2, r"
                )

                with self.SessionInstance as session:
                    result = session.run(query, name1=disease_df.iloc[i,j], name2=DiseaseName)
                if self.Verbose:
                    print("create {0} -knownTreatment-> {1}".format(disease_df.iloc[i,j], DiseaseName))
            else:
                break
    
    def PopulateNeo4j(self, neo4jSessionInstance, verbose=False):
        self.SessionInstance = neo4jSessionInstance
        self.Verbose = verbose
        disease_df = self.Disease_DF
        
        for i in range(disease_df.shape[0]):            
            # traverse row-by-row
            # set row index
            self.Disease_DF_RowIndex = i
            
            # Create disease nodes          
            self.CreateDiseaseNode()

            # Set some props to Disease
            # straight forward labelling are environment and affected fish at the moment
            # By right we should add Causes & Also treatment as Nodes
            # However, these are merely a chunk of text suitable only for props at this moment
            self.SetDiseaseProps()
            
            # Create AKA NODES - also known as
            self.CreateAKANode()
            
            # add symptom nodes and relationship to disease
            self.CreateSymptomNode()
            
            # add Med nodes
            self.CreateMedicationNode()
            
# To set up the neo4jDB
# Call the data access layer to first establish the data connection, then run the follow by uncommenting:
# dbcon = DataAccessLayer(username='neo4j',password='neo123456').CreateDBConnection
# dbcon.ClearCurrentDB  # This will clean up the neo4jDB
# DataSetUpPackage().ReadCSVAndPopulateDB.PopulateNeo4j(dbcon.Session, verbose=True)


# Once neo4jDB is setup
# at this moment you can
# 1) get all nodes of a type - eg  run the follow by uncommenting:

# dbcon = DataAccessLayer(username='neo4j',password='neo123456').CreateDBConnection
# result2 = dbcon.GetAllNodeListOfType('Disease')
# for resulti in result2:
#     print(resulti.name)
#     print(resulti.environment)
#     for r in resulti.symptoms:
#         print(r.name)

