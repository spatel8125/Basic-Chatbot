
import webbrowser

# Dictionary containing website names and URLs
websites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "linkedin": "https://www.linkedin.com",
    "stackoverflow": "https://stackoverflow.com",
    "gmail": "https://mail.google.com",
    "chatgpt": "https://chat.openai.com",
    "wikipedia": "https://www.wikipedia.org"
}


def open_website(command):
    """
    Opens a website based on the user's command.
    Example:
        open google
        open youtube
    """

    command = command.lower().replace("open", "").strip()

    if command in websites:
        webbrowser.open(websites[command])
        return f"Opening {command.title()}..."
    else:
        return "Website not found."