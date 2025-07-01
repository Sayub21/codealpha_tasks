def get_response(user_input):  

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I don't understand that."

def chatbot():
    print("Chatbot: Hello! Type something to begin (type 'bye' to exit).") 
    
    while True:  
        user_input = input("You: ").lower()  
        
        response = get_response(user_input)  
        print("Chatbot:", response)  
        
        if user_input == "bye":  
            break

chatbot()
