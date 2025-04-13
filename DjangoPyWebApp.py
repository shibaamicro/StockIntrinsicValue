from flask import Flask,request,jsonify
import pyodbc

app = Flask(__name__)

@app.route('/valuate',methods=['GET'])

def valuate():
    ticker = request.args.get('ticker')

    conn = pyodbc.connect(os.environ["SQL_CONNECTION_STRING"])
    cursor = conn.cursor()
    cursor.execute("SELECT IntrinsicValue FROM ValuationResults WHERE Ticker = ?",ticker)

    result = cursor.fetchone()

    return jsonify({"intrinsic_value":result[0]})