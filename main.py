import os

import telebot
from gradio_client import Client

from background import keep_alive

# Set up the telegram and huggingface api tokens
TG_TOKEN = os.environ['TG_TOKEN']
HF_TOKEN = os.environ['HF_TOKEN']

client = Client("abidlabs/whisper", hf_token=HF_TOKEN)

# Create a telebot object with the token
bot = telebot.TeleBot(TG_TOKEN)


# Define a message handler for the "/start" and "/help" commands
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
  # Send a welcome message to the user
  bot.send_message(
      message.chat.id,
      f"Hi, {message.from_user.first_name}. I was created to help you transcribe voice messages. Send "
      f"me a voice message or add me to a group to get started")


# Download a voice message and run it through API
@bot.message_handler(content_types=['voice'])
def voice_processing(message):
  file_info = bot.get_file(message.voice.file_id)
  downloaded_file = bot.download_file(file_info.file_path)
  with open('temp.ogg', 'wb') as new_file:
    new_file.write(downloaded_file)

  response = client.predict("temp.ogg")
  text = response
  bot.reply_to(message, text)
  os.remove("temp.ogg")


# Start polling
keep_alive()
bot.infinity_polling()
