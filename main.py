# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import reference
import sheet
import Tkinter
import sys
import random

# Your Account Sid and Auth Token from twilio.com/console
blacklist_on = False


# roll a number
def roll(n):
    # function call -> random.randint(a, b)
    # Return a random integer N such that a <= N <= b
    return random.randint(0, n - 1)


# read text file
def read_textfile(filename):
    array = []
    try:
        textfile = open(filename, "r")
    except IOError:
        print("File does not exist!")
        return []
    for line in textfile:
        line = line.strip('\n')
        array.append(line)
    print(array)
    textfile.close()
    return array


# send message via Twilio
def send_message():
    client = Client(reference.account_sid, reference.auth_token)

    message = client.messages.create(
        body="Congratulations! You won a Rutgers Esports giveaway! Come to the giveaway table to claim your prize!",
        from_=reference.phone_from,
        to=reference.phone_to)

    print(message.sid)


# main
if __name__ == "__main__":
    officers = read_textfile("officers.txt")
    new_officers = read_textfile("new_officers.txt")
    officers_banned = False
    new_officers_banned = False

    print("Hello! Welcome to the GiveawayBot! What would you like to do?")
    choice = 0
    constraint_choice = 0
    query = []
    entry = []

    while choice != 5:
        print('1. Load names and phone numbers in drawing.')
        print('2. Select a winner.')
        print('3. Send message to winner.')
        print('4. Edit constraints.')
        print('5. Quit Program')
        choice = input("Type number and hit enter: ")
        if choice == 1:
            query = sheet.get_sheet()

        elif choice == 2:
            entry = sheet.select_person(query, officers, new_officers, officers_banned, new_officers_banned)

        elif choice == 3:
            if len(entry) == 0:
                print("There is no winner selected!")
            else:
                print("Contacting " + entry[1] + " . . .")
                # send_message()
                # print("Winner has been contacted.")

        elif choice == 4:
            while constraint_choice != 3:
                print("Current constraints:")
                print("1. Officers = " + str(officers_banned))
                print("2. New Officers = " + str(new_officers_banned))
                print("3. Go back.")
                constraint_choice = input("Type the corresponding number and hit enter: ")
                if constraint_choice == 1:
                    if officers_banned is True:
                        officers_banned = False
                    else:
                        officers_banned = True
                elif constraint_choice == 2:
                    if new_officers_banned is True:
                        new_officers_banned = False
                    else:
                        new_officers_banned = True
                elif constraint_choice == 3:
                    continue
                else:
                    print("Invalid input!")
            constraint_choice = 0

        elif choice == 5:
            break

        else:
            print('Invalid input!')

    print("Thank you for using the GiveawayBot! Goodbye~")
