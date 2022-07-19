age=30
print(age)
print(30)
marcela_age=31
PI=3.141592 ##Constant

float_division=13/4
print(float_division)

integer_division=13//4 ##Parte Entera
print(integer_division)

remainder_division=13%4 ##Modulus
print(remainder_division)

x= 15
remainder_division=x%2
print(remainder_division)

string="Hello, it's me"
print("Marcela said: \"Hello it's me\" ") ##Quotation marks inside a string

multiline=""" Hi, 

Let's continue with this new course.

2022
"""

print(multiline)



"""
This is another way to comment.

Nice approach


"""




age=31
age_as_str=str(age)
print('Marcela is ' + age_as_str +' years old')

print(f"Marcela is {age}")


name='Hellen'
final_greeting="How are you {}"
mutable_greeting=final_greeting.format(name)
print(mutable_greeting)

name='Marce'
mutable_greeting=final_greeting.format(name)
print(mutable_greeting)


greeting="How are you {name}? How is your {moment} going on"
morning_greeting=greeting.format(name='Marce', moment='morning')
print(morning_greeting)


my_name='Marcela'
your_name=input('What is your name?')

print("Hi {}, it's {}".format(your_name, my_name))

age=input('How old are you?')
print(f"Your age in months is {age*12}") ##Repet the string 12 times

print(f"Your age in months is {int(age)*12}")

age=int(input('How old are you?'))
print(f"Your age in months is {age*12}")

age=int(input('How old are you?'))
months = age*12 ## This is a better practice
print(f"Your age in months is {months}")