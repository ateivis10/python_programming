#printing
print("Abdullah Al Fahim")
print("Fahim " * 10)
print('*' * 60)

# Variables
price = 20  #integer
rating = 4.6  #float
name = "Fahim "   #string
is_published = True   #boolean
print(price)
print(rating)
print(name *10)
print(is_published)


# Taking user inputs
name2 = input("What is your name: ")
print("Hi " + name2)

name3 = input("what's your name: ")
colour = input("What's your favourite colour: ")
print(name3 + " likes " + colour)

# Practice problem: Calculating Age
dob = int(input("Enter Death of birth: "))
age = 2025 - dob
print("your age is: ",age)

# Practice problem: converting weight ( pounds to kg)
pounds = float(input("Enter your weight in pounds: "))
kg = 0.45 * pounds
print("your weight in kilogram: ",kg)

# String manipulation
sen = "This is Abdullah's PC" #to use single quote inside a sentence we need to use double quote to indicate a string
print(sen)

sen1 = 'This is "Abdullah"' #to use double quote inside a sentence we need to use single quote to indicate a string
print(sen1)

sen2 = '''Hi, This is Abdullah.
How are you?
And what you doing?'''
print(sen2)     #triple quote to write multiple(three) line sentences

sen3 = 'This is Abdullah'
#index: 0123456789
print(sen3[1])      #positive index number to count the index from beginning, positive index starts from 0 and negative starts from -1
print(sen3[-3])     #negative to count the index from the end
print(sen3[1:6])    # to print index 1 to 6
print(sen3[1:-1])

first_name = 'Abdullah'
middle_name = 'Al'
last_name = 'Fahim'
#to write: Abdullah [Al] Fahim:
msg1 = first_name + ' [' + middle_name + '] ' + last_name   # this gets more complex when more symbols or formats start coming, so we use formatted string
msg2 = f'{first_name} [{middle_name}] {last_name}' #this is a formatted string
print(msg1)
print(msg2)
print(len(msg2)) #len function returns length of the string
#we can use many more string methods using dot operator:
print(msg2.upper())


#ARITHMATIC OPERATORS
print(10 + 2)
print(10 - 2)
print(10 * 2)
print(10 / 2)  #returns a float number
print(10 // 2) #returns integer part
print(10 ** 2) # double asteric means power
print(10 % 3)