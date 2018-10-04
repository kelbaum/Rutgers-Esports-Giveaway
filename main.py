# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import reference
import sheet
import Tkinter
import sys
import random

# Your Account Sid and Auth Token from twilio.com/console
blacklist_on = False


def roll(n):
    # function call -> random.randint(a, b)
    # Return a random integer N such that a <= N <= b
    return random.randint(0, n - 1)


def send_message():
    client = Client(reference.account_sid, reference.auth_token)

    message = client.messages.create(
        body="Congratulations! You won a Rutgers Esports giveaway! Come to the giveaway table to claim your prize!",
        from_=reference.phone_from,
        to=reference.phone_to)

    print(message.sid)


if __name__ == "__main__":
    print("Hello! Welcome to the GiveawayBot! What would you like to do?")
    print('1. Load names and phone numbers in drawing.')
    print('2. Select a winner.')
    print('3. Send message to winner.')
    print('4. Quit Program')
    choice = 0
    query = []
    entry = []

    while choice != 4:
        choice = input("Type number and hit enter: ")
        if choice == 1:
            query = sheet.get_sheet()
        elif choice == 2:
            entry = sheet.select_person(query)
        elif choice == 3:
            print("Contacting " + entry[1] + " . . .")
            # send_message()
            # print("Winner has been contacted.")
        elif choice == 4:
            break
        else:
            print('Invalid input!')

    print("Thank you for using the GiveawayBot! Goodbye~")
