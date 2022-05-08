magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")


even_numbers = list(range(2, 11, 2))
print(even_numbers)

#list comprehension
squares = [value**2 for value in range (1,11)]
print(squares)

#if statement
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#the if-elif-else chain
age = 12

if age < 4:
     print('Your admission cost is $0.')
elif age < 18:
    print('Your admission cost is $25.')
else:
    print('Your admission cost is $40.')


#checking for special items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")

