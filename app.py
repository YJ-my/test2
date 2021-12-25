from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.mini

@app.route('/')
def home():
   return render_template('visitor.html')

#방명록 저장
@app.route('/visitor_post', methods=['POST'])
def test_post():
   visitor_receive = request.form['visitor_give']
   print(visitor_receive)
   return jsonify({'msg': '이 요청은 POST!'})

#방명록 보여주기
@app.route('/visitor_post', methods=['GET'])
def test_get():
   visitor_receive = request.args.get('visitor_give')
   print(visitor_receive)
   return jsonify({'msg': '이 요청은 GET!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)