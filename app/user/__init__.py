from flask import Blueprint
from flask_restful import Api
from app.user.user_logic import GetUsers


user_bp =Blueprint('user_bp',__name__)
api=Api(user_bp)

api.add_resource(GetUsers,'/user')
