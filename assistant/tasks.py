import datetime
import wikipedia
import pywhatkit
from assistant.speech import speak

def execute_command(command, return_text=False):
    response = ""

    if command == "get_time":
        response = f"The time is {datetime.datetime.now().strftime('%H:%M')}"
    elif command == "get_date":
        response = f"Today is {datetime.datetime.now().strftime('%A, %B %d, %Y')}"
    elif command.startswith("wikipedia:"):
        query = command.split("wikipedia:")[1]
        try:
            response = wikipedia.summary(query, sentences=2)
        except:
            response = "I couldn't find information on that topic."
    elif command.startswith("search:"):
        query = command.split("search:")[1]
        response = f"Searching for {query}..."
        pywhatkit.search(query)
    elif command == "exit":
        response = "Goodbye!"
        speak(response)
        exit()
    else:
        response = "I'm still learning. I didn't understand that."

    if return_text:
        return response
    else:
        speak(response)
