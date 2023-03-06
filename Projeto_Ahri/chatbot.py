from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# cria o objeto chatbot
chatbot = ChatBot('Meu Chatbot')

# cria o treinador
trainer = ListTrainer(chatbot)


# treina o chatbot
trainer.train([
    'Olá!',
    'Oi, tudo bem?',
    'Qual é o seu nome?',
    'Meu nome é Chatbot',
    'O que você faz?',
    'Eu sou um chatbot e estou aqui para ajudar',
])


def get_response(user_input):
    response = chatbot.get_response(user_input)
    return response

while True:
    user_input = input('Você: ')
    if user_input.lower() == 'sair':
        break

    response = get_response(user_input)
    print('Chatbot:', response)
