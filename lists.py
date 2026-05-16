'''LIST 
   (1) Working with list
   (2) List methods
   (3) Lambda function
   (4)enumerate, map and filter
'''

print("========== Working with list ==========")
# Java/PHP/NodeJS array => Python list

# literal
person = {"name": "Justin", "age": 25}  # dictionary
people = ("Andrew", "John", "Michael")  # tuple
groups = ["MITT", "FLEXY", "DEVEX", "MG"]  # list

for team in groups:
    print(f"the team: {team}")


# constructor
letters = list("Hello World!")
print(f"the letters: {letters} and size: {len(letters)}")


print("----------")
fruits = ["apple", "orange", "lemon", "kiwi"]

a = fruits[0]
b = fruits[0:2]   # [0, 2)
c = fruits[:3]
d = fruits[::-1]

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)


print("========== List methods ==========")
# methods -> append() insert() pop() remove() clear() sort() index()

letters = ["a", "d", "b"]

letters.append("c")  # add behind
print(f"the append letters: {letters}")

letters.insert(0, "z")  # add front
print(f"the insert letters: {letters}")


size = len(letters) - 1
result1 = letters.pop(size)  # pop behind
print(f"the pop result1: {result1} and letters: {letters}")

result2 = letters.pop(0)  # pop front
print(f"the pop result2: {result2} and letters: {letters}")


print("------------")
animals = ["dog", "cat", "capybara", "fish", "lion"]

print("animals:", animals)

animals.remove("lion")
print("animals remove:", animals)

del animals[2:4]
print("animals delete:", animals)

exist = animals.index("cat")
print("cat exist:", exist)

animals.clear()
print("animals clear:", animals)

if "cat" in animals:
    print("index of cat:", animals.index("cat"))
else:
    print("cat does not exist")
