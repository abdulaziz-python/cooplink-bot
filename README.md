# 🤖 CoopLink Bot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?logo=python&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![HTML](https://img.shields.io/badge/HTML-46.5%25-orange?logo=html5&logoColor=white)
![Python](https://img.shields.io/badge/Python-53.5%25-blue?logo=python&logoColor=white)

</div>

## 📖 About

CoopLink Bot is a sophisticated Telegram bot designed to facilitate code selling through Telegram channels. The bot supports both Uzbek 🇺🇿 and Russian 🇷🇺 languages, making it accessible to a wider audience.

## ✨ Features

- 🌐 Multi-language Support (UZ/RU)
- 💻 Code Sales Management
- 📊 Channel Integration
- 🔐 Secure Transactions
- 👥 User-friendly Interface

## 🛠️ Tech Stack

- **Framework:** Aiogram 3.19.0
- **Database:** SQLite (aiosqlite)
- **Data Validation:** Pydantic
- **Async Support:** aiohttp, aiofiles
- **Frontend:** HTML

## 🚀 Installation

1. **Clone the repository**
```bash
git clone https://github.com/abdulaziz-python/cooplink-bot.git
cd cooplink-bot
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 📋 Dependencies

Key dependencies include:
- `aiogram` (v3.19.0) - Modern Telegram Bot API framework
- `aiosqlite` (v0.21.0) - Async SQLite database operations
- `pydantic` (v2.10.6) - Data validation using Python type annotations
- `aiohttp` (v3.11.14) - Async HTTP client/server framework

## 🔧 Configuration

1. Create a `.env` file in the root directory
```env
BOT_TOKEN=your_telegram_bot_token
ADMIN_ID=your_admin_telegram_id
```

2. Configure your sales channels in the bot settings

## 🌟 Usage

The bot provides several commands for different operations:

- `/start` - Initialize the bot
- `/help` - Get help information
- `/language` - Change language preference
- `/sell` - Start selling process
- `/stats` - View sales statistics

## 🏗️ Project Structure

```
cooplink-bot/
├── bot/
│   ├── handlers/
│   ├── keyboards/
│   ├── middleware/
│   └── utils/
├── database/
├── locales/
│   ├── uz/
│   └── ru/
├── requirements.txt
└── main.py
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Abdulaziz**
- GitHub: [@abdulaziz-python](https://github.com/abdulaziz-python)

## 📞 Support

If you have any questions or need support, feel free to:
- Open an issue
- Contact via Telegram: @yordam_42
- Send a pull request

---

<div align="center">
Made with ❤️ by Abdulaziz
</div>
