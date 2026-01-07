from datetime import datetime

LOG_FILE = "logs.txt"


def log_interaction(question, answer):
    timestamp = datetime.now().isoformat()

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}]\n")
        file.write(f"Q: {question}\n")
        file.write(f"A: {answer}\n")
        file.write("-" * 40 + "\n")
