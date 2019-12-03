import telebot
import config
import pytb
import datetime
import json
import traceback
<<<<<<< HEAD

bot = telebot.TeleBot(config.TOKEN)

=======



bot = telebot.TeleBot(config.TOKEN)
>>>>>>> ec9b105c369b9a641514b98da24f572266cd3846

@bot.message_handler(commands=['start'])  
def start_command(message):  
    bot.send_message(  
        message.chat.id,  
        'Greetings! I can show you exchange rates.\n' +  
        'To get the exchange rates press /exchange.\n' +  
        'To get help press /help.'  
  )

@bot.message_handler(commands=['help'])  
def help_command(message):  
    keyboard = telebot.types.InlineKeyboardMarkup()  
    keyboard.add(  
        telebot.types.InlineKeyboardButton(  
            'Message the developer', url='telegram.me/BlackStarJaxx'  
  )  
    )  
    bot.send_message(  
        message.chat.id,  
        '1) To receive a list of available currencies press /exchange.\n' +  
        '2) Click on the currency you are interested in.\n' +  
        '3) You will receive a message containing information regarding the source and the target currencies, ' +  
        'buying rates and selling rates.\n' +  
        '4) Click “Update” to receive the current information regarding the request. ' +  
        'The bot will also show the difference between the previous and the current exchange rates.\n' +  
        '5) The bot supports inline. Type @<botusername> in any chat and the first letters of a currency.',  
        reply_markup=keyboard  
    )

@bot.callback_query_handler(func=lambda call: True)  
def iq_callback(query):  
    data = query.data  
    if data.startswith('get-'):  
        get_ex_callback(query)

def get_ex_callback(query):  
    bot.answer_callback_query(query.id)  
    #send_exchange_result(query.message, query.data[4:])

<<<<<<< HEAD
def send_exchange_result(message, ex_code):  
    bot.send_chat_action(message.chat.id, 'typing')  
    ex = pytb.get_exchange(ex_code)  
    bot.send_message(  
        message.chat.id, serialize_ex(ex),  
        reply_markup=get_update_keyboard(ex),  
	parse_mode='HTML'  
    )
=======
# def send_exchange_result(message, ex_code):
#     bot.send_chat_action(message.chat.id, 'typing')
#     ex = pytb.get_exchange(ex_code)
#     bot.send_message(
#         message.chat.id, serialize_ex(ex),
#         reply_markup=get_update_keyboard(ex),
# 	parse_mode='HTML'
#     )
>>>>>>> ec9b105c369b9a641514b98da24f572266cd3846
def get_update_keyboard(ex):  
    keyboard = telebot.types.InlineKeyboardMarkup()  
    keyboard.row(  
        telebot.types.InlineKeyboardButton(  
            'Update',  
	    callback_data=json.dumps({
            't': 'u',
            'e': {
                'b': ex['buy'],
		        's': ex['sale'],
		        'c': ex['ccy']
            }
            }).replace(' ', '')  
        ),  
	telebot.types.InlineKeyboardButton('Share', switch_inline_query=ex['ccy'])  
    )  
    return keyboard
    

if __name__ == "__main__":
    bot.polling(none_stop=True)


