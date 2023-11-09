# Voice Message Transcriber Bot
This project is a Telegram bot that transcribes voice messages. It is built with Python and the Telebot library.

You can find running instance of this bot [here](https://t.me/voix_bot).

## Installation

1. Clone this repository 
```
git clone https://github.com/L1S69/voix.git
cd voix
```
2. Install the required libraries
```
pip install -r requirements.txt
```
3. Obtain a bot token from the [BotFather](https://t.me/BotFather) on Telegram
4. Replace the TG_TOKEN variable in `main.py` with your bot token
5. Obtain a Huggingface token [here](https://huggingface.co/settings/tokens)
6. Replace the HF_TOKEN variable in `main.py` with your Huggingface token
7. Run it
```
python main.py
```