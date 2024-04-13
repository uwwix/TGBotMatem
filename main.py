import telebot
from telebot import types

token='7161511597:AAEYvP6tscTiteMCYUpBFi3wX9u_MSLKb_c'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Задания")
    btn2 = types.KeyboardButton("Ответы")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! \
                      Я бот для подготовки к ЕГЭ. \
                     Нажимай кнопку Задания выбирай задание, \
                     решай, а затем проверяй его в ответах, которые можно найти по кнопке \
                     Ответы в главном меню".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Ответы"):
        bot.send_message(message.chat.id, text="1) 138   \n2) 33   \n3) 0,275   \n4) 0,5   \n5) 0,2   \n6) 8   \n7) 75")
    elif(message.text == "Задания"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("Задание 1")
        btn4 = types.KeyboardButton("Задание 2")
        btn5 = types.KeyboardButton("Задание 3")
        btn6 = types.KeyboardButton("Задание 4")
        btn7 = types.KeyboardButton("Задание 5")
        btn8 = types.KeyboardButton("Задание 6")
        btn9 = types.KeyboardButton("Задание 7")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn3, btn4, btn5, btn6, btn7, btn8, btn9, back)
        bot.send_message(message.chat.id, text="Выбери задание", reply_markup=markup)
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Задания")
        button2 = types.KeyboardButton("Ответы")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif (message.text == "Задание 1"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Два угла треугольника равны 33° и 105°.Найдите тупой угол, который образуют высоты треугольника, выходящие из вершин этих углов. Ответ дайте в градусах.", reply_markup=markup)

    elif (message.text == "Задание 2"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Объем правильной четырехугольной пирамиды SABCD равен 132.Точка E  — середина ребра SB. Найдите объем треугольной пирамиды EABC.", reply_markup=markup)

    elif (message.text == "Задание 3"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Конкурс исполнителей проводится в 4 дня. Всего заявлено 80 выступлений  — по одному от каждой страны, участвующей в конкурсе. Исполнитель из России участвует в конкурсе. В первый день 14 выступлений, остальные распределены поровну между оставшимися днями. Порядок выступлений определяется жеребьёвкой. Какова вероятность, что выступление представителя России состоится в третий день конкурса?", reply_markup=markup)

    elif (message.text == "Задание 4"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="При двукратном бросании игральной кости в сумме выпало 5 очков. Какова вероятность того, что хотя бы раз выпало 1 очко?", reply_markup=markup)

    elif (message.text == "Задание 5"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Найдите корень уравнения 1/(9x+5)=1/(4x+6)", reply_markup=markup)


    elif (message.text == "Задание 6"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Найдите значение выражения  (2a)^3/(a^5*a^2)", reply_markup=markup)

    elif (message.text == "Задание 7"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="Первую треть трассы автомобиль ехал со скоростью 100 км/ч, вторую треть  — со скоростью 75 км/ч, а последнюю  — со скоростью 60 км/ч. Найдите среднюю скорость автомобиля на протяжении всего пути. Ответ дайте в км/ч.", reply_markup=markup)


    else:
        bot.send_message(message.chat.id, text="Такое я к сожалению на данный момент не умею(...")

bot.polling(none_stop=True)