import json, os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

BOT_TOKEN = os.getenv('7862060581:AAHG1gN9wjVowHiIs9nLL8dafKYkxINgJ64')
CHANNEL_ID = int(os.getenv('DisesMeets'))
ADMIN_ID = os.getenv('alex18v')

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher()
DATA_FILE = 'data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        return json.load(open(DATA_FILE))
    return {}

def save_data(data):
    json.dump(data, open(DATA_FILE, 'w'))

@dp.message(Command('announce'))
async def cmd_announce(msg: types.Message):
    if str(msg.from_user.id) != ADMIN_ID:
        return await msg.reply("❌ Только админ.")
    await msg.answer("Название встречи?")
    dp.data['chat'] = msg.from_user.id
    dp.data['state'] = 'title'

@dp.message()
async def handler(msg: types.Message):
    if msg.from_user.id != dp.data.get('chat'): return
    state = dp.data.get('state')
    if state == 'title':
        dp.data['title'] = msg.text
        dp.data['state'] = 'when'
        return await msg.answer("Дата и время?")
    if state == 'when':
        dp.data['when'] = msg.text
        dp.data['state'] = 'where'
        return await msg.answer("Место?")
    if state == 'where':
        dp.data['where'] = msg.text
        data = load_data()
        pid = str(len(data)+1)
        data[pid] = {
            'title': dp.data['title'],
            'when': dp.data['when'],
            'where': dp.data['where'],
            'participants': []
        }
        save_data(data)
        btn = InlineKeyboardMarkup().add(
            InlineKeyboardButton("✅ Записаться", callback_data=f"join:{pid}")
        )
        text = (f"🎲 <b>{dp.data['title']}</b>\n"
                f"📅 {dp.data['when']}\n"
                f"📍 {dp.data['where']}\n\n"
                f"Уже записались: 0 человек")
        sent = await bot.send_message(CHANNEL_ID, text, reply_markup=btn)
        data[pid]['msg_id'] = sent.message_id
        save_data(data)
        dp.data.clear()
        return await msg.answer("✅ Анонс опубликован.")

@dp.callback_query(lambda c: c.data.startswith('join:'))
async def join(cq: types.CallbackQuery):
    pid = cq.data.split(':')[1]
    data = load_data()
    ev = data.get(pid)
    if not ev: return
    uname = cq.from_user.username or cq.from_user.first_name
    if uname in ev['participants']:
        return await cq.answer("❗ Уже записаны.", show_alert=True)
    ev['participants'].append(uname)
    save_data(data)
    text = (f"🎲 <b>{ev['title']}</b>\n"
            f"📅 {ev['when']}\n"
            f"📍 {ev['where']}\n\n"
            f"Уже записались: {len(ev['participants'])} человек")
    await bot.edit_message_text(text, CHANNEL_ID, ev['msg_id'],
                                reply_markup=InlineKeyboardMarkup().add(
                                    InlineKeyboardButton("✅ Записаться", callback_data=f"join:{pid}")
                                ))
    await cq.answer("✅ Вы записаны!")

@dp.message(Command('list'))
async def cmd_list(msg: types.Message):
    if str(msg.from_user.id) != ADMIN_ID:
        return await msg.reply("❌ Только админ.")
    data = load_data()
    if not data:
        return await msg.answer("Нет анонсов.")
    out = []
    for pid, ev in data.items():
        out.append(f"🔹 {ev['title']} — {len(ev['participants'])} чел.")
        out.extend(f"    • {u}" for u in ev['participants'])
    await msg.answer("\n".join(out))

if __name__ == "__main__":
    dp.run_polling(bot)
