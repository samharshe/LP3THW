# create an int variable and set its value to 10
types_of_people = 10
# create a string variable using a format string
# string inside string!
x = f"There are {types_of_people} types of people."

# create a string variable and set its value to "binary"
binary = "binary"

# do the same and set its value to "don't"
do_not = "don't"

# create a string variable using a format string and fill out its value using the variables binary and do_not 
# string inside string!
y = f"Those who know {binary} and those who {do_not}."

# print the string x
print(x)
# print the string y
print(y)

# print a new string created using format string and string variable x
# string inside string!
print(f"I said: {x}")
# print another new string created using format string and string variable y
# string inside string!
print(f"I also said: '{y}'")

# create a Boolean var named "hilarious" and set its value to false
hilarious = False
# create a string variable with open brackets that can be filled using .format
joke_evaluation = "Isn't that joke so funny?! {}"

# fill those open brackets using .format and print the result
# string inside string!
print(joke_evaluation.format(hilarious))

# create a new string variable
w = "This is the left side of..."
# and another...nothing special
e = "a string with a right side."

# concatenate them and print
print(w + e)