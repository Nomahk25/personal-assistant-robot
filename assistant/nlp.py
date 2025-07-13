def interpret_command(text):
    text = text.lower()
    if "time" in text:
        return "get_time"
    elif "date" in text:
        return "get_date"
    elif "who is" in text or "what is" in text:
        return f"wikipedia:{text}"
    elif "search" in text:
        return f"search:{text.replace('search', '').strip()}"
    elif "exit" in text or "quit" in text:
        return "exit"
    else:
        return f"unknown:{text}"
