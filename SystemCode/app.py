from flask import Flask, jsonify, request
from flask import render_template
from flask_cors import CORS, cross_origin
from conversation import *
from DataAccessLayer import *
from models import *
app = Flask(__name__)
cors = CORS(app)

class CaseService(metaclass=SingletonMeta):
    caseCache = {}
    def getCaseMessages(self, caseName):
        return self.caseCache.get(caseName)
    def saveCaseMessages(self, caseName, messages):
        self.caseCache[caseName] = messages

@app.route('/')
@cross_origin()
def hello_world():
    return render_template('index.html')

@app.route('/chat/<path:p>')
@cross_origin()
def hello_case(p):
    return render_template('index.html')

# @app.route('/greeting')
# def greeting():
#     covControl = Conversation()
#     return covControl.getGreeting()

@app.route('/cases/<string:caseId>/guided', methods=['POST'])
@cross_origin()
def getGuidedNext(caseId):
    req = request.json
    symptomsRequest = req.get('symptoms')
    symConfirmList = {}
    for s in symptomsRequest:
        symConfirmList[s.get('name')] = s.get('confirmed')


    resultProcess = Conversation().manageConversation(caseId,symConfirmList)

    rep = {'diseases':[], 'symptoms':[], 'nextOpen':False, 'confirmedDiseases':[]}
    for s in resultProcess.get('symptoms'):
        rep['symptoms'].append({'name':s.name, 'question':s.question, 'image':s.imageurl, 'confirmed':False})
        # app.logger.info(s['confirmed'])

    for i,d in enumerate(resultProcess.get('diseases')):
        if i>2:
            break
        if d[1]>0:
            rep['diseases'].append({'name': d[0].name, 'cause': d[0].cause, 'confidence': "{:.0%}".format(d[1])})
        # app.logger.info(s['confirmed'])

    for cd in resultProcess.get('confirmedDiseases'):
        cdSymptoms =[]
        cdMeds = []
        for cdsymp in cd.symptoms:
            cdSymptoms.append({'name':cdsymp.name, 'image':cdsymp.imageurl,'description':cdsymp.description})
        for cdMed in cd.medications:
            cdMeds.append({'name': cdMed.name, 'vet_or_OTC': cdMed.vet_or_OTC, 'description': cdMed.description})

        rep['confirmedDiseases'].append({
            'name': cd.name,
            'cause': cd.cause,
            'treatment': cd.treatment,
            'vet_advised': cd.vet_advised,
            'environment':cd.environment,
            'affectfish':cd.affectfish,
            'aka':cd.aka.name or None,
            'symptoms': cdSymptoms,
            'medication': cdMeds
        })
        # app.logger.info(s['confirmed'])

    if len(resultProcess.get('symptoms')) == 0:
        rep['nextOpen'] = True

    return jsonify(rep)

@app.route('/cases/<string:caseId>/open', methods=['POST'])
@cross_origin()
def getOpenNext(caseId):
    req = request.json
    resultProcess = Conversation().manageConversation(caseId, {}, req.get('body'))

    rep = {'diseases': [], 'symptoms': [], 'nextOpen': False, 'confirmedDiseases':[]}

    for s in resultProcess.get('symptoms'):
        rep['symptoms'].append({'name':s.name, 'question':s.question, 'image':s.imageurl,
                                'confirmed':False, 'AIconfirmed':True})
        # app.logger.info(s['confirmed'])

    for d in resultProcess.get('diseases'):
        rep['diseases'].append({'name': d[0].name, 'description': d[0].cause})
        # app.logger.info(s['confirmed'])

    for cd in resultProcess.get('confirmedDiseases'):
        cdSymptoms =[]
        cdMeds = []
        for cdsymp in cd.symptoms:
            cdSymptoms.append({'name':cdsymp.name, 'image':cdsymp.imageurl,'description':cdsymp.description})
        for cdMed in cd.medications:
            cdMeds.append({'name': cdMed.name, 'vet_or_OTC': cdMed.vet_or_OTC, 'description': cdMed.description})

        rep['confirmedDiseases'].append({
            'name': cd.name,
            'cause': cd.cause,
            'treatment': cd.treatment,
            'vet_advised': cd.vet_advised,
            'environment':cd.environment,
            'affectfish':cd.affectfish,
            'aka':{cd.aka.name},
            'symptoms': cdSymptoms,
            'medication': cdMeds
        })

    if len(resultProcess.get('symptoms')) == 0:
        rep['nextOpen'] = True

    return jsonify(rep)

@app.route('/cases/<string:caseId>')
@cross_origin()
def getCase(caseId):
    rep = {'messages':[{'body':'How can I help you?'}],'symptoms':[]}
    for i in range(6):
        rep['symptoms'].append({'name':"name"+str(i), 'question':caseId+str(i), 'image':'/img'+str(i)+'.jpg'})
    return jsonify(rep)

@app.route('/cases', methods=['POST'])
@cross_origin()
def createCase():
    rep = {'name':'case3'}
    dbcon = DataAccessLayer().CreateDBConnection
    case = dbcon.CreateOrGetCaseNode()
    rep['name'] = case.name
    return jsonify(rep)