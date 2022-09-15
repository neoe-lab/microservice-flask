from flask import Flask
import requests
app = Flask(__name__)

@app.route('/server1/gettasks',methods=["GET"])
def gettasks1():
    url = 'http://192.168.45.198:6009/todo/api/v1.0/tasks'
    response = requests.request('GET',url)
    return response.json()
@app.route('/server2/gettasks',methods=["GET"])
def gettasks2():
    url = 'http://127.0.0.1:6010/todo/api/v1.0/tasks'
    response = requests.request('GET',url)
    return response.json()


if __name__=='__main__':
    app.run(debug=True,port=5001)
