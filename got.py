from flask import Flask,request,render_template
import requests

# constants
RUN_URL = u'http://api.hackerearth.com/code/run/'
CLIENT_SECRET = 'f51a28c274f4cc60f453f00d4a761b1ec7a4299b'

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/compile/', methods=['GET','POST'])
def compile():
    source= request.args.get("source")
    inp=request.args.get("input")
    lang=request.args.get("lang")

    if(source and inp):
        data = {
        'client_secret': CLIENT_SECRET,
        'async': 0,
        'source': source,
        'lang': lang,
        'input':inp,
        'time_limit': 5,
        'memory_limit': 262144,
        }

        r = requests.post(RUN_URL, data=data)

        x=r.json()
        if(x["message"]=="OK"):
            if(x["compile_status"]=="OK"):
                return x["run_status"]["output_html"]
            else:
                return "Error"
    elif (source):
        data = {
            'client_secret': CLIENT_SECRET,
            'async': 0,
            'source': source,
            'lang': lang,
            'time_limit': 5,
            'memory_limit': 262144,
        }

        r = requests.post(RUN_URL, data=data)

        x = r.json()
        if (x["message"] == "OK"):
            if (x["compile_status"] == "OK"):
                return x["run_status"]["output_html"]
            else:
                return "Error"
    else:
        return "No Source"

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
