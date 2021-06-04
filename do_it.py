from flask import Flask, render_template, request ,Response,jsonify
from flask_sqlalchemy import SQLAlchemy
import json
""" Spot: 文化場館M 自然景觀N 宮廟T 老街、夜市X
    Restaurant: 小點D 中式C 日式J 西式W 泰式T 港式H 韓式K
    Hotel:民宿A 汽車旅館B 旅社C 背包客棧D 飯店/旅店E"""
app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:as4657669874@127.0.0.1:3306/testdb"
db.init_app(app)
zone=""
place=""
@app.route("/")
def test():
    return render_template('Home.html')
@app.route("/search")
def search():
    select="select Name, Description, Address "
    frm="from"
    where="where"
    query=" "
    if zone == 'N' : where = where + " "+"'zone'=='N'" + ","
    elif zone == 'S' : where = where + " " + "'zone'=='S'" + ","
    elif zone == 'W' : where = where + " " + "'zone'=='W'" + ","
    elif zone == 'E' : where = where + " " + "'zone'=='E'" + ","
    
 
    if place[0] == "S" : 
        frm = frm + " " + "spot "
        if place[1] == "M" : 
            where = where + " "+"'type'=='文化場館'" +","
        elif place[1] == "N" : 
            where = where + " "+"'type'=='自然景觀'" +","
        elif place[1] == "T" : 
            where = where + " "+"'type'=='宮廟'" +","
        elif place[1] == "X" : 
            where = where + " "+"'type'=='老街、夜市'" +","
    elif place[0] == "R" : 
        frm = frm + " "+"restaurant "
        if place[1] == "D" :  
            where = where + " "+"'type'=='小點'" +","
        elif place[1] == "C" : 
            where = where + " "+"'type'=='中式'" +","
        elif place[1] == "J" : 
            where = where + " "+"'type'=='日式'" +","
        elif place[1] == "W" : 
            where = where + " "+"'type'=='西式'" +","
        elif place[1] == "T" : 
            where = where + " "+"'type'=='泰式'" +","
        elif place[1] == "H" : 
            where = where + " "+"'type'=='港式'" +","
        elif place[1] == "K" : 
            where = where + " "+"'type'=='韓式'" +","
    else : 
        frm = frm + " "+"hotel "
        if place[1] == "A" : 
            where = where + " "+"'type'=='民宿'" +","
        elif place[1] == "B" : 
            where = where + " "+"'type'=='汽車旅館'" +","
        elif place[1] == "C" : 
            where = where + " "+"'type'=='旅社'" +","
        elif place[1] == "D" : 
            where = where + " "+"'type'=='背包客棧'" +","
        elif place[1] == "E" : 
            where = where + " "+"'type'=='飯店/旅店'" +","
    query = select + frm + where
    query=query[:-1]
    sql_cmd =query
    query_data = db.engine.execute(sql_cmd)
    print(query_data.fetchall())
    return render_template('Home.html')
@app.route("/name", methods=['POST'])
def index_name():
    t = {
        'a': 1,
        'b': 2,
        'c': [3, 4, 5]
    }
    print(t)
    return Response(json.dumps(t),mimetype='application/json')
if __name__ == "__main__":
	app.run(host="0.0.0.0",port=5000,debug=True)