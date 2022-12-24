import telebot

bot = telebot.TeleBot('5750263198:AAFdMsGtNUKcXVcNKmqoCMXmONEaNQtbhqM')

#Начало цепочки сообщений. Бот реагирует на начальное сообщение-команду Start и начинает дальнейшиую цепочку
@bot.message_handler(commands=['start'])
def start(message):
    photo = open('71Bp979TqaL._SL1500_.jpg', 'rb') #Функция вызывает фото, ранее добавленное в список файлов
    bot.send_message(message.chat.id, 'Доброго времени суток! Приветствую тебя в нашем предновогоднем магазине! Здесь ты можешь заказать подарок себе и своим близким. Если хочешь больше узнать о наших брелках, напиши "Брелки". Если уже уверен, что хочешь перейти к оплате, нажми "Купить". Если есть вопросы, напиши слово "Вопросы"')
    bot.send_photo(message.chat.id, photo)

#Заранее отмечаем переменные для оформления заказа
amount = '';
name = '';
surname = '';
phone = '';
address = '';

@bot.message_handler(content_types=['text'])
def message1 (message):
    if message.text == 'Брелки':
        bot.send_message(message.chat.id, 'Отлично! Рад, что ты поинтересовался! Мы делаем наши брелки из гипоалергенного пластика и монтируем внутрь настоящую фотопленку, на которую наносим до десяти твоих фотографий. После мы любезно запакуем твой подарок в подарочную упаковку и доставим прямо до твоего дома. Уже готов перейти к оплате? Если да, скорее отправляй в чат слово "Купить". Или же напиши "Ещё, если хочешь узнать больше про наше изделия')
    elif message.text == 'Ещё':
        bot.send_message(message.chat.id, 'Ух ты! А ты любопытный! Что ж, держи еще немного фактов: Мы производим наши брелки на заводах Германии и переправляем их уже готовые в Россию. Наши краски производят только проверенные поставщики, а фотографии печатаются на новейших принтерах. На каждом этапе сборки мы будем присылать вам фото вашего брелка. Ну что, заинтересовали?) Тогда скорее вводи "Купить" и переходи к оформлению заказа!')
    elif message.text == 'Доставка':
        #Далее идут вопросы из блока с вопросами
        #---------------------------------------
        bot.send_message(message.chat.id, 'Мы осуществляем доставку по всей России через СДЭК и Почтой России. В среднем доставка занимает три дня')
        bot.send_message(message.chat.id, 'Ввведите название вопроса из списка: "Сроки", "Фотографии", "Оплата", "Отзывы" и если вашего вопроса в списке нет, введите "Менеджер". Если хотите перейти к оплате, введите "Купить"')
    elif message.text =='Сроки':
        bot.send_message(message.chat.id, 'Мы делаем брелок в течение двух дней, в редких случаях в течение трех. Сразу после этого мы отправляем его вам на адрес')
        bot.send_message(message.chat.id, 'Ввведите название вопроса из списка: "Доставка", "Фотографии", "Оплата", "Отзывы" и если вашего вопроса в списке нет, введите "Менеджер". Если хотите перейти к оплате, введите "Купить"')
    elif message.text =='Фотографии':
        bot.send_message(message.chat.id, 'Нам нужны ваши фотографии любого формата, но строго до десяти штук. После мы напечатаем их на пленке и отправим вам')
        bot.send_message(message.chat.id, 'Ввведите название вопроса из списка: "Доставка", "Сроки", "Оплата", "Отзывы" и если вашего вопроса в списке нет, введите "Менеджер". Если хотите перейти к оплате, введите "Купить"')
    elif message.text =='Оплата':
        bot.send_message(message.chat.id, 'Оплата производится через Яндекс кассу. Мы скинем форму вам в чат и, когда оплата пройдет, мы будем собирать ваш брелок')
        bot.send_message(message.chat.id, 'Ввведите название вопроса из списка: "Доставка", "Сроки", "Фотографии", "Отзывы" и если вашего вопроса в списке нет, введите "Менеджер". Если хотите перейти к оплате, введите "Купить"')
    elif message.text == 'Отзывы':
        bot.send_message(message.chat.id, 'Все отзывы о нашем товаре вы можете найти в нашем ВК, мы регулярно публикуем их на стене!')
        bot.send_message(message.chat.id, 'Ввведите название вопроса из списка: "Доставка", "Сроки", "Фотографии", "Оплата" и если вашего вопроса в списке нет, введите "Менеджер". Если хотите перейти к оплате, введите "Купить"')
    elif messege.text == 'Менеджер':
        bot.send_message(message.chat.id, 'Все вопросы, которые вы не можете найти среди этого списка кидайте на почту BrelokChristmas@hse.ru. Мы вам ответим в ближайшее время')
        bot.send_message(message.chat.id, 'Ввведите название вопроса из списка: "Доставка", "Сроки", "Фотографии", "Оплата", "Отзывы". Если хотите перейти к оплате, введите "Купить"')
         # ---------------------------------------
    elif message.text == 'Вопросы':
        bot.send_message(message.chat.id, 'Пожалуйста, введите название вопроса из списка: "Доставка", "Сроки", "Фотографии", "Оплата", "Отзывы" и если вашего вопроса в списке нет, введите "Менеджер"')
    elif message.text == 'Купить':
        bot.send_message(message.chat.id, 'Отлично! Ты на верном пути, уже могу поздравить тебя с грядущим подарком! Осталось совсем чуть-чуть и этот красавец станет твоим)')
        photo2 = open('H14e913bd863f41c3886e8846065b92aa5.jpg', 'rb')
        bot.send_photo(message.chat.id, photo2)
        bot.send_message(message.chat.id, 'Отпавляй в чат слово "Дальше" и мы перейдем к оформлению твоего заказа!');
        bot.register_message_handler(message, get_name); #Создаем переход по цепочке к следующему шагу, где будем брать имя
    else:
        bot.send_message(message.chat.id, 'Извините, я вас не понимаю. Бот может отвечать только на предложенные варианты ответов')

def get_name(message):
    bot.send_message(message.chat.id, 'Отлично! Пожалуйста, введи количество брелком, сколько хочешь заказать');
    sbot.register_message_handler(message.chat.id, get_amount) #Переход к блоку с записью кол-ва брелков и сбором контактных данных

def get_amount(message):
   global amount;
   amount = message.text;
   bot.send_message(message.chat.id, 'Отлично, записал! Теперь напиши, пожалуйста, свое имя');
   bot.register_message_handler(message, get_name);

def get_name(message):
    global name;
    name = message.text;
    bot.send_message(message.chat.id, 'Отлично, записал! Теперь напиши, пожалуйста, свою фамилию');
    bot.register_message_handler(message,get_surname);

def get_surname(message):
    global surname;
    surname = message.text;
    mess = f'Супер, <b>{name} {surname}</b>, это тоже записал! Теперь пожалуйста, ввеи свой номер телефона'
    bot.send_message(message.chat.id, mess);
    bot.register_message_handler(message, get_phone);

def get_phone(message):
    global phone;
    phone = message.text;
    bot.send_message(message.chat.id, 'Супер! Уже почти все! Осталось лишь написать адресс доставки');
    bot.register_message_handler(message,get_address);

def get_address(message):
    global address;

#Ждем подтверждения заказа
    keyboard = types.InlineKeyboardMarkup();  # наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes');  # кнопка «Да»
    keyboard.add(key_yes);  # добавляем кнопку в клавиатуру
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no');
    keyboard.add(key_no);
    question = 'Ваши данные: вас зовут ' + name + ' ' + surname + ', Ваш контактный номер телефона: ' + phone + ', адрес доставки:' + address + ' И вы заказали у нас' + amount + 'брелков, верно?';
    bot.send_message(message.chat.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(message.chat.id, 'Великолепно! Скоро твой заказ будет собран и доставлен. Ждем твои фотографии и мы приступим к сборке. Помни, не более десяти штук на один брелок) : )');
    elif call.data == "no":
        bot.send_message(message.chat.id, 'В таком случае, тебе требуется снова пройти процедуру оформления заказа. Для этого введи в чат "Купить"')

bot.polling(none_stop=True)