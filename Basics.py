# Python variables
#same as vectors in R
#strings (chars), floaters (decimals), integers (whole)

string = "Hello World"
print(string)
#even though we have assigned string, we still need to use print

string2 = print("Hello World")
string2 # this approach does not store the string contents bc print doesn't return any values

num1= 66
print(string+str(num1)) #str() coerces data type in python

### Operators
#arithmatic + - *
# % is a division operator... returns remainder

## Assignment
x = 20
print(x)
x += 10 #adds 10 to x
print(x) #print() needed after every change to x
x -= 10 #subtracts
print(x)
# *= or /= works too

##comparison operators
# ==, !=, >, <

#logical operators
# and ; both conditions must be satisfied
#or ; only one condition needs to be satisfied


### Conditional Statements
#indentation instead of {} for scope of code
weather_cond = "cloudy" #main condition checked
if weather_cond == "sunny":
    print("dont forget your sunglasses") # what is executed if there is a match
elif weather_cond == "rainy": # secondary condition checked
    print("grab your umbrella") # secondary execution
else:
    print("seize the day") #final execution if neither condition is met


#### Functions
#def = definition or define; name_of_function(parameters / input)
def area(length,width):
    area = length * width
    print(area)
area(17,20)

def bank_withdraw(amount):
    balance = 1000
    current_bal = balance - amount
    return current_bal #return allows you to work within scope of previous code block

print("after withdrawal, you have $"+str(bank_withdraw(300))+" remaining")

withdraw=1200

if withdraw >1000:
    print("you have overdrafted your account by $"+str(abs(bank_withdraw(withdraw))))
else:
    print("after withdrawal, you have $" + str(bank_withdraw(withdraw)) + " remaining")

#previous code but else suffices since any other amount less than 100 would match the else condition
#elif  withdraw <=1000:
 #   print("after withdrawal, you have $"+str(bank_withdraw(withdraw))+" remaining")

#LOOPS / ITERATION
#FOR LOOP - within a given range / sequence
#exits bc it runs thru the sequence
i = 0
for i in range(10): #does not print for 10 in sequence
    print("hello world")


# While : continues until a specified condition is no longer satisfied
#step 1: Init
#Step 2: condition loop until false; FALSE exits loop

i = 0
while i <= 10 : #while i is less than or equal to 10, keep looping /printing
    print("my name is")
    i=i+1 # each iter increase i by 1 ; final iter i = 11 and exits

i = 10
while i>=0: # keep looping until i is greater than or = to 0
    print("Thi is loop " +str(i))
    i=i-1 # loop starts at 10 and subtracts 1 after each iter
