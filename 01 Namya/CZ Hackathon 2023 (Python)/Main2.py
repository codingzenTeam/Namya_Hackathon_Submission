import speech_recognition as sr


def calculate(expression):
    try:
        result = eval(expression)
        return result
    except (SyntaxError, ZeroDivisionError):
        return None


def voice_calculator():
    print("Welcome to the Voice Calculator!")
    print("===============================")

    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something...")
            audio = r.listen(source)

        try:
            print("Processing your speech...")
            expression = r.recognize_google(audio)
            print("You said:", expression)
            result = calculate(expression)

            if result is not None:
                print("Result:", result)
            else:
                print("Invalid mathematical expression!")

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand your speech. Please try again.")

        except sr.RequestError as e:
            print("Sorry, an error occurred. Please check your internet connection.")

        choice = input("Do you want to continue (Y/N)? ")
        if choice.lower() != 'y':
            print("Thank you for using the Voice Calculator. Goodbye!")
            break


voice_calculator()