import random


# Question 1 and Bonus 5: Generate a random temperature
def get_random_temp(season):
    if season == "winter":
        return round(random.uniform(-10, 16), 1)

    elif season == "spring":
        return round(random.uniform(0, 25), 1)

    elif season == "summer":
        return round(random.uniform(16, 40), 1)

    elif season == "autumn":
        return round(random.uniform(0, 25), 1)


# Questions 2, 3, 4 and Bonus 6
def main():
    month = int(input("Enter a month number (1-12): "))

    if month < 1 or month > 12:
        print("Invalid month! Please enter a number between 1 and 12.")
        return

    # Determine the season from the month
    if month in [12, 1, 2]:
        season = "winter"
    elif month in [3, 4, 5]:
        season = "spring"
    elif month in [6, 7, 8]:
        season = "summer"
    else:
        season = "autumn"

    print(f"The season is {season}.")

    # Generate a temperature for the season
    temp = get_random_temp(season)

    print(f"The temperature right now is {temp} degrees Celsius.")

    # Give advice based on the temperature
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif temp <= 15:
        print("Quite chilly! Don't forget your coat.")
    elif temp <= 23:
        print("The weather is cool. A light sweater should be fine.")
    elif temp <= 31:
        print("It's warm. A t-shirt should be comfortable.")
    else:
        print("It's hot! Stay hydrated and wear light clothing.")

main()