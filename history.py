

from datetime import datetime

FILE_NAME = "chat_history.txt"


def save_message(sender, message):
    """
    Save a message to chat_history.txt
    """

    with open(FILE_NAME, "a", encoding="utf-8") as file:

        current_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

        file.write(f"[{current_time}] {sender}: {message}\n")


def clear_history():
    """
    Delete all previous chat history.
    """

    open(FILE_NAME, "w").close()


def show_history():
    """
    Display previous conversations.
    """

    try:

        with open(FILE_NAME, "r", encoding="utf-8") as file:

            history = file.read()

            if history.strip() == "":
                return "No chat history found."

            return history

    except FileNotFoundError:

        return "No chat history found."