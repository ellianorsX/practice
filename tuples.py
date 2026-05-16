''' Tuple
    (1) What is tuple: tuple vs list
    (2) Unpacking arguments
    (3) zip
'''

print("========== What is tuple: tuple vs list ==========")
# Java/PHP/NodeJS array => Python list 

# literal 
numbs = [3, 4, 6, 1]


# constructor
letters = list("Hello World!")

fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits:", fruits)

fruits[2] = "melon"
print("after fruits:", fruits)

# We can not mutate tuple
animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
# animals[0} = "bird"

# try avoid thse
people = "MARY", "ELLIA"
animals = "dog"


print("========== uNPACKING ARGUMENTS ==========")
groups = ["MIT", "FLEXY", "DEVEX", "MG" ]
(x, y, *z) = groups
print(f"the x: {x} and y: {y}")
print("z:", z) #list 

# *args > tuple
def calculate(*args):
    print("*args >", args)
    total = 1
    for x in args:
        total *= x
    print(f"the total value: {total}")
    return total



# call
calculate(1, 7, 2, 5)
print("------------")
calculate(0, 2, 300)
print("------------")
calculate(5, 7)


print("+++++++++++++")
#  **kwargs > dictionary


def introduce(**kwargs):
    print(f"the type(**kwargs) value: {type(kwargs)}")
    print(f"Hi, I am {kwargs["name"]} and I am {kwargs["age"]} years old!")
    
    
    
# call
introduce(name="Mary", age=25)
introduce(name="Ellianor", age=24, single=True)



def greeting(*args, **kwargs):
    print("*args >", args)
    print("**kwargs >", kwargs)
    
    
# call
greeting("Hi", True, 10, name="Mary", age=23)