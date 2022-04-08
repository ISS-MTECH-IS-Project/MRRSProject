from topicmodel import TopicModel
from DataAccessLayer import DataAccessLayer

dbcon = DataAccessLayer(username='neo4j',password='neo123456').CreateDBConnection
#question = "My fish has worm sticking out from its anus."
#question = "boy My fish has sore anus"
#question = "my fish has worm on body"
question = "My fish eye so bloody out and the scale is coming out. Yesterday night, he does not eat and is not balancing well OH THE EYES now like cloud"
#question = "My fish eye so bloody out and the scale is coming out."
#question = "Yesterday night, my fish does not eat and is not balancing well"
tm = TopicModel()

symptoms = tm.getSymptoms(dbcon, question, verbose=True)
#print(symptoms)
if len(symptoms) > 0:    
    for key in symptoms:
        # print('*** symptom ***: ', s.description)
        # print('** confidence **: ', s.confidence)
        # print('* question *: ', s.question)
        mysymp = dbcon.GetOneSymptomNode(key)
        print(key)
        for d in mysymp.diseases:
            print('disease: ', d.name)
else:
    print('No disease found')

#print(tm.convert_to_tokens("Grey or green dots on skin"))