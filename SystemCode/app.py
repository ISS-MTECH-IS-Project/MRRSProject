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
@app.route('/chat/<path:path>')
@cross_origin()
def hello_world():
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

    rep = {'diseases':[], 'symptoms':[], 'nextOpen':False}
    for s in resultProcess.get('symptoms'):
        rep['symptoms'].append({'name':s.name, 'question':s.question, 'image':s.imageurl, 'confirmed':False})
        # app.logger.info(s['confirmed'])

    for d in resultProcess.get('diseases'):
        rep['diseases'].append({'name': d[0].name, 'description': d[0].cause})
        # app.logger.info(s['confirmed'])

    if len(resultProcess.get('symptoms')) == 0:
        rep['nextOpen'] = True

    return jsonify(rep)

@app.route('/cases/<string:caseId>/open', methods=['POST'])
@cross_origin()
def getOpenNext(caseId):
    req = request.json
    resultProcess = Conversation().manageConversation(caseId, {}, req.get('body'))

    rep = {'diseases': [], 'symptoms': [], 'nextOpen': False}

    for s in resultProcess.get('symptoms'):
        rep['symptoms'].append({'name':s.name, 'question':s.question, 'image':s.imageurl, 'confirmed':False})
        # app.logger.info(s['confirmed'])

    for d in resultProcess.get('diseases'):
        rep['diseases'].append({'name': d[0].name, 'description': d[0].cause})
        # app.logger.info(s['confirmed'])

    if len(resultProcess.get('symptoms')) == 0:
        rep['nextOpen'] = True

    return jsonify(rep)

@app.route('/cases/<string:caseId>')
@cross_origin()
def getCase(caseId):
    req = request.json
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