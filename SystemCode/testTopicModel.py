from topicmodel import TopicModel

question = "My fish has worm sticking out from its anus."
#question = "My fish eye so bloody out and the scale is coming out. Yesterday night, he does not eat and is not balancing well OH THE EYES now like cloud"
tm = TopicModel()
symptoms = tm.getSymptoms(question, '', False)
for s in symptoms:
    print('*** symptom ***: ', s.description)
    print('** confidence **: ', s.confidence)
    print('* question *: ', s.question)
    for d in s.diseases:
        print('disease: ', d.name)
    print()

print(tm.convert_to_tokens("Grey or green dots on skin"))