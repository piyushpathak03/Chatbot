from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

bot = ChatBot('bot')
trainer = ChatterBotCorpusTrainer(bot)

corpus_path = (r'''C:\Users\Rachit\Desktop\chatterbot-corpus-master\chatterbot_corpus\data\English/''')

for file in os.listdir(corpus_path):
    trainer.train(corpus_path + file)

while True:
    message = input('You:')
    print(message)
    if message.strip() == 'Bye':
        print('ChatBot: Bye')
        break
    else:
        reply = bot.get_response(message)
        print('ChatBot:', reply)
