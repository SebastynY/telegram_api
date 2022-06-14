from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.user import User
from telegram import send_message


class UserListResource(Resource):
    @staticmethod
    def post() -> tuple[dict[str, str], int]:
        json_data = request.get_json()
        first_name = json_data.get('first_name')
        last_name = json_data.get('last_name')
        telegram = json_data.get('telegram')
        age = json_data.get('age')

        if User.get_by_telegram(telegram):
            return {'message': 'telegram already used'}, HTTPStatus.BAD_REQUEST

        user = User(
            first_name=first_name,
            last_name=last_name,
            telegram=telegram,
            age=age
        )
        user.save()
        data = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'telegram': user.telegram,
            'age': user.age
        }
        send_message(user)
        return data, HTTPStatus.CREATED
