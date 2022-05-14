message = input("Tell me something, and I will repeat it back to you:  ")
print(message)


nome = input("Please enter your name: ")
print(f"\nHello, {nome}!")

#Multi-line string
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhats is your first Name?"

name = input(prompt)

#Multiple of 10
number = input("Pick a number:")
number = int(number)

if number % 10 == 0:
    print("It's multiple of ten.")
else:
    print("It's not multiple of ten.")


#While loop
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)


prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}")


#Start with users that need to be verified,
#and an empty list to hold confirmed users.

unconfirmed_users = ['alice' , 'brian', 'candace']
confirmed_users = []

#Verified each user until there are no more uncorfimed users.
#Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

#Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())