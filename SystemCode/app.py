from flask import Flask, jsonify, request
from flask import render_template
from flask_cors import CORS, cross_origin
from conversation import *
app = Flask(__name__)
cors = CORS(app)

@app.route('/')
@app.route('/chat/<path:path>')
@cross_origin()
def hello_world():
    return render_template('index.html')

@app.route('/greeting')
def greeting():
    covControl = Conversation()
    return covControl.getGreeting()

@app.route('/cases/<string:caseId>/guided', methods=['POST'])
@cross_origin()
def getGuidedNext(caseId):
    req = request.json
    rep = {'disease':[], 'symptoms':[], 'nextOpen':True}
    for s in req.symptoms:
        rep['symptoms'].append({'name':s.name, 'question':caseId, 'image':'/img.jpg'})
        app.logger.info(s.confirmed)
    return jsonify(rep)

@app.route('/cases/<string:caseId>/open', methods=['POST'])
@cross_origin()
def getOpenNext(caseId):
    req = request.json
    rep = {'disease':[], 'symptoms':[], 'nextOpen':True}
    for i in range(6):
        rep['symptoms'].append({'name':"name"+str(i), 'question':caseId+str(i), 'image':'/img'+str(i)+'.jpg'})
    return jsonify(rep)

@app.route('/cases/<string:caseId>')
@cross_origin()
def getCase(caseId):
    req = request.json
    rep = {'messages':[{}],'symptoms':[]}
    for i in range(6):
        rep['symptoms'].append({'name':"name"+str(i), 'question':caseId+str(i), 'image':'/img'+str(i)+'.jpg'})
    return jsonify(rep)