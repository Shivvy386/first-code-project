def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")


def main():
    user_input = input("Enter your input: ")

    result = convert(user_input)
    print(result)

main()
