# Telegram Bot for Ministry of Health Ethiopia

This code is a Telegram bot that provides information from the Ministry of Health Ethiopia website. The bot can scrape specific sections of the website and send the information to a Telegram group chat. It uses the requests library to make HTTP requests, bs4 library for web scraping, and telebot library for interacting with the Telegram Bot API.

## Setup

To use the bot, you need to set up a Telegram bot and obtain a bot token. Follow these steps to set up the bot:

1. Create a new bot on Telegram by talking to the BotFather (https://core.telegram.org/bots#botfather). BotFather will provide you with a token for your bot.

2. Fill in the TELEGRAM_BOT_TOKEN constant in the code with your bot token.

3. Set the GROUP_CHAT_ID constant with the ID of the Telegram group chat where you want to send the scraped information.

4. Install the required libraries by running pip install requests bs4 telebot in your command line.

## Usage

The bot provides several commands or button options to scrape and send information from specific sections of the Ministry of Health Ethiopia website. The available commands are:

- /start: Initializes the bot and displays the available buttons.

The available buttons are:

- ABOUT: Scrapes and sends information about the mission, vision, and objectives of the Ministry of Health Ethiopia.
- PROGRAMS: Scrapes and sends information about the initiatives and programs of the Ministry of Health Ethiopia.
- PILLARS: Scrapes and sends information about the projects and pillars of the Ministry of Health Ethiopia.
- RESOURCES: Scrapes and sends information about the publications and resources of the Ministry of Health Ethiopia.
- NEWS: Scrapes and sends the latest news articles from the Ministry of Health Ethiopia website.

To use the bot, simply run the code and start a conversation with the bot in your Telegram group chat. The bot will send the welcome message and display the available buttons. Select a button to scrape and send the corresponding information to the group chat.

Note: Make sure the bot has proper permissions to send messages and access the group chat.

## Dependencies

The code uses the following dependencies which need to be installed:

- requests: Library for making HTTP requests.
- bs4: Beautiful Soup library for web scraping.
- telebot: Library for interacting with the Telegram Bot API.

You can install these dependencies by running pip install requests bs4 telebot.

## Contributing

If you want to contribute to this project, you can add more functionality, improve the scraping logic, or enhance the interaction with the Telegram Bot API. Feel free to fork the project, make changes, and submit a pull request.
