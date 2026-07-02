import sys
from voice import speak, listen
from brain import think
from config.config import STARTUP_MESSAGE, AI_NAME, WAKE_WORD


def format_name_for_speech(name: str) -> str:
    return name.replace("_", " ").strip().title()


def normalize_command(command: str) -> str:
    if not command:
        return ""

    command = command.strip().lower()
    wake_word = WAKE_WORD.lower().strip()

    if wake_word and command.startswith(wake_word):
        return command[len(wake_word):].strip()

    return command


def main():
    if sys.version_info < (3, 11):
        print(
            "WARNING: This project needs Python 3.11 or newer. "
            f"Current interpreter: {sys.version_info.major}.{sys.version_info.minor}"
        )

    spoken_name = format_name_for_speech(AI_NAME)

    speak(STARTUP_MESSAGE)
    speak(f"Hello Boss, I am {spoken_name}. I am your assistant.")
    speak("I am more like your little sister. I am cute, sweet, and always here for you.")

    try:
        while True:
            command = listen()

            if command == "":
                speak("I didn't catch that. Please say it again.")
                continue

            command = normalize_command(command)
            response = think(command)

            if response == "EXIT":
                speak("Goodbye Boss.")
                break

            speak(response)
    except KeyboardInterrupt:
        speak("Goodbye Boss.")


if __name__ == "__main__":
    main()
