from flask import Flask, request, render_template
import re
import json
from os import path
import move

# adding line following 
import main

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/settings", methods=['GET', 'POST'])
def settigns():
    myfile_path = path.join(path.dirname(__file__), 'settings.json')
    if request.method == 'POST':
        with open(myfile_path, "w") as settings:
            decodedRequestToString = request.data.decode("utf-8")
            parseTheDecodedString = json.loads(decodedRequestToString)
            json.dump(parseTheDecodedString, settings)
        move.loadSettings()
        return "saved"
    elif request.method == "GET":
        with open(myfile_path, "r") as settings:
            res = json.load(settings)
            print(type(res))
            
            return json.dumps(res)

@app.route("/pimove/<howToMove>")
def pimove(howToMove):
    print("move :", howToMove)
    dir = re.split("_", howToMove)[0]
    turbo = re.split("_", howToMove)[1]
    print(dir, turbo)

    if dir == "back":
        move.back()
    elif dir == "back" and turbo == "true":
        move.fast_back()
    elif dir == "forward":
        move.forward()
    elif dir == "forward" and turbo == "true":
        move.fast_forward()    
    elif dir == "right":
        move.right()
    elif dir == "left":
        move.left()
    elif dir == "forwardRight":
        move.forward_right()
    elif dir == "forwardLeft":
        move.forward_left()
    elif dir == "backRight":
        move.back_right()
    elif dir == "backLeft":
        move.back_left()
    elif dir == "stop":
        move.stop()
    
    return dir

@app.route("/follow/<follow>")
def followTheLine(follow):
    if follow == "start":
        print("start")
        #call the start
        main.lineFollowing()
    elif follow == "stop":
        print("stop")
        #call the stop
        main.stp()      
    return "yoo"

@app.route("/sumo/<sumo>")
def sumo(follow):
    if follow == "start":
        print("start")
        #call the start
        main.takeOut()
    elif follow == "stop":
        print("stop")
        #call the stop
        move.stop()
    return "yoo"

app.run(host="0.0.0.0")
