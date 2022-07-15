#rest APIs
#Request Method:
    #Get  ->Endpoint: www.godev.today/api.v1/testAPI , It returns message 'Simple APi Test: This app is working'
    #GET  ->Endpoint: www.godev.today/api/v1/student , It returns list of all the srudents(JSON)
    #POST
    #PATCH
    #Delete

# localhost = 127.0.0.
# Port number = 5000, -> different ports for different environments

import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/V1/testAPI')
def simpleAPITest():
    try:
        #introduce error just for test
        #raise TypeError('Invalid HTTP Request')
        return jsonify({'message': 'Simple API Test: This app is working'})
    except:
        return jsonify({'Error Message':'Error happened'}), 500

#Main driver

if __name__=='__main__':
    app.run()