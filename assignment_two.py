# By Scout Crooke, 9/23/19, unit 2 assignment option 1

# introductions
print("Hi my name is BotBot!")
name = input("What is your name?")
print("Hi", name, "nice to meet you!")

location = input("Where are you from?")
print("Cool! I've always wanted to visit", location + ".", location, "sounds like a wonderful place to live!")

number = int(input("What is your favorite number?"))
my_number = number + 24
print("Interesting! My favorite number is actually", my_number)

car = input("What is your favorite car?")
print("Woah! I've always wanted a", car)

cost = int(input("How much does a car like that cost?"))
print("Wow!")

interest = int(input("What is a reasonable yearly interest rate on a great car like that?"))
print("Alright!")

years = int(input("And if you were to take out a loan to buy the car, how many years would you take the loan out for?"))
n = 12 * years
monthly_payment = (interest * cost) / (1 - ( 1 + interest) ** -n)
total =
print("If you bought a", car, "you would have a monthly payment of", "I hope that is reasonable with your budget. That would be a total of", total)
