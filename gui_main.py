import tkinter as tk
from assistant.nlp import interpret_command
from assistant.tasks import execute_command
from assistant.speech import speak

class AssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Personal Assistant")
        self.root.geometry("500x600")
        self.root.config(bg="#1e1e1e")

        self.chat_display = tk.Text(
            root,
            bg="#2d2d2d",
            fg="white",
            font=("Arial", 12),
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.append_chat(
            "Assistant: Hello! I can help you with time, date, facts, and even web searches.\n"
            "Just type 'search' followed by what you want to find online.\n"
            "For example: search cute dog videos\n"
        )

        self.user_input = tk.Entry(root, font=("Arial", 14))
        self.user_input.pack(padx=10, pady=10, fill=tk.X)
        self.user_input.bind("<Return>", self.send_message)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

    def send_message(self, event=None):
        text = self.user_input.get()
        if not text.strip():
            return

        self.append_chat(f"You: {text}")
        self.user_input.delete(0, tk.END)

        command = interpret_command(text)
        response = execute_command(command, return_text=True)
        self.append_chat(f"Assistant: {response}")
        speak(response)

    def append_chat(self, message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, message + "\n\n")
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = AssistantGUI(root)
    root.mainloop()
