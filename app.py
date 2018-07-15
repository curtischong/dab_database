from flask import Flask, request
import json

app = Flask(__name__)

req = ""

@app.route("/send_dabs", methods=['POST','OPTIONS'])
def send_dabs():
    data = request.form.get('data') + "\n"
    with open("dabs.txt", "a") as myfile:
    	myfile.write(data)
    print(data[0][0])
    
    #data = json.loads(request.data)
    #data = request.json("stuff")
    return 'did things', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')

