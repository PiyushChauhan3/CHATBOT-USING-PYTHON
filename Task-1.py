def chatbot_response(user_input):

    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hi there! How can I help you today?"
    
    elif "how are you" in user_input:
        return "I'm doing well, thank you! How about you?"
    
    elif "what is your name" in user_input :
        return "I'm a Bot. What's up?"
    
    elif "help" in user_input:
        return "Sure thing! What do you need help with?"
    
    elif "weather" in user_input:
        return "I can't check the weather right now, but you can find it online or on your phone."
    
    elif "time" in user_input:
        return "I can't give you the current time, but any clock or device should have it."
    
    else:
        return "I'm not sure what you mean. Can you say it differently?"

def main():
    print("Chatbot: Hi! I'm a Bot. How Can i Help You?")
    
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye","Thank You" ,"Thanks"]:
            print("Chatbot: Goodbye! See you later! Have a great day! Take care!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
