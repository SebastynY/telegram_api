import telebot

from models.user import User

TOKEN = "5378299384:AAEnU0jD3ml6ZxntdNb69b5omRR1uaKLDN4"
bot = telebot.TeleBot(TOKEN)
user_id = 2082769354


def send_message(user: User) -> None:
    text = f"Успешная регистрация! \nВаши данные:\n Имя - {user.first_name}, " \
           f"\n Фамилия - {user.first_name}" \
           f"\n Возраст - {user.age}"
    bot.send_message(user_id, text)
