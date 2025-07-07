import google.generativeai as genai

API_KEY = \
    "AIzaSyBl-V9AGVtoB4k9Uwaudmyj0k7kgYAzmCo"
    
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-pro")
chat = model.start_chat()

while True: 
    userInput = input("Your Message: ")
    if userInput.lower() == "exit":
        print("Exiting chat.")
        break
    response = chat.send_message(userInput)
    print("Goft Ai: " + response.text)