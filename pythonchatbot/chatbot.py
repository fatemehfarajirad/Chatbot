from chatterbot import ChatBot

# CREAT NEW CHATBOT WHO'S NAME IS NORMAN
bot = ChatBot("Norman")

bot = ChatBot(
    'Norman',
    # CONNECT TO DATABASE
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    #
     logic_adapters=[
         # The MathematicalEvaluation adapter solves math problems that use basic operations.
        'chatterbot.logic.MathematicalEvaluation',
        # The TimeLogicAdapter returns the current time when the input statement asks for it
        'chatterbot.logic.TimeLogicAdapter'
        'chatterbot.logic.BestMatch'
    ],
    # CREAT A SQLITE DATABASE
    # THIS FILE WILL BE CREATED IF IT DOSEN'T EXIST
    database_uri='sqlite:///database.sqlite3'
)

