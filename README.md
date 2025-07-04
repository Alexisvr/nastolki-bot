# 🎲 Настолки-Бот

Telegram-бот для анонсов настольных встреч с возможностью автоматической записи участников, счётчиком и списком.

---

## 📦 Что умеет бот

- Команда `/announce` — создать встречу (только для админа).
- Кнопка «✅ Записаться» — участники записываются на встречу.
- Счётчик записавшихся в сообщении.
- Команда `/list` — показать список участников (только для админа).

---

## 🚀 Как развернуть бота на Railway

1. **Форкни или скачай** этот репозиторий:
   - Кнопка `Fork` или `Code → Download ZIP`.

2. **Создай бота в Telegram**:
   - Напиши в [@BotFather](https://t.me/BotFather)
   - Команда `/newbot`
   - Получи токен (например: `123456:ABC-DEF...`)

3. **Узнай свой Telegram ID** (чтобы быть админом бота):
   - Напиши [@RawDataBot](https://t.me/RawDataBot)
   - Он пришлёт твой ID (например `123456789`)

4. **Узнай ID канала**:
   - Добавь бота в канал как админа.
   - Напиши в канал что-нибудь.
   - Перешли это сообщение в [@getidsbot](https://t.me/getidsbot)
   - Он скажет ID канала, например `-1001234567890`

5. **Зайди на [https://railway.app](https://railway.app)**:
   - Зарегистрируйся.
   - Нажми `New Project → Deploy from GitHub`
   - Выбери свой репозиторий

6. **Задай переменные окружения в Railway**:

| Переменная   | Значение                  |
|--------------|----------------------------|
| `BOT_TOKEN`  | токен от BotFather         |
| `CHANNEL_ID` | ID твоего канала (`-100...`) |
| `ADMIN_ID`   | твой Telegram ID (число)   |

7. Нажми **Deploy** — Railway всё сам установит.

---

## 📲 Как пользоваться ботом

1. Напиши боту в личку `/announce`
2. Ответь на его вопросы: название, время, место.
3. Он опубликует анонс в канал с кнопкой ✅
4. Участники смогут нажимать — и записываться.
5. Ты сможешь в любой момент ввести `/list`, чтобы увидеть кто записался.

---

## 👨‍💻 Автор

Создан с ❤️ с помощью aiogram 3
