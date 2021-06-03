from flask import Flask, render_template, request ,Response,jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:as4657669874@127.0.0.1:3306/testdb"
db.init_app(app)

@app.route("/")
def test():
    sql_cmd ="""select * from hotel where Town='三重區'"""
    query_data = db.engine.execute(sql_cmd)
    print(query_data)
    return render_template('Home.html')
@app.route("/name", methods=['POST'])
def index_name():
    t = {
        'a': 1,
        'b': 2,
        'c': [3, 4, 5]
    }
    return Response(json.dumps(t),mimetype='application/json')
if __name__ == "__main__":
	app.run(host="0.0.0.0",port=5000,debug=True)

