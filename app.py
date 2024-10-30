from flask import Flask,jsonify,request
from DataBaseHandler import DatabaseHandler

app = Flask("API")

db = DatabaseHandler("data.json","asia/kolkata")

@app.route("/",methods=['GET'])
def home():
  return jsonify({"response":"enter some endpoint"})

@app.route("/add-question",methods=['POST'])
def add():
  content = request.json

  if content['ques'] and content['ans']:
    db.add_question(content['ques'],content['ans'])

  return ""

@app.route("/get-all-questions",methods=['GET'])
def all():
  return jsonify(db.list_all_questions())

@app.route("/rm-question",methods=['DELETE'])
def remove():
  ques = request.json["ques"]

  db.remove_question(ques)

  return "removed"

@app.route("/edit-question",methods=['PUT'])
def edit():
  ques = request.json["ques"]
  newAns = request.json["newAns"]

  db.edit_question(ques,newAns)

  return "edited"

@app.route("/get-answer",methods=['GET'])
def answer():
  ques = request.json["ques"]

  return jsonify(db.get_answer(ques))

if __name__=="__main__":
  app.run("0.0.0.0",8000)