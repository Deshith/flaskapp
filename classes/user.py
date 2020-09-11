from flask_restful import Resource, request, reqparse
from flask_cors import cross_origin
import json, logging, os

class User(Resource):
    user_args = ["name", "email", "password"]
    args = ["email", "uuid"]
    del_args = ["user_name", "host", "uuid"]

    @cross_origin(origin="*")
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument(self.user_args[0], required=True, location='json', help="name cannot be blank!")
            parser.add_argument(self.user_args[1], required=True, location='json', help="email cannot be blank!")
            parser.add_argument(self.user_args[2], required=True, location='json', help="password cannot be blank!")
            parser.parse_args()
            data = request.get_json()

            current_file =  os.path.dirname(os.path.abspath(__file__)) 
            root_folder =  os.path.normpath(current_file + os.sep + os.pardir)
            file_path = root_folder + '/data/user.json'
            file_data = []

            # read data from file
            with open(file_path) as f:
                file_data = json.load(f)
                print(file_data)

            file_data.append(data)

            # write data to file
            with open(file_path, 'w') as json_file:
                json.dump(file_data, json_file)

        
            return { "msg": "User has successfully created!"  }, 200
        except Exception as e:
            logging.error(str(e))
            return { 'msg': 'User creation failed' }, 500
    
    @cross_origin(origin="*")
    def get(self, **kwargs):
        parser = reqparse.RequestParser()
        # parser.add_argument(self.args[0], required=True, location='values', help="user cannot be blank!")
        parser.parse_args() # validating

        # email = request.args.get(self.args[0])

        email = kwargs['email']
        current_folder =  os.path.dirname(os.path.abspath(__file__)) 
        root_folder =  os.path.normpath(current_folder + os.sep + os.pardir)
        file_path = root_folder + '/data/user.json'
        
        try:
            file_data = []
            # read data from file
            with open(file_path) as f:
                file_data = json.load(f)
                print(file_data)
        
            user_object = {}
            for row in file_data:
                if row['email'] == email:
                    user_object = row
            return { "data": user_object   }, 200
        except Exception as e:
            logging.error(str(e))
            return { 'msg': 'operation failed' }, 500