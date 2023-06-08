from textblob import TextBlob
import math


z=input("Do you wish to talk to me through voice? ")
if(z.lower()=="yes"):
    import Main2
else:
    def calculate(expression):
        try:
            result = eval(expression)
            return result
        except (SyntaxError, ZeroDivisionError):
            return None


    def analyze_sentiment(sentence):
        blob = TextBlob(sentence)
        sentiment_score = blob.sentiment.polarity
        return sentiment_score


    def creative_calculator():
        print("Welcome to the Here 4 U Calculator!")
        print("============================================")

        while True:
            user_input = input("How are you feeling today? ")
            sentiment_score = analyze_sentiment(user_input)

            if sentiment_score > 0.3:
                print("I'm glad you're feeling positive! Let's do some calculations.")
            elif sentiment_score < -0.3:
                print("I'm sorry to hear that. Stay positive! Let's do some calculations anyway.")
            else:
                print("Neutral sentiment detected. Let's proceed with some calculations.")

            print("\nSelect an operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Dog Years Converter")
            print("6. Round-off")
            print("7. Remainder")
            print("8. Percentages")
            choice = input("Enter your choice (1-8): ")

            if choice == '1':
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = num1 + num2
                print("Result:", result)
                print("Learn more about addition here: https://byjus.com/maths/addition/")
            elif choice == '2':
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = num1 - num2
                print("Result:", result)
                print("Learn more about subtraction here: https://www.mathsisfun.com/numbers/subtraction.html")
            elif choice == '3':
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = num1 * num2
                print("Result:", result)
                print("Learn more about multiplication here: https://www.mathsisfun.com/tables.html")
            elif choice == '4':
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                if num2 != 0:
                    result = num1 / num2
                    print("Result:", result)
                    print("Learn more about division here: https://www.mathsisfun.com/numbers/division.html")
                else:
                    print("Error: Division by zero!")
            elif choice == '5':
                age = int(input("Enter your age: "))
                dog_years = age * 7
                print("Your age in dog years is:", dog_years)
            elif choice == '6':
                num1 = float(input("Enter the number: "))
                result = math.ceil(num1)
                print("Result:", result)
                print("Learn more about round-off here: https://www.mathsisfun.com/rounding-numbers.html")
            elif choice == '7':
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = num1 % num2
                print("Result:", result)
                print("Learn more about remainders here: https://www.splashlearn.com/math-vocabulary/division/remainder")
            elif choice == '8':
                def calculate_percentage(number, percentage):
                    return (number * percentage) / 100
                number = float(input("Enter a number: "))
                percentage = float(input("Enter a percentage: "))
                result = calculate_percentage(number, percentage)
                print(f"{percentage}% of {number} is: {result}")
                print("Learn more about percentages here: https://www.splashlearn.com/math-vocabulary/division/remainder")
            else:
                print("Invalid choice. Please try again.")

            choice = input("Do you want to continue (y/n)? ")
            if choice.lower() != 'y':
                print("Thank you for using the Here 4 U Calculator. Goodbye!")
                break


    creative_calculator()