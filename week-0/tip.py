def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percentage = percent_to_float(input("What percent would you like to tip? "))
    tip = dollars * percentage
    print(f"Leave ${tip:.2f}")

def dollars_to_float(dollars):
    return float(dollars.replace("$", ""))


def percent_to_float(percentage):
    return float(percentage.replace("%", ""))/100

main()
