from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
import openai
import sys

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY") 

class Reference:
    '''
    A class to store previously response from the openai API
    '''

    def __init__(self) -> None:
        self.response = ""
        
reference = Reference()
model_name = "gpt-3.5-turbo"


# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher(bot)

def clear_past():
    """A function to clear the previous conversation and context.
    """
    reference.response = ""
    
@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    A handler to clear the previous conversation and context.
    """
    clear_past()
    await message.reply("I've cleared the past context.")

    
@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """
    A handler to start the conversation
    """
    await message.reply("Hi\nI am Tele Bot!\nCreated to learn about ai together.\nDeveloped by Malavika Gowthaman. How can i assist you?")
    

@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    """
    A handler to help the user
    """
    help_command = """
    Hi there!, 
    I am Telegram Bot!. 
    Created to learn about ai together.
    Developed by Malavika Gowthaman.
    
    /start - to start the conversation
    /clear - to clear the past context of bot
    /help - to get this menu.
    
    I hope this helps you. :)
    """
    await message.reply(help_command)   


@dispatcher.message_handler()
async def helper(message: types.Message):
    """
    A handler to process the user's input and generate an output response using Chatgpt API.
    """
    print(f">>> USER: \n\t{message.text}")
    response = openai.ChatCompletion.create(
        model = model_name,
        messages = [
            {"role":"assistant","content":reference.response},
            {"role": "user", "content": message.text} #our query 
        ]
    )
    reference.response = response['choices'][0]['message']['content']
    print(f">>> chatGPT: \n\t{reference.response}")
    await bot.send_message(chat_id = message.chat.id, text = reference.response)
      


if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=False) # to make the bot activate once the code running/activated.