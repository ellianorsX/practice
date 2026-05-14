''' CLASS deep diving
    (1) ENCAPSULATION
    (2) INHEITENCE
    (3) POLYMORPHISM
'''

print("===== INHERITENCE =====")

# parent > child
# parent > only provides only public & protected properties(state + method) to child

class Animal: # Parent
    description = "The class in parent for animals"
    
    
    def __init__(self, voice):
        self.voice = voice
        
        
    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")
        
        
class Dog(Animal): #child
    
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)
        
        
    def introdece(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")
        
    def protect(self):
        print("Yes, I can protect you!")
        
        
dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "ZzZ", False)        
            
            
dog.introdece()
cat.introduce()
fish.introduce()

print("========")
dog,make_voice()
fish.make_voice()            