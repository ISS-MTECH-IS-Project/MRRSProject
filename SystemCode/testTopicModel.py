from topicmodel import TopicModel
from DataAccessLayer import DataAccessLayer

dbcon = DataAccessLayer(username='neo4j',password='neo123456').CreateDBConnection
question = "My fish has worm sticking out from its anus."
#question = "My fish eye so bloody out and the scale is coming out. Yesterday night, he does not eat and is not balancing well OH THE EYES now like cloud"
tm = TopicModel()
symptoms = tm.getSymptoms(dbcon, question, verbose=True)
for key in symptoms:
    # print('*** symptom ***: ', s.description)
    # print('** confidence **: ', s.confidence)
    # print('* question *: ', s.question)
    mysymp = dbcon.GetOneSymptomNode(key)
    print(key)
    for d in mysymp.diseases:
        print('disease: ', d.name)

print(tm.convert_to_tokens("Grey or green dots on skin"))