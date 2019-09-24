# By Scout Crooke, 9/20/19, this program calculates the area of different shapes and compounded interest

sphere_volume = 4 / 3 * 3.14 * (5**3)

print("The volume of the sphere is", sphere_volume)

num_books = 60
book_price = 24.95 * .6 * num_books
shipping = 3 + (.75 * (num_books - 1))
total_cost = shipping + book_price

print("The total wholesale cost for 60 copies is", total_cost)

# calculate the area of a rectangle
rectangle_base = 5
rectangle_height = 9
area = rectangle_base * rectangle_height
print("THe area of the rectangle is", area)

# calculate the area of a triangle
triangle_base = 4
triangle_height = 8
triangle_area = triangle_base * triangle_height / 2
print("The area of the triangle is", triangle_area)

# calculate compounded interest
p = 10000  # principal amount
n = 12  # how often the interest is compounded per year
r = 0.08  # interest rate
t = 10  # number of years
a = p * (1 + (r / n )) ** (n * t)
print("The final amount of compounded interest is", a)

first_name = input("Hello, what is your first name?")
last_name = input("Cool! What is your last name?")
print(last_name, first_name)

hours = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
pay = hours * rate
print("Pay:", pay)

temp_C = flaot(input("what is the temperature in degrees Celcius?"))
temp_F = (temp_C * 9 / 5) + 32
print(temp_C, "degrees Celsius equals")