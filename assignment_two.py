# By Scout Crooke, 9/24/19,
# This program has a conversation with the user and calculates to cost of the user's favorite car

print("Hi my name is BotBot!")
name = input("What is your name?")
print("Hi", name, "nice to meet you!")

location = input("Where are you from?")
print("Cool! I've always wanted to visit", location + ".", location, "sounds like a wonderful place to live!")

number = float(input("What is your favorite number?"))
my_number = number + 24
print("Interesting! My favorite number is actually", my_number)

car = input("What is your favorite car?")
print("Woah! I've always wanted a", car)

cost = float(input("How much does a car like that cost?"))
print("Wow!")

interest = float(input("What is a reasonable yearly interest rate on a great car like that?"))
print("Alright!")
r = interest / 100 / 12  # converting to a decimal, then dividing by the number of month in a year

years = int(input("And if you were to take out a loan to buy the car, how many years would you take the loan out for?"))
n = 12 * years
monthly_payment = (r * cost) / (1 - (1 + r) ** -n)
total_cost = years * 12 * monthly_payment
print("Alright. So, if you bought a", car, "you would have a monthly payment of $" + str(monthly_payment))
print("I hope that is reasonable with your budget. That would be a total of $" + str(total_cost))
print("Well, I better get going now. It has been nice talking with you", name + "!")
