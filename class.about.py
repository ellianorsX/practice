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




print("======= special/magic methods =======")
# Python's most common special methods are below:
# __init__ __new__ __str__ __call__ __getitem__ __eq__ __len__...

class Car():
    # state
    description = "This class makes cars"
    
    # constructor
    def __new__(cls, *args):
        print("* __new__ *")
        return super() .__new__(cls)
    
    def __init__(self, name, year):
        self.name = name
        self.year = year
        
    # method
    def start_engine(self):
        print(f"the {self.name} started engine!")
        
    def stop_engine(self):
        print(f"the {self.name} stopped engine!")
        
    def __str__(self):
        return f"{self.name} was produced in {self.year} year!"
    
    def __call__(self):
        print("Object called as function!")
        
        
        
    my_car = Car("Toyota", 2027)
    my_car.start_engine()
    my_car.stop_engine()
    
    print("----------")
    your_car = Car("Genesis", 2027)
    print(your_car)
    response = your_car()  
    print("response:", response)   