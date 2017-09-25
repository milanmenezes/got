from flask import Flask,request,render_template
import requests

# constants
RUN_URL = u'http://api.hackerearth.com/code/run/'
CLIENT_SECRET = 'f51a28c274f4cc60f453f00d4a761b1ec7a4299b'

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/third/')
def third():
    return render_template('third.html')

@app.route('/first/')
def first():
    return render_template('first.html')

@app.route('/second/')
def second():
    return render_template('second.html')

@app.route('/third_c/', methods=['GET','POST'])
def third_c():
    source= request.form.get("source")
    inp='''9
0 4 0 0 0 0 0 8 0
4 0 8 0 0 0 0 11 0
0 8 0 7 0 4 0 0 2
0 0 7 0 9 14 0 0 0
0 0 0 9 0 10 0 0 0
0 0 4 14 10 0 2 0 0
0 0 0 0 0 2 0 1 6
8 11 0 0 0 0 1 0 7
0 0 2 0 0 0 6 7 0'''

    if(source):
        data = {
        'client_secret': CLIENT_SECRET,
        'async': 0,
        'source': source,
        'lang': "C",
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
    else:
        return "No Source"

@app.route('/first_c/', methods=['GET','POST'])
def first_c():
    source= request.form.get("source")

    if(source):
        data = {
        'client_secret': CLIENT_SECRET,
        'async': 0,
        'source': source,
        'lang': "CPP",
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
    else:
        return "No Source"

@app.route('/second_c/', methods=['GET','POST'])
def second_c():
    source= request.form.get("source")

    if(source):
        data = {
        'client_secret': CLIENT_SECRET,
        'async': 0,
        'source': source,
        'lang': "CPP",
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
    else:
        return "No Source"



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
