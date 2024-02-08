from flask_restful import Resource
from app.user.user_tables import User




class GetUsers(Resource):
    def get(self):
        user =User.query.all()
        if user:
            return{ 'username':user.username,'email':user.email}
        else:
             return{ 'message':'user not found'},404
    

