from flask_sqlalchemy import SQLAlchemy
from flask import Flask


db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:as4657669874@127.0.0.1:3306/testdb"

db.init_app(app)

@app.route('/')
def index():

    sql_cmd = """
      insert into school(id,name,x,y) values('3','c','21','34')
        """

    query_data = db.engine.execute(sql_cmd)
    print(query_data)
    return 'ok'
    
if __name__ == "__main__":
	app.run(host="0.0.0.0",port=5000,debug=True)
