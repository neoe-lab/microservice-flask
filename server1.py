from flask import Flask,jsonify
app = Flask(__name__)

tasks = [
        {
            'id':1,
            'name':u'john tennih'
        },
        {
            'id':2,
            'name': u'bob ui'
        }
        ]
@app.route('/todo/api/v1.0/tasks',methods=['GET'])
def get_tasks():
    return jsonify({'tasks':tasks})
if __name__ == '__main__':
    app.run(debug=True,port=6009)
