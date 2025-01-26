import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! How's it going?"]
    ],
    [
        r"what is your name\??",
        ["I'm Chatbot, your friendly conversational assistant.", "You can call me Chatbot!"]
    ],
    [
        r"how are you\??",
        ["I'm just a program, but I'm here to help!", "Doing great! What about you?"]
    ],
    [
        r"(.) your favorite (.)",
        ["I don't have preferences, but I can help you choose yours!"]
    ],
    [
        r"quit",
        ["Goodbye! It was nice chatting with you.", "See you later!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Could you rephrase?", "Interesting. Can you tell me more?"]
    ]
]


chatbot = Chat(pairs, reflections)

def start_chat():
    print("Chatbot: Hi! Type 'quit' to exit the chat.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == 'quit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            response = chatbot.respond(user_input)
            print(f"Chatbot: {response}")

if _name_ == "_main_":

    nltk.download('punkt')
    start_chat()
