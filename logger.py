from datetime import datetime


def log(text: str, filepath: str = "log.txt") -> None:
    """Append text with timestamp to log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filepath, "a") as f:
        f.write(f"[{timestamp}] {text}\n")


if __name__ == "__main__":
    log("Test entry")
    print("Logged to log.txt")
