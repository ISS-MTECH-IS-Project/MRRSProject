from tkinter import S
# from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from models import *
import spacy
from DataAccessLayer import DataAccessLayer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from TextPreprocessing import text_preprocessing

# Hyperparameters for TopicModel
similarityThreshold = 0.75


class TopicModel(metaclass=SingletonMeta):

    allSymptomNodes = []
    stopwords = []

    def __init__(self):
        self.symptoms_size = 10
        self.nlp = spacy.load('en_core_web_lg')
        self.nlp = self.add_stopwords(self.nlp)
        self.stopwords = self.nlp.Defaults.stop_words
        dbcon = DataAccessLayer().CreateDBConnection
        self.allSymptomNodes = dbcon.GetAllNodeListOfType('Symptom')

    # get list of symptoms from the question and answer
    def getSymptoms(self, dbcon: DataAccessLayer, question: str, threshold=similarityThreshold, verbose=False) -> {str: float}:
        #topicFromUser = self.build_top_model(question)
        # passing dcon in to prevent object bloat and also eventual managed instanced connection (factory or singleton)
        # dbcon = DataAccessLayer(dbName='fishdiseases', username='neo4j',password='password').CreateDBConnection
        if len(self.allSymptomNodes) == 0:
            self.allSymptomNodes = dbcon.GetAllNodeListOfType('Symptom')
        if verbose:
            print("text from user: ", question)
            #print('keywords: ', topicFromUser)
            print()
        #tempSymptoms = []
        symptoms = {}
        #sentence1 = self.nlp(question)
        sentence1 = self.nlp(self.text_preprocessing(question, self.nlp))
        #sentence1 = self.nlp(topicFromUser)
        print("tokens = ", sentence1)
        for symptomNode in self.allSymptomNodes:
            # using spacy
            #sentence2 = self.nlp(self.lower_casing(symptomNode.description))
            sentence2 = self.nlp(self.text_preprocessing(
                symptomNode.description, self.nlp))
            similarity = sentence1.similarity(sentence2)

            if similarity > threshold:
                symptoms[symptomNode.name] = similarity

            # tempSymptoms.append({'symptom':symptomNode.description, 'symptom_name':symptomNode.name,
                # 'similarity':similarity, 'question':symptomNode.question,
                # 'diseases':symptomNode.diseases})

        symptoms = dict(
            sorted(symptoms.items(), key=lambda item: item[1], reverse=True))

        # for s in symptoms:
        #    print("symptom: ", s)
        #    print("confidence: ", symptoms[s])

        # for tempSymptom in tempSymptoms[0:self.symptoms_size]:
        #     if tempSymptom['similarity'] > threshold:
        #         symptom = dbcon.GetOneSymptomNode(tempSymptom['symptom_name'])
        #         symptoms[symptom] = tempSymptom['similarity']
        #         symptom.description = tempSymptom['symptom']
        #         symptom.question = tempSymptom['question']
        #         symptom.confidence = tempSymptom['similarity']
        #         symptom.diseases = tempSymptom['diseases']
        if verbose:
            print('===============')

        return symptoms

    def build_top_model(self, text, delimiter=" "):
        text = text_preprocessing(text)
        sparse_vectorizer = CountVectorizer(strip_accents='unicode')
        sparse_vectors = sparse_vectorizer.fit_transform(text)
        # print(sparse_vectors.shape)
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
            t = delimiter.join([feature_names[i]
                               for i in topic.argsort()[:-n_top_words - 1:-1]])

        return t

    # Print the top-n key words
    def print_top_words(model, feature_names, n_top_words):
        for topic_idx, topic in enumerate(model.components_):
            print("Topic #%d:" % topic_idx)
            print(" ".join([feature_names[i]
                  for i in topic.argsort()[:-n_top_words - 1:-1]]))
        print()

    def jaccard_similarity(self, x, y):
        """ returns the jaccard similarity between two lists """
        intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
        union_cardinality = len(set.union(*[set(x), set(y)]))
        return intersection_cardinality/float(union_cardinality)

    def convert_to_tokens(self, desc: str, delimiter=" "):
        tokens = self.build_top_model(desc, delimiter)

        return tokens

    def lower_casing(self, sentence):
        new_sentence = ''.join([(chr(ord(char) + 32) if ord(char) >
                               64 and ord(char) < 91 else chr(ord(char))) for char in sentence])
        return new_sentence

    def add_stopwords(self, nlp):
        stopwords = None
        with open('./stopwords.txt') as file:
            stopwords = [stopword.replace('\n', '')
                         for stopword in file.readlines()]

        for stopword in stopwords:
            nlp.Defaults.stop_words.add(stopword)

        return nlp

    def text_preprocessing(self, raw_sentence, nlp_tool):
        token_sentence = nlp_tool(self.lower_casing(raw_sentence))
        preprocessed_sentence = None

        preprocessed_sentence = [token.lemma_ for token in token_sentence if token.text not in self.stopwords and not token.pos_ ==
                                 'X' and not token.is_punct and not token.is_digit and not token.is_quote]
        #preprocessed_sentence = spell_correction(preprocessed_sentence)

        preprocessed_sentence = " ".join(preprocessed_sentence)
        #print("processed user sentence: ", preprocessed_sentence)
        return preprocessed_sentence
