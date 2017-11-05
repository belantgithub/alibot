import telepot

bot_token = '394087266:AAEev4uWXngwCSwjdJLa6fbupfOVoPy-t4Q'
bot = telepot.Bot(bot_token)
ngrok_token = 'd710a825'
print('https://{ngrok_token}.ngrok.io/BBot/bot/{bot_token}/'.format(bot_token=bot_token, ngrok_token=ngrok_token))
bot.setWebhook('https://{ngrok_token}.ngrok.io/BBot/bot/{bot_token}/'.format(bot_token=bot_token, ngrok_token=ngrok_token))