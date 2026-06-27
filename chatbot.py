# chatbot.py

from datetime import datetime
import random
import difflib

from responses import responses
from jokes import jokes
from quotes import quotes
from calculator import calculate
from websites import open_website
from history import save_message, show_history, clear_history


# -----------------------------
# Greeting Messages
# -----------------------------

greetings = [
    "Hello",
    "Hi",
    "Hey",
    "Welcome",
    "Nice to see you",
    "Glad you're here"
]


# -----------------------------
# Available Commands
# -----------------------------

commands = [
    "hello",
    "hi",
    "hey",
    "help",
    "time",
    "date",
    "joke",
    "quote",
    "history",
    "clear history",
    "calculate",
    "search",
    "open google",
    "open youtube",
    "open github",
    "open linkedin",
    "python",
    "java",
    "c",
    "cpp",
    "html",
    "css",
    "javascript",
    "sql",
    "git",
    "github",
    "ai",
    "machine learning",
    "deep learning",
    "data science",
    "dbms",
    "operating system",
    "computer network",
    "cyber security",
    "cloud computing",
    "bye"
]


# -----------------------------
# Help Menu
# -----------------------------

def show_help():

    print("\n" + "=" * 55)
    print("📋 AVAILABLE COMMANDS")
    print("=" * 55)

    print("👋 Greetings")
    print("   hello, hi, hey")

    print("\n📅 Date & Time")
    print("   date")
    print("   time")

    print("\n😂 Fun")
    print("   joke")
    print("   quote")

    print("\n🧮 Calculator")
    print("   calculate 25+5")

    print("\n🌐 Websites")
    print("   open google")
    print("   open youtube")
    print("   open github")
    print("   open linkedin")

    print("\n📚 Programming")
    print("   python")
    print("   java")
    print("   c")
    print("   cpp")
    print("   html")
    print("   css")
    print("   javascript")
    print("   sql")
    print("   git")
    print("   ai")
    print("   machine learning")
    print("   deep learning")
    print("   data science")
    print("   dbms")
    print("   operating system")
    print("   computer network")
    print("   cyber security")
    print("   cloud computing")

    print("\n📝 History")
    print("   history")
    print("   clear history")

    print("\n👋 Exit")
    print("   bye")

    print("=" * 55)


# -----------------------------
# Welcome Screen
# -----------------------------

print("=" * 60)
print("🤖 SMART PERSONAL ASSISTANT CHATBOT")
print("=" * 60)

name = input("Hello! What's your name? : ").strip()

print(f"\n{random.choice(greetings)}, {name}! 😊")
print("Type 'help' to see all available commands.")

save_message("System", "Chat Started")
save_message("User", name)
# -----------------------------
# Main Chat Loop
# -----------------------------

while True:

    user = input(f"\n{name}: ").strip().lower()

    save_message(name, user)

    # ---------------- Greetings ----------------

    if user in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]:

        bot = random.choice(greetings) + f", {name}! 😊"

        print("Bot:", bot)
        save_message("Bot", bot)

    # ---------------- Help ----------------

    elif user == "help":

        show_help()
        save_message("Bot", "Displayed help menu.")

                    
    # ---------------- Small Talk ----------------

    elif "how are you" in user:

        bot = random.choice([
            "I'm doing great! Thanks for asking. 😊",
            "I'm fine and ready to help you!",
            "I'm just a chatbot, but I'm doing well!",
            "I'm always happy to chat with you!"
        ])

        print("Bot:", bot)
        save_message("Bot", bot)

    elif "your name" in user:

        bot = "I'm Smart Personal Assistant Chatbot."

        print("Bot:", bot)
        save_message("Bot", bot)

    elif "who created you" in user or "who made you" in user:

        bot = "I was created by Shaili Patel using Python."

        print("Bot:", bot)
        save_message("Bot", bot)

    elif "thank" in user:

        bot = random.choice([
            "You're welcome! 😊",
            "Happy to help!",
            "Anytime!",
            "Glad I could help!"
        ])

        print("Bot:", bot)
        save_message("Bot", bot)

    elif user == "good morning":

        bot = "Good Morning! ☀️ Have a wonderful day!"

        print("Bot:", bot)
        save_message("Bot", bot)

    elif user == "good afternoon":

        bot = "Good Afternoon! 😊"

        print("Bot:", bot)
        save_message("Bot", bot)

    elif user == "good evening":

        bot = "Good Evening! 🌙"

        print("Bot:", bot)
        save_message("Bot", bot)

    elif user == "good night":

        bot = "Good Night! 😴 Sweet dreams!"

        print("Bot:", bot)
        save_message("Bot", bot)

    # ---------------- Joke ----------------

    elif user == "joke":

        bot = random.choice(jokes)

        print("😂", bot)
        save_message("Bot", bot)

    # ---------------- Quote ----------------

    elif user == "quote":

        bot = random.choice(quotes)

        print("💡", bot)
        save_message("Bot", bot)

    # ---------------- Calculator ----------------

    elif user.startswith(("calculate", "calc", "solve")):

        expression = (
            user.replace("calculate", "")
                .replace("calc", "")
                .replace("solve", "")
                .strip()
        )

        bot = calculate(expression)

        print("Bot:", bot)
        save_message("Bot", bot)

    # ---------------- Programming Questions ----------------

    elif user in responses:

        bot = responses[user]

        print("Bot:", bot)
        save_message("Bot", bot)

    # ---------------- Open Website ----------------

    elif user.startswith("open"):

        bot = open_website(user)

        print("Bot:", bot)
        save_message("Bot", bot)

    # ---------------- History ----------------

    elif user == "history":

        print("\n========== CHAT HISTORY ==========\n")
        print(show_history())

    elif user == "clear history":

        clear_history()

        bot = "Chat history cleared."

        print("Bot:", bot)
        save_message("Bot", bot)

    # ---------------- Exit ----------------

    elif user == "bye":

        bot = f"Goodbye, {name}! 👋"

        print("\nBot:", bot)

        save_message("Bot", bot)
        save_message("System", "Chat Ended")

        break

    # ---------------- Unknown Command ----------------

    else:

        suggestion = difflib.get_close_matches(user, commands, n=1)

        if suggestion:

            bot = f"I don't understand.\nDid you mean '{suggestion[0]}'?"

        else:

            bot = "Sorry, I don't know that.\nType 'help' to see available commands."

        print("Bot:", bot)

        save_message("Bot", bot)
