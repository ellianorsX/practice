''' OPERATORS & CONDITIONS
    (1) Operators
    (2) Conditions
    (3) Logical operators
'''

print("===== Operators =====")
# + - > >= < <= == is * / // % += -= ** referance uchun (is)

a = 19
b = 5

print(a / b)
result = a // b
left = a % b
print(f"the result: {result} and left: {left}")

# a = a + 100
a += 100
print("a:", a)

print("b**2", b**2)
print("b**3", b**3)

print("="*5)

c = dict(name="Ellia", age=23)
d = dict(name="Ellia", age=23)
e = c

print("c==d", c == d)  # only value
print(id(c), id(d), id(e))

print("c is d", c is d)
print("c is e", c is e)


print("===== CONDITIONS =====")

x = 15

if x > 50:
    print("case A")
    
elif x > 10:
    print("case B")
    
else:
    print("case c")
    
print("----------")  



print("===== LOGICAL OPERATIONS =====")

age = 21 

# person = None
# if age > 16:
#     person = "adult"
    
# else:
#     person = "minor"    
        
        # TERNARY oper
person = "adult" if age > 18 else "minor" 
print("person:", person)       

print("=====  =====")

# and or

is_student = False
is_Engineer = True
is_SeniorCTO = True
is_Drprofesser = True
is_President = False

if not is_student:
    print("Wellcome here, do u want to be student!")
elif is_Engineer:
    print("Please go to office!")
elif is_SeniorCTO:
    print("We need to your help!")
    
else:
    print("other case")    
