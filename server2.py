from flask import Flask,jsonify
app = Flask(__name__)

tasks = [
        {
            'id':1,
            'item':u'notebook'
        },
        {
            'id':2,
            'item': u'pencil'
        }
        ]
@app.route('/todo/api/v1.0/tasks',methods=['GET'])
def get_tasks():
    return jsonify({'tasks':tasks})
if __name__ == '__main__':
    app.run(debug=True,port=6010)