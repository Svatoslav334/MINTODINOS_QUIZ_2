#6541829338:AAHftopC_mKOU3xFCHnlxAN24I789hoXobY
#1281869576
#https://lh3.googleusercontent.com/pw/AIL4fc8CzEhBu0EszdwUM-5CltbbRphdhFg9Dvre5PKo8R-3uZs6kUY7Wfy9iL2h8Oe8SARMavOkVNBQ2-H6C2zpTKCBPYCIOXahAdYXSOuNKUPE8Hyb3agxK9NYRsOS1nSvlRq4MvIPyw4IDXAjB99bsWiBARe5Mhq2-Mc19Mw0qqqgr1cKvwaQFWSf1oZReCBl6Wgeb6NC-L_OZb9_GYAJJjN1x-4feCAOzM73_AmDVyVkrdryxOy4kSl0YxHqxASZUEqhx5B-VXUGMhfhNCVjPnXSsYTsY50RvTyyHQcsgdI2uAiAajNzeqX7CSp7LcUEPJX6m3dhbF-J5dMeylcy_gSA1q6IwWiZHII8Zf-tiAL2hlaYm9_UqN0UR8r65YUC-EVu3ZjjYkTKEfKUrxHuYAMq_GC3APs9a5mRkOU0Jw2zmddRa39b3N5pD2ytjjLHr5DIkAjSe4hJSbG_2Steo-SZoK0-qtbab13zJiIgoaYV8AeNANCmnq_L0Q4sNQTHb3YjrqZ4pHa5OxZ6QGumOYuihmXHaD_F8pAJ9Y0M9uOsJyFERU2D19m8YgRJKMEnn7iKYdTVg51o6LIhpXq4DvlH-e37wXqb2iKl7D7cRhRX7m54nM4-Z0Lw8Qqck9Dr-DVGHFi3T3GUOW-Y6Mi_4QOOFJEPgZP7EsV3qM491MnFJHNTY73V3NGKRFFU61k6xI_sdbVtahy3u0PrO_vaEf-QPzq_rn-zE0vlWpbeuB1AAaTaYZGHf1S5DJ7TpuEf_EeMWQYWAlx7-P3_ng0Mb80m3IT3tybCfC6RccriyB0oWb-Y5--g6JRAlXAd8FYNWMFWaOlJOZiEH7JTVmpc0_ICKmVOpnPOyxQvchuVn59q7oJoYasN4NnV1VJdTH-uCRM2Kx4FWgF6G3o8NuV7MQ=w1080-h1080-s-no?authuser=0
import logging
import asyncio
from aiogram import Bot, Dispatcher, types, executor

# Устанавливаем уровень логирования
logging.basicConfig(level=logging.INFO)

# Создаем экземпляр бота
bot = Bot(token="6029099768:AAFseZUTFPOHo")
dispatcher = Dispatcher(bot)

good = 0
user_info = None
q = {}
prev_question_message_id = None

questions = [
    {"question": "Какой из этих динозавров был растительноядным? 🌿", "answers": ["a) Тираннозавр Рекс", "b) Велоцираптор", "c) Трицератопс", "d) Спинозавр"], "correct": "c) Трицератопс"},
    {"question": "Как называется динозавр с длинным выдвижным шеейподобным отростком на голове? 🦕", "answers": ["a) Парацератозавр", "b) Стегозавр", "c) Велоцираптор", "d) Апатозавр"], "correct": "a) Парацератозавр"},
    {"question": "Какая из этих частей тела у тираннозавра Рекса была маленькой и непропорциональной? 😅", "answers": ["a) Голова", "b) Шея", "c) Руки", "d) Ноги"], "correct": "d) Ноги"},
    {"question": "Какой динозавр считается самым крупным из всех земных обитателей? 🌎", "answers": ["a) Брахиозавр", "b) Аргентинозавр", "c) Спинозавр", "d) Велоцираптор"], "correct": "b) Аргентинозавр"},
    {"question": "Какой динозавр был первым обнаруженным учеными в Северной Америке? 🦖", "answers": ["a) Тираннозавр Рекс", "b) Стегозавр", "c) Трицератопс", "d) Апатозавр"], "correct": "c) Трицератопс"},
    {"question": "Какое растение считается основным кормом большинства травоядных динозавров? 🌿", "answers": ["a) Папоротник", "b) Цветок", "c) Кустарник", "d) Хвоя"], "correct": "a) Папоротник"},
    {"question": "Какая группа динозавров включала множество хищников? 🦖", "answers": ["a) Завроподы", "b) Сауроподы", "c) Тероподы", "d) Анкилозавры"], "correct": "c) Тероподы"},
    {"question": "Какой динозавр был назван в честь известного физика и математика? 🔍", "answers": ["a) Дарвинозавр", "b) Ньютонозавр", "c) Эйнштейнозавр", "d) Диплодок"], "correct": "b) Ньютонозавр"},
    {"question": "Какой динозавр считается предком современных птиц? 🐦", "answers": ["a) Археоптерикс", "b) Птеранодон", "c) Тираннозавр Рекс", "d) Велоцираптор"], "correct": "a) Археоптерикс"},
    {"question": "Какой динозавр имел гребень на своей голове для коммуникации с другими особями? 🎶", "answers": ["a) Трицератопс", "b) Велоцираптор", "c) Стегозавр", "d) Парацератозавр"], "correct": "a) Трицератопс"},
    {"question": "Как называется гигантская группа динозавров с длинными шеями? 🦕", "answers": ["a) Брахиозавры", "b) Сауроподы", "c) Велоцирапторы", "d) Птеранодоны"], "correct": "b) Сауроподы"},
    {"question": "Какой динозавр был первым обнаруженным динозавром в Африке? 🌍", "answers": ["a) Тираннозавр Рекс", "b) Брахиозавр", "c) Стегозавр", "d) Масайрозавр"], "correct": "d) Масайрозавр"},
    {"question": "Какой динозавр был одним из первых, обнаруженных с перьями? 🦚", "answers": ["a) Тираннозавр Рекс", "b) Велоцираптор", "c) Стегозавр", "d) Археоптерикс"], "correct": "d) Археоптерикс"},
    {"question": "Какая из этих характеристик была характерной для анкилозавров? 🛡️", "answers": ["a) Длинная шея", "b) Перья на теле", "c) Жесткий панцирь", "d) Большие крылья"], "correct": "c) Жесткий панцирь"},
    {"question": "Какой динозавр был назван в честь великого древнегреческого бога-титана? 🏛️", "answers": ["a) Аполлозавр", "b) Зевсозавр", "c) Гераклезавр", "d) Афродон"], "correct": "b) Зевсозавр"},
    {"question": "Какой динозавр считается одним из наиболее агрессивных хищников? 😠", "answers": ["a) Велоцираптор", "b) Тираннозавр Рекс", "c) Брахиозавр", "d) Стегозавр"], "correct": "a) Велоцираптор"},
    {"question": "Какой динозавр считается самым умным? 🧠", "answers": ["a) Велоцираптор", "b) Трицератопс", "c) Археоптерикс", "d) Птеранодон"], "correct": "a) Велоцираптор"},
    {"question": "Какой динозавр был первым открытым в Австралии? 🇦🇺", "answers": ["a) Тираннозавр Рекс", "b) Велоцираптор", "c) Кулчискиозавр", "d) Стегозавр"], "correct": "c) Кулчискиозавр"},
    {"question": "Какой динозавр обладал крупными рогоподобными структурами на голове для защиты? 🦏", "answers": ["a) Трицератопс", "b) Стегозавр", "c) Брахиозавр", "d) Парацератозавр"], "correct": "a) Трицератопс"},
    {"question": "Какой динозавр считается самым быстрым на ногах? 🏃‍♂️", "answers": ["a) Тираннозавр Рекс", "b) Спинозавр", "c) Велоцираптор", "d) Стегозавр"], "correct": "c) Велоцираптор"}
]

current_question = 0  # Индекс текущего вопроса

# Функция для отправки текущего вопроса и удаления предыдущего вопроса
async def send_question(chat_id):
    global prev_question_message_id

    if prev_question_message_id:
        try:
            await bot.delete_message(chat_id, prev_question_message_id)  # Удаляем предыдущий вопрос
        except Exception as e:
            logging.error(f"Error while deleting previous question: {e}")

    question_data = questions[current_question]
    keyboard = types.InlineKeyboardMarkup()
    for i, answer in enumerate(question_data["answers"]):
        button = types.InlineKeyboardButton(answer, callback_data=f"{current_question}-{i}")
        keyboard.add(button)

    message = await bot.send_message(chat_id, question_data["question"], reply_markup=keyboard)
    prev_question_message_id = message.message_id

# Id администратора (замените на ваш id, который вы получили после отправки /start)
admin_id = 1281869576
quiz_access_key = None

# Обработчик команды /start
@dispatcher.message_handler(commands=['start'])
async def start(message: types.Message):
    global good
    global user_info
    global q
    global current_question
    global prev_question_message_id

    user = message.from_user
    if user.username:
        user_info = user.username
    else:
        user_info = f"id: {user.id}"

    if user_info not in q:
        await bot.send_photo(message.chat.id, "https://lh3.googleusercontent.com/pw/AIL4fc8CzEhBu0EszdwUM-5CltbbRphdhFg9Dvre5PKo8R-3uZs6kUY7Wfy9iL2h8Oe8SARMavOkVNBQ2-H6C2zpTKCBPYCIOXahAdYXSOuNKUPE8Hyb3agxK9NYRsOS1nSvlRq4MvIPyw4IDXAjB99bsWiBARe5Mhq2-Mc19Mw0qqqgr1cKvwaQFWSf1oZReCBl6Wgeb6NC-L_OZb9_GYAJJjN1x-4feCAOzM73_AmDVyVkrdryxOy4kSl0YxHqxASZUEqhx5B-VXUGMhfhNCVjPnXSsYTsY50RvTyyHQcsgdI2uAiAajNzeqX7CSp7LcUEPJX6m3dhbF-J5dMeylcy_gSA1q6IwWiZHII8Zf-tiAL2hlaYm9_UqN0UR8r65YUC-EVu3ZjjYkTKEfKUrxHuYAMq_GC3APs9a5mRkOU0Jw2zmddRa39b3N5pD2ytjjLHr5DIkAjSe4hJSbG_2Steo-SZoK0-qtbab13zJiIgoaYV8AeNANCmnq_L0Q4sNQTHb3YjrqZ4pHa5OxZ6QGumOYuihmXHaD_F8pAJ9Y0M9uOsJyFERU2D19m8YgRJKMEnn7iKYdTVg51o6LIhpXq4DvlH-e37wXqb2iKl7D7cRhRX7m54nM4-Z0Lw8Qqck9Dr-DVGHFi3T3GUOW-Y6Mi_4QOOFJEPgZP7EsV3qM491MnFJHNTY73V3NGKRFFU61k6xI_sdbVtahy3u0PrO_vaEf-QPzq_rn-zE0vlWpbeuB1AAaTaYZGHf1S5DJ7TpuEf_EeMWQYWAlx7-P3_ng0Mb80m3IT3tybCfC6RccriyB0oWb-Y5--g6JRAlXAd8FYNWMFWaOlJOZiEH7JTVmpc0_ICKmVOpnPOyxQvchuVn59q7oJoYasN4NnV1VJdTH-uCRM2Kx4FWgF6G3o8NuV7MQ=w1080-h1080-s-no?authuser=0")
        await bot.send_message(message.chat.id, "Здравствуй! Вы сейчас будете проходить Quiz от Mintodinos.\nВсего будет 20 вопросов")
        await send_question(message.chat.id)
        q[user_info] = {"good": 0}
        good = 0
    else:
        await bot.send_message(message.chat.id, "Ты уже проходил квиз, обмануть не получиться 😡")

# Обработчик команды /delete
@dispatcher.message_handler(commands=['delete'])
async def secret_command(message: types.Message):
    global q
    if message.from_user.id == admin_id:
        args = message.get_args().strip()
        if args.startswith('@'):
            username = args[1:]
            if username in q:
                del q[username]
                await bot.send_message(message.chat.id, f"Пользователь {username} удален из списка участников.")
            else:
                await bot.send_message(message.chat.id, f"Пользователь {username} не найден в списке участников.")
        else:
            await bot.send_message(message.chat.id, "Пожалуйста, укажите имя пользователя (@username), чтобы удалить его из списка.")
    else:
        await bot.send_message(message.chat.id, "Извините, у вас нет доступа к этой команде.")

# Обработчик команды /vse
@dispatcher.message_handler(commands=['vse'])
async def show_all_results(message: types.Message):
    if message.from_user.id == admin_id:
        result_message = "Результаты участников:\n"
        for user, data in q.items():
            user_good = data["good"]
            result_message += f"{user}: {user_good}\n"

        await bot.send_message(message.chat.id, result_message)
    else:
        await bot.send_message(message.chat.id, "Извините, у вас нет доступа к этой команде.")
# Обработчик команды /code
@dispatcher.message_handler(commands=['code'])
async def set_quiz_access_code(message: types.Message):
    global quiz_access_key
    if message.from_user.id == admin_id:
        args = message.get_args().strip()
        if args:
            quiz_access_key = args
            await bot.send_message(message.chat.id, f"Ключ для повторного прохождения квиза установлен: {quiz_access_key}")
        else:
            await bot.send_message(message.chat.id, "Пожалуйста, укажите ключ после команды /code.")
    else:
        await bot.send_message(message.chat.id, "Извините, у вас нет доступа к этой команде.")

# Обработчик команды /key
@dispatcher.message_handler(commands=['key'])
async def use_quiz_access_key(message: types.Message):
    global quiz_access_key
    global q

    args = message.text.split(" ", 1)[1].strip()  # Получаем аргумент после команды
    if quiz_access_key and message.from_user.id != admin_id:
        if args == quiz_access_key:
            user_info = message.from_user.username if message.from_user.username else f"id: {message.from_user.id}"
            del q[user_info]
            await bot.send_message(message.chat.id, "Вы успешно удалены из списка участников квиза.")

# Обработчик нажатий на кнопки inline клавиатуры
@dispatcher.callback_query_handler(lambda call: True)
async def callback_query(call: types.CallbackQuery):
    global current_question
    global good
    global user_info
    global q

    question_data = questions[current_question]
    question_index, answer_index = call.data.split('-')
    question_index = int(question_index)
    answer_index = int(answer_index)
    if question_index == current_question:
        selected_answer = question_data["answers"][answer_index]
        correct_answer = question_data["correct"]
        if selected_answer == correct_answer:
            # Увеличение количества правильных ответов пользователя
            good += 1

        current_question += 1  # Переходим к следующему вопросу

        if current_question < len(questions):
            await send_question(call.message.chat.id)
        else:
            await bot.send_message(call.message.chat.id, f"Конец викторины! Спасибо за участие.😊\nВаше кол-во правильных ответов: {good}")
            q[user_info] = {"good": good}  # Сохраняем результаты пользователя в словарь q
            # Отправляем результаты администратору
            result_message = f"{user_info} - {good}"
            await bot.send_message(admin_id, result_message)  # Отправляем результаты только администратору

            # Сбрасываем счетчик вопросов и очищаем предыдущий вопрос
            current_question = 0
            good = 0
            global prev_question_message_id
            prev_question_message_id = None

# Запускаем бота с помощью асинхронного цикла событий
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(executor.start_polling(dispatcher, skip_updates=True, loop=loop))  # Используем 'dp' вместо 'dispatcher'
