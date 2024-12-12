import os
import requests
import openai
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Set your OpenAI API key and Telegram bot token
OPENAI_API_KEY = '************************'
TELEGRAM_BOT_TOKEN = '************************'
ALPHA_VANTAGE_API_KEY = '***************'

# Initialize OpenAI API
openai.api_key = OPENAI_API_KEY

def fetch_top_investors():
    # Example API call to get stock data (replace 'MSFT' with your desired symbol)
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    data = response.json()

    investors_data = {}
    
    if "Time Series (Daily)" in data:
        time_series = data["Time Series (Daily)"]
        for date, metrics in list(time_series.items())[:10]:  # Get the last 10 days
            investors_data[date] = {
                "name": "Top Investor",  # Replace with actual investor names if available
                "company": "Microsoft",
                "current_price": float(metrics["4. close"]),
                "future_prediction": float(metrics["4. close"]) * 1.1,  # Example prediction (10% increase)
                "pros": "Strong company fundamentals.",
                "cons": "Market saturation risks."
            }

    return investors_data

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Welcome! This is a simple investment bot.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Use /start to begin.\n/topinvestors - Show top investors\n/invest - Get investment recommendations.')

async def top_investors_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    top_investors = fetch_top_investors()  # Fetch live data
    message = "Top Investors:\n"
    for key, investor in top_investors.items():
        message += f"{key}. {investor['name']} - Invests in {investor['company']}\n"
        message += f"   Current Price: ${investor['current_price']:.2f}, Future Prediction: ${investor['future_prediction']:.2f}\n"
    await update.message.reply_text(message)

async def invest(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Which company do you want to invest in? Please type the name (e.g., Microsoft).')

async def handle_investment_response(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_input = update.message.text
    top_investors = fetch_top_investors()  # Fetch live data
    for investor in top_investors.values():
        if user_input.lower() == investor['company'].lower():
            message = f"Investment Analysis for {investor['company']}:\n"
            message += f"Current Price: ${investor['current_price']:.2f}\n"
            message += f"Future Prediction: ${investor['future_prediction']:.2f}\n"
            message += f"Pros: {investor['pros']}\n"
            message += f"Cons: {investor['cons']}\n"
            message += "Would you like to proceed with this investment?"
            await update.message.reply_text(message)
            return

    await update.message.reply_text("Sorry, I don't have information on that company. Please try again.")

async def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("topinvestors", top_investors_list))
    app.add_handler(CommandHandler("invest", invest))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_investment_response))

    await app.run_polling()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
