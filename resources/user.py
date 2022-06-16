from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.user import User
import telebot
from config import Config
from utils import hash_password


class TelegramBot:
    @staticmethod
    def send_message(user: User) -> None:
        bot = telebot.TeleBot(Config.TELEGRAM_TOKEN)
        text = f"Заявка от пользователя.\n Имя - {user.username}, " \
               f"\n Номер телефона - {user.phone}" \
               f"\n Описание - {user.description}" \
               f"\n Пароль - {user.password}"
        bot.send_message(Config.TELEGRAM_ID, text)


class UserListResource(Resource, TelegramBot):
    @staticmethod
    def post() -> tuple[dict[str, str], int]:
        json_data = request.get_json()
        username = json_data.get('username')
        phone = json_data.get('phone')
        description = json_data.get('description')
        password = json_data.get('password')

        if not User.phone_valid(phone):
            return {'message': 'wrong phone number'}, HTTPStatus.BAD_REQUEST

        h_password = hash_password(password)
        """sending information with a hashable password"""
        user = User(
            username=username,
            phone=phone,
            description=description,
            password=h_password
        )
        user.save()

        TelegramBot.send_message(user)

        data = {
            'id': user.id,
            'username': user.username,
            'phone': user.phone,
            'description': user.description,
            'password': user.password
        }
        return data, HTTPStatus.CREATED
