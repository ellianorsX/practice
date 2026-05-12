''' CLASS 
    (1) What is class
    (2) ordinary vs static properties
    (3) special methods
'''

print("======= What is class =======")
# class - blueprint for object creation!
# Class = Blueprint
# Ob'ektlar yaratish uchun "qolip". Bir class dan ko'plab ob'ekt yaratish mumkin.
# structure > state constructor methods

class Person():
    # state
    message = "static state property"
    
    
    # construction construction — ob'ekt yaratilganda avtomatik chaqiriladi
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
    # method 
    def introduce(self): 
        print(f"{self.name} says: How do you do!")
        
    def say_age(self):
        print(f"{self.name} says I am {self.age}!")
    
    
    
    @classmethod 
    def explain(cls):
        print("static method executed") 
        
           
# State + Constructor + Methods
# Har bir classning uch qismi bor. Bu uchala narsa birga ishlaydi

# Class vs Object
# Class — retsept. Object — o'sha retsept bo'yicha pishirilgan taom
        

person1 = Person("Ellia", 23)
person2 = Person("Mary", 25)
Person3 = Person("Max", 27)

# ordinary state
print("person1.name:", person1.name)

# ordinary method 
person1.introduce()
person2.say_age()

    
        
print("======= ordinary vs static properties =======")

# static state
new_message = Person.message
print("new_message", new_message)

# static method 
Person.explain()