from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
filename = "logs/data.txt"
app.filehandler = None
app.trackingList = []
app.isWorking = False

@app.route('/tracker', methods=['GET', 'POST'])
def track():
    if request.method == 'POST':
        app.trackingList.append(request.json['data'])
    
    return jsonify({'tracking': app.trackingList})
    
def toFile(response):
    if response.status_code == 200 and request.method == 'POST':
        if app.isWorking and len(app.trackingList)>0:
            app.filehandler.write(app.trackingList[-1]+os.linesep)
            app.filehandler.flush()
        else:
            print("Could not write file: "+filename)
    return response

def setup():
    try:
        if os.path.exists(filename):
            app.filehandler = open(filename, 'r+')
            app.trackingList = app.filehandler.readlines()
            app.isWorking = True
        else:
            app.filehandler = open(filename, 'w')
            app.trackingList = []
            app.isWorking = True
    except IOError:
        print ("Could not read file: "+ filename)


app.before_first_request(setup)
app.after_request(toFile)

if __name__ == '__main__':
    app.run(debug=False)