from aiogram import Bot, Dispatcher, executor, types
from config import TELEGRAM_TOKEN
from keboard.keyboards import get_keyboard_1, get_keyboard_2
from keboard.key_inline import get_keyboard_1_inline, get_keyboard_2_inline
from database.database import initialize_db, add_user, get_user

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

initialize_db()


@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    user = get_user(message.from_user.id)
    if user is None:
        add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        await message.answer('Привет, я твой первый бот', reply_markup=get_keyboard_1())
    else:
        await message.answer('Привет, я твой первый бот', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Предсказание')
async def button_1_click(message: types.Message):
    await message.answer('Через 3 дня, произойдёт что-то хорошее')

@dp.message_handler(lambda message: message.text == 'Отправь фото машины - BMW M5')
async def button_2_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://files.libertycity.net/download/gta5_bmw/fulls/2021-02/bmw-m5-competition_1686006578_240244.jpg', caption='Вот тебе BMW M5', reply_markup=get_keyboard_1_inline())

@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_3_click(message: types.Message):
    await message.answer('Тут ты можешь узнать текущее время, а также, ознакомиться и приобрести машину RAM', reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Отправь фото машины - RAM')
async def button_4_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://w.forfun.com/fetch/24/244e097d270230f61e5960d29de3b8c8.jpeg', caption='Вот тебе RAM', reply_markup=get_keyboard_2_inline())

@dp.message_handler(lambda message: message.text == 'Вернуться на 1 клавиатуру')
async def button_5_click(message: types.Message):
    await message.answer('Тут ты можешь ознакомиться и приобрести машину BMW M5, а также узнать предсказание', reply_markup=get_keyboard_1())


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда для того, чтобы запустить бота'),
        types.BotCommand(command='/help', description='Команда для того, чтобы бот тебя поддержал'),
        types.BotCommand(command='/quote', description='Цитата'),
        types.BotCommand(command='/love', description='Команда для того, чтобы бот, отправил моё стихотворение '),
        types.BotCommand(command='/fact', description='Команда для того, чтобы бот, рассказал интересный факт'),
        types.BotCommand(command='/pk', description='Команда для того, чтобы бот, рассказал строение ПК')
    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, я твой первый эхо бот')


@dp.message_handler(commands='help')
async def start(message: types.Message):
    await message.reply('Знай, что ты особенный человек, способный преодолевать любые трудности. Твоя сила и умение справляться с трудностями вдохновляют окружающих. Помни, что ты не одинок - всегда можно найти поддержку у друзей, близких и любящих людей. Верь в себя и помни, что даже в сложные моменты всегда есть светлое будущее. Ты сильный, умный и способный на большее, чем думаешь. Все будет хорошо!')

@dp.message_handler(commands='quote')
async def start(message: types.Message):
    await message.reply('«Жизнь слишком коротка, поэтому начинайте с десерта» (Барбра Стрейзанд).')

@dp.message_handler(commands='love')
async def start(message: types.Message):
    await message.reply('Шли дни, года, любовь угасла \nНо пустота внутри твоя…\nНастигла будто бы меня…\nТвои глаза остались в сердце\nИ..разум больше не кричит.\nИ лишь, одно, тревожит сердце…\nВнутри..как будто бы магнит!\nВсе тянет-тянет, словно гиря.\nК тебе..туда..где тихо-тихо,\nГде мы вдвоем, только с тобой\nПоём другу другу обо всём.')

@dp.message_handler(commands='fact')
async def start(message: types.Message):
    await message.reply('Если убрать всё межатомное пространство, человечество уместится в кубике сахара.')

@dp.message_handler(commands='pk')
async def start(message: types.Message):
    await message.reply('Вот перечень основных элементов, необходимых для сборки компьютера:\n 1. Центральный процессор (CPU)\n2. Материнская плата (Motherboard)\n3. Оперативная память (RAM)\n4. Жесткий диск (HDD или SSD)\n5. Блок питания (Power supply unit, PSU)\n6. Видеокарта (Graphics card, GPU)\n7. Охлаждение (вентиляторы, система охлаждения ЦПУ и GPU)\n8. Корпус (Case)\n9. Монитор (Monitor)\n10. Клавиатура и мышь (Keyboard and mouse)\nКроме основных компонентов, также могут потребоваться различные кабели, интерфейсные карты, а также опциональные устройства, такие как оптические приводы, звуковые карты и т.д.')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)