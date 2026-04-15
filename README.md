  
![Bot Banner](https://img.shields.io/badge/Telegram-Bot-blue?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3.11-brightgreen?style=for-the-badge) ![OpenAI](https://img.shields.io/badge/OpenAI-GPT-orange?style=for-the-badge)

Топовый Telegram-бот с **GPT-чатом, генерацией картинок через DALL·E и менеджером задач**. Полностью асинхронный, чистый и масштабируемый код, готовый к GitHub.

---

## 🛠 Возможности

- 🤖 **GPT-чат**: `/gpt <текст>` – общение с ИИ на любые темы  
- 🖼 **Генерация картинок**: `/img <текст>` – создаёт картинку по описанию  
- 📝 **Менеджер задач**:  
  - `/add_task <текст>` – добавить задачу  
  - `/tasks` – показать список задач  
  - `/del_task <номер>` – удалить задачу  
- 📜 **Логирование сообщений** пользователей в `data/logs.txt`  
- ⚡ Асинхронная архитектура, легко расширять новыми командами и сервисами  

---

## ⚡ Запуск бота

1️⃣ **Клонируем репозиторий**  

git clone https://github.com/Nersisiian/Telegram_Bot.git

cd Telegram_Bot


2️⃣ **Создаём виртуальное окружение и ставим зависимости**  

python -m venv venv

Linux/macOS

source venv/bin/activate

Windows

venv\Scripts\activate
pip install -r requirements.txt


3️⃣ **Создаём `.env` с токенами**  

BOT_TOKEN=твой_токен_от_BotFather
OPENAI_API_KEY=твой_ключ_OpenAI


4️⃣ **Запускаем бота**  

python bot.py


---

## 🎯 Примеры команд

| Команда | Описание |
|---------|----------|
| /start  | Запуск бота |
| /help   | Список команд |
| /gpt Как дела? | Общение с ИИ |
| /img Космический кот | Генерация картинки |
| /add_task Купить молоко | Добавление задачи |
| /tasks  | Показать все задачи |
| /del_task 1 | Удалить задачу №1 |

---

## 📊 Блок-схема работы бота

```mermaid
flowchart TD
A[Пользователь] -->|сообщение/команда| B[Bot Handler]
B --> C{Команда?}
C -->|/gpt| D[AI Service: GPT]
C -->|/img| E[AI Service: DALL·E]
C -->|/add_task| F[Task Service: add_task]
C -->|/tasks| G[Task Service: list_tasks]
C -->|/del_task| H[Task Service: delete_task]
C -->|текст| I[Logger: log_message]
D --> J[Отправка ответа пользователю]
E --> J
F --> J
G --> J
H --> J
I --> J
