from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
import openai
import logging

# Load environment variables
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY") 

# Configure logging
logging.basicConfig(level=logging.INFO)

class Reference:
    """A class to store previously received responses from the OpenAI API."""
    def __init__(self) -> None:
        self.response = ""

reference = Reference()
model_name = "gpt-3.5-turbo"

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher(bot)

def clear_past():
    """A function to clear the previous conversation and context."""
    reference.response = ""

@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """Handler to clear the previous conversation and context."""
    clear_past()
    await message.reply("I've cleared the past context.")

@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """Handler to start the conversation."""
    await message.reply("Hi! I am your Food Recipe Bot 🍲.\nAsk me for food recipes and cooking tips!\nDeveloped by Malavika Gowthaman.")

@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    """Handler to help the user."""
    help_command = """
    Hi there! I am your specialized Food Recipe Bot! 🍜 
    You can ask me for recipes, ingredients, cooking tips, and more.

    Available commands:
    /start - Start the conversation
    /clear - Clear previous conversation context
    /help - Get this menu
    
    Happy cooking! 👨‍🍳
    """
    await message.reply(help_command)

@dispatcher.message_handler()
async def process_user_input(message: types.Message):
    """Handler to process the user's input and generate a response using the ChatGPT API."""
    logging.info(f">>> USER: {message.text}")

    prompt = "You are a helpful assistant that only provides information about food recipes and cooking tips."
    try:
        response = openai.ChatCompletion.create(
            model=model_name,
            messages=[
                {"role": "system", "content": prompt},  # for prompt
                {"role": "assistant", "content": reference.response},  # assistant
                {"role": "user", "content": message.text}  # our query 
            ]
        )
        reference.response = response['choices'][0]['message']['content']
        logging.info(f">>> chatGPT: {reference.response}")
        await bot.send_message(chat_id=message.chat.id, text=reference.response)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        await message.reply("Sorry, I encountered an error while processing your request.")

if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=False)
