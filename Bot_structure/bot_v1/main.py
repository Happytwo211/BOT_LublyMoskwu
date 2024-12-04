import json

import telebot
from telebot import types
from Sistem_files import token, admin_list
import requests
from bs4 import BeautifulSoup



bot = telebot.TeleBot(token.TOKEN)
admin_id = admin_list.admin_id




inline_kb_st = types.InlineKeyboardMarkup(row_width=2)
inline_bt_1 = types.InlineKeyboardButton('Запустить "ЛюМ"', 'https://www.wikipedia.org')
inline_bt_2 = types.InlineKeyboardButton('Московская Афиша', 'https://www.afisha.ru')
inline_bt_3 = types.InlineKeyboardButton('Наша Афиша (прямо в боте)', callback_data='check_lum_afisha')
inline_bt_4 = types.InlineKeyboardButton(text="О нас!", callback_data='about_us')
inline_bt_5 = types.InlineKeyboardButton('Наша Афиша', 'https://t.me/+O9krp9Je02RjNWEy')

inline_kb_st.add(inline_bt_1).add(inline_bt_2).add(inline_bt_5).add(inline_bt_4).add(inline_bt_3)

keyboard_start = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2,
                                               input_field_placeholder='"ЛюМ"- Люблю Москву!',
                                                   one_time_keyboard=True)

button1 = types.KeyboardButton('Домашняя страница')
button2 = types.KeyboardButton('Кнопка 2')
button3 = types.KeyboardButton('Кнопка 3')

keyboard_start.add(button1, button2, button3)  # Кнопки по вертикали




# keyboard.add(button1).add(button2).add(button3) #.add(button4).add(button5) #Кнопки по шиирине


class CommandStart:


    @bot.message_handler(commands=['start'])
    def handle_start(message):
        bot.send_photo(message.chat.id, 'https://imgur.com/a/O1lm2hZ',
                       f'Добро пожаловать, {message.chat.username}!'
                       f'\n'
                       f'\nЭто телеграм-бот от проекта «ЛюМ» - Люблю Москву!'
                       f'\n'
                       f'\n В меню ниже вы сможете найти:'
                       f'\n -актуальную афишу событый в Москве'
                       f'\n -авторские маршруты прогулок'
                       f'\n -тематические квизы'
                       , reply_markup=inline_kb_st)


        bot.send_message(message.chat.id, f'Или нажми на кнопку', reply_markup=keyboard_start, disable_notification=True)



class AdmPanel:
    @bot.message_handler(commands=['adm'])
    def amd_panel(message):
        if message.from_user.id in admin_id:
            amd_kb = types.InlineKeyboardMarkup(row_width=2)
            amd_b1 = types.InlineKeyboardButton('Админская функция 1', callback_data='adm1')
            amd_b2 = types.InlineKeyboardButton('Админская функция 2', callback_data='amd2')
            amd_b3 = types.InlineKeyboardButton('Админская функция 3', callback_data='adm3')
            amd_kb.add(amd_b1).add(amd_b2).add(amd_b3)
            bot.send_message(message.chat.id, f'Вы вошли в админскую панель', reply_markup=amd_kb)

        else:
            bot.send_message(message.chat.id, f'У вас нет доступа к админ-панели')



class CallBackData:


    @bot.callback_query_handler(func=lambda call: call.data == 'about_us')
    def start_lum(call):

        inline_kb_link = types.InlineKeyboardMarkup()
        inline_link = types.InlineKeyboardButton('t.me/lum_moscow'
                                                 , 'https://t.me/lum_moscow')
        inline_kb_link.add(inline_link)

        message = call.message
        bot.send_message(message.chat.id, f'ЛюМ - развлекательный проект, который создает авторские тематические аудиоэкскурсии по Москве.'
                                          f'\n'
                                          f'\nМы предлагаем по новому взглянуть на концепцию экскурсий и показать Москву с разных сторон - спорт, искусство, история, личности, события и многие другие.'
                                          f'\n'
                                          f'\nЕсли вы любите Москву так же, как и мы, или хотите познакомиться со столицей поближе то присоединяйтесь к нам!'
                                          f'\n'
                                          f'\nАктуальные новости о развитии проекта'
                                          f'\n'
                                          f'                                                  👇👇👇' ,
                         reply_markup=inline_kb_link)


        # bot.send_message(message.chat.id, f'Наша комманда:' ,reply_markup=inline_social_media_kb)

    # inline_bt_3 = types.InlineKeyboardButton('Cтать частичкой ЛЮМ', 'https://t.me/lum_moscow')
    @bot.callback_query_handler(func=lambda call: call.data == 'adm1')
    def hanlde_adm1(call):
        message = call.message
        bot.send_message(message.chat.id, f'Админская фукция 1')

    @bot.callback_query_handler(func=lambda call: call.data == 'amd2')
    def hanlde_adm1(call):
        message = call.message
        bot.send_message(message.chat.id, f'Админская фукция 2')

    @bot.callback_query_handler(func=lambda call: call.data == 'adm3')
    def hanlde_adm1(call):
        message = call.message
        bot.send_message(message.chat.id, f'Админская фукция 3')

    @bot.callback_query_handler(func=lambda call: call.data == 'check_lum_afisha')
    def call_back_data_afisha(call):
        message = call.message
        r = requests.get('http://127.0.0.1:8000/afisha_bot/')
        print(r.text)
        soup = BeautifulSoup(r.text, 'html.parser')
        bot.send_message(message.chat.id, f'Афиша экскурсий на сегодня: \n{soup.p.string}')

        # a = requests.get('http://127.0.0.1:8000/route')
        # print(a.text)
        # soup = BeautifulSoup(r.text, 'html.parser')





class NotHandle:

    @bot.message_handler(content_types=['video', 'audio', 'sticker', 'photo', 'document', 'contact', 'emoji'])
    def handle_content_types(message):
        bot.send_message(message.chat.id, f'Бот такое не понимает'

                         f'\nВот список доступных комманд:', reply_markup=inline_kb_st)


class ReplyButtons:

    @bot.message_handler(func=lambda message: True)
    def handle_message(message):

        if message.text == 'Домашняя страница':
            # bot.send_message(message.chat.id,f'Вы перешли на домашнюю страницу',  reply_markup=inline_kb_st)
            CommandStart.handle_start(message)

        elif message.text == 'Кнопка 2':
            bot.send_message(message.chat.id, f'Вы нажали кнопку 2', reply_markup=inline_kb_st)

        elif message.text == 'Кнопка 3':
            bot.send_message(message.chat.id, f'Вы нажали кнопку 3', reply_markup=inline_kb_st)


        else:
            bot.send_message(message.chat.id, f'Такой комманды нет'
                                              f'\nСписок доступных комманд',
                             reply_markup=inline_kb_st)





bot.infinity_polling()

