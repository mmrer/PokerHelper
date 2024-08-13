import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils import executor
import content

bot = Bot(token='TOKEN-BOT')
dp = Dispatcher(bot)
Lan1 = 2
users = {}
logging.basicConfig(level=logging.INFO)
langKB = types.ReplyKeyboardMarkup(resize_keyboard=True)
lang_btn1 = types.KeyboardButton(text='Русский 🇷🇺')
lang_btn2 = types.KeyboardButton(text='English 🇺🇸')
lang_btn3 = types.KeyboardButton(text='Spain 🇪🇸')
lang_btn4 = types.KeyboardButton(text='Portugal 🇵🇹')
lang_btn5 = types.KeyboardButton(text='Việt Nam 🇻🇳')
langKB.add(lang_btn1, lang_btn2, lang_btn5, lang_btn3, lang_btn4)
roomsKBRus = types.ReplyKeyboardMarkup(resize_keyboard=True)
roomsKBRus.add(types.KeyboardButton(text=''),
               types.KeyboardButton(text='Сделки'),
               types.KeyboardButton(text='Установка'),
               types.KeyboardButton(text='Дополнительные функции'),
               types.KeyboardButton(text='◀️'))
roomsKBEng = types.ReplyKeyboardMarkup(resize_keyboard=True)
roomsKBEng.add(types.KeyboardButton(text=''),
               types.KeyboardButton(text='Deals'),
               types.KeyboardButton(text='Installation'),
               types.KeyboardButton(text='Extra functions'),
               types.KeyboardButton(text='◀️'))

roomsKBSpain = types.ReplyKeyboardMarkup(resize_keyboard=True)
roomsKBSpain.add(types.KeyboardButton(text=''),
               types.KeyboardButton(text='Transacción'),
               types.KeyboardButton(text='Instalación'),
               types.KeyboardButton(text='Funciones adicionales'),
               types.KeyboardButton(text='◀️'))

roomsKBPorty = types.ReplyKeyboardMarkup(resize_keyboard=True)
roomsKBPorty.add(types.KeyboardButton(text=''),
               types.KeyboardButton(text='Transação'),
               types.KeyboardButton(text='Instalação'),
               types.KeyboardButton(text='Recursos adicionais'),
               types.KeyboardButton(text='◀️'))

roomsKBVietnam = types.ReplyKeyboardMarkup(resize_keyboard=True)
roomsKBVietnam.add(types.KeyboardButton(text=''),
               types.KeyboardButton(text='Giao dịch'),
               types.KeyboardButton(text='Cài đặt'),
               types.KeyboardButton(text='Các tính năng bổ sung'),
               types.KeyboardButton(text='◀️'))
# Keyboard install
roomsKBRusinstall = types.ReplyKeyboardMarkup(resize_keyboard=True)
roomsKBRusinstall.add(types.KeyboardButton(text=''),
               # types.KeyboardButton(text='Телефон'),
               types.KeyboardButton(text='Компьютер'),
               types.KeyboardButton(text='Назад'))
roomsKBEnginstall = types.ReplyKeyboardMarkup(resize_keyboard=True)
roomsKBEnginstall.add(types.KeyboardButton(text=''),
               # types.KeyboardButton(text='Phone'),
               types.KeyboardButton(text='computer'),
               types.KeyboardButton(text='Back'))
roomsKBSpaininstall = types.ReplyKeyboardMarkup(resize_keyboard=True)
roomsKBSpaininstall.add(types.KeyboardButton(text=''),
               # types.KeyboardButton(text='teléfono'),
               types.KeyboardButton(text='computadora'),
               types.KeyboardButton(text='atrás'))
roomsKBPortyinstall = types.ReplyKeyboardMarkup(resize_keyboard=True)
roomsKBPortyinstall.add(types.KeyboardButton(text=''),
               # types.KeyboardButton(text='Telefone'),
               types.KeyboardButton(text='computador'),
               types.KeyboardButton(text='voltar'))
roomsKBVieinstall = types.ReplyKeyboardMarkup(resize_keyboard=True)
roomsKBVieinstall.add(types.KeyboardButton(text=''),
               # types.KeyboardButton(text='Điện thoại'),
               types.KeyboardButton(text='máy tính'),
               types.KeyboardButton(text='trở lại'))
#extra -button---------------------------------------------------------------------------------------------------
roomsExtraRus = types.ReplyKeyboardMarkup(resize_keyboard=True)
roomsExtraRus.add(types.KeyboardButton(text=''),
               types.KeyboardButton(text='Панель администратора'),

types.KeyboardButton(text='Панель регулирования статистики'),
               types.KeyboardButton(text='Вывод статистики оппонентов'),
               types.KeyboardButton(text='Бот менеджер'),
               types.KeyboardButton(text='Чат хаб'),
               types.KeyboardButton(text='Назад'))
roomsExtraEng = types.ReplyKeyboardMarkup(resize_keyboard=True)
roomsExtraEng.add(types.KeyboardButton(text=''),
               types.KeyboardButton(text='Admin panel'),
               types.KeyboardButton(text='Statistics control panel'),
               types.KeyboardButton(text='Opponents statistics output'),
               types.KeyboardButton(text='Bot manager'),
               types.KeyboardButton(text='Chat hub'),
               types.KeyboardButton(text='Back'))
roomsExtraSpain = types.ReplyKeyboardMarkup(resize_keyboard=True)
roomsExtraSpain.add(types.KeyboardButton(text=''),
               types.KeyboardButton(text='Panel de administración'),
               types.KeyboardButton(text='Panel de control de estadísticas'),
               types.KeyboardButton(text='Salida de estadísticas de oponentes'),
               types.KeyboardButton(text='Administrador de bots'),
               types.KeyboardButton(text='Centro de chat'),
               types.KeyboardButton(text='atrás'))
roomsExtraPorty = types.ReplyKeyboardMarkup(resize_keyboard=True)
roomsExtraPorty.add(types.KeyboardButton(text=''),
               types.KeyboardButton(text='Painel de administração'),
               types.KeyboardButton(text='Painel de controle de estatísticas'),
               types.KeyboardButton(text='Saída de estatísticas dos oponentes'),
               types.KeyboardButton(text='Gerenciador de bots'),
               types.KeyboardButton(text='Hub de bate-papo'),
               types.KeyboardButton(text='voltar'))
roomsExtraViet = types.ReplyKeyboardMarkup(resize_keyboard=True)
roomsExtraViet.add(types.KeyboardButton(text=''),
               types.KeyboardButton(text='Bảng điều khiển quản trị'),
               types.KeyboardButton(text='Bảng điều khiển thống kê'),
               types.KeyboardButton(text='Đầu ra thống kê đối thủ'),
               types.KeyboardButton(text='Quản lý bot'),
               types.KeyboardButton(text='Trung tâm trò chuyện'),
               types.KeyboardButton(text='trở lại'))
#Deals-button------------------------------------------------------------------------------------------

roomsKBRusDeal = types.ReplyKeyboardMarkup(resize_keyboard=True)
roomsKBRusDeal.add(types.KeyboardButton(text=''),
               types.KeyboardButton(text='Экология'),
               types.KeyboardButton(text='Сделка %'),
               types.KeyboardButton(text='Назад'))
roomsKBEngDeal = types.ReplyKeyboardMarkup(resize_keyboard=True)
roomsKBEngDeal.add(types.KeyboardButton(text=''),
               types.KeyboardButton(text='Ecology'),
               types.KeyboardButton(text='Deal %'),
               types.KeyboardButton(text='Back'))
roomsKBSpainDeal = types.ReplyKeyboardMarkup(resize_keyboard=True)
roomsKBSpainDeal.add(types.KeyboardButton(text=''),
               types.KeyboardButton(text='Ecología'),
               types.KeyboardButton(text='% de trato'),
               types.KeyboardButton(text='atrás'))
roomsKBPortyDeal = types.ReplyKeyboardMarkup(resize_keyboard=True)
roomsKBPortyDeal.add(types.KeyboardButton(text=''),
               types.KeyboardButton(text='Ecologia'),
               types.KeyboardButton(text='Negócio %'),
               types.KeyboardButton(text='voltar'))
roomsKBVietDeal = types.ReplyKeyboardMarkup(resize_keyboard=True)
roomsKBVietDeal.add(types.KeyboardButton(text=''),
               types.KeyboardButton(text='Sinh thái học'),
               types.KeyboardButton(text='Giao dịch %'),
               types.KeyboardButton(text='trở lại'))
# Messages handling
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, text=content.Welcome, reply_markup=langKB)
    await bot.send_message(chat_id=-1002119938787, text="Впервые юзнул бота @" + message.from_user.username)

@dp.message_handler(content_types=['text', 'document', 'file'])
async def choice_room(message: types.Message):
    if message.chat.id not in users:
        users[message.chat.id] = {'lang': 2}

    if message.text == "Русский 🇷🇺":
        await bot.send_message(message.chat.id, text='Выбран Русский язык', reply_markup=roomsKBRus)
        Lan1 = 1
        users[message.chat.id]['lang'] = 1
        await bot.send_message(message.chat.id, text=content.RusInfo)
    elif message.text == "English 🇺🇸":
        await bot.send_message(message.chat.id, text='Selected English', reply_markup=roomsKBEng)
        Lan1 = 2
        users[message.chat.id]['lang'] = 2
        await bot.send_message(message.chat.id, text=content.EngInfo)
    elif message.text == "Spain 🇪🇸":
        await bot.send_message(message.chat.id, text='Idioma español seleccionado', reply_markup=roomsKBSpain)
        Lan1 = 3
        users[message.chat.id]['lang'] = 3
        await bot.send_message(message.chat.id, text=content.SpainInfo)
    elif message.text == "Portugal 🇵🇹":
        await bot.send_message(message.chat.id, text='Idioma português selecionado', reply_markup=roomsKBPorty)
        Lan1 = 4
        users[message.chat.id]['lang'] = 4
        await bot.send_message(message.chat.id, text=content.PortyInfo)
    elif message.text == "Việt Nam 🇻🇳":
        await bot.send_message(message.chat.id, text='Đã chọn tiếng Việt', reply_markup=roomsKBVietnam)
        Lan1 = 5
        users[message.chat.id]['lang'] = 5
        await bot.send_message(message.chat.id, text=content.VietnamInfo)
#----------------------------------------RU---------------------------------------------------------------------

    elif message.text == 'Сделки':
        if users[message.chat.id]['lang'] == 1:
            await bot.send_message(message.chat.id, text=content.RusDeal, reply_markup=roomsKBRusDeal)
            await bot.send_message(chat_id=-1002119938787, text="Залез в вкладку сделки @" + message.from_user.username)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=roomsKBRus)

    elif message.text == 'Установка':
        if users[message.chat.id]['lang'] == 1:
            await bot.send_message(message.chat.id, text=content.RusInstall, reply_markup=roomsKBRusinstall)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'Дополнительные функции':
        if users[message.chat.id]['lang'] == 1:
            await bot.send_message(message.chat.id, text=content.RusExtra, reply_markup=roomsExtraRus)
            await bot.send_message(chat_id=-1002119938787, text="Залез в вкладку допки @" + message.from_user.username)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == '◀️':
        if users[message.chat.id]['lang'] == 1:
            await bot.send_message(message.chat.id, text="Назад", reply_markup=langKB)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'Назад':
        if users[message.chat.id]['lang'] == 1:
            await bot.send_message(message.chat.id, text="Назад", reply_markup=roomsKBRus)
        else:
                await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'Back':
            if users[message.chat.id]['lang'] == 2:
                await bot.send_message(message.chat.id, text="Back", reply_markup=roomsKBEng)
            else:
                await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'atrás':
        if users[message.chat.id]['lang'] == 3:
            await bot.send_message(message.chat.id, text="atrás", reply_markup=roomsKBSpain)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'voltar':
        if users[message.chat.id]['lang'] == 4:
            await bot.send_message(message.chat.id, text="voltar", reply_markup=roomsKBPorty)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'trở lại':
        if users[message.chat.id]['lang'] == 5:
            await bot.send_message(message.chat.id, text="trở lại", reply_markup=roomsKBVietnam)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
        # -------------------------------------------------ENG------------------------------------------------
    elif message.text == 'Deals':
        if users[message.chat.id]['lang'] == 2:
            await bot.send_message(message.chat.id, text=content.EngDeals, reply_markup=roomsKBEngDeal)
            await bot.send_message(chat_id=-1002119938787, text="Залез в вкладку сделки @" + message.from_user.username)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'Installation':
        if users[message.chat.id]['lang'] == 2:
            await bot.send_message(message.chat.id, text=content.EngInstall, reply_markup=roomsKBEnginstall)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'Extra functions':
        if users[message.chat.id]['lang'] == 2:
            await bot.send_message(message.chat.id, text=content.EngExtra, reply_markup=roomsExtraEng)
            await bot.send_message(chat_id=-1002119938787, text="Залез в вкладку допки @" + message.from_user.username)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
        # ------------------------------------------SPAIN-------------------------------------
    elif message.text == 'Transacción':
        if users[message.chat.id]['lang'] == 3:
            await bot.send_message(message.chat.id, text=content.SpainDeal, reply_markup=roomsKBSpainDeal)
            await bot.send_message(chat_id=-1002119938787, text="Залез в вкладку сделки @" + message.from_user.username)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'Instalación':
        if users[message.chat.id]['lang'] == 3:
            await bot.send_message(message.chat.id, text=content.SpainInstall, reply_markup=roomsKBSpaininstall)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'Funciones adicionales':
        if users[message.chat.id]['lang'] == 3:
            await bot.send_message(message.chat.id, text=content.SpainExtra, reply_markup=roomsExtraSpain)
            await bot.send_message(chat_id=-1002119938787, text="Залез в вкладку допки @" + message.from_user.username)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
        # ------------------------------portu---------------------------------------------------
    elif message.text == 'Transação':
        if users[message.chat.id]['lang'] == 4:
            await bot.send_message(message.chat.id, text=content.PortyDeals, reply_markup=roomsKBPortyDeal)
            await bot.send_message(chat_id=-1002119938787, text="Залез в вкладку сделки @" + message.from_user.username)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'Instalação':
            if users[message.chat.id]['lang'] == 4:
                await bot.send_message(message.chat.id, text=content.PortyInstall, reply_markup=roomsKBPortyinstall)
            else:
                await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'Recursos adicionais':
            if users[message.chat.id]['lang'] == 4:
                await bot.send_message(message.chat.id, text=content.PortyExtra, reply_markup=roomsExtraPorty)
                await bot.send_message(chat_id=-1002119938787, text="Залез в вкладку допки @" + message.from_user.username)
            else:
                await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
        # ----------------------------------Vietnam-------------------------------------------------
    elif message.text == 'Giao dịch':
            if users[message.chat.id]['lang'] == 5:
                await bot.send_message(message.chat.id, text=content.VietnamDeals, reply_markup=roomsKBVietDeal)
                await bot.send_message(chat_id=-1002119938787, text="Залез в вкладку сделки @" + message.from_user.username)
            else:
                await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'Cài đặt':
            if users[message.chat.id]['lang'] == 5:
                await bot.send_message(message.chat.id, text=content.VietnamInstall, reply_markup=roomsKBVieinstall)
            else:
                await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'Các tính năng bổ sung':
            if users[message.chat.id]['lang'] == 5:
                await bot.send_message(message.chat.id, text=content.VietnamExtra, reply_markup=roomsExtraViet)
                await bot.send_message(chat_id=-1002119938787, text="Залез в вкладку допки @" + message.from_user.username)
            else:
                await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
        # eco-ru---------------------
    elif message.text == 'Экология':
            if users[message.chat.id]['lang'] == 1:
                await bot.send_message(message.chat.id, text=content.RusEco, reply_markup=roomsKBRusDeal)
            else:
                await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'Сделка %':
            if users[message.chat.id]['lang'] == 1:
                await bot.send_message(message.chat.id, text=content.RusDealinfo, reply_markup=roomsKBRusDeal)
            else:
                await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
        # eco-eng---------------------
    elif message.text == 'Ecology':
        if users[message.chat.id]['lang'] == 2:
            await bot.send_message(message.chat.id, text=content.Engdealinfo, reply_markup=roomsKBEngDeal)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'Deal %':
        if users[message.chat.id]['lang'] == 2:
            await bot.send_message(message.chat.id, text=content.EngDealEco, reply_markup=roomsKBEngDeal)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
        # eco-spain---------------------
    elif message.text == 'Ecología':
        if users[message.chat.id]['lang'] == 3:
            await bot.send_message(message.chat.id, text=content.Spainecoinfo, reply_markup=roomsKBSpainDeal)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == '% de trato':
        if users[message.chat.id]['lang'] == 3:
            await bot.send_message(message.chat.id, text=content.Spaindealinfo, reply_markup=roomsKBSpainDeal)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
        # eco-porty---------------------
    elif message.text == 'Ecologia':
        if users[message.chat.id]['lang'] == 4:
            await bot.send_message(message.chat.id, text=content.Portyecoinfo, reply_markup=roomsKBPortyDeal)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'Negócio %':
            if users[message.chat.id]['lang'] == 4:
                await bot.send_message(message.chat.id, text=content.Portydealsinfo, reply_markup=roomsKBPortyDeal)
            else:
                await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
        # eco-viet---------------------
    elif message.text == 'Sinh thái học':
        if users[message.chat.id]['lang'] == 5:
            await bot.send_message(message.chat.id, text=content.Vietecoinfo, reply_markup=roomsKBVietDeal)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'Giao dịch %':
        if users[message.chat.id]['lang'] == 5:
            await bot.send_message(message.chat.id, text=content.Vietdealsinfo, reply_markup=roomsKBVietDeal)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    # install-ru---------------------
    # elif message.text == 'Телефон':
    #     if users[message.chat.id]['lang'] == 1:
    #         await bot.send_message(message.chat.id, text=content.Rusinstallphone, reply_markup=roomsKBRusinstall)
    #     else:
    #         await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'Компьютер':
        if users[message.chat.id]['lang'] == 1:
            await bot.send_message(message.chat.id, text=content.Rusinstallpc, reply_markup=roomsKBRusinstall)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    # ----------eng---------------------
    # elif message.text == 'Phone':
    #     if users[message.chat.id]['lang'] == 2:
    #         await bot.send_message(message.chat.id, text=content.EngInstallphone, reply_markup=roomsKBEnginstall)
    #     else:
    #         await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'computer':
        if users[message.chat.id]['lang'] == 2:
            await bot.send_message(message.chat.id, text=content.Enginstallpc, reply_markup=roomsKBEnginstall)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    # -------------------spain---------------------
    # elif message.text == 'teléfono':
    #     if users[message.chat.id]['lang'] == 3:
    #         await bot.send_message(message.chat.id, text=content.Spainnstallphone, reply_markup=roomsKBSpaininstall)
    #     else:
    #         await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'computadora':
        if users[message.chat.id]['lang'] == 3:
            await bot.send_message(message.chat.id, text=content.Spaininstallpc, reply_markup=roomsKBSpaininstall)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    # --------------porty---------------------
    # elif message.text == 'Telefone':
    #     if users[message.chat.id]['lang'] == 4:
    #         await bot.send_message(message.chat.id, text=content.Portyinstallphone, reply_markup=roomsKBPortyinstall)
    #     else:
    #         await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'computador':
        if users[message.chat.id]['lang'] == 4:
            await bot.send_message(message.chat.id, text=content.Portyinstallpc, reply_markup=roomsKBPortyinstall)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    # ---------------------viet---------------------
    # elif message.text == 'Điện thoại':
    #     if users[message.chat.id]['lang'] == 5:
    #         await bot.send_message(message.chat.id, text=content.Vietnstallphone, reply_markup=roomsKBVieinstall)
    #     else:
    #         await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)
    elif message.text == 'máy tính':
        if users[message.chat.id]['lang'] == 5:
            await bot.send_message(message.chat.id, text=content.Vietinstallpc, reply_markup=roomsKBVieinstall)
        else:
            await bot.send_message(message.chat.id, text="/start", reply_markup=langKB)


executor.start_polling(dp)
