#rest APIs
#Request Method:
    #Get  ->Endpoint: http://127.0.0.1:5000/api/V1/getResult

from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api/V1/getResult')

def getResult():
    try:
        f = open("result.txt.json", "r")
        data = json.loads(f.read())
        f.close()

        return jsonify(data)
    except Exception as err:
        return jsonify({'Error Message':'Error happened'}), 500

if __name__== "__main__":
    app.run()
    