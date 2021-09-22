from chatterbot import conversation
from chatterbot import trainers
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

# Create a new chat bot named Norman
bot = ChatBot("Norman")

trainer = ListTrainer(bot)
 
 # TEACHING YOUR CHABOT TO COMMUNICATE
trainer.train([
    'How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])



# we can exit the loop and stop the program when a user enters ctrl+c.
while True:
    try:
        # INPUT STATEMENT
        bot_input = bot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break