from flask import Flask, jsonify, request
from flask import render_template
from flask_cors import CORS, cross_origin
from conversation import *
from models import *
from datetime import datetime
app = Flask(__name__)
cors = CORS(app)


@app.route('/')
@cross_origin()
def hello_world():
    return render_template('index.html')


@app.route('/chat/<path:p>')
@cross_origin()
def hello_case(p):
    return render_template('index.html')


def processResponse(caseId, req, guided=True):
    rep = {'diseases': [], 'symptoms': [],
           'nextOpen': False, 'confirmedDiseases': []}

    tmProcess = Conversation().manageConversation(caseId, {}, req.get('body'))

    symConfirmList = {}
    symptomsRequest = req.get('symptoms')
    if symptomsRequest:
        for s in symptomsRequest:
            symConfirmList[s.get('name')] = s.get('confirmed')

    for s in tmProcess.get('symptoms'):
        rep['symptoms'].append({'name': s.name, 'question': s.question, 'image': s.imageurl,
                                'confirmed': True, 'AIconfirmed': True})
        symConfirmList[s.name] = True

    resultProcess = Conversation().manageConversation(caseId, symConfirmList)

    # only guided would return next set of symptoms
    if guided:
        for s in resultProcess.get('symptoms'):
            rep['symptoms'].append(
                {'name': s.name, 'question': s.question, 'image': s.imageurl, 'confirmed': False})
        # app.logger.info(s['confirmed'])

    for i, d in enumerate(resultProcess.get('diseases')):
        if i > 2:
            break
        if d[1] > 0:
            cdSymptoms = []
            cdMeds = []
            for cdsymp in d[0].symptoms:
                cdSymptoms.append(
                    {'name': cdsymp.name, 'image': cdsymp.imageurl, 'description': cdsymp.description})
            for cdMed in d[0].medications:
                cdMeds.append(
                    {'name': cdMed.name, 'vet_or_OTC': cdMed.vet_or_OTC, 'description': cdMed.description})

            rep['diseases'].append({
                'name': d[0].name,
                'cause': d[0].cause,
                'confidence': "{:.0%}".format(d[1]),
                'rating': d[2],
                'treatment': d[0].treatment,
                'vet_advised': d[0].vet_advised,
                'environment': d[0].environment,
                'affectfish': d[0].affectfish,
                'aka': d[0].aka[0].name if d[0].aka and len(d[0].aka) > 0 else None,
                'symptoms': cdSymptoms,
                'medication': cdMeds
            })
    return rep


@app.route('/cases/<string:caseId>/guided', methods=['POST'])
@cross_origin()
def getGuidedNext(caseId):
    req = request.json
    rep = processResponse(caseId, req)
    return jsonify(rep)


@app.route('/cases/<string:caseId>/open', methods=['POST'])
@cross_origin()
def getOpenNext(caseId):
    req = request.json
    rep = processResponse(caseId, req, False)
    return jsonify(rep)


@app.route('/cases/<string:caseId>')
@cross_origin()
def getCase(caseId):
    rep = {'messages': [{'body': 'How can I help you?',
                         'time': datetime.now().strftime("%H:%M")}]}
    messages = CaseService().getCaseMessages(caseId)
    if messages and len(messages) > 0:
        rep['messages'] = messages
    return jsonify(rep)


@app.route('/cases/<string:caseId>', methods=['POST'])
@cross_origin()
def updateCase(caseId):
    req = request.json
    CaseService().saveCaseMessages(caseId, req)
    return ""


@app.route('/cases/<string:caseId>/rating', methods=['POST'])
@cross_origin()
def updateCaseRating(caseId):
    req = request.json
    CaseService().updateCaseRating(caseId, req['diseaseName'], req['rating'])
    return ""


@app.route('/cases', methods=['POST'])
@cross_origin()
def createCase():
    rep = {'name': 'case3'}
    case = CaseService().createCase()
    rep['name'] = case.name
    return jsonify(rep)
