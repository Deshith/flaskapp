from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
from classes.User import User

app = Flask(__name__)
CORS(app)
Rapi = Api(app)

@app.route('/', methods=['GET'])
def health():
        # app.logger.info('Welcome to Flask APP') 
        return { "msg": "'Flask Server - version 1.0.0" }, 200


api_version = '/v1'
Rapi.add_resource(User , api_version + '/user/<string:email>', endpoint="get_user", methods=['GET'])
# Rapi.add_resource(User , api_version + '/user', endpoint="get_user", methods=['GET'])
Rapi.add_resource(User , api_version + '/user/create', endpoint="create_user", methods=['POST'])