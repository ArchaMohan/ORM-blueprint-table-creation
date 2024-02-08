# from flask import Flask
# from flask_restful import Resource, Api

# app = Flask(__name__)
# api = Api(app)

# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}
    
#     def post(self):
#         return {'Post': 'hello'}
    

# api.add_resource(HelloWorld, '/')

# if __name__ == '__main__':
#     app.run(debug=True)


##################################################Splitting the similar ones to different py files

# from flask_restful import Resource



# class HelloWorld(Resource):
#     def get(self):
#         return {'GET hello': 'world'}
    
#     def post(self):
#         return {'Post': 'hello'}
    

################################################
    
    
from flask_restful import Resource



class HelloWorld(Resource):
    def get(self):
        return {'GET hello': 'world'}
    
    def post(self):
        return {'Post': 'hello'}
    
class GetMessage_by_id(Resource):
    def get(self,id):
        return {'GET hello': 'world'}
    
    
    




