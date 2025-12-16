import pyttsx3


def speak(s):
    engine = pyttsx3.init()
    engine.say(s)
    engine.runAndWait()
    return "Done!"


if __name__ == "__main__":
    s = "Hey, there! Welcome to python tutorial."

    print(speak(s))
