from tkinter import S
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from models import *
import spacy

from DataAccessLayer import DataAccessLayer
from NeomodelGraphObject import (Symptom, Disease, AKA, Medication, CaseInc, SuspectedSymptomRel)

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from TextPreprocessing import text_preprocessing

class TopicModel(metaclass=SingletonMeta):
    symptoms_size = 10
        
    nlp = spacy.load('en_core_web_lg')

    # get list of symptoms from the question and answer
    def getSymptoms(self, question:str, threshold = 0.7) -> list:
        topicFromUser = self.build_top_model(question)
        dbcon = DataAccessLayer(dbName='fishdiseases', username='neo4j',password='password').CreateDBConnection        
        allSymptomNodes = dbcon.GetAllNodeListOfType('Symptom')
        print("text from user: ", question)
        print('keywords: ', topicFromUser)
        print()
        tempSymptoms = []
        symptoms = []

        for symptomNode in allSymptomNodes:       
            # using spacy
            sentence1 = self.nlp(topicFromUser)
            sentence2 = self.nlp(symptomNode.description) 
            similarity = sentence1.similarity(sentence2)

            tempSymptoms.append({'symptom':symptomNode.description, 'similarity':similarity, 'question':symptomNode.question, 'diseases':symptomNode.diseases})
        
        tempSymptoms = sorted(tempSymptoms, key=lambda x: x['similarity'], reverse=True)

        for tempSymptom in tempSymptoms[0:self.symptoms_size]:  
            if tempSymptom['similarity'] > threshold:
                symptom = Symptom()
                symptom.description = tempSymptom['symptom']
                symptom.question = tempSymptom['question']
                symptom.confidence = tempSymptom['similarity']
                symptom.diseases = tempSymptom['diseases']
                symptoms.append(symptom)

        print('===============')

        return symptoms

    def build_top_model(self, text):
        text = text_preprocessing(text)
        sparse_vectorizer = CountVectorizer(strip_accents = 'unicode')
        sparse_vectors = sparse_vectorizer.fit_transform(text)
        #print(sparse_vectors.shape)
        # To define number of topics
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

    def convert_to_tokens(self, desc:str):
        tokens = self.build_top_model(desc)

        return tokens

