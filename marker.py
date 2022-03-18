from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
but = types.KeyboardButton('🔮Всевидящий Бэн')
but1 = types.KeyboardButton('💬Информация')
prof = types.KeyboardButton('🏅Профиль')
markup.add(but, but1, prof)


markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
zag = types.KeyboardButton('👨‍🌾Загадал')
back = types.KeyboardButton('🔙Назад')
markup2.add(zag, back)
  
