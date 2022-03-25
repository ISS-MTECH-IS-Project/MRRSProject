from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from models import *

from DataAccessLayer import DataAccessLayer
from NeomodelGraphObject import (Symptom, Disease, AKA, Medication, CaseInc, SuspectedSymptomRel)

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from TextPreprocessing import text_preprocessing

class TopicModel(metaclass=SingletonMeta):
    symptoms_size = 10
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    
    # get list of symptoms from the question and answer
    def getSymptoms(self, question:str, answer:str, isOption:bool) -> list:

        topicFromUser = self.build_top_model(question)
        dbcon = DataAccessLayer(dbName='fishdiseases', username='neo4j',password='password').CreateDBConnection        
        result2 = dbcon.GetAllNodeListOfType('Symptom')
        tempSymptoms = []
        symptoms = []

        for resulti in result2:
            #print('Symptom: ', resulti.name)
            #print('Question', resulti.question)
            #print('Diseases: ', len(resulti.diseases))
            topicFromDB = self.build_top_model(resulti.description)
            sentences = [topicFromUser, topicFromDB]
            #sentence_embeddings = self.model.encode(sentences)

            result = self.jaccard_similarity(sentences[0], sentences[1])

            tempSymptoms.append({'symptom':resulti.description, 'similarity':result, 'question':resulti.question, 'diseases':resulti.diseases})
        
        tempSymptoms = sorted(tempSymptoms, key=lambda x: x['similarity'], reverse=True)

        for tempSymptom in tempSymptoms[0:self.symptoms_size]:
            print(tempSymptom['symptom'], tempSymptom['similarity'])
            symptom = Symptom()
            symptom.description = tempSymptom['symptom']
            symptom.question = tempSymptom['question']
            symptom.diseases = tempSymptom['diseases']
            symptoms.append(symptom)

        print('===============')

        return symptoms

    def text_preprocessing(self, text):
        text = text_preprocessing(text)
        sparse_vectorizer = CountVectorizer(strip_accents = 'unicode')
        sparse_vectors = sparse_vectorizer.fit_transform(text)
        #print(sparse_vectors.shape)

        return sparse_vectors

    def build_top_model(self, text):
        text = text_preprocessing(text)
        sparse_vectorizer = CountVectorizer(strip_accents = 'unicode')
        sparse_vectors = sparse_vectorizer.fit_transform(text)
        #print(sparse_vectors.shape)
        # Your super power to define number of topics
        n_topics = 1

        # Run LDA to generate topics/clusters
        lda = LatentDirichletAllocation(n_components=n_topics, max_iter=1000,
                                        learning_method='online',
                                        random_state=0)

        lda.fit(sparse_vectors)

        # Show the first n_top_words key words
        n_top_words = 10
        feature_names = sparse_vectorizer.get_feature_names()

        t = None
        for i, topic in enumerate(lda.components_):
            t = " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])

        return t

    # Print the top-n key words
    def print_top_words(model, feature_names, n_top_words):
        for topic_idx, topic in enumerate(model.components_):
            print("Topic #%d:" % topic_idx)
            print(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
        print()

    def jaccard_similarity(self, x, y):
        """ returns the jaccard similarity between two lists """
        intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
        union_cardinality = len(set.union(*[set(x), set(y)]))
        return intersection_cardinality/float(union_cardinality)

##### TEST #####
tm = TopicModel()
symptoms = tm.getSymptoms("my fish skin is peeling", '', False)
for s in symptoms:
    print('* symptom *: ', s.description)
    for d in s.diseases:
        print('disease: ', d.name)
    print()
