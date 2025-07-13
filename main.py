from assistant.speech import listen, speak
from assistant.nlp import interpret_command
from assistant.tasks import execute_command

def main():
    speak("Hello, I am your personal assistant. How can I help you?")
    while True:
        query = listen()
        if query:
            command = interpret_command(query)
            execute_command(command)

if __name__ == "__main__":
    main()
