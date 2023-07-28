import requests
import bs4
import telebot

# Set the Telegram bot token and group chat ID
TELEGRAM_BOT_TOKEN = "6309059679:AAHJkh8_LHbhrDXiShZX-9wZNKDZ5mEdi1c"
GROUP_CHAT_ID = "@MOH_health_all"

# Start the bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# A function to send a message to the Telegram group chat
def send_message(message):
    if message.strip() != "":
        bot.send_message(GROUP_CHAT_ID, message)

# A function to scrape and send a message to the Telegram group chat
def scrape_and_send_message(url, tag, attrs=None):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all(tag, attrs=attrs)
    message = ""
    for element in elements:
        if element.name == "li":
            message += "- " + element.get_text(strip=True) + "\n"
        elif element.name == "strong":
            message += "**" + element.get_text(strip=True) + "**\n\n"
        elif element.name == "h1":
            message += "# " + element.get_text(strip=True) + "\n\n"
        elif element.name == "a":
            message += "" + element.get_text(strip=True) + " + \n\n"
        elif element.name == "p":
            message += "  " + element.get_text(strip=True) + " + \n\n"
        else:
            message += element.get_text(strip=True) + "\n\n"
    send_message(message)


# ABOUT
about_url = "https://www.moh.gov.et/site/mission-vission-objectives"

# PROGRAMS
programs_url = "https://www.moh.gov.et/site/initiatives-4-col"

# PILLARS
pillars_url = "https://www.moh.gov.et/site/projects-3-col"

# RESOURCES
resources_url = "https://www.moh.gov.et/site/publications-and-litretures"

# NEWS
news_url = "https://www.moh.gov.et/site/articles"

# A function to handle button clicks
def handle_button_click(button_text):
    if button_text == "ABOUT":
        scrape_and_send_message(about_url, "h1", {"class": "title page-title"})
        scrape_and_send_message(about_url, "strong")
        scrape_and_send_message(about_url, "p")
    elif button_text == "PROGRAMS":
        scrape_and_send_message(programs_url, "h1", {"class": "title page-title"})
        scrape_and_send_message(programs_url, "div", {"class": "col-md-3 col-sm-6 views-row"})
    elif button_text == "PILLARS":
        scrape_and_send_message(pillars_url, "h1", {"class": "title page-title"})
        scrape_and_send_message(pillars_url, "div", {"class": "col-md-4 col-sm-6 views-row"})
        scrape_and_send_message(pillars_url, "img", {"class": "image-style-mt-product-image"})
    elif button_text == "RESOURCES":
        scrape_and_send_message(resources_url, "h1", {"class": "title page-title"})
        scrape_and_send_message(resources_url, "a")
        scrape_and_send_message(resources_url, "strong")
        scrape_and_send_message(resources_url, "p")
    elif button_text == "NEWS":
        scrape_and_send_message(news_url, "h1", {"class": "title page-title"})
        scrape_and_send_message(news_url, "h2")
        scrape_and_send_message(news_url, "span", {"class": "node__submitted-date"})
        scrape_and_send_message(news_url, "span", {"property": "schema:name"})
    elif button_text == "":
        pass

# Create a list of buttons
buttons = [
    "ABOUT",
    "PROGRAMS",
    "PILLARS",
    "RESOURCES",
    "NEWS",
]

# Create a keyboard with the buttons
keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
for button in buttons:
    keyboard.add(button)

# Handle the '/start' command
@bot.message_handler(commands=["start"])
def start(message):
    # Send the welcome message
    send_message("Welcome to the Ministry of Health Ethiopia Telegram bot! Please select a button below.")
  
    # Display the custom keyboard with buttons
    bot.send_message(message.chat.id, "Please select an option:", reply_markup=keyboard)

# Handle button clicks
@bot.message_handler(content_types=["text"])
def button_click(message):
    handle_button_click(message.text)

bot.polling()
