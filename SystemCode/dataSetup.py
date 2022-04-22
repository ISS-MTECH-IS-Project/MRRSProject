from DataSetupPackage import DataSetUpPackage
from DataAccessLayer import DataAccessLayer
import nltk
import spacy

# download nlp dependencies
spacy.cli.download('en_core_web_lg')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')

# setup the knowledge in Neo4j database
dbcon = DataAccessLayer(
    username='neo4j', password='neo123456').CreateDBConnection
dbcon.ClearCurrentDB  # This will clean up the neo4jDB
DataSetUpPackage().ReadCSVAndPopulateDB.PopulateNeo4j(dbcon.Session, verbose=True)
